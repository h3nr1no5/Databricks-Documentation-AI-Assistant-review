import streamlit as st

from src.assistant import Assistant

st.set_page_config(
    page_title="Databricks AI Assistant",
    layout="wide"
)

assistant = Assistant()

st.title("Databricks Documentation AI Assistant")

question = st.chat_input(
    "Ask anything about Databricks..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Searching documentation..."):

        response = assistant.ask(question)

    with st.chat_message("assistant"):

        st.write(response["answer"])

        with st.expander("📚 Sources"):

            for source in response["sources"]:

                st.markdown(
                    f"**{source['title']}**"
                )

                st.write(source["url"])

        with st.expander("🔎 Retrieved Context"):

            for doc in response["retrieved_docs"]:

                st.markdown(
                    f"### {doc['title']}"
                )

                st.caption(
                    f"Distance: {doc['distance']:.4f}"
                )

                st.write(doc["text"][:1200])

                st.divider()