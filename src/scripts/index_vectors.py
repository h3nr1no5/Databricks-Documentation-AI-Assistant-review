import json

import sys
from pathlib import Path

import chromadb
from tqdm import tqdm

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import CHUNKS_DIR, EMBEDDING_MODEL

BATCH_SIZE = 100

client = OpenAI()

db = chromadb.PersistentClient("vector_db")

collection = db.get_or_create_collection(
    name="databricks_docs"
)

with open(CHUNKS_DIR / "chunks.jsonl", encoding="utf8") as f:

    docs = [json.loads(line) for line in f]

for i in tqdm(range(0, len(docs), BATCH_SIZE)):

    batch = docs[i : i + BATCH_SIZE]

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=[doc["text"] for doc in batch],
    )

    collection.upsert(
        ids=[doc["id"] for doc in batch],
        embeddings=[item.embedding for item in response.data],
        documents=[doc["text"] for doc in batch],
        metadatas=[{
            "title": doc["title"],
            "url": doc["url"],
            "chunk_id": doc["chunk_id"]
        } for doc in batch],
    )

print(collection.count())