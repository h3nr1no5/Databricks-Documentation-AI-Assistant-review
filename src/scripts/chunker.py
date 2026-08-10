from pathlib import Path
import json
import sys
import uuid

import tiktoken
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import CHUNKS_DIR, DOCS_DIR

OUTPUT = CHUNKS_DIR
INPUT = DOCS_DIR

OUTPUT.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT / "chunks.jsonl"

encoding = tiktoken.get_encoding("cl100k_base")

CHUNK_SIZE = 500
OVERLAP = 100


def chunk_text(text):
    tokens = encoding.encode(text)

    start = 0

    while start < len(tokens):

        end = start + CHUNK_SIZE

        yield encoding.decode(tokens[start:end])

        start += CHUNK_SIZE - OVERLAP


with open(OUTPUT_FILE, "w", encoding="utf8") as out:

    for file in tqdm(sorted(INPUT.glob("*.json"))):

        if file.name == "urls.json":
            continue

        with open(file, encoding="utf8") as f:
            doc = json.load(f)

        markdown = doc.get("markdown")

        if not markdown:
            continue

        for i, chunk in enumerate(chunk_text(markdown)):

            record = {
                "id": str(uuid.uuid4()),
                "title": doc.get("title", ""),
                "url": doc["url"],
                "chunk_id": i,
                "text": chunk
            }

            out.write(json.dumps(record) + "\n")

print("Finished chunking.")