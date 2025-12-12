import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from rag.ingest import get_embedding, EMBEDDING_MODEL, EMBEDDING_DIMENSION, COLLECTION_NAME, cohere_client
import asyncio
import cohere

load_dotenv(override=True)

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_API_URL = os.getenv("QDRANT_API_URL")
COHERE_API = os.getenv("COHERE_API")

# Initialize Cohere client for async operations if available
cohere_async_client = cohere.AsyncClient(COHERE_API) if COHERE_API else None

client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)

async def retrieve_context(query: str, top_k: int = 3) -> list[str]:
    try:
        # Use async Cohere client if available, otherwise use sync
        if cohere_async_client:
            # Using async Cohere client
            response = await cohere_async_client.embed(
                texts=[query],
                model=EMBEDDING_MODEL,
                input_type="search_query"
            )
            query_vector = response.embeddings[0]
        else:
            # Fallback to sync method if async client is not available
            query_vector = cohere_client.embed(
                texts=[query],
                model=EMBEDDING_MODEL,
                input_type="search_query"
            ).embeddings[0]

        search_result = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=top_k,
            query_filter=None,
            with_payload=True
        )

        # Extract both text and source information
        context = []
        sources = []
        for hit in search_result:
            if hit.payload and "text" in hit.payload:
                context.append(hit.payload["text"])
                if "source" in hit.payload:
                    sources.append(hit.payload["source"])

        # Return both context and sources for the response
        return context, sources
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return ["Error retrieving context from the knowledge base."], []

if __name__ == "__main__":
    # Example usage
    async def test_retrieve():
        sample_query = "What are the applications of humanoid robotics?"
        context, sources = await retrieve_context(sample_query)
        print(f"Retrieved context for query '{sample_query}':\n{context}")
        print(f"Sources: {sources}")

    asyncio.run(test_retrieve())