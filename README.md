# Physical AI & Humanoid Robotics - Research Documentation

This repository contains comprehensive documentation and implementation for the Physical AI & Humanoid Robotics research project, featuring an AI-powered RAG (Retrieval-Augmented Generation) chatbot system integrated with a Docusaurus-based textbook.

## Project Overview

The Physical AI & Humanoid Robotics project is a comprehensive educational resource that combines traditional textbook content with cutting-edge AI technology. The project features:

- **Interactive Docusaurus-based textbook** with comprehensive content on Physical AI and Humanoid Robotics
- **AI-powered RAG chatbot** for natural language querying of textbook content
- **Vector search system** using Qdrant for semantic retrieval
- **Google Gemini integration** for intelligent response generation
- **Frontend-Backend architecture** with seamless integration

## Key Components

### 1. Docusaurus Documentation System
- **Location**: `physical-ai-and-humanoid-robotics/`
- **Purpose**: Hosts the interactive textbook content using Docusaurus
- **Features**:
  - Responsive web interface
  - Searchable documentation
  - Organized content structure
  - Integration-ready architecture

### 2. RAG Chatbot Backend
- **Location**: `physical-ai-and-humanoid-robotics/rag-chatbot/`
- **Purpose**: AI-powered query processing system
- **Components**:
  - **Ingestion Pipeline** (`rag/ingest.py`): Processes textbook content into vector embeddings
  - **Retrieval System** (`rag/retrieve.py`): Performs semantic search using vector database
  - **AI Agent** (`my_agent/course_agent.py`): Processes queries using Google Gemini
  - **API Layer** (`main.py`, `routers/chat.py`): FastAPI endpoints for chat functionality

### 3. Frontend Chatbot UI
- **Location**: `physical-ai-and-humanoid-robotics/src/components/`
- **Purpose**: Interactive chat interface integrated into the textbook
- **Components**:
  - **ChatbotButton.tsx**: Floating button for accessing the chat interface
  - **ChatbotWindow.tsx**: Full chat interface with message history
  - **CSS Modules**: Themed styling for light/dark mode support

### 4. Integration Layer
- **Location**: `physical-ai-and-humanoid-robotics/src/theme/Root.tsx`
- **Purpose**: Global integration of chatbot components across all textbook pages
- **Features**:
  - Persistent chat interface across all pages
  - State management for chat window visibility
  - Seamless user experience

## Technical Architecture

### Backend Technologies
- **Python 3.11**: Core backend implementation
- **FastAPI**: Web framework for API endpoints
- **Google Generative AI**: Gemini models for embeddings and responses
- **Qdrant**: Vector database for semantic search
- **OpenAI Agents SDK**: Agent orchestration framework
- **Trafilatura**: HTML to text extraction
- **uv**: Package management

### Frontend Technologies
- **React**: Component-based UI development
- **Docusaurus**: Static site generation and documentation
- **TypeScript**: Type-safe development
- **CSS Modules**: Scoped styling with theme support

### AI/ML Components
- **Google text-embedding-004**: 768-dimensional vector embeddings
- **Gemini Flash**: Language model for response generation
- **RAG Pipeline**: Retrieval-Augmented Generation for contextual responses
- **Vector Similarity Search**: Semantic matching of queries to textbook content

## Features

- **Natural Language Querying**: Ask questions about textbook content in plain English
- **Semantic Search**: Find relevant content using vector embeddings
- **Source Attribution**: Responses include citations to original sources
- **Rate Limit Management**: Handles API quotas and prevents rate limiting
- **Asynchronous Processing**: Non-blocking operations for better performance
- **Error Handling**: Robust error management and retry logic
- **Scalable Vector Storage**: Qdrant-based vector database for efficient similarity search
- **Responsive Design**: Works on desktop and mobile devices
- **Dark/Light Mode**: Automatic theme detection and support

## Project Structure

```
00-my-research-papar/
├── physical-ai-and-humanoid-robotics/          # Docusaurus textbook
│   ├── docs/                                  # Textbook content
│   ├── src/
│   │   ├── components/                        # Chatbot UI components
│   │   │   ├── ChatbotButton.tsx
│   │   │   ├── ChatbotWindow.tsx
│   │   │   ├── ChatbotButton.module.css
│   │   │   └── ChatbotWindow.module.css
│   │   └── theme/
│   │       └── Root.tsx                       # Global chatbot integration
│   ├── rag-chatbot/                           # Backend implementation
│   │   ├── main.py                           # FastAPI application
│   │   ├── my_agent/
│   │   │   └── course_agent.py               # AI agent implementation
│   │   ├── my_config/
│   │   │   └── gemini_config.py              # LLM configuration
│   │   ├── rag/
│   │   │   ├── ingest.py                     # Content ingestion pipeline
│   │   │   └── retrieve.py                   # Vector retrieval system
│   │   └── routers/
│   │       └── chat.py                       # API endpoints
│   ├── docusaurus.config.ts                  # Docusaurus configuration
│   └── sidebars.ts                           # Documentation navigation
├── specs/                                     # Project specifications
│   └── project-rag-working-chatbot/          # RAG chatbot specs
├── history/prompts/                          # Development history
└── README.md                                 # This file
```

## Development Workflow

The project follows a structured development approach using the Spec-Kit Plus methodology:

1. **Specification**: Feature requirements documented in specs/
2. **Planning**: Implementation strategy in plan.md
3. **Tasking**: Detailed tasks in tasks.md
4. **Implementation**: Code changes following the task list
5. **Testing**: Validation of functionality

## Migration History

The system was originally built with Cohere embeddings and later migrated to Google's Gemini embedding model, providing:
- Increased rate limits (from 1000 requests/month to 1500 requests/day)
- Improved performance (reduced API delay)
- Better embedding quality
- Enhanced cost efficiency

## Usage

The system provides an interactive learning experience where users can:
1. Browse the comprehensive Physical AI & Humanoid Robotics textbook
2. Access the floating chat button on any page
3. Ask natural language questions about the content
4. Receive AI-generated responses with proper citations
5. Explore referenced sources for deeper understanding

## Contributing

This project uses Claude Code and Spec-Kit Plus for AI-assisted development. Contributions should follow the established development workflow and maintain the project's architectural patterns.