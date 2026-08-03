import chromadb

from openai import OpenAI
from src.config import EMBEDDING_MODEL, TOP_K

client = OpenAI()

db = chromadb.PersistentClient("vector_db")
collection = db.get_collection("databricks_docs")


class Retriever:

    def search(self, question: str):

        embedding = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=question
        ).data[0].embedding

        results = collection.query(
            query_embeddings=[embedding],
            n_results=TOP_K,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        retrieved = []

        for doc, meta, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):

            retrieved.append(
                {
                    "text": doc,
                    "title": meta["title"],
                    "url": meta["url"],
                    "chunk_id": meta["chunk_id"],
                    "distance": distance
                }
            )

        return retrieved