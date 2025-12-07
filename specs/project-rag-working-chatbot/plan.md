# Implementation Plan: RAG Chatbot Integration for Docusaurus Book

## 1. Project Setup and Environment Configuration

**Phase Goal**: Establish the foundational project structure and configure the development environment.

### 1.1. Folder Structure Establishment

*   **Action**: Verify and, if necessary, create the following directory structure:
    ```
    00-my-research-papar/
    ├── physical-ai-and-humanoid-robotics/
    │   ├── src/
    │   │   ├── components/       # For ChatbotButton.tsx, ChatbotWindow.tsx
    │   └── rag-chatbot/
    │       ├── my_config/        # For gemini_config.py
    │       ├── my_agent/         # For course_agent.py
    │       ├── routers/          # For chat.py
    │       ├── rag/              # For ingest.py, retrieve.py
    │       ├── main.py
    │       └── .env.example
    ├── specs/project-rag-working-chatbot/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ```

### 1.2. Dependency Installation

*   **Action**: Navigate to `00-my-research-papar/physical-ai-and-humanoid-robotics/rag-chatbot`.
*   **Action**: Install Python dependencies using `uv`:
    ```bash
    uv add openai-agents python-dotenv qdrant-client requests cohere fastapi uvicorn
    ```

### 1.3. Environment Variables Configuration

*   **Action**: Create a `.env` file within `00-my-research-papar/physical-ai-and-humanoid-robotics/rag-chatbot` based on `.env.example`.
*   **Action**: Populate the `.env` file with placeholders for the following variables:
    *   `QDRANT_API_KEY`
    *   `QDRANT_API_URL`
    *   `GEMINI_API_KEY`
    *   `GEMINI_BASE_URL`
    *   `COHERE_API` (Optional, if Cohere is used for embeddings)

## 2. Backend Development (FastAPI + RAG + Qdrant + Gemini)

**Phase Goal**: Implement the core RAG chatbot logic and expose it via a FastAPI endpoint.

### 2.1. Gemini Configuration (`my_config/gemini_config.py`)

*   **Action**: Create `my_config/gemini_config.py`.
*   **Action**: Implement the `AsyncOpenAI` client configuration, loading `GEMINI_API_KEY` and `GEMINI_BASE_URL` from environment variables.
    ```python
    # Example snippet
    import os
    from openai import AsyncOpenAI
    from dotenv import load_dotenv

    load_dotenv()

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")

    CLIENT = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)
    # MODEL = OpenAIChatCompletionsModel(model="gemini-pro", client=CLIENT) # Will be defined in course_agent.py
    ```

### 2.2. RAG Pipeline - Ingestion (`rag/ingest.py`)

*   **Action**: Create `rag/ingest.py`.
*   **Action**: Implement functionality to:
    *   Fetch `https://giaic-hackathon-book-rag-2025.vercel.app/sitemap.xml`.
    *   Parse the sitemap to get book content URLs.
    *   Fetch content from each URL.
    *   Clean and chunk the content.
    *   Generate embeddings for chunks using a selected embedding model (e.g., from `openai-agents` or Cohere).
    *   Store embeddings and text chunks in Qdrant.

**Decision Needed**: Sitemap ingestion approach (e.g., `requests` for fetching, `BeautifulSoup` for parsing HTML, chunking strategy).

### 2.3. RAG Pipeline - Retrieval (`rag/retrieve.py`)

*   **Action**: Create `rag/retrieve.py`.
*   **Action**: Implement functionality to:
    *   Receive a user query.
    *   Embed the query using the same model as ingestion.
    *   Perform a similarity search in Qdrant to retrieve top-k relevant document chunks.

### 2.4. Agent Configuration (`my_agent/course_agent.py`)

*   **Action**: Create `my_agent/course_agent.py`.
*   **Action**: Define the `course_agent` using `openai-agents` SDK.
*   **Action**: Integrate the Gemini client (`CLIENT` from `gemini_config.py`) as the LLM.
*   **Action**: Integrate `rag/retrieve.py` as a tool for the agent.
*   **Action**: Implement logic for the agent to process queries, use the retrieval tool, and generate responses.

### 2.5. FastAPI Chat Router (`routers/chat.py`)

*   **Action**: Create `routers/chat.py`.
*   **Action**: Define a FastAPI router with a `POST /chat` endpoint.
*   **Action**: The endpoint should:
    *   Receive a JSON request with a `message` field.
    *   Pass the message to the `course_agent`.
    *   Return the agent's response, including any retrieved sources.

### 2.6. Main FastAPI Application (`main.py`)

*   **Action**: Create `main.py`.
*   **Action**: Initialize the FastAPI application.
*   **Action**: Include the `chat` router.
*   **Action**: Configure CORS policies to allow requests from the Docusaurus frontend.
*   **Action**: Add basic input validation and rate limiting.

