import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

load_dotenv(PROJECT_ROOT / ".env", override=True)

GITHUB_PAT = os.getenv("GITHUB_PAT")

CHAT_MEMORY_PATH = BASE_DIR / "Memory" / "chat_memory.json"
