"""Tests for Pandoc-safe Markdown spacing (scripts/build_pdf)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from build_pdf import (
    ensure_blank_line_after_figure_slika_captions,
    ensure_blank_line_before_atx_headings,
)


def test_inserts_blank_between_paragraph_and_heading():
    md = "End of paragraph here.\n### 2.3 Next section\nBody."
    assert ensure_blank_line_before_atx_headings(md) == (
        "End of paragraph here.\n\n### 2.3 Next section\nBody."
    )


def test_inserts_blank_between_figure_caption_and_heading():
    md = (
        '<p class="img-wrap"><img src="x.svg" alt=""></p>\n'
        "*Figure 2.4: Caption text.*\n"
        "### 2.3.1 Subsection\n"
        "More text."
    )
    out = ensure_blank_line_before_atx_headings(md)
    assert "\n\n### 2.3.1 Subsection\n" in out


def test_no_extra_blank_between_consecutive_headings():
    md = "# Title\n## Subtitle\n\nPara."
    assert ensure_blank_line_before_atx_headings(md) == md


def test_skips_inside_fenced_code():
    md = "```\n# not a heading\n### also not\n```\n### Real heading\n"
    out = ensure_blank_line_before_atx_headings(md)
    assert "# not a heading" in out
    assert out.count("### Real heading") == 1


def test_idempotent():
    md = "A\n\n### B\n"
    once = ensure_blank_line_before_atx_headings(md)
    twice = ensure_blank_line_before_atx_headings(once)
    assert once == twice


def test_blank_after_figure_caption_before_paragraph():
    md = "*Figure 2.4: Caption.*\nNext paragraph."
    assert ensure_blank_line_after_figure_slika_captions(md) == (
        "*Figure 2.4: Caption.*\n\nNext paragraph."
    )


def test_blank_after_slika_caption_before_blockquote():
    md = "*Slika 1.1: Opis.*\n> Citat"
    out = ensure_blank_line_after_figure_slika_captions(md)
    assert out == "*Slika 1.1: Opis.*\n\n> Citat"


def test_no_insert_when_blank_already_present():
    md = "*Figure 1.1: X.*\n\nBody."
    assert ensure_blank_line_after_figure_slika_captions(md) == md


def test_caption_suffix_letter():
    md = "*Slika 2.3a: Note.*\nMore."
    assert "\n\nMore." in ensure_blank_line_after_figure_slika_captions(md)
