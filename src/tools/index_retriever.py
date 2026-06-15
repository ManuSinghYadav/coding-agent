from pathlib import Path
import json

from agents import function_tool
from pydantic import BaseModel, Field

from src.config import openai


class ReleventFile(BaseModel):
	file_name: str = Field("Name of the relevent file")
	file_path: str = Field("File path")
	reason: str = Field("Reason for selecting this file as relevent")

class ReleventFiles(BaseModel):
	relevent_files: list[ReleventFile]


@function_tool
def file_filter(query: str, repo_name: str) -> str:
	"""Used for retrieving the relevent file names with reason.
	Args:
		query: query of user
		repo_name: Exact name of repository
	Returns:
		Relevent file names with path and reason.
	"""
	index_path = Path.cwd() / "coding_agent" / f"index_of_{repo_name}.json"

	if index_path.exists():
		with open(index_path, 'r') as f:
			content = f.read()
			content = json.loads(content)

		p = []
		for i in content:
			p.append(f"Name: {i["name"]}\nFile Path: {i["file_path"]}\nSummary: {i["summary"]}")

		system_prompt = f"""
		You are given a list of files from a codebase.

		Each file has:
		- file_name
 		- file_path
		- summary

		Files:
		{p}

		Select the most relevant files.
		Return their name and file path and reason.
		"""

		summary = openai.chat.completions.parse(
			model="gpt-4.1-nano",
			messages=[
				{"role": "system", "content": system_prompt},
				{"role": "user", "content": query}
				],
				response_format=ReleventFiles
				)

		return summary.choices[0].message.parsed
	
	else:
		return "Index does not exists"
