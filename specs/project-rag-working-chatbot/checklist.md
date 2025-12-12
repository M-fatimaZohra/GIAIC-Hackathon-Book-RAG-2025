# RAG Chatbot Implementation Checklist

## Data Fetching and Ingestion Tasks

- [ ] Run ingestion script to populate Qdrant with sitemap content
- [ ] Verify Qdrant collection has been created and contains data
- [ ] Test retrieval functionality to ensure data can be fetched
- [ ] Validate complete RAG pipeline with sample queries
- [ ] Confirm sources are properly returned with responses
- [ ] Test with various question types to ensure robustness
- [ ] Fix ingestion script error: sitemap contains placeholder URLs (line 94 in ingest.py - sitemap_url, line 71 in ingest.py - fetch_and_clean_content call, line 42 in ingest.py - requests.get)