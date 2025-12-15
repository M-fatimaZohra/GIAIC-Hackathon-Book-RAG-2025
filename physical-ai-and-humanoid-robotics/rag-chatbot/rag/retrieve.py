import os
import traceback
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
import asyncio
from google import genai

load_dotenv(override=True)

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_API_URL = os.getenv("QDRANT_API_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
genai_client = genai.Client()

client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)

async def retrieve_context(query: str, top_k: int = 3) -> list[str]:
    COLLECTION_NAME = "physical-ai-and-humanoid-robotics"  # Same as in ingest.py
    try:
        print(f"Retrieval Step 1: Starting context retrieval for query: '{query[:50]}...'")

        # Generate query embedding with Gemini
        print("Retrieval Step 2: Generating query embedding with Gemini...")
        result = genai_client.models.embed_content(
            model="text-embedding-004",
            contents=[query]  # Pass as list as shown in the example
        )
        query_vector = result.embeddings[0].values

        print(f"Retrieval Step 2: Query embedding completed with dimension {len(query_vector)}")

        print(f"Retrieval Step 3: Searching in Qdrant collection '{COLLECTION_NAME}'...")
        search_result = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=top_k,
            with_payload=True
        )

        # Extract context directly from points
        context = [point.payload["text"] for point in search_result.points]
        sources = [point.payload.get("source", "") for point in search_result.points if point.payload and "source" in point.payload]

        print(f"Retrieval Step 3: Qdrant search completed, found {len(context)} results")

        print(f"Retrieval Step 4: Context extraction completed. Retrieved {len(context)} context chunks and {len(sources)} sources.")

        # Return both context and sources for the response
        return context, sources
    except Exception as e:
        print(f"ERROR in retrieve_context - Retrieval Error: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        return ["Error retrieving context from the knowledge base."], []

if __name__ == "__main__":
    # Example usage for Gemini embedding retrieval
    async def test_retrieve():
        sample_query = "What are the applications of humanoid robotics?"
        context, sources = await retrieve_context(sample_query)
        print(f"Retrieved context for query '{sample_query}':\n{context}")
        print(f"Sources: {sources}")

    asyncio.run(test_retrieve())