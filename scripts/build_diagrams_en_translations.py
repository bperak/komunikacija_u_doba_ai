#!/usr/bin/env python3
"""
Build docs/diagrams_en/string_translations.json from unique <text> strings in chapter SVGs.
Uses deep-translator (Google) hr->en. Idempotent: skips lines already in JSON.
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT = Path(__file__).resolve().parent.parent
HR_TEXTS = PROJECT / "docs" / "_svg_unique_texts_hr.json"
OUT_JSON = PROJECT / "docs" / "diagrams_en" / "string_translations.json"


def collect_unique_texts() -> list[str]:
    ch = PROJECT / "manuscript" / "chapters"
    diag = PROJECT / "docs" / "diagrams"
    seen_files: set[str] = set()
    for p in ch.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r"docs/diagrams/([^)\s\"']+\.svg)", t):
            seen_files.add(m.group(1))
    texts: set[str] = set()
    for name in seen_files:
        fp = diag / name
        if not fp.exists():
            continue
        s = fp.read_text(encoding="utf-8")
        for m in re.finditer(r">([^<]{2,})</text>", s):
            tx = m.group(1).strip()
            if tx and not tx.startswith("var("):
                texts.add(tx)
    return sorted(texts, key=lambda x: x.lower())


def main() -> None:
    from deep_translator import GoogleTranslator

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    data: dict[str, str] = {}
    if OUT_JSON.exists():
        data = json.loads(OUT_JSON.read_text(encoding="utf-8"))

    texts = collect_unique_texts()
    HR_TEXTS.write_text(json.dumps(texts, ensure_ascii=False, indent=2), encoding="utf-8")

    translator = GoogleTranslator(source="hr", target="en")
    pending = [t for t in texts if t not in data]
    print("Already translated:", len(data), "| Pending:", len(pending))

    for i, text in enumerate(pending):
        try:
            en = translator.translate(text)
            data[text] = en if en else text
        except Exception as exc:
            try:
                en = GoogleTranslator(source="auto", target="en").translate(text)
                data[text] = en if en else text
            except Exception:
                data[text] = text
            print("WARN:", repr(text[:72]), type(exc).__name__)
        if (i + 1) % 25 == 0:
            OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print("  checkpoint", i + 1)
        time.sleep(0.12)

    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", OUT_JSON, "entries:", len(data))


if __name__ == "__main__":
    main()
