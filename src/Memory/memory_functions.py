import os
import json
from src.config import CHAT_MEMORY_PATH

MEMORY_FILE = str(CHAT_MEMORY_PATH)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "chat_history": [],
            # "repo_context": {}
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def build_context(memory, user_input):
    chat_history = memory["chat_history"][-5:]
    context = ""
    for msg in chat_history:
        context += f"{msg['role']}: {msg['content']}\n"

    # Add repo ONLY when needed
    #  if intent in ["repo_query", "repo_task"]:
    #   context += f"\nRepo Context:\n{memory['repo_context']}\n"

    context += f"\nUser: {user_input}"
    return context
