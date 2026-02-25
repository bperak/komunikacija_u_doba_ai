"""Specialist agent definitions for Scientific Book Builder."""

from __future__ import annotations

from agents import Agent

from ..tools import (
    web_search,
    retrieve_facts,
    check_citation,
    style_lint,
)

__all__ = [
    "web_agent",
    "rag_agent",
    "citation_agent",
    "style_agent",
    "writer_agent",
    "proofreader_agent",
]

# Web search specialist
web_agent = Agent(
    name="Web Searcher",
    handoff_description="Performs live web searches for background info",
    instructions="Use the web_search tool to gather info. Summarise results.",
    tools=[web_search],
)

# Retrieval-augmented generation specialist
rag_agent = Agent(
    name="RAG Retriever",
    handoff_description="Retrieves precise scientific facts from a vector DB",
    instructions="Use retrieve_facts tool. Provide bullet-point facts.",
    tools=[retrieve_facts],
)

# Citation checking specialist
citation_agent = Agent(
    name="Citation Checker",
    handoff_description="Verifies that citations are correct and formatted",
    instructions="Use check_citation tool; reply OK or list bad citations.",
    tools=[check_citation],
)

# Style checking specialist
style_agent = Agent(
    name="Style Enforcer",
    handoff_description="Ensures the chapter follows IEEE style",
    instructions="Use style_lint tool; produce diffs or 'OK'.",
    tools=[style_lint],
)

# Content writing specialist
writer_agent = Agent(
    name="Content Writer",
    handoff_description="Generates initial prose given an outline",
    instructions="Write clear, concise scientific prose with citations.",
)

# Proofreading specialist
proofreader_agent = Agent(
    name="Proofreader",
    handoff_description="Does final copy-editing and polish",
    instructions="Fix typos, grammar, and improve flow.",
) 