import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from my_config.gemini_config import CLIENT
from rag.ingest import get_embedding, EMBEDDING_MODEL, EMBEDDING_DIMENSION, COLLECTION_NAME, cohere_client
import asyncio

load_dotenv(override=True)

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_API_URL = os.getenv("QDRANT_API_URL")

client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)

async def retrieve_context(query: str, top_k: int = 3) -> list[str]:
    query_vector = (await cohere_client.embed(texts=[query], model=EMBEDDING_MODEL, input_type="search_query")).embeddings[0]

    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k,
        query_filter=None,
        with_payload=True
    )

    context = [hit.payload["text"] for hit in search_result if hit.payload and "text" in hit.payload]
    return context

if __name__ == "__main__":
    # Example usage
    sample_query = "What are the applications of humanoid robotics?"
    retrieved_context = asyncio.run(retrieve_context(sample_query))
    print(f"Retrieved context for query '{sample_query}':\n{retrieved_context}")
