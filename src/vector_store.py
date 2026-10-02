import chromadb

from src.config import (
    CHROMA_PATH,
    COLLECTION_NAME
)


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)


collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def add_documents(chunks, embeddings):

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "documents": results["documents"][0],
        "metadatas": results["metadatas"][0],
        "distances": results["distances"][0]
    }


def get_collection_count():
    return collection.count()