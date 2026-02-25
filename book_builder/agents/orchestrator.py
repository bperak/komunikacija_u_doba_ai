"""Top-level orchestrator agent for the Scientific Book Builder.

This agent decides which specialist to invoke at each step.
"""

from __future__ import annotations

import asyncio

from dotenv import load_dotenv

from agents import Agent, Runner, InputGuardrail

load_dotenv()
from pydantic import BaseModel

from .specialists import (
    web_agent,
    rag_agent,
    citation_agent,
    style_agent,
    writer_agent,
    proofreader_agent,
)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

__all__ = ["orchestrator", "main"]


# ---------------------------------------------------------------------------
# Guardrails – ensure user submitted substantive text
# ---------------------------------------------------------------------------
class ManuscriptInput(BaseModel):
    """Simple schema to validate manuscript-like input."""

    text: str


validator_agent = Agent(
    name="Input Validator",
    instructions="Return true if the provided text looks like a manuscript section (≥10 chars).",
    output_type=bool,
)


async def manuscript_guardrail(ctx, agent, input_data: str):  # noqa: D401
    """Guardrail callback that checks if `input_data` appears valid."""

    if not isinstance(input_data, str):
        # Tripwire
        return False
    return len(input_data.strip()) >= 10


# ---------------------------------------------------------------------------
# Orchestrator definition
# ---------------------------------------------------------------------------
ORCHESTRATOR_PROMPT = (
    f"{RECOMMENDED_PROMPT_PREFIX}"
    "You are the Orchestrator in a multi-agent system that writes, improves, and validates "
    "scientific-book chapters. Based on the user's request or the current draft, decide which "
    "specialist agent to invoke next.\n\n"
    "Specialists and their purposes:\n"
    "- Web Searcher: gather new info from the web.\n"
    "- RAG Retriever: fetch academic facts from the knowledge base.\n"
    "- Content Writer: generate or expand manuscript text.\n"
    "- Citation Checker: validate references and formatting.\n"
    "- Style Enforcer: ensure the text meets the IEEE style guide.\n"
    "- Proofreader: final polish and copy-editing.\n\n"
    "When you determine a specialist is needed, handoff to that agent. If the draft is complete, "
    "call Proofreader and then return the polished text."
)

orchestrator = Agent(
    name="Book Orchestrator",
    instructions=ORCHESTRATOR_PROMPT,
    handoffs=[
        web_agent,
        rag_agent,
        writer_agent,
        citation_agent,
        style_agent,
        proofreader_agent,
    ],
    input_guardrails=[InputGuardrail(guardrail_function=manuscript_guardrail)],
)


# ---------------------------------------------------------------------------
# CLI helper
# ---------------------------------------------------------------------------
async def main() -> None:  # pragma: no cover
    """CLI entrypoint for quick manual testing."""

    import textwrap

    user_input = textwrap.dedent(
        """
        Write an overview of the CRISPR-Cas9 gene-editing mechanism and its recent applications in agriculture.
        """
    ).strip()

    result = await Runner.run(orchestrator, user_input)
    print("\n==== FINAL OUTPUT ====\n")
    print(result.final_output)


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main()) 