# RAG Chatbot Implementation Checklist

## Data Fetching and Ingestion Tasks

- [X] Run ingestion script to populate Qdrant with sitemap content
- [X] Verify Qdrant collection has been created and contains data
- [X] Test retrieval functionality to ensure data can be fetched
- [X] Validate complete RAG pipeline with sample queries
- [X] Confirm sources are properly returned with responses
- [X] Test with various question types to ensure robustness
- [X] Fix ingestion script error: sitemap contains placeholder URLs (line 94 in ingest.py - sitemap_url, line 71 in ingest.py - fetch_and_clean_content call, line 42 in ingest.py - requests.get)
- [X] Optimize content extraction using trafilatura for better content cleaning (replace basic regex approach in fetch_and_clean_content function)
- [X] Reduce embedding API calls by improving content chunking strategy
- [X] Implement batch processing with extended delays to handle API rate limits