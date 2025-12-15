# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Migration from Cohere embed-english-v3.0 (1024-dim) to Google's text-embedding-004 (768-dim) for the RAG chatbot. This involves replacing embedding API calls in both ingestion and retrieval pipelines, updating Qdrant collection dimensions, re-ingesting all textbook content, and adjusting rate limits from 1000 requests/month to 1500 requests/day with reduced API delays from 2 seconds to 0.5 seconds. The migration preserves all existing API contracts and user functionality while improving performance and removing rate limit constraints.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, Qdrant, Google Generative AI SDK, OpenAI Agents SDK
**Storage**: Qdrant Cloud vector database
**Testing**: pytest (existing project structure)
**Target Platform**: Linux server (backend API)
**Project Type**: Web backend service
**Performance Goals**: Support 1500 embedding requests/day, sub-0.5s API response time, maintain current chat response quality
**Constraints**: Must maintain API contract, preserve async/await patterns, support rollback, operate within Qdrant Cloud free tier limits
**Scale/Scope**: Single textbook (Physical AI & Humanoid Robotics), ~1000+ content chunks, 768-dimensional vectors

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Gate 1: Accuracy & Verifiability
✅ Plan maintains accurate API contracts and preserves response quality metrics
✅ All changes are based on documented technical requirements from feature spec

### Gate 2: Clarity & Pedagogy
✅ Migration approach is clearly documented in phases with specific actions
✅ Rollback strategy ensures system reliability during transition

### Gate 3: Reliability & Error Handling
✅ Plan includes comprehensive rollback strategy for each phase
✅ Error handling for API failures is addressed in technical approach

### Gate 4: Scalability & Modularity
✅ Migration preserves existing architecture patterns
✅ Changes are isolated to embedding functionality without affecting other components

### Gate 5: Automation-First
✅ Migration can be executed via automated scripts and commands
✅ Dependencies managed through uv package manager

### Gate 6: Reproducibility & Testing
✅ Plan includes validation and testing phases to verify functionality
✅ Performance metrics defined for verification of success criteria

### Post-Design Verification
✅ API contracts defined and preserved (chat-api.yaml)
✅ Data model documented (data-model.md)
✅ Migration approach maintains all constitutional principles

## Project Structure

### Documentation (this feature)

```text
specs/001-cohere-to-gemini-embed/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
physical-ai-and-humanoid-robotics/rag-chatbot/
├── main.py              # FastAPI app entry point
├── .env                 # Environment variables
├── pyproject.toml       # Project dependencies
├── uv.lock              # Dependency lock file
├── my_agent/
│   └── course_agent.py  # OpenAI Agents SDK implementation
├── my_config/
│   └── gemini_config.py # LLM configuration
├── rag/
│   ├── ingest.py        # Content ingestion and embedding
│   └── retrieve.py      # Vector retrieval and context extraction
└── routers/
    └── chat.py          # FastAPI chat endpoint
```

**Structure Decision**: Web backend service structure selected to match existing RAG chatbot architecture. Changes will be focused on the rag/ directory files for embedding functionality while preserving all other components.

## Migration Phases

### Phase 1: Pre-Migration Audit (10 min)
- Document Cohere config (model, dimensions, rate limits, delay)
- Test Gemini API access (verify GEMINI_API_KEY works)
- Backup ingest.py and retrieve.py
- Create rollback.md

### Phase 2: Dependency Migration (5 min)
- Remove cohere: `uv remove cohere`
- Install google-generativeai: `uv add google-generativeai`
- Update .env: Remove COHERE_API

### Phase 3: Code Migration - rag/ingest.py (20 min)
- Replace imports: cohere → google.generativeai
- Update embed() function: Cohere API → genai.embed_content()
- Change vector dimension: 1024 → 768 in create_collection()
- Update rate limits: MAX_MONTHLY_CALLS (1000) → MAX_DAILY_CALLS (1500)
- Reduce API delay: time.sleep(2) → time.sleep(0.5)

### Phase 4: Code Migration - rag/retrieve.py (15 min)
- Replace imports: cohere → google.generativeai
- Update retrieve_context(): Cohere embed → genai.embed_content()
- Use task_type="retrieval_query" (different from ingestion)
- Remove async Cohere client logic

### Phase 5: Data Re-ingestion (30-60 min)
- Delete old Qdrant collection (auto-happens in create_collection)
- Run: `python rag/ingest.py`
- Monitor progress: URL count, chunk count, API calls
- Verify Qdrant dashboard: 768-dim vectors stored

### Phase 6: Testing & Validation (15 min)
- Unit test: embed() outputs 768-dim vectors
- Integration test: `python rag/retrieve.py` with sample query
- End-to-end test: FastAPI /api/chat returns accurate response
- Performance test: Query response time <2 seconds

### Phase 7: Cleanup & Documentation (10 min)
- Remove backup files
- Update root spec.md with migration note
- Create STATUS.md completion marker

## Time Estimates
- **Total hands-on time**: ~75 minutes
- **Total elapsed time**: ~120 minutes (with re-ingestion)
- **Critical path**: Data re-ingestion phase (30-60 min)

## Risk Mitigation
- Risk: Gemini rate limit during ingestion → Mitigation: Exponential backoff
- Risk: Response quality degrades → Mitigation: A/B test queries, adjust top_k
- Risk: Qdrant free tier exceeded → Mitigation: Verify size before deletion

## Rollback Strategy
If migration fails:
1. Run: `uv add cohere`
2. Restore: `cp rag/ingest.py.backup rag/ingest.py`
3. Restore: `cp rag/retrieve.py.backup rag/retrieve.py`
4. Restore COHERE_API to .env
5. Re-run: `python rag/ingest.py`
Time: 10 min + re-ingestion

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

✅ No constitution violations identified. All gates passed successfully.
