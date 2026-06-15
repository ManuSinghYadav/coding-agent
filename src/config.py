import os
from pathlib import Path
from dotenv import load_dotenv

from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = BASE_DIR.parent


load_dotenv(PROJECT_ROOT / ".env", override=True)

openai = OpenAI()

GITHUB_PAT = os.getenv("GITHUB_PAT")

CHAT_MEMORY_PATH = BASE_DIR / "memory" / "chat_memory.json"
