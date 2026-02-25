"""Tests for Mermaid diagram setup (beautiful-mermaid), unify, map, insert refs."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = PROJECT_ROOT / "docs" / "diagrams"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
RENDER_SCRIPT = SCRIPTS_DIR / "render_mermaid.mjs"
RENDER_DIAGRAMS_PY = SCRIPTS_DIR / "render_diagrams.py"

# Scripts are not a package; add scripts dir for direct imports
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def test_diagrams_dir_exists():
    """docs/diagrams exists and contains at least one .mmd file."""
    assert DIAGRAMS_DIR.is_dir(), "docs/diagrams should exist"
    mmd = list(DIAGRAMS_DIR.glob("*.mmd"))
    assert len(mmd) >= 1, "At least one .mmd source in docs/diagrams"


def test_architecture_mmd_content():
    """Architecture diagram source contains expected agent names."""
    arch = DIAGRAMS_DIR / "architecture.mmd"
    assert arch.is_file(), "docs/diagrams/architecture.mmd should exist"
    text = arch.read_text(encoding="utf-8")
    assert "graph" in text or "flowchart" in text.lower()
    assert "Orchestrator" in text
    assert "Proofreader" in text


def test_render_script_exists():
    """Node render script exists for beautiful-mermaid."""
    assert RENDER_SCRIPT.is_file(), "scripts/render_mermaid.mjs should exist"


def test_render_diagrams_py_exists():
    """Python batch render script exists."""
    assert RENDER_DIAGRAMS_PY.is_file(), "scripts/render_diagrams.py should exist"


def test_unify_truncate_label():
    """unify_diagram_style truncates long labels to MAX_LABEL_LENGTH."""
    import unify_diagram_style
    truncate_label = unify_diagram_style.truncate_label
    MAX_LABEL_LENGTH = unify_diagram_style.MAX_LABEL_LENGTH
    short = "Kratka"
    assert truncate_label(short) == short
    long_label = "A" * (MAX_LABEL_LENGTH + 10)
    out = truncate_label(long_label)
    assert len(out) <= MAX_LABEL_LENGTH
    assert out.endswith("...")


def test_unify_strips_style_and_html():
    """unify_mermaid removes style lines and HTML from content."""
    import unify_diagram_style
    unify_mermaid = unify_diagram_style.unify_mermaid
    content = """graph TD
A[Test <br> label]
B(Normal)
style A fill:#ccc,stroke:#333
"""
    out = unify_mermaid(content)
    assert "style" not in out
    assert "<br>" not in out
    assert "Test" in out and "label" in out


def test_insert_diagram_refs_placeholder_fallback():
    """insert_diagram_refs returns list of line numbers (from file or built-in)."""
    import insert_diagram_refs
    get_placeholder_lines = insert_diagram_refs.get_placeholder_lines
    got = get_placeholder_lines(PROJECT_ROOT)
    # Either from file or built-in; built-in has 33 entries
    assert len(got) >= 1
    assert all(isinstance(x, int) for x in got)


def test_map_diagram_fallback_candidate_anchor_lines():
    """map_diagram_positions_from_docx _candidate_anchor_lines returns headings and short lines."""
    import map_diagram_positions_from_docx
    cand = map_diagram_positions_from_docx._candidate_anchor_lines
    md_lines = [
        "",
        "# Naslov poglavlja",
        "Dugi redak " + "x" * 150,
        "Kratak redak.",
        "## Podnaslov",
        "```mermaid",
    ]
    indices = cand(md_lines)
    # Line 0 empty, 1 = #, 2 long skip (or include if <=120 - "Dugi" + 150 x = 155, so skip), 3 short, 4 = ##, 5 code skip
    assert 1 in indices
    assert 4 in indices
    assert 3 in indices
    assert 5 not in indices
    assert indices == sorted(indices)
