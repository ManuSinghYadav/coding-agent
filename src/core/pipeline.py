import time
import threading
import traceback

from agents import trace, Runner

from src.mcp.mcp_servers import github_mcp_server
from src.agents.main_agent import github_agent
from src.memory.memory_functions import load_memory, save_memory, build_context


def spinner(stop_event):
    i = 0
    ANIMATION = ["   ", ".  ", ".. ", "...", " ..", "  .", "   "]
    while not stop_event.is_set():
        print(f"\rAgent: {ANIMATION[i % len(ANIMATION)]}", end="")
        time.sleep(0.2)
        i += 1


async def main_agent_loop():
    memory = load_memory()
    c = 0

    while c < 20:
        user_input = input("User: ")

        context = build_context(memory, user_input)

        result = None
        stop_loading = None
        thread = None

        try:
            stop_loading = threading.Event()

            thread = threading.Thread(target=spinner, args=(stop_loading,))
            thread.start()

            async with github_mcp_server:
                with trace("Coding-agent"):
                    result = await Runner.run(github_agent, context)

        except Exception:
            traceback.print_exc()

        finally:
            if stop_loading:
                stop_loading.set()
            if thread:
                thread.join()

        if result is not None:
            print(f"\rAgent: {result.final_output}")
            memory["chat_history"].append({"role": "user", "content": user_input})
            memory["chat_history"].append(
                {"role": "assistant", "content": result.final_output}
            )
        else:
            print("Agent: Error occurred")

        memory["chat_history"] = memory["chat_history"][-10:]
        save_memory(memory)

        c += 1
