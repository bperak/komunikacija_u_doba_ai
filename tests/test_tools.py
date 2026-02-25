"""Unit tests for tool stubs in book_builder.tools.core."""

from book_builder.tools import (
    web_search,
    check_citation,
    style_lint,
)


def test_web_search_expected_use():
    result = web_search("CRISPR Cas9 latest news")
    assert "CRISPR" in result


def test_web_search_edge_empty():
    result = web_search("")
    assert result.startswith("[SERP results summarised")


def test_check_citation_failure_case():
    # With random.stubs there is 50% chance; repeat until we get False within few tries.
    for _ in range(10):
        if check_citation("Invalid citation") is False:
            break
    else:
        # If never False, raise fail.
        assert False, "check_citation never returned False in 10 tries"


def test_style_lint():
    assert style_lint("Some text") == "OK (stub style lint)" 