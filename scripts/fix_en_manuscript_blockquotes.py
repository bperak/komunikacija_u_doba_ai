#!/usr/bin/env python3
"""
Insert blank lines before/after blockquote definition blocks (> **) in EN chapters
so body paragraphs are not glued to definitions in rendered HTML.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT = Path(__file__).resolve().parent.parent
EN_DIR = PROJECT / "manuscript" / "en" / "chapters"


def fix_blockquote_spacing(text: str) -> str:
    lines = text.splitlines()
    n = len(lines)
    insert_blank_before = [False] * n

    def prev_non_empty_index(idx: int) -> int:
        for j in range(idx - 1, -1, -1):
            if lines[j].strip():
                return j
        return -1

    for i in range(n):
        cur = lines[i].lstrip()
        if not cur.startswith(">"):
            continue
        j = prev_non_empty_index(i)
        if j < 0:
            continue
        if not lines[j].lstrip().startswith(">"):
            insert_blank_before[i] = True

    for i in range(1, n):
        cur = lines[i].lstrip()
        if not cur or cur.startswith(">") or cur.startswith("#") or cur.startswith("|") or cur.startswith("```"):
            continue
        j = prev_non_empty_index(i)
        if j < 0:
            continue
        if lines[j].lstrip().startswith(">"):
            insert_blank_before[i] = True

    out: list[str] = []
    for i, line in enumerate(lines):
        if insert_blank_before[i] and out and out[-1].strip() != "":
            out.append("")
        out.append(line)

    ending = "\n" if (text.endswith("\n") or not text) else ""
    return "\n".join(out) + ending


def main() -> None:
    changed = 0
    for path in sorted(EN_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        new = fix_blockquote_spacing(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print("updated", path.name)
    print("files changed:", changed)


if __name__ == "__main__":
    main()
