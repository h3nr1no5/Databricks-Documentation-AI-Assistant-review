import json

import os
import sys
from pathlib import Path

import chromadb
from tqdm import tqdm

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import DOCS_DIR, CHUNKS_DIR, EMBEDDING_MODEL

client = OpenAI()

db = chromadb.PersistentClient("vector_db")

collection = db.get_or_create_collection(
    name="databricks_docs"
)

with open(CHUNKS_DIR / "chunks.jsonl", encoding="utf8") as f:

    for line in tqdm(f):

        doc = json.loads(line)

        embedding = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=doc["text"]
        ).data[0].embedding

        collection.add(
            ids=[doc["id"]],
            embeddings=[embedding],
            documents=[doc["text"]],
            metadatas=[{
                "title": doc["title"],
                "url": doc["url"],
                "chunk_id": doc["chunk_id"]
            }]
        )

print(collection.count())