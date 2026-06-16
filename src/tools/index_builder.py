import json
from pathlib import Path

from agents import function_tool

from src.config import openai


def summary_builder(index_path: str) -> str:
    """Creates summary of files of repository.
    Args:
            index_path: Path of index.
    Returns:
            Status
    """
    try:
        print("Building summaries in Index . . . ")

        with open(index_path, "r") as repo:
            json_repo = repo.read()
            list_repo = json.loads(json_repo)

        for file in list_repo:
            if file["summary"] is None:
                with open(file["file_path"], "r", encoding="latin-1") as code:
                    snippit = code.read()[:2000]
                    summary = openai.chat.completions.create(
                        model="gpt-4.1-nano",
                        messages=[
                            {
                                "role": "system",
                                "content": "Summarize the purpose of this code file briefly.",
                            },
                            {"role": "user", "content": snippit},
                        ],
                    )

                file["summary"] = summary.choices[0].message.content

        with open(index_path, "w") as f:
            json.dump(list_repo, f, indent=2)

        return "success"

    except Exception as e:
        return f"Failed with an error {str(e)}"


@function_tool
def index_builder(repo_name: str) -> str:
    """Builds index of repositroy in JSON format, which cointains
            - file_name
            - file_path
            - summary
    Args:
            repo_name: The name of repository.
    Returns:
            It creates the index.
    """
    index_path = Path.cwd() / "coding_agent" / f"index_of_{repo_name}.json"

    if not index_path.exists():
        print("Building Index")

        index = []

        repo_path = Path.cwd() / "coding_agent" / "repos" / repo_name

        if repo_path.exists():
            files = list(repo_path.rglob("*"))

            # This removed all empty folders and .git files
            relevent_files = [
                i for i in files if i.suffix != "" and ".git" not in i.parts
            ]

            for file in relevent_files:
                index.append(
                    {"name": file.name, "file_path": str(file), "summary": None}
                )

            with open(
                Path.cwd() / "coding_agent" / f"index_of_{repo_name}.json", "w"
            ) as file:
                json.dump(index, file, indent=2)

            print("Index built")

            summary_status = summary_builder(
                Path.cwd() / "coding_agent" / f"index_of_{repo_name}.json"
            )

            return {"index_status": "success", "summary_status": summary_status}
        else:
            return "This repo doesn't exists"

    else:
        return "Index already exists"
