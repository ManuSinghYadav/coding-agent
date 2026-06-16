import os
import subprocess

from agents import function_tool


@function_tool
def clone_repo(repo_url: str, branch: str = None):
    """
    Clone a GitHub repository locally.

    :param repo_url: HTTPS or SSH repo URL
    :param clone_dir: Directory where repo will be cloned
    :param branch: Optional branch name
    """

    # Hardcoded path of cloning
    clone_dir = "./coding_agent/repos"

    os.makedirs(clone_dir, exist_ok=True)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    target_path = os.path.join(clone_dir, repo_name)

    if os.path.exists(target_path):
        print(f"Repo already exists at {target_path}")
        return target_path

    cmd = ["git", "clone"]

    if branch:
        cmd += ["-b", branch]

    cmd += [repo_url, target_path]

    try:
        subprocess.run(cmd, check=True)
        print(f"Cloned into {target_path}")
        return target_path
    except subprocess.CalledProcessError as e:
        print("Error cloning repo:", e)
        return None
