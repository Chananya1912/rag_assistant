import sys

from src.ingestion import (
    load_pdf,
    chunk_pages
)

from src.embeddings import (
    create_embeddings
)

from src.vector_store import (
    add_documents,
    get_collection_count
)


def main():

    if len(sys.argv) < 2:
        print("Usage: python ingest.py <pdf_path>")
        return

    pdf_path = sys.argv[1]

    print("Loading PDF...")

    pages = load_pdf(pdf_path)

    print(f"Pages loaded: {len(pages)}")

    print("Creating chunks...")

    chunks = chunk_pages(pages)

    print(f"Chunks created: {len(chunks)}")

    print("Creating embeddings...")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = create_embeddings(texts)

    print("Storing in ChromaDB...")

    add_documents(
        chunks,
        embeddings
    )

    print(
        f"Documents in database: "
        f"{get_collection_count()}"
    )

    print("Ingestion completed!")


if __name__ == "__main__":
    main()