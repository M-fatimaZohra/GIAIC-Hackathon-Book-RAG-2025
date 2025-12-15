# Implementation Tasks: Migration from Cohere to Gemini embeddings for RAG chatbot

**Feature**: Cohere to Gemini embedding migration
**Generated**: 2025-12-14
**Based on**: specs/001-cohere-to-gemini-embed/spec.md, plan.md, research.md, data-model.md

## Implementation Strategy

This migration will replace Cohere embed-english-v3.0 (1024-dim) with Google's text-embedding-004 (768-dim) for the RAG chatbot. The approach follows the planned 7-phase process with atomic tasks that can be executed sequentially or in parallel where indicated. The MVP scope covers the core embedding replacement which requires the foundational changes in phases 1-3.

## Phase 1: Pre-Migration Audit (Tasks 1-4)

**Goal**: Prepare for migration and document current state

- [x] T001 [P] Document Cohere config (model, dimensions, rate limits, delay) in rag/ingest.py
- [x] T002 [P] Test Gemini API access (verify GEMINI_API_KEY works)
- [x] T003 [P] Backup rag/ingest.py and rag/retrieve.py files
- [x] T004 Create rollback.md with rollback instructions

## Phase 2: Dependency Migration (Tasks 5-7)

**Goal**: Update dependencies to support Gemini instead of Cohere

- [x] T005 Remove cohere package: `uv remove cohere`
- [x] T006 Install google-generativeai: `uv add google-generativeai`
- [x] T007 Update .env: Remove COHERE_API variable

## Phase 3: Code Migration - rag/ingest.py (Tasks 8-12)

**Goal**: Update ingestion pipeline to use Gemini embeddings instead of Cohere

- [x] T008 Update imports in rag/ingest.py to replace cohere with google.generativeai (line ~8-15)
- [x] T009 Update embed() function in rag/ingest.py to use Gemini API call (line ~60)
- [x] T010 Update rate limiting in rag/ingest.py from monthly to daily limits (line ~18, ~67)
- [x] T011 Update create_collection() dimensions from 1024 to 768 (line ~88)
- [x] T012 Test rag/ingest.py changes with unit tests
## Phase 4: Code Migration - rag/retrieve.py (Tasks 13-16)

**Goal**: Update retrieval pipeline to use Gemini embeddings for query processing

- [x] T013 Update imports in rag/retrieve.py to replace cohere with google.generativeai (line ~6-15)
- [x] T014 Update retrieve_context() function in rag/retrieve.py to use Gemini API (line ~25)
- [x] T015 Update comments/logs in rag/retrieve.py to reflect Gemini usage
- [x] T016 Test rag/retrieve.py changes with sample queries

## Phase 5: Data Re-ingestion (Tasks 17-19)

**Goal**: Re-ingest all textbook content using new embedding model

- [x] T017 Verify Qdrant collection deletion/recreation with 768-dimensional vectors
- [x] T018 Run full data ingestion using `python rag/ingest.py` (30-60 min)
- [x] T019 Verify data integrity and correct vector dimensions in Qdrant

## Phase 6: End-to-End Testing (Tasks 20-22)

**Goal**: Validate complete functionality after migration

- [x] T020 Test retrieval accuracy with 5 sample queries
- [x] T021 Test /api/chat endpoint functionality
- [x] T022 Regression testing to ensure no functionality is broken

## Phase 7: Cleanup & Documentation (Tasks 23-25)

**Goal**: Complete migration and clean up temporary artifacts

- [x] T023 Remove backup files created during migration
- [x] T024 Update root spec.md with migration completion note
- [x] T025 Create STATUS.md completion marker file

## Dependencies

- T005, T006, T007 must complete before T008, T009, T010, T011, T013, T014
- T008, T009, T010, T011, T012 must complete before T017
- T013, T014, T015, T016 must complete before T017
- T017, T018, T019 must complete before T020, T021, T022
- T020, T021, T022 must pass before T023, T024, T025

## Parallel Execution Examples

- T001, T002, T003 can run in parallel during Phase 1
- T005, T006, T007 can run in parallel during Phase 2
- T008, T013 can run in parallel (different files)
- T009, T014 can run in parallel (different files)
- T020, T021 can run in parallel (different tests)

## Acceptance Criteria Summary

**Task 9**: embed() function returns list of 768 floats, unit test passes
**Task 14**: retrieve_context() function works with Gemini embeddings, returns proper context
**Task 18**: Full ingestion completes with all textbook content embedded using 768-dim vectors
**Task 21**: /api/chat endpoint returns responses with proper source attribution
**Task 22**: All regression tests pass, no functionality broken

## MVP Scope

MVP includes: T001-T016 (foundational changes and core embedding replacement) to ensure the basic functionality continues to work with the new embedding provider.