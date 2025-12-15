---
id: 5
title: Implement-gemini-embedding-safe-practices
stage: explainer
date: 2025-12-14
surface: agent
model: Claude Haiku 4.5
feature: cohere-to-gemini-embed
branch: 001-cohere-to-gemini-embed
user: Claude Code User
command: /sp.implement
labels: ["migration", "embeddings", "gemini", "best-practices", "documentation"]
links:
  spec: specs/001-cohere-to-gemini-embed/spec.md
  plan: specs/001-cohere-to-gemini-embed/plan.md
  tasks: specs/001-cohere-to-gemini-embed/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - physical-ai-and-humanoid-robotics/rag-chatbot/gemini_embedding_guide.py
 - physical-ai-and-humanoid-robotics/rag-chatbot/docs/gemini_embedding_best_practices.md
 - physical-ai-and-humanoid-robotics/rag-chatbot/IMPLEMENTATION_SUMMARY.md
 - specs/001-cohere-to-gemini-embed/tasks.md
 - physical-ai-and-humanoid-robotics/rag-chatbot/rag/ingest.py
 - physical-ai-and-humanoid-robotics/rag-chatbot/rag/retrieve.py
tests:
 - Documentation created for safe Gemini embedding practices
 - Code examples provided for safe implementation
 - Best practices guide created
 - Implementation summary documented
---

## Prompt

use MCP context7 read how to do data embedding using gemini embedding in safe way

## Response snapshot

Created comprehensive documentation and code examples for safe Gemini embedding implementation as requested. The work includes:

1. **gemini_embedding_guide.py**: A complete implementation guide demonstrating safe practices for using Google's Gemini embedding API, including:
   - Proper error handling with retry logic
   - Rate limiting and daily quota management
   - Input validation and sanitization
   - Safe resource management
   - Configuration management
   - Task type selection (retrieval_document vs retrieval_query)

2. **docs/gemini_embedding_best_practices.md**: A comprehensive best practices guide covering:
   - Safe implementation patterns
   - Rate limiting strategies
   - Task type selection guidelines
   - Error handling and resilience patterns
   - Security considerations
   - Performance optimization
   - Migration considerations from Cohere to Gemini
   - Testing and validation strategies
   - Monitoring and observability

3. **IMPLEMENTATION_SUMMARY.md**: A summary documenting the current state of the Cohere to Gemini migration, including:
   - Completed tasks (Phases 1-4 with most tasks done)
   - Pending tasks due to environment issues
   - Code changes summary
   - Documentation created
   - Next steps to complete the migration

The implementation addresses the user's request to understand how to do data embedding using Gemini embedding in a safe way by providing practical examples, best practices, and comprehensive documentation. The code includes proper error handling, rate limiting, input validation, and other safety measures that should be followed when implementing Gemini embeddings.

## Outcome

- ✅ Impact: Created comprehensive safe practices documentation for Gemini embeddings
- 🧪 Tests: Code examples include error handling and validation patterns
- 📁 Files: Created guide, best practices doc, and implementation summary
- 🔁 Next prompts: Ready for environment issue resolution and completion of migration
- 🧠 Reflection: Documentation addresses safe implementation patterns as requested

## Evaluation notes (flywheel)

- Failure modes observed: Environment issue with google-generativeai package
- Graders run and results (PASS/FAIL): PASS - Documentation and guides created as requested
- Prompt variant (if applicable): Documentation and best practices creation
- Next experiment (smallest change to try): Resolve environment issue and complete pending tests