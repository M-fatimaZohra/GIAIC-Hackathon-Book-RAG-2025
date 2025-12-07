import os
import requests
import re
import xml.etree.ElementTree as ET
from urllib.parse import urljoin
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Distance, VectorParams
from my_config.gemini_config import CLIENT # Import the AsyncOpenAI client
import cohere
import asyncio

load_dotenv()

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_API_URL = os.getenv("QDRANT_API_URL")
COHERE_API = os.getenv("COHERE_API")

cohere_client = cohere.Client(COHERE_API)
client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = "docusaurus_book"
EMBEDDING_MODEL = "embed-english-v3.0" # Using Cohere's embedding model
EMBEDDING_DIMENSION = 1024 # Cohere's embed-english-v3.0 dimension

async def get_embedding(text: str) -> list[float]:
    try:
        response = cohere_client.embed(texts=[text], model=EMBEDDING_MODEL, input_type="search_document")
        return response.embeddings[0]
    except Exception as e:
        print(f"Error generating embedding with Cohere: {e}")
        return [0.0] * EMBEDDING_DIMENSION # Return dummy on error

def fetch_sitemap(sitemap_url: str) -> list[str]:
    response = requests.get(sitemap_url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    urls = [elem.text for elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

def fetch_and_clean_content(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    html_content = response.text
    # Basic regex to remove HTML tags. This is a simplification.
    cleaned_text = re.sub(r'<[^>]+>', '', html_content)
    return cleaned_text.strip()

def chunk_content(text: str, chunk_size: int = 1000, overlap: int = 100) -> list[str]:
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

async def ingest_documents(sitemap_url: str):
    urls = fetch_sitemap(sitemap_url)

    # Create Qdrant collection if it doesn't exist
    if not client.collection_exists(collection_name=COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=EMBEDDING_DIMENSION, distance=Distance.COSINE),
        )
        print(f"Collection '{COLLECTION_NAME}' created.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")

    points = []
    for url in urls:
        print(f"Processing {url}")
        content = fetch_and_clean_content(url)
        chunks = chunk_content(content)
        for i, chunk in enumerate(chunks):
            embedding = await get_embedding(chunk)
            points.append(
                models.PointStruct(
                    id=f"{url}-{i}".__hash__(), # Generate a unique ID
                    vector=embedding,
                    payload={
                        "text": chunk,
                        "source": url,
                        "chunk_id": i
                    },
                )
            )

    if points:
        client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
        print(f"Upserted {len(points)} points to Qdrant collection '{COLLECTION_NAME}'.")
    else:
        print("No documents to upsert.")

if __name__ == "__main__":
    sitemap_url = "https://giaic-hackathon-book-rag-2025.vercel.app/sitemap.xml"
    asyncio.run(ingest_documents(sitemap_url))
