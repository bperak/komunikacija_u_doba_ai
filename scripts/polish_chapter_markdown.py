#!/usr/bin/env python3
"""Normalize chapter Markdown on disk for Pandoc (blank lines around captions and ATX headings)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SCRIPTS = PROJECT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_pdf import (  # noqa: E402
    CHAPTER_FILES,
    ensure_blank_line_after_figure_slika_captions,
    ensure_blank_line_before_atx_headings,
    fix_caption_newlines,
)


def polish(md: str) -> str:
    md = fix_caption_newlines(md)
    md = ensure_blank_line_after_figure_slika_captions(md)
    md = ensure_blank_line_before_atx_headings(md)
    return md


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--locale",
        choices=("hr", "en", "all"),
        default="all",
        help="hr = manuscript/chapters, en = manuscript/en/chapters, all = both",
    )
    args = parser.parse_args()

    dirs: list[Path] = []
    if args.locale in ("hr", "all"):
        dirs.append(PROJECT / "manuscript" / "chapters")
    if args.locale in ("en", "all"):
        dirs.append(PROJECT / "manuscript" / "en" / "chapters")

    changed: list[str] = []
    for d in dirs:
        if not d.is_dir():
            print(f"Skip (missing): {d}")
            continue
        for fname in CHAPTER_FILES:
            path = d / fname
            if not path.exists():
                continue
            raw = path.read_text(encoding="utf-8")
            new = polish(raw)
            if new != raw:
                path.write_text(new, encoding="utf-8", newline="\n")
                changed.append(str(path.relative_to(PROJECT)))

    if changed:
        print("Updated:")
        for p in changed:
            print(f"  {p}")
    else:
        print("No changes needed (already polished).")


if __name__ == "__main__":
    main()
