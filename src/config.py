import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# src/config.py
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"

CHUNKS_DIR = DATA_DIR / "chunks"
DOCS_DIR = DATA_DIR / "docs"
SITEMAP_DIR = DATA_DIR / "sitemap"

api_key = os.getenv("OPENAI_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"

CHAT_MODEL = "gpt-4.1-mini"

TOP_K = 5

client = OpenAI(api_key=OPENAI_API_KEY)
if not api_key:
    raise ValueError(
        f"OPENAI_API_KEY not found. Expected .env at: {env_path}"
    )