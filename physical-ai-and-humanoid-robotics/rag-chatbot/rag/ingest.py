import os
import requests
import xml.etree.ElementTree as ET
import time
import traceback
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Distance, VectorParams
from google import genai
import trafilatura

load_dotenv(override=True)

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_API_URL = os.getenv("QDRANT_API_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SITEMAP_URL = "https://giaic-hackathon-book-rag-2025.vercel.app/sitemap.xml"
COLLECTION_NAME = "physical-ai-and-humanoid-robotics"

client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)
genai_client = genai.Client()

# Track API calls to respect daily limit
api_call_count = 0
MAX_DAILY_CALLS = 1500  # Gemini free tier limit

def get_all_urls():
    """Fetch sitemap and extract all URLs"""
    try:
        print("Step 1: Fetching sitemap from URL...")
        response = requests.get(SITEMAP_URL)
        response.raise_for_status()
        print(f"Step 1: Sitemap fetched successfully, status code: {response.status_code}")

        print("Step 2: Parsing sitemap XML...")
        root = ET.fromstring(response.content)
        print("Step 2: Sitemap XML parsed successfully")

        print("Step 3: Extracting URLs from sitemap...")
        urls = [elem.text for elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        print(f"Step 3: Found {len(urls)} URLs in sitemap")

        return urls
    except requests.exceptions.HTTPError as e:
        print(f"ERROR in get_all_urls - HTTP Error: {e}")
        print(f"Status code: {e.response.status_code}")
        print(f"Response text: {e.response.text[:500]}...")  # First 500 chars
        raise
    except requests.exceptions.RequestException as e:
        print(f"ERROR in get_all_urls - Request Error: {e}")
        raise
    except ET.ParseError as e:
        print(f"ERROR in get_all_urls - XML Parse Error: {e}")
        print(f"Response content (first 1000 chars): {response.content[:1000]}")
        raise
    except Exception as e:
        print(f"ERROR in get_all_urls - Unexpected Error: {e}")
        raise

def extract_text_from_url(url):
    """Fetch HTML and extract clean text using trafilatura"""
    try:
        print(f"Step 4: Extracting text from URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        print(f"Step 4: Successfully fetched content from {url}, status code: {response.status_code}")

        print(f"Step 5: Extracting text using trafilatura from {url}...")
        text = trafilatura.extract(response.text, include_comments=False, include_tables=True, include_formatting=True)
        print(f"Step 5: Text extraction completed for {url}, text length: {len(text) if text else 0}")

        return text if text else ""
    except requests.exceptions.HTTPError as e:
        print(f"ERROR in extract_text_from_url for {url} - HTTP Error: {e}")
        print(f"Status code: {e.response.status_code}")
        print(f"Response text: {e.response.text[:500]}...")  # First 500 chars
        raise
    except requests.exceptions.RequestException as e:
        print(f"ERROR in extract_text_from_url for {url} - Request Error: {e}")
        raise
    except Exception as e:
        print(f"ERROR in extract_text_from_url for {url} - Unexpected Error: {e}")
        raise

def chunk_text(text, chunk_size=2000):
    """Split text into chunks of about 2000 characters, splitting on '. '"""
    if not text:
        return []

    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        sentence_with_period = sentence + '. '
        if len(current_chunk + sentence_with_period) <= chunk_size:
            current_chunk += sentence_with_period
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence_with_period

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def embed(text):
    """Generate embedding using Gemini with rate limiting"""
    global api_call_count

    try:
        print(f"Step 6: Generating embedding for text of length {len(text)}...")

        # Check if we're approaching the API limit
        if api_call_count >= MAX_DAILY_CALLS:
            print(f"Warning: Reached API call limit of {MAX_DAILY_CALLS}. Stopping.")
            raise Exception("Daily API limit reached")

        # Reduce delay to 0.5 seconds as per Gemini's better rate limits
        print(f"Step 6.1: Waiting before API call (call #{api_call_count + 1})...")
        time.sleep(0.5)  # 0.5 second delay between API calls - reduced from 2 seconds

        result = genai_client.models.embed_content(
            model="text-embedding-004",
            contents=[text]  # Pass as list as shown in the example
        )

        # Extract the embedding from the result
        embedding = result.embeddings[0].values
        api_call_count += 1
        print(f"Step 6: Embedding generated successfully, vector dimension: {len(embedding)}, API calls used: {api_call_count}/{MAX_DAILY_CALLS}")
        return embedding
    except Exception as e:
        print(f"ERROR in embed function - Embedding Error: {e}")
        # Add a longer wait if we hit rate limits
        if "quota" in str(e).lower() or "rate" in str(e).lower():
            print("Waiting 60 seconds due to quota/rate limit error...")
            time.sleep(60)
            # Retry once after waiting
            result = genai_client.models.embed_content(
                model="text-embedding-004",
                contents=[text]  # Pass as list as shown in the example
            )

            # Extract the embedding from the result
            embedding = result.embeddings[0].values
            api_call_count += 1
            print(f"Step 6: Embedding generated successfully after retry, vector dimension: {len(embedding)}, API calls used: {api_call_count}/{MAX_DAILY_CALLS}")
            return embedding
        else:
            raise

def create_collection():
    """Create Qdrant collection with 768-dimensional vectors (Gemini)"""
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),  # 768-dim for Gemini
    )
    print(f"Collection '{COLLECTION_NAME}' created with 768-dimensional vectors.")

