#!/usr/bin/env python3
"""
Copy chapter-referenced SVGs from docs/diagrams to docs/diagrams_en and apply
string_translations.json to <text>...</text> nodes (longest keys first).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT = Path(__file__).resolve().parent.parent
CH = PROJECT / "manuscript" / "chapters"
SRC = PROJECT / "docs" / "diagrams"
DST = PROJECT / "docs" / "diagrams_en"
MAP_PATH = DST / "string_translations.json"


def referenced_svgs() -> list[str]:
    seen: set[str] = set()
    for p in CH.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r"docs/diagrams/([^)\s\"']+\.svg)", t):
            seen.add(m.group(1))
    return sorted(seen)


def escape_xml_text(s: str) -> str:
    """Escape for raw text inside XML text element."""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def apply_map(svg: str, mapping: dict[str, str]) -> str:
    pairs = sorted(mapping.items(), key=lambda kv: -len(kv[0]))
    out = svg
    for hr, en in pairs:
        if not hr:
            continue
        en_esc = escape_xml_text(en)
        out = out.replace(f">{hr}</text>", f">{en_esc}</text>")
    return out


def main() -> None:
    mapping = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    DST.mkdir(parents=True, exist_ok=True)
    missing = []
    for name in referenced_svgs():
        sp = SRC / name
        if not sp.exists():
            missing.append(name)
            continue
        raw = sp.read_text(encoding="utf-8")
        new = apply_map(raw, mapping)
        (DST / name).write_text(new, encoding="utf-8")
    if missing:
        print("Missing source SVG:", missing)
    print("Wrote", len(referenced_svgs()) - len(missing), "files to diagrams_en/")


if __name__ == "__main__":
    main()
