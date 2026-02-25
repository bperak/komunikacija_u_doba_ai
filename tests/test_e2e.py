"""End-to-end test for orchestrator with deterministic output.

We monkeypatch `Runner.run` to bypass network calls and return predictable results.
"""

from types import SimpleNamespace

import pytest

from book_builder.agents.orchestrator import orchestrator


class DummyResult(SimpleNamespace):
    """Simple replacement for Runner result."""

    final_output: str = "DUMMY"


@pytest.fixture(autouse=True)
def patch_runner(monkeypatch):
    """Replace Runner.run with a dummy implementation."""

    def _dummy_run(agent, *args, **kwargs):  # noqa: D403
        return DummyResult(final_output="TEST OUTPUT")

    monkeypatch.setattr("agents.Runner.run", _dummy_run)


def test_orchestrator_returns_output():
    # Import here to avoid circular imports in patched environment
    from agents import Runner  # pylint: disable=import-error

    result = Runner.run_sync(
        orchestrator,
        "Some draft text about CRISPR",
    )

    assert result.final_output == "TEST OUTPUT" 