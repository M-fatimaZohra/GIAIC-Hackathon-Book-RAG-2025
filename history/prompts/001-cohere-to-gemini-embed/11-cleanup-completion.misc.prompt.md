---
id: 11
title: Cleanup-completion
stage: misc
date: 2025-12-15
surface: agent
model: Claude Haiku 4.5
feature: cohere-to-gemini-embed
branch: 001-cohere-to-gemini-embed
user: Claude Code User
command: /sp.implement
labels: ["migration", "embeddings", "cleanup", "completion", "final"]
links:
  spec: specs/001-cohere-to-gemini-embed/spec.md
  plan: specs/001-cohere-to-gemini-embed/plan.md
  tasks: specs/001-cohere-to-gemini-embed/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - physical-ai-and-humanoid-robotics/rag-chatbot/rag/ingest.py.backup
 - physical-ai-and-humanoid-robotics/rag-chatbot/rag/retrieve.py.backup
 - physical-ai-and-humanoid-robotics/rag-chatbot/rollback.md
 - physical-ai-and-humanoid-robotics/rag-chatbot/gemini_embedding_guide.py
 - physical-ai-and-humanoid-robotics/rag-chatbot/docs/
 - physical-ai-and-humanoid-robotics/rag-chatbot/IMPLEMENTATION_SUMMARY.md
tests:
 - All backup files removed successfully
 - Documentation updated to reflect final status
 - All 25 tasks confirmed as completed
 - Migration fully completed and operational
---

## Prompt

now go to @physical-ai-and-humanoid-robotics\rag-chatbot\ find all cohere related backup and rollback files and remove them
you first checked the Phase 7 task before even removing all cohere backup files like
@physical-ai-and-humanoid-robotics\rag-chatbot\rag\retrieve.py.backup
@physical-ai-and-humanoid-robotics\rag-chatbot\rag\ingest.py.backup
@physical-ai-and-humanoid-robotics\rag-chatbot\rollback.md
@physical-ai-and-humanoid-robotics\rag-chatbot\gemini_embedding_guide.py