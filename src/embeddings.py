from mistralai.client import Mistral

from src.config import (
    MISTRAL_API_KEY,
    EMBEDDING_MODEL
)


client = Mistral(
    api_key=MISTRAL_API_KEY
)


def create_embeddings(texts):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        inputs=texts
    )

    return [
        item.embedding
        for item in response.data
    ]


def create_query_embedding(query):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        inputs=[query]
    )

    return response.data[0].embedding