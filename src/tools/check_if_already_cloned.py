from pathlib import Path

from agents import function_tool


@function_tool
def check_if_already_cloned(repo_url: str) -> str:
    """It checks if repo is already cloned or not.
    Args:
        repo_url: It takes repo_url or repo_name
    """
    clone_dir = "./coding_agent/repos"

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    target_path = Path(clone_dir) / repo_name

    if target_path.exists():
        return f"Repo already exists at {target_path}"
    else:
        return "It is not cloned"
