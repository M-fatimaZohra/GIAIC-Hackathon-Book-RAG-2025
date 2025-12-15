---
id: 3
title: Tasks-cohere-to-gemini-migration
stage: tasks
date: 2025-12-14
surface: agent
model: Claude Haiku 4.5
feature: cohere-to-gemini-embed
branch: 001-cohere-to-gemini-embed
user: Claude Code User
command: /sp.tasks
labels: ["migration", "embeddings", "rag", "chatbot", "tasks"]
links:
  spec: specs/001-cohere-to-gemini-embed/spec.md
  plan: specs/001-cohere-to-gemini-embed/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-cohere-to-gemini-embed/tasks.md
tests:
 - tasks.md validated for proper format and dependencies
 - 25 tasks created as requested with proper numbering
 - [P] markers added for parallelizable tasks
 - Dependencies properly documented
---

## Prompt

Migration from Cohere to Gemini embeddings for RAG chatbot

Save to: specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/task.md

Target audience: Development team executing atomic tasks

Focus: 25 numbered tasks with dependencies, acceptance criteria, and [P] markers for parallel work

Success criteria:

- Each task is atomic (single action, clear outcome)
- Tasks numbered sequentially (1-25) across all phases
- Dependencies explicitly listed (e.g., "Dependencies: Task 1, Task 2")
- [P] markers for tasks that can run in parallel
- Specific commands, file paths, line numbers included
- Clear acceptance criteria for each task

Context:

Executing migration plan from Cohere (1024-dim) to Gemini (768-dim) embeddings. Files affected:

- rag/ingest.py: embed() function (~line 60), create_collection() (~line 88), rate limiting (~line 18)

- rag/retrieve.py: retrieve_context() function (~line 25), imports (~line 8)

- .env: Remove COHERE_API

- Dependencies: cohere → google-generativeai

Task structure per phase:

PHASE 1: Pre-Migration Audit (Tasks 1-4)

- Task 1 [P]: Document Cohere config

- Task 2 [P]: Test Gemini API

- Task 3 [P]: Backup files

- Task 4: Create rollback.md

PHASE 2: Dependency Migration (Tasks 5-7)

- Task 5: Remove cohere package

- Task 6: Install google-generativeai

- Task 7: Update .env

PHASE 3: Code Migration - rag/ingest.py (Tasks 8-12)

- Task 8: Update imports (line ~8-15)

- Task 9: Update embed() function (line ~60)

- Task 10: Update rate limiting (line ~18, ~67)

- Task 11: Update create_collection() dimensions (line ~88)

- Task 12: Test ingest.py changes

PHASE 4: Code Migration - rag/retrieve.py (Tasks 13-16)

- Task 13: Update imports (line ~6-15)

- Task 14: Update retrieve_context() (line ~25-35)

- Task 15: Update comments/logs

- Task 16: Test retrieve.py changes

PHASE 5: Data Re-ingestion (Tasks 17-19)

- Task 17: Verify Qdrant collection deletion

- Task 18: Run full ingestion (30-60 min)

- Task 19: Verify data integrity

PHASE 6: End-to-End Testing (Tasks 20-22)

- Task 20: Test retrieval accuracy (5 sample queries)

- Task 21: Test /api/chat endpoint

- Task 22: Regression testing

PHASE 7: Cleanup & Documentation (Tasks 23-25)

- Task 23: Remove backup files

- Task 24: Update root spec.md

- Task 25: Create STATUS.md

Example task format (use this style):

Task 9: Update embed() function

- Description: Replace Cohere API call with Gemini API call in rag/ingest.py

- File: rag/ingest.py, line ~60

- Changes:

  - Remove: `response = co.embed(texts=[text], model="embed-english-v3.0", input_type="search_document")`

  - Remove: `return response.embeddings[0]`

  - Add: `result = genai.embed_content(model="models/text-embedding-004", content=text, task_type="retrieval_document")`

  - Add: `return result['embedding']`

- Acceptance Criteria: embed() function returns list of 768 floats, unit test passes

- Dependencies: Task 8

Constraints:

- 25 total tasks

- Each task atomic (completable in <30 min)

- Specific commands for all actionable tasks

- File paths and line numbers where applicable

- Clear pass/fail acceptance criteria

Not including:

- Frontend testing (unchanged)

- Performance optimization beyond migration

- New feature development

- Code refactoring beyond migration needs

Output format: Save to specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/task.md

## Response snapshot

Created comprehensive task list for Cohere to Gemini embedding migration with 25 sequentially numbered tasks across 7 phases. Each task is atomic with specific file paths, line numbers, and clear acceptance criteria. Parallelizable tasks are marked with [P] markers. Dependencies are documented both within task descriptions and in the Dependencies section. The tasks follow the required format with checkboxes, task IDs, and proper descriptions.

## Outcome

- ✅ Impact: 25 atomic tasks created as requested with proper formatting
- 🧪 Tests: Tasks validated for proper checklist format and dependencies
- 📁 Files: tasks.md created with complete task breakdown
- 🔁 Next prompts: Ready for implementation phase
- 🧠 Reflection: Tasks are properly structured for parallel execution where possible

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All 25 tasks created with proper format
- Prompt variant (if applicable): Standard task generation workflow
- Next experiment (smallest change to try): Begin implementation with Task 1