---
id: 1
title: Create-spec-cohere-to-gemini-embed
stage: spec
date: 2025-12-14
surface: agent
model: Claude Haiku 4.5
feature: cohere-to-gemini-embed
branch: 001-cohere-to-gemini-embed
user: Claude Code User
command: /sp.specify
labels: ["migration", "embeddings", "rag", "chatbot"]
links:
  spec: specs/001-cohere-to-gemini-embed/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-cohere-to-gemini-embed/spec.md
 - specs/001-cohere-to-gemini-embed/checklists/requirements.md
tests:
 - specs/001-cohere-to-gemini-embed/spec.md reviewed for completeness
 - checklists/requirements.md created to validate spec quality
---

## Prompt

Migration from Cohere to Gemini embeddings for RAG chatbot

Save to: specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/spec.md

Target audience: Development team executing the migration

Focus: Replacing Cohere embed-english-v3.0 (1024-dim) with Gemini text-embedding-004 (768-dim)

Success criteria:

- Clearly identifies all breaking changes (vector dimensions, Qdrant collection, data re-ingestion)

- Documents unchanged components (FastAPI endpoints, agent logic, frontend, LLM)

- Provides comparison table: Cohere vs Gemini (rate limits, dimensions, performance)

- Includes Mermaid diagram showing old vs new embedding flow

- Lists all affected files with specific changes needed

Context:

Working RAG chatbot for Docusaurus book (Physical AI & Humanoid Robotics). Current system uses:

- Cohere embed-english-v3.0 (1024-dim vectors)

- Qdrant Cloud vector database

- FastAPI backend with OpenAI Agents SDK

- Gemini 2.5 Flash Lite as LLM (not changing)

- Data source: sitemap.xml → HTML → 2000-char chunks

Problems with current Cohere setup:

- Rate limit: 1000 requests/month (hitting limit)

- API delay: 2 seconds between calls (slow ingestion)

- Response quality: Suboptimal relevance in retrieved context

Migration requirements:

- Switch to Gemini text-embedding-004 (768-dim, free tier)

- Increase rate limit to 1500 requests/day

- Reduce API delay to 0.5 seconds

- Recreate Qdrant collection (dimension change)

- Re-ingest all data from sitemap

- Maintain all existing functionality

Affected files:

- rag/ingest.py: Replace Cohere API calls, update vector dimensions, change rate limits

- rag/retrieve.py: Replace Cohere query embeddings with Gemini

- .env: Remove COHERE_API, verify GEMINI_API_KEY

- Dependencies: Remove cohere, add google-generativeai

Unchanged files:

- my_agent/course_agent.py (agent logic stays same)

- routers/chat.py (FastAPI endpoint unchanged)

- main.py (CORS and app structure unchanged)

- my_config/gemini_config.py (LLM client unchanged)

Constraints:

- Must use Gemini free tier (text-embedding-004)

- Must preserve async/await patterns

- Must maintain source URL attribution in responses

- Must support rollback to Cohere if migration fails

- No changes to frontend (Docusaurus components)

- No changes to API contract (request/response JSON format)

Not building:

- New embedding models beyond Gemini

- Changes to chunking strategy (stays 2000 chars)

- Frontend modifications

- New FastAPI endpoints

- Agent prompt engineering improvements

Output format: Create specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/ directory if it doesn't exist, then save spec.md there

## Response snapshot

Created feature branch 001-cohere-to-gemini-embed and specification file specs/001-cohere-to-gemini-embed/spec.md for migrating from Cohere to Gemini embeddings for the RAG chatbot. The specification includes:

- User scenarios for RAG chatbot query processing, content ingestion, and system performance
- Functional requirements covering embedding service replacement, vector storage updates, content re-ingestion, API compatibility, rate limits, and rollback capability
- Key entities: Textbook Content, Vector Embeddings, Qdrant Collection, and Chat Query
- Success criteria focused on maintaining user experience, performance improvements, and system reliability
- Edge cases for API availability, vector dimension mismatches, and partial ingestion failures
- Quality checklist to validate the specification

## Outcome

- ✅ Impact: Created comprehensive specification for Cohere to Gemini embedding migration
- 🧪 Tests: Specification reviewed for completeness and quality
- 📁 Files: spec.md and requirements.md created in feature directory
- 🔁 Next prompts: Ready for clarification and planning phases
- 🧠 Reflection: Specification captures technical requirements while maintaining user-focused perspective

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Specification meets all required criteria
- Prompt variant (if applicable): Standard specification generation
- Next experiment (smallest change to try): Proceed to planning phase with /sp.plan