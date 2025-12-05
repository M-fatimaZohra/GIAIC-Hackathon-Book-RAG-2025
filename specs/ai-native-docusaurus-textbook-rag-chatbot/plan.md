<!--
Sync Impact Report:
Version change: 1.0.0 -> 1.0.1
List of modified principles: None
Added sections: Detailed Book Structure, Refined Subagents & Responsibilities, Updated Task Flow
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
Follow-up TODOs: None
-->
# Implementation Plan: AI-Native Docusaurus Textbook + RAG Chatbot

**Branch**: `main` | **Date**: 2025-12-03 | **Spec**: specs/ai-native-docusaurus-textbook-rag-chatbot/spec.md
**Input**: Feature specification from `/specs/ai-native-docusaurus-textbook-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the automated production of an AI-Native Docusaurus Textbook and an integrated RAG chatbot focusing on Physical AI & Humanoid Robotics, based on the Panaversity course outline. The goal is to automatically generate a comprehensive textbook, deploy it on GitHub Pages, and build a fully functional RAG chatbot using FastAPI, Qdrant, and the Agents SDK. The textbook will feature a detailed Table of Contents with modules covering ROS 2, Gazebo, NVIDIA Isaac, and conversational AI integration, enhanced with code examples, diagrams, and educational explanations. Optional features like user personalization and Urdu translation are also considered. The workflow leverages specialized AI subagents for content drafting, research validation, code generation, deployment, RAG system building, and testing, all automated through Claude Code.

## Technical Context

**Language/Version**: Python 3.x (FastAPI backend, ROS 2 rclpy), TypeScript/JavaScript (Docusaurus book)
**Primary Dependencies**: Docusaurus, FastAPI, Qdrant, Agents SDK, Claude Code, Spec-Kit Plus.
**Storage**: Qdrant (vector database for RAG), GitHub Pages (static content hosting for Docusaurus book).
**Testing**: Automated by TestingAgent (chatbot queries accuracy, book link integrity, frontend functionality, Docusaurus build).
**Target Platform**: GitHub Pages (frontend Docusaurus book), Render/Vercel (FastAPI backend).
**Performance Goals**: RAG chatbot provides accurate, cited, and non-hallucinatory responses; subagents efficiently generate and validate content/code; Docusaurus builds compile with no errors and load quickly.
**Constraints**: All tasks fully automated by Claude Code/subagents; no human intervention for code push, deployment, or backend setup; free-tier APIs only (GitHub Pages, Qdrant Cloud, free API keys for Claude Code/UV/OpenRouter); book size manageable (avoid heavy assets); simulations only described (no requirement to run them); RAG answers must cite sources (chapter + section).
**Scale/Scope**: Comprehensive textbook with Preface, 6 core Modules, Appendices, and Bonus/Optional Features (totaling more than 10-15 chapters/sections); integrated RAG chatbot; optional user personalization and Urdu translation.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Accuracy and Verifiability**: Content drafted by WriterAgent will be validated by ResearchAgent against primary robotics/AI sources. (PASS)
- **II. Clarity and Pedagogical Approach**: Chapters designed for clarity for beginner/intermediate students, with diagrams and examples. (PASS)
- **III. Practical Embodied AI Focus**: Textbook content heavily focused on Physical AI, humanoid robot control, and real-world/simulated interfaces. (PASS)
- **IV. Modular Design**: Book structure (Docusaurus) and RAG system (FastAPI, Qdrant) designed for modularity. Subagents are modular. (PASS)
- **V. Spec-Driven Development (SDD)**: This plan follows the SDD workflow, derived from the feature specification. (PASS)

## Project Structure

### Documentation (this feature)

```text
specs/ai-native-docusaurus-textbook-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output (research from ResearchAgent)
├── data-model.md        # Phase 1 output (RAG data model, Qdrant schema)
├── quickstart.md        # Phase 1 output (deployment quickstart)
├── contracts/           # Phase 1 output (API contracts for FastAPI)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
./
├── physical-ai-and-humanoid-robotics/ # Docusaurus project root
│   ├── docs/                   # Markdown/MDX chapters and sections
│   │   ├── preface.mdx
│   │   ├── module1/
│   │   │   ├── _category_.json
│   │   │   ├── introduction.mdx
│   │   │   ├── why_humanoid_robots.mdx
│   │   │   └── overview_embodied_intelligence.mdx
│   │   ├── module2/
│   │   │   ├── _category_.json
│   │   │   ├── ros2_basics.mdx
│   │   │   ├── rclpy_packages.mdx
│   │   │   ├── urdf_sdf.mdx
│   │   │   └── simple_humanoid_urdf.mdx
│   │   ├── module3/
│   │   │   ├── _category_.json
│   │   │   ├── gazebo_setup.mdx
│   │   │   ├── physics_simulation.mdx
│   │   │   ├── simulating_sensors.mdx
│   │   │   └── unity_integration.mdx (optional)
│   │   ├── module4/
│   │   │   ├── _category_.json
│   │   │   ├── intro_nvidi-isaac.mdx
│   │   │   ├── perception.mdx
│   │   │   ├── navigation_path_planning.mdx
│   │   │   └── sim_to_real.mdx
│   │   ├── module5/
│   │   │   ├── _category_.json
│   │   │   ├── vla_concepts.mdx
│   │   │   ├── voice_commands_ros2.mdx
│   │   │   ├── llm_high_level_planning.mdx
│   │   │   └── clean_room_pipeline.mdx
│   │   ├── module6/
│   │   │   ├── _category_.json
│   │   │   ├── capstone_project.mdx
│   │   │   ├── simulation_to_edge.mdx
│   │   │   └── limitations.mdx
│   │   ├── appendices/
│   │   │   ├── _category_.json
│   │   │   ├── sensors_primer.mdx
│   │   │   ├── robotics_math.mdx
│   │   │   ├── glossary_terms.mdx
│   │   │   └── setup_guides.mdx
│   │   ├── bonus_features/ (optional)
│   │   │   ├── _category_.json
│   │   │   ├── personalization.mdx
│   │   │   ├── urdu_translation.mdx
│   │   │   ├── using_rag_chatbot.mdx
│   │   │   └── agentic_ai_robotics.mdx
│   │   └── sidebar.js             # Docusaurus generated sidebar config
│   ├── src/                    # Custom Docusaurus components (TSX)
│   ├── static/                 # Static assets (images, diagrams)
│   └── docusaurus.config.js      # Docusaurus main config
├── backend/                    # FastAPI RAG chatbot backend
│   ├── app/                    # FastAPI application code
│   │   ├── api/                # API endpoints for RAG queries
│   │   ├── services/           # RAG logic, Qdrant integration, embedding models
│   │   └── models/             # Pydantic models for data (e.g., query, response)
│   ├── tests/                  # Backend tests
│   └── main.py                 # FastAPI application entry point
├── agents/                     # Claude Code subagents and skills
│   ├── writer_agent.py         # Handles chapter drafting and content generation
│   ├── research_agent.py       # Validates content accuracy and references
│   ├── code_agent.py           # Generates code snippets, diagrams, ROS 2 packages
│   ├── deployment_agent.py     # Manages Docusaurus deployment to GitHub Pages
│   ├── rag_builder_agent.py    # Indexes content, builds RAG backend
│   ├── testing_agent.py        # Validates chatbot, book links, frontend
│   ├── auth_agent.py (optional) # Handles user authentication and profile
│   ├── personalization_agent.py (optional) # Adapts content based on user profile
│   └── urdu_agent.py (optional)  # Translates content to Urdu
├── history/                    # Prompt History Records (PHRs)
├── .github/workflows/          # CI/CD for Docusaurus deployment (e.g., deploy.yml)
├── .specify/                   # SpecKit Plus templates and configs
└── README.md                   # Project README
```

**Structure Decision**: A monorepo-like structure is chosen to co-locate the Docusaurus book, FastAPI backend, and AI agents. This facilitates unified version control and simplifies local development while allowing independent deployment for the book (GitHub Pages) and backend (Render/Vercel). The `physical-ai-and-humanoid-robotics/` directory will contain the Docusaurus project, with a detailed `docs/` structure reflecting the textbook's Table of Contents. `backend/` will host the FastAPI application, and `agents/` will house the specialized Claude Code subagents and their skills. CI/CD configurations for Docusaurus will be in `.github/workflows/`. Optional agents are clearly marked.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A       | N/A        | N/A                                  |
