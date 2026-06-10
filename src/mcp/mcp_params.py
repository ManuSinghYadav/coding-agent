from src.config import GITHUB_PAT
from src.config import MCP_MEMORY_FILE_PATH


if not GITHUB_PAT:
    raise RuntimeError("GITHUB_PAT is missing. Add it to .env before starting the GitHub MCP server.")

github_params = {"url": "https://api.githubcopilot.com/mcp/",
        "headers": {
            "Authorization": f"Bearer {GITHUB_PAT}"
        }
    }

memory_params = {"command": "npx","args": ["-y", "@modelcontextprotocol/server-memory"],"env": {"MEMORY_FILE_PATH": str(MCP_MEMORY_FILE_PATH)}}
