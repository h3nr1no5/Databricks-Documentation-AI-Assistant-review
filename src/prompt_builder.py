SYSTEM_PROMPT = """
You are a Senior Databricks Solutions Architect.

You MUST answer ONLY from the supplied documentation.

Rules:

1. Never invent APIs.

2. Never use outside knowledge if the documentation is missing.

3. If the answer cannot be found, clearly state that.

4. Quote only small excerpts when necessary.

5. Always cite the relevant source URLs at the end.

6. Prefer concise technical explanations.
"""


class PromptBuilder:

    @staticmethod
    def build(question, docs):

        context = ""

        for i, doc in enumerate(docs, start=1):

            context += f"""
            ==================================================
            Document {i}

            Title:
            {doc['title']}

            URL:
            {doc['url']}

            Content:

            {doc['text']}

            ==================================================

            """

        prompt = f"""
        Answer the question using ONLY the documentation below.

        Documentation:

        {context}

        Question:

        {question}

        Answer:
        """

        return prompt