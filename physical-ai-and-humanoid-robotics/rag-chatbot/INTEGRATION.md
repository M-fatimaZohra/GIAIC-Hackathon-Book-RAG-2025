# Frontend-Backend Integration Documentation

## Overview
This document explains how the Docusaurus frontend chatbot UI integrates with the deployed FastAPI backend at `https://giaic-hackathon-book-rag-2025-production.up.railway.app/api/chat`.

## Architecture

### Frontend Components
- **ChatbotButton.tsx**: A floating button component that appears on all Docusaurus pages
- **ChatbotWindow.tsx**: The chat interface that displays messages and handles user input
- **Root.tsx**: Integrates both components globally across the Docusaurus site

### Backend Components
- **FastAPI Application**: Hosted at `https://giaic-hackathon-book-rag-2025-production.up.railway.app`
- **API Endpoint**: `/api/chat` accepts POST requests with user queries
- **RAG Pipeline**: Processes queries using vector search and Gemini LLM

## Integration Flow

1. User clicks the floating chat button on any Docusaurus page
2. Chat window appears with input field and message display
3. User types a message and clicks "Send"
4. Frontend makes a POST request to `https://giaic-hackathon-book-rag-2025-production.up.railway.app/api/chat`
5. Backend processes the query using RAG pipeline (retrieve + generate)
6. Backend returns response with optional sources
7. Frontend displays the response in the chat window

## API Contract

### Request
```
POST https://giaic-hackathon-book-rag-2025-production.up.railway.app/api/chat
Content-Type: application/json

{
  "message": "What is humanoid robotics?"
}
```

### Response
```
{
  "response": "Humanoid robotics is a subfield of robotics that focuses on the design...",
  "sources": [
    "https://giaic-hackathon-book-rag-2025.vercel.app/docs/chapter1/introduction"
  ]
}
```

## CORS Configuration

The backend is configured to allow requests from:
- `https://giaic-hackathon-book-rag-2025.vercel.app` (production Docusaurus site)
- `http://localhost:3000` (local development)

## Error Handling

- Network errors display an error message in the chat window
- Timeout after 30 seconds displays a timeout message
- Backend errors return appropriate HTTP status codes

## Deployment Notes

- Frontend: Deployed on Vercel at `https://giaic-hackathon-book-rag-2025.vercel.app`
- Backend: Deployed on Railway at `https://giaic-hackathon-book-rag-2025-production.up.railway.app`
- Both use HTTPS for secure communication