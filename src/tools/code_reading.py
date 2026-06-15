from pathlib import Path

from agents import function_tool


@function_tool
def read_code(files: list[str]) -> str:
	"""Returns the whole code of the file.
	Args:
		files: list[str]: It takes the list of the names of the relevent files
	Returns:
		Gives the whole code for each file
	"""
	code_formatted = ""

	for file in files:
		if len(code_formatted) > 15000:
			code_formatted += "\n[Truncated due to size]\n"
			break
		path = next(Path(Path.cwd() / "coding_agent").rglob(file))
		if path.exists():
			try:
				with open(path, 'r', encoding='utf-8') as f:
					code = f.read()
					code_formatted += f"{path}:\n{code}\n{'-'*30}\n"
			except Exception as e:
				code_formatted += f"{path}: [Error reading file: {str(e)}]\n{'-'*30}\n"
		else:
			code_formatted += f"{path}: [File not found]\n{'-'*30}\n"
	return code_formatted
