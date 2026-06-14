from src.agents.main_agent import github_agent
from agents import trace, Runner
from src.mcp.mcp_servers import github_mcp_server


async def run_pipeline(prompt):
    async with github_mcp_server:
        with trace("Coding-agent"):
            result = await Runner.run(github_agent, prompt)

        return result
