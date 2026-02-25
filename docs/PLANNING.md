# Scientific Book Builder – Architecture & Conventions

## Purpose
An extensible multi-agent system, powered by `openai-agents`, that collaborates to draft, refine, and polish scientific-book chapters.  The system must respect project coding rules (≤500 lines per file, tests in `/tests`, etc.).

## High-Level Components
| Layer | Module(s) | Responsibility |
|-------|-----------|----------------|
| Function Tools | `book_builder/tools/` | Pure-Python functions that hit external services (or stubs in tests). Decorated with `@function_tool`. |
| Specialist Agents | `book_builder/agents/specialists.py` | Domain-specific agents (web search, RAG, citation, style, content writer, proofreader). Each exposes `handoff_description` for routing. |
| Orchestrator | `book_builder/agents/orchestrator.py` | Top-level agent that decides which specialist to invoke and maintains run context. Includes optional guardrails. |
| Entrypoint | `book_builder/agents/orchestrator.py` (`main` function) | Scriptable runner for CLI or integration with FastAPI later. |
| Tests | `tests/` | Pytest suites for tool logic and one end-to-end flow with mocks. |

**Diagram:** `docs/diagrams/architecture.mmd` (Mermaid) → render with [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid): `node scripts/render_mermaid.mjs -f docs/diagrams/architecture.mmd -o docs/diagrams/architecture.svg` or `python scripts/render_diagrams.py`.

## Naming & Structure
```
book_builder/
 ├─ __init__.py
 ├─ tools/
 │   ├─ __init__.py
 │   └─ core.py
 └─ agents/
     ├─ __init__.py
     ├─ specialists.py
     └─ orchestrator.py
```

## Coding Standards
* Python 3.10+, PEP8, `black`-formatted.
* All functions & classes documented (Google-style docstrings).
* Keep each file <500 LOC; split further if necessary.
* Use type hints & `pydantic` for structured data.

## Future Extensions
* Replace stubbed tools with real integrations (SerpAPI, vector DB, Zotero).
* Persist drafts & citations in a database via SQLModel.
* Wrap orchestrator behind FastAPI plus WebSockets for UI.

---
_Last updated: 2024-06-11_ 