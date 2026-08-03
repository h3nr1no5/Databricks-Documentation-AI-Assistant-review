import json
from pathlib import Path

import chromadb

client = chromadb.PersistentClient("vector_db")

collection = client.get_or_create_collection(
    "databricks"
)

INPUT = Path("data/embeddings")


for file in INPUT.glob("*.json"):

    with open(file, encoding="utf8") as f:

        docs = json.load(f)

    for doc in docs:

        collection.add(
            ids=[
                f"{file.stem}_{doc['chunk_id']}"
            ],
            embeddings=[
                doc["embedding"]
            ],
            documents=[
                doc["text"]
            ],
            metadatas=[
                {
                    "title": doc["title"],
                    "url": doc["url"],
                }
            ],
        )

print(collection.count())