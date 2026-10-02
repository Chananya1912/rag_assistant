from pypdf import PdfReader

from src.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):
        text = page.extract_text()

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    return pages


def chunk_pages(pages):
    chunks = []

    step = CHUNK_SIZE - CHUNK_OVERLAP

    for page in pages:

        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            if chunk.strip():

                chunks.append({
                    "text": chunk,
                    "metadata": {
                        "source": "doc.pdf",
                        "page": page_number
                    }
                })

            start += step

    return chunks