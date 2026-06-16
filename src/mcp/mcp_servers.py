from agents.mcp import MCPServerStreamableHttp
from src.mcp.mcp_params import github_params

github_mcp_server = MCPServerStreamableHttp(
    params=github_params, client_session_timeout_seconds=30
)
