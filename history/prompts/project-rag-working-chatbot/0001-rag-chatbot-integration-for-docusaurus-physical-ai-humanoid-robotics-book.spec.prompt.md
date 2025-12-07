---
id: 0001
title: RAG Chatbot Integration for Docusaurus Physical AI & Humanoid Robotics Book
stage: spec
date: 2025-12-06
surface: agent
model: claude-opus-4-5-20251101
feature: project-rag-working-chatbot
branch: Backend-RAG-bot
user: user
command: /sp.specify
labels: ["spec","rag","chatbot","docusaurus"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/project-rag-working-chatbot/spec.md
tests:
  null
---

## Prompt

Feature: "RAG Chatbot Integration for Docusaurus Physical AI & Humanoid Robotics Book"

# PROJECT CONTEXT

Root: 00-my-research-papar

Branch: Backend-RAG-bot

Docusaurus App: 00-my-research-papar/physical-ai-and-humanoid-robotics

RAG backend: 00-my-research-papar/physical-ai-and-humanoid-robotics/rag-chatbot

Specs/Plan/Tasks: 00-my-research-papar/specs/project-rag-working-chatbot

# FRONTEND (Docusaurus)

- Add global floating button visible on all pages

- Clicking toggles floating chat window connected to FastAPI backend

- UI must not break navigation/theme

# BACKEND (FastAPI + RAG + Qdrant + Gemini)

Dependencies (install via UV):

uv add openai-agents python-dotenv qdrant-client requests cohere fastapi uvicorn

ENV VARIABLES:

QDRANT_API_KEY

QDRANT_API_URL

GEMINI_API_KEY

GEMINI_BASE_URL

COHERE_API

# GEMINI CONFIG

from openai import AsyncOpenAI

CLIENT = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)

MODEL = OpenAIChatCompletionsModel(...)

# BACKEND FOLDER STRUCTURE

rag-chatbot/

 ├── my_config/gemini_config.py

 ├── my_agent/course_agent.py

 ├── routers/chat.py

 ├── rag/ingest.py

 ├── rag/retrieve.py

 ├── main.py

 └── .env.example

# FRONTEND-BACKEND CONNECTION

- Docusaurus → /api/chat → FastAPI

- Backend uses OpenAI Agents SDK + Gemini

- Backend uses Qdrant for embeddings & vector search

- Optional: Cohere for embeddings

# SITEMAP

https://giaic-hackathon-book-rag-2025.vercel.app/sitemap.xml

# WHAT TO GENERATE

SPEC must include:

1. Problem definition

2. Feature overview

3. Functional & non-functional requirements

4. Architecture & data-flow

5. Folder structure

6. Backend services

7. Embedding + RAG pipeline

8. Agent config

9. Frontend integration

10. Security & deployment considerations

11. Environment variables

12. API contract (JSON input/output)

END

## Response snapshot

Created initial feature specification `specs/project-rag-working-chatbot/spec.md`.

## Outcome

- ✅ Impact: Created initial feature specification.
- 🧪 Tests: No tests run yet.
- 📁 Files: Created spec.md.
- 🔁 Next prompts: Generate implementation plan (/sp.plan).
- 🧠 Reflection: Initial specification generated based on user input and template requirements.

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
