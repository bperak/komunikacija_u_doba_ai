"""Tests for scripts/polish_en_translation.py — EN-only machine-translation polish."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from polish_en_translation import polish_text


def test_strips_zero_width_space():
    zwsp = "\u200b"
    src = f"values {zwsp}{zwsp}and history"
    assert polish_text(src) == "values and history"


def test_drops_redundant_english_paren_gloss():
    src = "large language models (English *Large Language Model*, LLM)"
    assert polish_text(src) == "large language models (*Large Language Model*, LLM)"


def test_drops_from_english_paren_gloss():
    src = "API (from English *Application Programming Interface*)"
    assert polish_text(src) == "API (*Application Programming Interface*)"


def test_drops_eng_paren_gloss():
    src = "persona (eng. *role-playing*)"
    assert polish_text(src) == "persona (*role-playing*)"


def test_drops_eng_open_with_multiple_italics():
    src = "(eng. *real-time* or *online* inference)"
    assert polish_text(src) == "(*real-time* or *online* inference)"


def test_drops_english_after_comma():
    src = "centrality, English *betweenness*, which measures"
    assert polish_text(src) == "centrality, *betweenness*, which measures"


def test_drops_english_after_en_dash():
    src = "absolute value – English *magnitude pruning*"
    assert polish_text(src) == "absolute value – *magnitude pruning*"


def test_collapses_self_gloss_plain():
    src = "Application Programming Interface (*Application Programming Interface*) is"
    assert polish_text(src) == "Application Programming Interface is"


def test_collapses_self_gloss_bold():
    src = "**System prompt** (*system prompt*) occupies"
    assert polish_text(src) == "**System prompt** occupies"


def test_keeps_distinct_italic_gloss():
    src = "role and a person (*role-playing*)."
    assert polish_text(src) == "role and a person (*role-playing*)."


def test_normalizes_eg_inside_paren():
    src = "(eg predicting the next word)"
    assert polish_text(src) == "(e.g. predicting the next word)"


def test_normalizes_eg_after_dash():
    src = "attitudes or mood - eg frustration"
    assert polish_text(src) == "attitudes or mood - e.g. frustration"


def test_fixes_mt_active_offender():
    src = "the active offender remains just"
    assert polish_text(src) == "the active agent remains just"


def test_fixes_mt_propulsive_borders():
    src = "boundary becoming more and more propulsive, and"
    assert polish_text(src) == "boundary becoming increasingly permeable, and"


def test_idempotent():
    src = (
        "An API (English *API*), with eg. *cases* and a – English *quirk* "
        "(from English *foo*) that becoming more and more propulsive."
    )
    once = polish_text(src)
    assert polish_text(once) == once
