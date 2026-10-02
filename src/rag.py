from mistralai.client import Mistral

from src.config import (
    MISTRAL_API_KEY,
    LLM_MODEL
)

from src.embeddings import create_query_embedding
from src.vector_store import search


client = Mistral(
    api_key=MISTRAL_API_KEY
)


def retrieve_context(query, top_k=3):

    query_embedding = create_query_embedding(
        query
    )

    results = search(
        query_embedding,
        top_k
    )

    return results


def generate_answer(query, results):

    documents = results["documents"]
    metadatas = results["metadatas"]

    context_parts = []

    for i, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1
    ):

        context_parts.append(
            f"""
Source {i}
Page: {metadata.get("page")}

{document}
"""
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
Answer the user's question using only the provided context.

If the answer cannot be found in the context,
say that the information is not available in
the provided document.

Context:
{context}

Question:
{query}
"""

    response = client.chat.complete(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a document question-answering "
                    "assistant. Use only the provided context."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return answer, metadatas