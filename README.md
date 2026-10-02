# Production-Style RAG Assistant

A document question-answering system built using Retrieval-Augmented Generation (RAG).

The system allows users to ask questions about PDF documents. It retrieves relevant document chunks using vector similarity and uses an LLM to generate answers grounded in the retrieved context.

## Architecture

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Query Embedding
↓
Similarity Search
↓
Top-K Relevant Chunks
↓
LLM
↓
Grounded Answer

## Tech Stack

- Python
- Mistral API
- Mistral Embeddings
- ChromaDB
- PyPDF
- python-dotenv

## Features

- PDF text extraction
- Document chunking
- Chunk overlap
- Vector embeddings
- Persistent ChromaDB vector store
- Semantic search
- Top-K retrieval
- Context-aware LLM generation
- Source/page tracking
- Environment-based API key management

## Project Structure

```text
rag-assistant/
│
├── data/
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── ingestion.py
│   ├── vector_store.py
│   └── rag.py
│
├── ingest.py
├── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md