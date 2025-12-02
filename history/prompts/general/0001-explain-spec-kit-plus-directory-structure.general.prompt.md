---
id: 0001
title: Explain Spec-Kit Plus directory structure
stage: general
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: unknown
command: user question
labels: ["project-setup", "documentation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- history/prompts/general/0001-explain-spec-kit-plus-directory-structure.general.prompt.md
tests:

---

## Prompt

"I just installed Spec-Kit Plus and ran specifyplus init my-research-paper. Walk me through the directory structure: What's the purpose of .specify/, .claude/commands/, and specs/? How do these directories support the SDD-RI workflow?"

## Response snapshot

In a Spec-Kit Plus project, the `.specify/`, `.claude/commands/`, and `specs/` directories play distinct yet integrated roles in supporting the Spec-Driven Development with Rapid Iteration (SDD-RI) workflow.

-   `.specify/`: Core configuration hub for SpecKit Plus, containing templates, scripts, and foundational documents like `constitution.md`. Supports SDD-RI by ensuring consistency and reducing overhead for artifact creation.
-   `.claude/commands/`: Defines project-specific custom slash commands (e.g., `/sp.clarify`, `/sp.plan`, `/sp.tasks`) to automate complex workflows. Central to rapid iteration by streamlining development cycles.
-   `specs/`: Organizes feature-specific documentation (`spec.md`, `plan.md`, `tasks.md`). Underpins SDD by guiding development with well-defined specifications, facilitating traceability and agile adjustments.

## Outcome

- ✅ Impact: Provided a clear explanation of the Spec-Kit Plus directory structure and its role in SDD-RI.
- 🧪 Tests: No tests were run for this informational request.
- 📁 Files: One file was created (the PHR).
- 🔁 Next prompts: Awaiting user's next request.
- 🧠 Reflection: Successfully used `claude-code-guide` subagent for documentation lookup and followed PHR creation instructions.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
