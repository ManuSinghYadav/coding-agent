from agents import Agent

from src.instructions.system import instructions
from src.mcp.mcp_servers import github_mcp_server

from src.tools.check_if_already_cloned import check_if_already_cloned
from src.tools.clone_repo import clone_repo
from src.tools.index_builder import index_builder
from src.tools.index_retriever import file_filter
from src.tools.code_reading import read_code


github_agent = Agent (
	name="Github agent",
	instructions=instructions,
	model="gpt-4.1-mini",
	tools=[check_if_already_cloned, clone_repo, index_builder, file_filter, read_code],
	mcp_servers=[github_mcp_server]
)
