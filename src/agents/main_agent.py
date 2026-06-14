from agents import Agent
from src.instructions.system import agent_instructions
from src.mcp.mcp_servers import github_mcp_server


github_agent = Agent (
	name="Github agent",
	instructions=agent_instructions,
	model="gpt-4.1-mini",
	mcp_servers=[github_mcp_server]
)