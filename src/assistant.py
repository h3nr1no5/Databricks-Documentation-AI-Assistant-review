from src.config import client, CHAT_MODEL
from src.prompt_builder import (
    SYSTEM_PROMPT,
    PromptBuilder
)
from src.retriever import Retriever


class Assistant:

    def __init__(self):

        self.retriever = Retriever()

    def ask(self, question):

        docs = self.retriever.search(question)

        prompt = PromptBuilder.build(
            question,
            docs
        )

        response = client.responses.create(
            model=CHAT_MODEL,
            instructions=SYSTEM_PROMPT,
            input=prompt,
        )

        sources = []

        seen = set()

        for doc in docs:

            if doc["url"] not in seen:

                seen.add(doc["url"])

                sources.append(
                    {
                        "title": doc["title"],
                        "url": doc["url"]
                    }
                )

        return {
            "answer": response.output_text,
            "sources": sources,
            "retrieved_docs": docs
        }