#!/usr/bin/env python3
"""Polish English translation artefacts in manuscript/en/chapters/*.md.

Targets common machine-translation leftovers that make the English edition
read awkwardly:

1. Strip U+200B (zero-width space) that survived from the Croatian source.
2. Drop redundant "(English *term*)" / "(from English *term*)" / "(eng. *term*)"
   glosses — the book is already in English, so these only add noise.
3. Collapse self-redundant glosses like "Application Programming Interface
   (*Application Programming Interface*)" introduced by step 2.
4. Fix a known mistranslation ("active offender" -> "active agent").

The script is idempotent: repeated runs produce no further changes.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
EN_DIR = PROJECT / "manuscript" / "en" / "chapters"

ZWSP = "\u200b"

# "(English *X*)" and "(English *X*, Y)" -> "(*X*)" / "(*X*, Y)"
PAT_ENGLISH_PAREN = re.compile(
    r"\((?:from\s+)?English\s+(\*[^*]+\*)(\s*,\s*[^)]+)?\)",
)
# "(eng. *X*)" and "(eng. *X*, Y)" -> "(*X*)" / "(*X*, Y)"
PAT_ENG_PAREN = re.compile(
    r"\(eng\.\s+(\*[^*]+\*)(\s*,\s*[^)]+)?\)",
    re.IGNORECASE,
)
# Drop "eng. " right after "(" when multiple italic segments follow — PAT_ENG_PAREN misses those.
PAT_ENG_OPEN = re.compile(r"\((?:eng\.|from\s+English|English)\s+(?=\*)")
# Inline: ", English *X*" / " – English *X*" / " — English *X*" -> drop "English "
PAT_INLINE_ENGLISH = re.compile(r"(?<=[,\-\u2013\u2014])\s+English\s+(\*[^*]+\*)")
# "eg " (MT artefact of Croatian "npr.") inside parens or after a dash -> "e.g. "
PAT_EG_OPEN = re.compile(r"\(eg\s+(?=[A-Za-z])")
PAT_EG_DASH = re.compile(r"([-\u2013\u2014])\s+eg\s+(?=[A-Za-z])")

# Collapse "<phrase> (*<same phrase>*)" into just "<phrase>" (plain or bold)
PAT_SELF_GLOSS = re.compile(
    r"([A-Za-z][A-Za-z0-9 \-]{2,}?)\s+\(\*([A-Za-z0-9 \-]+)\*\)",
)
PAT_SELF_GLOSS_BOLD = re.compile(
    r"(\*\*[A-Za-z][A-Za-z0-9 \-]{2,}?\*\*)\s+\(\*([A-Za-z0-9 \-]+)\*\)",
)

MANUAL_FIXES = [
    ("active offender", "active agent"),
    # "propusnija" = "more permeable"; MT rendered it as "propulsive".
    ("becoming more and more propulsive", "becoming increasingly permeable"),
]


def _normalize_phrase(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip()).lower()


def _collapse_self_gloss(text: str) -> str:
    def repl_plain(match: re.Match[str]) -> str:
        phrase = match.group(1)
        inside = match.group(2)
        if _normalize_phrase(phrase) == _normalize_phrase(inside):
            return phrase
        return match.group(0)

    def repl_bold(match: re.Match[str]) -> str:
        bold_phrase = match.group(1)
        inner_phrase = bold_phrase.strip("*")
        inside = match.group(2)
        if _normalize_phrase(inner_phrase) == _normalize_phrase(inside):
            return bold_phrase
        return match.group(0)

    text = PAT_SELF_GLOSS_BOLD.sub(repl_bold, text)
    text = PAT_SELF_GLOSS.sub(repl_plain, text)
    return text


def polish_text(md: str) -> str:
    original = md
    if ZWSP in md:
        md = md.replace(ZWSP, "")
    md = PAT_ENGLISH_PAREN.sub(lambda m: "(" + m.group(1) + (m.group(2) or "") + ")", md)
    md = PAT_ENG_PAREN.sub(lambda m: "(" + m.group(1) + (m.group(2) or "") + ")", md)
    md = PAT_ENG_OPEN.sub("(", md)
    md = PAT_INLINE_ENGLISH.sub(r" \1", md)
    md = PAT_EG_OPEN.sub("(e.g. ", md)
    md = PAT_EG_DASH.sub(r"\1 e.g. ", md)
    md = _collapse_self_gloss(md)
    for old, new in MANUAL_FIXES:
        md = md.replace(old, new)
    return md


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Only report what would change; do not write files.",
    )
    args = parser.parse_args()

    if not EN_DIR.is_dir():
        raise SystemExit(f"English chapters dir not found: {EN_DIR}")

    changed: list[tuple[str, int]] = []
    for path in sorted(EN_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        new = polish_text(raw)
        if new != raw:
            diff_lines = sum(1 for a, b in zip(raw.splitlines(), new.splitlines()) if a != b)
            diff_lines += abs(len(raw.splitlines()) - len(new.splitlines()))
            changed.append((path.name, diff_lines))
            if not args.check:
                path.write_text(new, encoding="utf-8", newline="\n")

    if changed:
        label = "Would update" if args.check else "Updated"
        print(f"{label}:")
        for name, n in changed:
            print(f"  {name}  ({n} line(s) affected)")
    else:
        print("No English polish changes needed.")


if __name__ == "__main__":
    main()
