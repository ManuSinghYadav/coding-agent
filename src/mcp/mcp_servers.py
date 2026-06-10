from agents.mcp import MCPServerStreamableHttp, MCPServerStdio
from src.mcp.mcp_params import github_params, memory_params

github_mcp_server = MCPServerStreamableHttp(params=github_params, client_session_timeout_seconds=30)
memory_mcp_server = MCPServerStdio(params=memory_params, client_session_timeout_seconds=30)