## 3. Frontend Development (Docusaurus)

**Phase Goal**: Integrate the chatbot UI components into the Docusaurus site.

### 3.1. Chatbot UI Components (`src/components/`)

*   **Action**: Create `src/components/ChatbotButton.tsx` for the floating button.
*   **Action**: Create `src/components/ChatbotWindow.tsx` for the chat interface.
*   **Action**: Implement React logic for toggling the chat window visibility and sending/receiving messages to/from the backend.

**Decision Needed**: Floating UI design (position, styling, animation).

### 3.2. Global Integration

*   **Action**: Integrate `ChatbotButton.tsx` and `ChatbotWindow.tsx` into the Docusaurus layout. This may involve:
    *   Swizzling a Docusaurus theme component (e.g., `Layout`) if necessary.
    *   Adding components to a global wrapper if available.
*   **Action**: Ensure UI does not break Docusaurus navigation or theme.

### 3.3. Styling

*   **Action**: Add custom CSS rules to `physical-ai-and-humanoid-robotics/src/css/custom.css` for styling the chatbot components.

## 4. Frontend-Backend Integration

**Phase Goal**: Ensure seamless communication between the Docusaurus frontend and the FastAPI backend.

*   **Action**: Verify that the frontend components correctly send requests to `FastAPI_BASE_URL/api/chat`.
*   **Action**: Confirm that the frontend correctly parses and displays responses from the backend.

## 5. Testing Strategy

**Phase Goal**: Validate the functionality, performance, and accuracy of the integrated system.

### 5.1. Unit Testing

*   **Action**: Write unit tests for `gemini_config.py`, `ingest.py`, `retrieve.py`, and `course_agent.py`.
*   **Action**: Test individual FastAPI router endpoints (`chat.py`).

### 5.2. Integration Testing

*   **Action**: Validate backend API endpoints for correct request/response handling.
*   **Action**: Test the vector search accuracy by querying Qdrant directly and ensuring relevant chunks are returned.
*   **Action**: Test the end-to-end RAG pipeline, from query to contextualized response.

### 5.3. Frontend Testing

*   **Action**: Verify the frontend chatbot button toggles correctly.
*   **Action**: Ensure the chat window displays messages and responses properly.
*   **Action**: Validate that the UI does not break Docusaurus navigation or theme.

### 5.4. End-to-End Testing

*   **Action**: Perform full end-to-end tests: User query in Docusaurus frontend -> FastAPI -> Qdrant -> Gemini -> FastAPI -> Docusaurus frontend.

## Decisions Needing Documentation

*   **Branch Name**: The current branch `Backend-RAG-bot` will be used for implementation.
*   **Dependencies**: The specified `uv add` dependencies are confirmed.
*   **API Keys**: `GEMINI_API_KEY`, `GEMINI_BASE_URL`, `QDRANT_API_KEY`, `QDRANT_API_URL`, `COHERE_API` (optional) are critical and will be handled via `.env` files and environment variables.
*   **Floating UI Design**: Specifics of button placement (e.g., bottom-right), color, size, and chat window appearance (e.g., slide-out from right, modal) will be decided during frontend implementation.
*   **Sitemap Ingestion Approach**: The exact libraries and methods for fetching, parsing, cleaning, chunking, and embedding content from the sitemap will be detailed in `rag/ingest.py`.

## Architectural Sketch

```mermaid
graph TD
    A[Docusaurus Frontend] -->|HTTP Request| B(FastAPI Backend)
    B -->|Embed Query & Search| C(Qdrant Vector DB)
    C -->|Relevant Context| B
    B -->|Generate Response| D(Gemini LLM)
    D -->|LLM Response| B
    B -->|HTTP Response| A

    subgraph FastAPI Backend
        B_ENTRY[main.py] --> B_ROUTER(routers/chat.py)
        B_ROUTER --> B_AGENT(my_agent/course_agent.py)
        B_AGENT --> B_RETRIEVE(rag/retrieve.py)
        B_AGENT --> B_CONFIG(my_config/gemini_config.py)
        B_RETRIEVE -- Uses --> B_QDRANT(Qdrant Client)
    end

    subgraph Docusaurus Frontend
        A_LAYOUT[Docusaurus Layout] --> A_BUTTON(src/components/ChatbotButton.tsx)
        A_LAYOUT --> A_WINDOW(src/components/ChatbotWindow.tsx)
        A_WINDOW -- Sends User Input --> B
    end

    subgraph Data Ingestion (Offline Process)
        I_SITEMAP[Sitemap.xml] --> I_FETCHER(rag/ingest.py)
        I_FETCHER --> I_EMBEDDER(Embedding Model)
        I_EMBEDDER --> I_QDRANT_STORE(Qdrant Vector DB)
    end

    style I_QDRANT_STORE fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#f9f,stroke:#333,stroke-width:2px
```
