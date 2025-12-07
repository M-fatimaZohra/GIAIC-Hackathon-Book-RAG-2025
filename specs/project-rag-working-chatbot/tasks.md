# RAG Chatbot Integration: Atomic Tasks

This document outlines the atomic tasks required to implement the RAG Chatbot Integration for the Docusaurus Physical AI & Humanoid Robotics Book, structured into logical phases with dependencies and testing considerations.

## Phase 1: Setup and Environment Configuration

1.  **Task**: Virtual environment setup and dependency installation.
    *   **Description**: Create a Python virtual environment and install all specified dependencies (`openai-agents`, `python-dotenv`, `qdrant-client`, `requests`, `cohere`, `fastapi`, `uvicorn`) using `uv` in the `rag-chatbot` directory.
    *   **Acceptance Criteria**: All dependencies are successfully installed in the virtual environment. `uv list` shows the installed packages.
    *   **Dependencies**: None.

2.  **Task**: Create `.env.example` and environment variable template.
    *   **Description**: Create an `.env.example` file in the `rag-chatbot` directory, listing all required environment variables (`QDRANT_API_KEY`, `QDRANT_API_URL`, `GEMINI_API_KEY`, `GEMINI_BASE_URL`, `COHERE_API`).
    *   **Acceptance Criteria**: The `.env.example` file exists and contains all specified environment variables as placeholders.
    *   **Dependencies**: None.

3.  **Task**: Create backend folder structure.
    *   **Description**: Ensure the `rag-chatbot` directory contains the subdirectories: `my_config`, `my_agent`, `routers`, `rag`, and the `main.py` file.
    *   **Acceptance Criteria**: The folder structure `rag-chatbot/my_config`, `rag-chatbot/my_agent`, `rag-chatbot/routers`, `rag-chatbot/rag`, and `rag-chatbot/main.py` exists.
    *   **Dependencies**: None.

## Phase 2: Backend Development

4.  **Task [P]**: Write Gemini configuration (`my_config/gemini_config.py`).
    *   **Description**: Implement `my_config/gemini_config.py` to configure the `AsyncOpenAI` client using `GEMINI_API_KEY` and `GEMINI_BASE_URL` from environment variables.
    *   **Acceptance Criteria**: `my_config/gemini_config.py` is created and correctly loads API keys from `.env` and initializes `AsyncOpenAI` client. Unit tests for `gemini_config.py` pass.
    *   **Dependencies**: Task 1, Task 2.

5.  **Task**: Write basic FastAPI application (`main.py`) with CORS.
    *   **Description**: Create `main.py` to initialize a basic FastAPI app and configure CORS to allow requests from the Docusaurus frontend.
    *   **Acceptance Criteria**: `main.py` runs successfully, and a simple GET endpoint (e.g., `/health`) is accessible with correct CORS headers.
    *   **Dependencies**: Task 3.

## Phase 3: RAG Pipeline Implementation

6.  **Task**: Write ingestion script (`rag/ingest.py`) - Sitemap fetch and parse.
    *   **Description**: Implement the initial part of `rag/ingest.py` to fetch `https://giaic-hackathon-book-rag-2025.vercel.app/sitemap.xml` and parse it to extract content URLs.
    *   **Acceptance Criteria**: `rag/ingest.py` can successfully fetch and parse the sitemap, logging all extracted URLs. Unit tests for sitemap fetching/parsing pass.
    *   **Dependencies**: Task 1, Task 2.

7.  **Task**: Write ingestion script (`rag/ingest.py`) - Content fetch, clean, and chunk.
    *   **Description**: Extend `rag/ingest.py` to fetch content from the extracted URLs, clean the HTML/Markdown, and split it into manageable text chunks.
    *   **Acceptance Criteria**: `rag/ingest.py` processes a sample set of URLs, producing cleaned and chunked text. Unit tests for content processing pass.
    *   **Dependencies**: Task 6.

8.  **Task**: Write ingestion script (`rag/ingest.py`) - Generate embeddings and store in Qdrant.
    *   **Description**: Complete `rag/ingest.py` to generate embeddings for each text chunk (using `openai-agents` or Cohere compatible models) and store them in Qdrant with associated metadata.
    *   **Acceptance Criteria**: `rag/ingest.py` successfully populates Qdrant with embeddings and text chunks. Verification script shows stored vectors and data in Qdrant. Unit tests for embedding generation and Qdrant storage pass.
    *   **Dependencies**: Task 7, Task 1 (Qdrant client).

9.  **Task**: Write retrieval module (`rag/retrieve.py`) - Query embedding.
    *   **Description**: Implement the initial part of `rag/retrieve.py` to receive a query and generate its embedding using the same model as `ingest.py`.
    *   **Acceptance Criteria**: `rag/retrieve.py` can successfully embed a given query. Unit tests for query embedding pass.
    *   **Dependencies**: Task 1, Task 2.

10. **Task**: Write retrieval module (`rag/retrieve.py`) - Qdrant search and context return.
    *   **Description**: Complete `rag/retrieve.py` to perform a similarity search in Qdrant using the query embedding and return the top-k most relevant text chunks.
    *   **Acceptance Criteria**: `rag/retrieve.py` returns accurate, contextually relevant text chunks for sample queries from Qdrant. Unit tests for Qdrant search pass.
    *   **Dependencies**: Task 9, Task 8 (populated Qdrant).

