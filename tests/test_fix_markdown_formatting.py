"""Testovi za automatsko popravljanje bold/italic u Markdownu (scripts/fix_markdown_formatting)."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from fix_markdown_formatting import fix_bold_and_italic, fix_standalone_asterisks


def test_merge_consecutive_bold():
    text = "Riječ **a** **b** **c**."
    assert fix_bold_and_italic(text) == "Riječ **a b c**."


def test_merge_consecutive_italic():
    text = "engl. *shared* *intentionality*"
    assert fix_bold_and_italic(text) == "engl. *shared intentionality*"


def test_italic_broken_with_double_asterisk():
    text = "(engl. *theory** **of** **mind*)"
    assert fix_bold_and_italic(text) == "(engl. *theory of mind*)"


def test_bold_with_four_asterisks_between():
    text = "**zajedničke** **** **intencionalnosti**"
    assert fix_bold_and_italic(text) == "**zajedničke intencionalnosti**"


def test_standalone_four_asterisks_becomes_hr():
    text = "line1\n****\nline2"
    assert fix_standalone_asterisks(text) == "line1\n---\nline2"