def save_chunk_to_qdrant(chunk, url, chunk_id):
    """Save a single chunk to Qdrant"""
    try:
        print(f"Step 7: Saving chunk {chunk_id} from {url} to Qdrant...")
        print(f"Step 7.1: Chunk length: {len(chunk)}")
        print(f"Step 7.2: Generating embedding...")

        vector = embed(chunk)
        print(f"Step 7.3: Embedding generated, dimension: {len(vector)}")

        print(f"Step 7.4: Creating Qdrant point with ID...")
        point_id = abs(hash(f"{url}-{chunk_id}"))
        print(f"Step 7.4: Point ID generated: {point_id}")

        point = models.PointStruct(
            id=point_id,
            vector=vector,
            payload={
                "text": chunk,
                "source": url,
                "chunk_id": chunk_id
            }
        )
        print(f"Step 7.5: Qdrant point created")

        print(f"Step 8: Upserting vector to Qdrant collection '{COLLECTION_NAME}'...")
        print(f"Step 8.1: About to call client.upsert with collection: {COLLECTION_NAME}")
        print(f"Step 8.2: Point ID: {point_id}, Vector length: {len(vector)}")

        client.upsert(collection_name=COLLECTION_NAME, points=[point])
        print(f"Step 8: Successfully saved chunk {chunk_id} from {url} to Qdrant")

    except Exception as e:
        print(f"ERROR in save_chunk_to_qdrant for {url}, chunk {chunk_id} - Qdrant Error: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        raise

def ingest_book():
    """Full pipeline: load URLs → extract → chunk → embed → store"""
    try:
        print("=== STARTING INGESTION PROCESS ===")
        print("Step 0: Starting ingestion pipeline...")
        print("Starting ingestion...")

        print("Step 1: Fetching URLs from sitemap...")
        urls = get_all_urls()
        print(f"Step 1: Found {len(urls)} URLs in sitemap")

        print("Step 2: Creating Qdrant collection...")
        create_collection()
        print("Step 2: Qdrant collection created successfully")

        print("Step 3: Processing each URL...")
        total_chunks = 0
        for i, url in enumerate(urls):
            print(f"Processing page {i+1}/{len(urls)}: {url}")
            try:
                print(f"Step 3.{i+1}.1: Extracting text from {url}...")
                text = extract_text_from_url(url)
                print(f"Step 3.{i+1}.2: Text extraction completed, length: {len(text) if text else 0}")

                if text:
                    print(f"Step 4: Chunking text for {url}...")
                    chunks = chunk_text(text)
                    print(f"Step 4: Text chunked into {len(chunks)} chunks for {url}")

                    for j, chunk in enumerate(chunks):
                        print(f"Step 5: Processing chunk {j+1}/{len(chunks)} for {url} [length: {len(chunk)}]...")
                        print(f"Step 5.{j+1}.1: Calling save_chunk_to_qdrant for chunk {j} of {url}")
                        save_chunk_to_qdrant(chunk, url, f"{i}-{j}")
                        total_chunks += 1
                        print(f"Step 5.{j+1}.2: Completed save_chunk_to_qdrant for chunk {j} of {url}")
                        print(f"Step 5: Completed chunk {j+1}/{len(chunks)} for {url}")
                else:
                    print(f"Warning: No text extracted from {url}")
            except Exception as e:
                print(f"ERROR processing URL {url}: {e}")
                import traceback
                print(f"Full traceback: {traceback.format_exc()}")
                continue  # Continue with next URL even if one fails

        print(f"Ingestion completed! Processed {len(urls)} pages and {total_chunks} chunks.")
        print("=== INGESTION PROCESS COMPLETED ===")
    except Exception as e:
        print(f"=== FATAL ERROR IN INGESTION PROCESS ===")
        print(f"ERROR in ingest_book - Main Process Error: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        raise

if __name__ == "__main__":
    ingest_book()