11. **Task [P]**: Implement `course_agent.py` - Agent initialization and tool integration.
    *   **Description**: Create `my_agent/course_agent.py` to initialize the OpenAI Agents SDK agent, integrate the Gemini client from `gemini_config.py` as the LLM, and `rag/retrieve.py` as a retrieval tool.
    *   **Acceptance Criteria**: `course_agent.py` successfully initializes the agent and its tools. Basic agent interaction (without full RAG flow) works. Unit tests for agent initialization pass.
    *   **Dependencies**: Task 4, Task 10.

12. **Task**: Implement `course_agent.py` - RAG logic and response generation.
    *   **Description**: Extend `my_agent/course_agent.py` to implement the logic for processing user queries, utilizing the retrieval tool, combining context, and generating responses with Gemini.
    *   **Acceptance Criteria**: The `course_agent` can process a query, retrieve context, and generate a coherent, contextualized response. Unit tests for agent RAG logic pass.
    *   **Dependencies**: Task 11.

13. **Task**: Write FastAPI chat router (`routers/chat.py`).
    *   **Description**: Create `routers/chat.py` with a `POST /api/chat` endpoint that accepts a JSON message, calls the `course_agent` with the message, and returns the agent's response (including sources).
    *   **Acceptance Criteria**: The `/api/chat` endpoint is accessible, accepts JSON input, and returns a structured JSON response. Basic integration tests for the `/api/chat` endpoint pass.
    *   **Dependencies**: Task 5, Task 12.

14. **Task**: Write basic tests for backend route (`routers/chat.py`).
    *   **Description**: Implement unit/integration tests for the `POST /api/chat` route, covering input validation, mocking `course_agent` calls, and verifying expected output structure.
    *   **Acceptance Criteria**: All backend route tests pass.
    *   **Dependencies**: Task 13.

## Phase 4: Frontend UI Development

15. **Task [P]**: Create floating chatbot button component (`src/components/ChatbotButton.tsx`).
    *   **Description**: Develop the React component for a global floating button that is fixed to a corner of the screen in `src/components/ChatbotButton.tsx`.
    *   **Acceptance Criteria**: `ChatbotButton.tsx` is created, renders correctly in Docusaurus, and can be toggled via local state (no backend connection yet).
    *   **Dependencies**: None.

16. **Task [P]**: Create chat window skeleton component (`src/components/ChatbotWindow.tsx`).
    *   **Description**: Develop the React component for the chat interface skeleton (input field, message display area) in `src/components/ChatbotWindow.tsx`. No styling or backend connection initially.
    *   **Acceptance Criteria**: `ChatbotWindow.tsx` is created and renders a basic chat interface when toggled, without breaking Docusaurus layout.
    *   **Dependencies**: None.

17. **Task**: Integrate chatbot components into Docusaurus global layout.
    *   **Description**: Integrate `ChatbotButton.tsx` and `ChatbotWindow.tsx` into the Docusaurus global layout (e.g., via `Layout` swizzle or custom `Theme` wrapper) to ensure global visibility and toggling.
    *   **Acceptance Criteria**: The floating button appears on all Docusaurus pages, and clicking it toggles the basic `ChatbotWindow.tsx` without layout issues.
    *   **Dependencies**: Task 15, Task 16.

## Phase 5: Integration & Testing

18. **Task**: Connect frontend chatbot to backend API endpoint.
    *   **Description**: Modify `ChatbotWindow.tsx` to send user messages to the `/api/chat` backend endpoint and display the received responses.
    *   **Acceptance Criteria**: Sending a message from the frontend results in a network request to `/api/chat`, and the backend's (mocked or actual) response is displayed in the chat window.
    *   **Dependencies**: Task 13, Task 17.

19. **Task**: Basic styling for chatbot UI.
    *   **Description**: Add minimal styling to `physical-ai-and-humanoid-robotics/src/css/custom.css` to ensure the chatbot button and window are visually presentable and integrated with the Docusaurus theme.
    *   **Acceptance Criteria**: Chatbot UI elements are consistently styled and do not clash with the Docusaurus theme.
    *   **Dependencies**: Task 17.

20. **Task**: End-to-end integration test (UI to RAG response).
    *   **Description**: Perform an end-to-end test by asking a question via the Docusaurus UI and verifying that a relevant and accurate response (with sources) is returned by the fully integrated RAG chatbot.
    *   **Acceptance Criteria**: A user query from the frontend successfully triggers the full RAG pipeline and returns a correct, contextualized answer in the chat window.
    *   **Dependencies**: Task 18.

21. **Task**: Document `rag-chatbot` README.
    *   **Description**: Create a `README.md` file in the `rag-chatbot` directory explaining how to set up the environment, install dependencies, configure environment variables, run the ingestion script, and start the FastAPI backend.
    *   **Acceptance Criteria**: A clear and comprehensive `rag-chatbot/README.md` exists, detailing all necessary steps for local development and deployment of the backend.
    *   **Dependencies**: All backend-related tasks complete.
