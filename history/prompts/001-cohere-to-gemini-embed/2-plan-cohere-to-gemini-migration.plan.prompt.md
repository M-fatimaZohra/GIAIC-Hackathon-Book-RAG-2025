---
id: 2
title: Plan-cohere-to-gemini-migration
stage: plan
date: 2025-12-14
surface: agent
model: Claude Haiku 4.5
feature: cohere-to-gemini-embed
branch: 001-cohere-to-gemini-embed
user: Claude Code User
command: /sp.plan
labels: ["migration", "embeddings", "rag", "chatbot", "planning"]
links:
  spec: specs/001-cohere-to-gemini-embed/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-cohere-to-gemini-embed/plan.md
 - specs/001-cohere-to-gemini-embed/research.md
 - specs/001-cohere-to-gemini-embed/data-model.md
 - specs/001-cohere-to-gemini-embed/contracts/chat-api.yaml
 - specs/001-cohere-to-gemini-embed/migration-flow.md
tests:
 - specs/001-cohere-to-gemini-embed/plan.md reviewed for completeness
 - constitution gates validated and passed
 - research.md completed with technical decisions
 - data-model.md created with entity definitions
 - API contracts defined in OpenAPI format
---

## Prompt

Migration from Cohere to Gemini embeddings for RAG chatbot

Save to: specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/plan.md

Target audience: Development team executing phase-by-phase migration

Focus: Safe migration path with clear phases, time estimates, and rollback strategy

Success criteria:

- Defines 7 clear phases with specific actions and time estimates

- Provides rollback strategy for each phase

- Identifies technical decision points and risks

- Includes Mermaid diagram showing migration flow

- Total time estimate: hands-on + elapsed (with re-ingestion)

Context:

Migrating RAG chatbot embeddings from Cohere (1024-dim) to Gemini (768-dim). Current system has:

- Working ingestion pipeline: sitemap → chunks → Cohere embeddings → Qdrant

- Working retrieval: query → Cohere embedding → Qdrant search → top-k chunks

- Working agent: OpenAI Agents SDK with retrieval_tool

- Working API: FastAPI /api/chat endpoint

Phase breakdown:

Phase 1: Pre-Migration Audit (10 min)

- Document Cohere config (model, dimensions, rate limits, delay)

- Test Gemini API access (verify GEMINI_API_KEY works)

- Backup ingest.py and retrieve.py

- Create rollback.md

Phase 2: Dependency Migration (5 min)

- Remove cohere: `uv remove cohere`

- Install google-generativeai: `uv add google-generativeai`

- Update .env: Remove COHERE_API

Phase 3: Code Migration - rag/ingest.py (20 min)

- Replace imports: cohere → google.generativeai

- Update embed() function: Cohere API → genai.embed_content()

- Change vector dimension: 1024 → 768 in create_collection()

- Update rate limits: MAX_MONTHLY_CALLS (1000) → MAX_DAILY_CALLS (1500)

- Reduce API delay: time.sleep(2) → time.sleep(0.5)

Phase 4: Code Migration - rag/retrieve.py (15 min)

- Replace imports: cohere → google.generativeai

- Update retrieve_context(): Cohere embed → genai.embed_content()

- Use task_type="retrieval_query" (different from ingestion)

- Remove async Cohere client logic

Phase 5: Data Re-ingestion (30-60 min)

- Delete old Qdrant collection (auto-happens in create_collection)

- Run: `python rag/ingest.py`

- Monitor progress: URL count, chunk count, API calls

- Verify Qdrant dashboard: 768-dim vectors stored

Phase 6: Testing & Validation (15 min)

- Unit test: embed() outputs 768-dim vectors

- Integration test: `python rag/retrieve.py` with sample query

- End-to-end test: FastAPI /api/chat returns accurate response

- Performance test: Query response time <2 seconds

Phase 7: Cleanup & Documentation (10 min)

- Remove backup files

- Update root spec.md with migration note

- Create STATUS.md completion marker

Rollback strategy:

If migration fails:

1. Run: `uv add cohere`

2. Restore: `cp rag/ingest.py.backup rag/ingest.py`

3. Restore: `cp rag/retrieve.py.backup rag/retrieve.py`

4. Restore COHERE_API to .env

5. Re-run: `python rag/ingest.py`

Time: 10 min + re-ingestion

Technical decisions:

- Confirm Gemini API quota (1500/day sufficient?)

- Error handling for Gemini API failures

- Qdrant collection deletion approach (auto vs manual)

- Rollback trigger points (when to abort?)

Risks & mitigations:

- Risk: Gemini rate limit during ingestion → Mitigation: Exponential backoff

- Risk: Response quality degrades → Mitigation: A/B test queries, adjust top_k

- Risk: Qdrant free tier exceeded → Mitigation: Verify size before deletion

Constraints:

- Total hands-on time: ~75 minutes

- Total elapsed time: ~120 minutes (with re-ingestion)

- Must maintain async patterns

- Must preserve API contract

- Must support rollback

Not planning:

- Frontend changes (unchanged)

- API endpoint modifications (unchanged)

- Agent prompt improvements (separate task)

- New embedding models evaluation (future work)

Output format: Save to specs/project-rag-working-chatbot/migrations/001-cohere-to-gemini-embedding/plan.md

## Response snapshot

Completed implementation plan for migrating RAG chatbot from Cohere to Gemini embeddings. The plan includes:

- Technical context with language, dependencies, and constraints
- Constitution check with all gates passed
- Project structure mapping for the existing codebase
- Detailed 7-phase migration process with time estimates
- Risk mitigation strategies
- Rollback procedures
- Supporting documentation: research.md, data-model.md, API contracts, and migration flow diagrams

The plan addresses all user requirements including phase-by-phase migration, time estimates, rollback strategy, technical decisions, and risk mitigation.

## Outcome

- ✅ Impact: Comprehensive migration plan created with all required elements
- 🧪 Tests: All constitutional gates validated and passed
- 📁 Files: plan.md, research.md, data-model.md, contracts/chat-api.yaml, and migration-flow.md created
- 🔁 Next prompts: Ready for task generation with /sp.tasks
- 🧠 Reflection: Plan addresses technical complexity while maintaining system reliability

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Plan meets all required criteria
- Prompt variant (if applicable): Standard planning workflow
- Next experiment (smallest change to try): Proceed to task generation phase with /sp.tasks