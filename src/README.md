# 🚀 Databricks Documentation AI Assistant

> An end-to-end Retrieval-Augmented Generation (RAG) application that enables natural language interaction with the official Databricks documentation using semantic search, vector embeddings, and OpenAI models.

---

# 🎯 Problem Statement

Databricks documentation spans hundreds of technical pages covering Spark, Delta Lake, Unity Catalog, Workflows, SQL, ML, Governance, and platform administration.

Finding precise information often requires navigating multiple documentation pages and manually connecting concepts.

This project addresses that challenge by building an AI-powered documentation assistant that:

* understands natural language questions
* retrieves the most relevant documentation sections using semantic search
* generates grounded answers using Retrieval-Augmented Generation (RAG)
* cites the official documentation used to generate every response

Instead of relying solely on an LLM's pretrained knowledge, the assistant retrieves relevant documentation first, significantly improving answer accuracy and reducing hallucinations.

---

# ✨ Features

## Documentation Pipeline

* Automated sitemap discovery
* Bulk documentation download
* HTML → Markdown conversion
* Metadata preservation
* Incremental indexing ready

## Knowledge Base

* Token-aware chunking
* Configurable overlap
* OpenAI Embeddings
* Persistent vector database
* Semantic indexing

## AI Assistant

* Natural language question answering
* Context-aware retrieval
* Source citations
* Grounded responses
* Hallucination reduction

## User Interface

* Interactive Streamlit chat
* Retrieved source visualization
* Retrieved context inspection
* Simple deployment

---

# 🏗 System Architecture

```text
                       Official Databricks Documentation
                                      │
                                      ▼
                            Documentation Ingestion
                       (Sitemap + HTML Download + Parsing)
                                      │
                                      ▼
                             Markdown Document Store
                                      │
                                      ▼
                           Token-based Chunk Generator
                                      │
                                      ▼
                           OpenAI Embedding Generation
                                      │
                                      ▼
                              Chroma Vector Database
                                      │
                                      ▼
                              Semantic Vector Search
                                      │
                                      ▼
                               Prompt Construction
                                      │
                                      ▼
                            OpenAI Responses API
                                      │
                                      ▼
                           Grounded AI Generated Answer
                                      │
                                      ▼
                              Streamlit Web Interface
```

---

# ⚙️ Technology Stack

| Category        | Technology             |
| --------------- | ---------------------- |
| Language        | Python 3.12            |
| LLM             | OpenAI Responses API   |
| Embeddings      | text-embedding-3-small |
| Vector Database | ChromaDB               |
| Tokenizer       | tiktoken               |
| Web UI          | Streamlit              |
| HTML Extraction | Trafilatura            |
| HTTP Client     | requests               |
| Configuration   | python-dotenv          |

---

# 📂 Project Structure

```text
Databricks-Documentation-AI-Assistant/

├── app.py
├── pyproject.toml
├── uv.lock
├── README.md
│
├── src/
│   ├── assistant.py
│   ├── config.py
│   ├── prompt_builder.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── scripts/
│       ├── download_sitemap.py
│       ├── download_docs.py
│       ├── chunker.py
│       └── index_vectors.py
│
├── data/
│   ├── raw/
│   ├── chunks/
│   └── urls.json
│
└── vector_db/
```

---

# 🔄 End-to-End Pipeline

## 1. Documentation Discovery

Retrieve all documentation URLs from the official Databricks sitemap.

```
Sitemap
   ↓
Documentation URLs
```

---

## 2. Documentation Ingestion

Download documentation pages and convert them into clean Markdown.

```
Documentation URL
        ↓
HTML Download
        ↓
Markdown Extraction
```

---

## 3. Chunk Generation

Split documentation into overlapping token-aware chunks for semantic retrieval.

```
Markdown
    ↓
Tokenization
    ↓
Chunks
```

---

## 4. Embedding Generation

Convert each chunk into a dense vector representation using OpenAI embeddings.

```
Chunk
   ↓
Embedding
```

---

## 5. Vector Indexing

Store embeddings and metadata inside ChromaDB.

Stored metadata includes:

* Title
* URL
* Chunk ID
* Document Content

---

## 6. Semantic Retrieval

```
Question
     ↓
Embedding
     ↓
Vector Similarity Search
     ↓
Top-K Chunks
```

---

## 7. Retrieval-Augmented Generation

```
Retrieved Context
       ↓
Prompt Builder
       ↓
OpenAI Responses API
       ↓
Grounded Answer
```

---

# 📊 Dataset Statistics

| Metric                      |                             Value |
| --------------------------- | --------------------------------: |
| Documentation Pages Indexed |                               291 |
| Source                      | Official Databricks Documentation |
| Chunking Strategy           |                       Token-based |
| Embedding Model             |            text-embedding-3-small |
| Vector Database             |                          ChromaDB |

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/<username>/Databricks-Documentation-AI-Assistant.git

cd Databricks-Documentation-AI-Assistant
```

---

## Install Dependencies

Using uv

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## Configure

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key
```

---

# 📥 Build the Knowledge Base

Download documentation URLs

```bash
python src/scripts/download_sitemap.py
```

Download documentation

```bash
python src/scripts/download_docs.py
```

Generate chunks

```bash
python src/scripts/chunker.py
```

Generate embeddings and build the vector database

```bash
python src/scripts/index_vectors.py
```

---

# 💬 Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 💡 Example Questions

* What is Unity Catalog?
* Explain Delta Lake architecture.
* What is Photon?
* How do Workflows differ from Jobs?
* Explain Auto Loader.
* What are cluster policies?
* How do I optimize Spark performance?
* Explain Delta Live Tables.
* How does Unity Catalog manage permissions?
* What is Databricks Connect?

---

# 📸 Demo

## Chat Interface

```
User
──────

What is Unity Catalog?

Assistant
─────────

Unity Catalog is Databricks' unified governance solution...

Sources

• https://docs.databricks.com/...
• https://docs.databricks.com/...
```

---

# 📈 Performance

Current implementation:

* Semantic vector search
* Persistent vector database
* Grounded responses
* Source attribution

Potential production optimizations:

* Response streaming
* Retrieval caching
* Batch embedding generation
* Parallel document ingestion
* Metadata filtering

---

# 🛣 Roadmap

* Hybrid Search (BM25 + Vector Search)
* Cross-Encoder Re-ranking
* PostgreSQL + pgvector backend
* Conversation Memory
* Streaming Responses
* Incremental Documentation Refresh
* REST API
* Docker Deployment
* Kubernetes Deployment
* Authentication
* Monitoring & Observability

---

# 🤝 Acknowledgements

* Databricks for providing comprehensive public documentation.
* DataTalks.Club LLM Zoomcamp for introducing practical Retrieval-Augmented Generation concepts.

---

# 📄 License

This project is provided for educational and portfolio purposes.

Documentation content remains the property of Databricks and is retrieved from publicly available official documentation.