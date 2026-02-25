"""Core tool implementations for the Scientific Book Builder.

These are deliberately simple stubs so unit tests remain deterministic.
Replace with real API calls or library integrations later.
"""

from __future__ import annotations

import random
from agents import function_tool


@function_tool
def web_search(query: str) -> str:  # noqa: D401
    """Perform a (stub) web search.

    Args:
        query: Search string.

    Returns:
        str: Fake SERP summary.
    """

    # Reason: keep deterministic for tests; later integrate real search.
    return f"[SERP results summarised for '{query}']"


@function_tool
def retrieve_facts(topic: str) -> str:
    """Retrieve facts from a vector DB (stub).

    Args:
        topic: Scientific topic.

    Returns:
        str: Bullet-point facts.
    """

    bullets = [
        "• Fact 1",
        "• Fact 2",
        "• Fact 3",
    ]
    return f"Facts about {topic}:\n" + "\n".join(bullets)


@function_tool
def check_citation(citation_text: str) -> bool:
    """Validate a citation string (stub)."""

    # Reason: pseudorandom response to mimic pass/fail.
    return random.choice([True, False])


@function_tool
def style_lint(text: str) -> str:
    """Perform a style lint (stub)."""

    return "OK (stub style lint)"


__all__ = [
    "web_search",
    "retrieve_facts",
    "check_citation",
    "style_lint",
] 