# RAG Chatbot for Physical AI & Humanoid Robotics

This repository contains an AI-powered RAG (Retrieval-Augmented Generation) chatbot designed specifically for the Physical AI & Humanoid Robotics textbook. The system leverages Google's Gemini embedding model to provide accurate, context-aware responses based on the textbook content.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Migration from Cohere to Gemini](#migration-from-cohere-to-gemini)
- [Configuration](#configuration)
- [Development](#development)

## Overview

The RAG chatbot system is designed to help students and researchers interact with the Physical AI & Humanoid Robotics textbook through natural language queries. The system extracts content from the textbook's sitemap, processes it into embeddings, stores it in a vector database, and responds to user queries with relevant context from the textbook.

Key capabilities:
- Natural language querying of textbook content
- Accurate retrieval of relevant passages
- Proper citation of source materials
- Scalable vector search using Qdrant
- Integration with Google's Gemini AI model

## Architecture

The system follows a classic RAG architecture:

1. **Ingestion Pipeline** (`rag/ingest.py`):
   - Fetches content from sitemap.xml
   - Extracts text using trafilatura
   - Chunks text into 2000-character segments
   - Generates embeddings using Google's text-embedding-004 model
   - Stores embeddings in Qdrant vector database

2. **Retrieval Component** (`rag/retrieve.py`):
   - Embeds user queries using the same model
   - Performs vector similarity search in Qdrant
   - Returns relevant text chunks and sources

3. **Chat Interface** (`my_agent/course_agent.py`):
   - Implements OpenAI Agents SDK
   - Orchestrates query processing
   - Generates contextual responses
   - Maintains conversation history

4. **API Layer** (`routers/chat.py`, `main.py`):
   - FastAPI endpoints for chat interaction
   - Request/response handling
   - CORS configuration

## Features

- **Intelligent Query Processing**: Natural language understanding for textbook content
- **Accurate Retrieval**: Semantic search using 768-dimensional embedding vectors
- **Source Attribution**: Responses include citations to original textbook sources
- **Rate Limit Management**: Handles API quotas and prevents rate limiting
- **Asynchronous Processing**: Non-blocking operations for better performance
- **Error Handling**: Robust error management and retry logic
- **Scalable Vector Storage**: Qdrant-based vector database for efficient similarity search

## Technical Stack

- **Backend**: Python 3.11, FastAPI
- **AI/ML**: Google Generative AI (text-embedding-004, Gemini Flash)
- **Vector Database**: Qdrant Cloud
- **AI Framework**: OpenAI Agents SDK
- **Data Processing**: Trafilatura (HTML to text extraction)
- **Package Management**: uv
- **HTTP Client**: Requests
- **Environment**: python-dotenv

## Directory Structure

```
physical-ai-and-humanoid-robotics/rag-chatbot/
├── main.py                 # FastAPI application entry point
├── .env                    # Environment variables
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Dependency lock file
├── my_agent/
│   └── course_agent.py     # OpenAI Agents SDK implementation
├── my_config/
│   └── gemini_config.py    # LLM configuration
├── rag/
│   ├── ingest.py           # Content ingestion and embedding
│   └── retrieve.py         # Vector retrieval and context extraction
└── routers/
    └── chat.py             # FastAPI chat endpoint
```

## Installation

1. Clone the repository
2. Install dependencies:
   ````
   uv sync
   ````
3. Set up environment variables in `.env`:
   - `QDRANT_API_KEY`: Your Qdrant Cloud API key
   - `QDRANT_API_URL`: Your Qdrant Cloud endpoint
   - `GEMINI_API_KEY`: Your Google Generative AI API key
   - `GEMINI_BASE_URL`: Base URL for Gemini API

4. Run the ingestion pipeline to populate the vector database:
   ````
   python rag/ingest.py
   ````

## Usage

1. Start the API server:
   ````
   uv run uvicorn main:app --reload
   ````
2. Access the chat endpoint at `/api/chat`
3. Send POST requests with a JSON body containing your query:
   ````
   {
     "message": "What are the key components of a humanoid robot?"
   }
   ````

## Migration from Cohere to Gemini

This system originally used Cohere's embedding model (embed-english-v3.0 with 1024-dimensional vectors). In December 2025, it was migrated to Google's text-embedding-004 model with 768-dimensional vectors.

### Migration Benefits:
- **Increased Rate Limits**: From 1000 requests/month to 1500 requests/day
- **Improved Performance**: Reduced API delay from 2 seconds to 0.5 seconds
- **Better Embedding Quality**: Enhanced semantic understanding
- **Cost Efficiency**: Leveraging Gemini's free tier

### Key Changes:
- Updated embedding model from Cohere to Google Generative AI
- Changed vector dimensions from 1024 to 768
- Modified rate limiting from monthly to daily quotas
- Updated Qdrant collection configuration for new vector dimensions

## Configuration

The system relies on several environment variables:

- `QDRANT_API_KEY`: Authentication key for Qdrant Cloud
- `QDRANT_API_URL`: Endpoint URL for Qdrant Cloud instance
- `GEMINI_API_KEY`: Google Generative AI API key
- `GEMINI_BASE_URL`: Base URL for Gemini API endpoints

## Frontend Integration

The RAG chatbot includes a floating chat button that appears on all pages of the Docusaurus site. This button toggles a chat window where users can ask questions about the book content.

The frontend components are located in the `physical-ai-and-humanoid-robotics/src/components/` directory:
- `ChatbotButton.tsx` - The floating button component
- `ChatbotWindow.tsx` - The chat interface component
- `ChatbotButton.module.css` - Styling for the button
- `ChatbotWindow.module.css` - Styling for the chat window

These components are integrated into the Docusaurus layout through the `physical-ai-and-humanoid-robotics/src/theme/Root.tsx` file, which makes them available on all pages.

## Frontend-Backend Integration

The frontend chatbot communicates with a deployed backend API at `https://giaic-hackathon-book-rag-2025-production.up.railway.app/api/chat`. When a user submits a question:

1. The frontend sends a POST request to the backend API with the user's message
2. The backend processes the query using the RAG pipeline (retrieval + generation)
3. The backend returns a response with optional sources
4. The frontend displays the response in the chat window

The integration is documented in detail in [INTEGRATION.md](INTEGRATION.md).

## Development

The project follows a structured development approach using the Spec-Kit Plus methodology:

1. **Specification**: Feature requirements documented in specs/
2. **Planning**: Implementation strategy in plan.md
3. **Tasking**: Detailed tasks in tasks.md
4. **Implementation**: Code changes following the task list
5. **Testing**: Validation of functionality

### Development Workflow

1. Create feature branch using the naming convention `###-feature-name`
2. Develop according to the task breakdown in `specs/###-feature-name/tasks.md`
3. Follow the 7-phase implementation plan:
   - Pre-migration audit
   - Dependency migration
   - Code migration
   - Data re-ingestion
   - Testing & validation
   - Cleanup & documentation

## Contributing

This project uses Claude Code and Spec-Kit Plus for AI-assisted development. Contributions should follow the established development workflow and maintain the project's architectural patterns.

## License

[Add license information as appropriate for your project]