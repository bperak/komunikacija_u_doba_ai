"""Tool functions usable by agents (web search, RAG, etc.)."""

from .core import (
    web_search,
    retrieve_facts,
    check_citation,
    style_lint,
)

__all__ = [
    "web_search",
    "retrieve_facts",
    "check_citation",
    "style_lint",
] 