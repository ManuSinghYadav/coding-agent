from src.config import GITHUB_PAT


if not GITHUB_PAT:
    raise RuntimeError("GITHUB_PAT is missing. Add it to .env before starting the GitHub MCP server.")

github_params = {"url": "https://api.githubcopilot.com/mcp/",
        "headers": {
            "Authorization": f"Bearer {GITHUB_PAT}"
        }
    }