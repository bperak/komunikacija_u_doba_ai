#!/usr/bin/env python3
"""
Izvlači definicije iz poglavlja 01–08 i piše Glosar (10_glosar.md).

Hrvatski (default): > **Definicija (Pojam):** Tekst.
Engleski: > **Term:** Tekst.  (blokcitati s podebljanim pojmom prije dvotočke)
Kodiranje: UTF-8.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHAPTER_FILES = [
    "01_uvod.md",
    "02_povijest_tehnologija.md",
    "03_veliki_jezicni_modeli.md",
    "04_dekonstrukcija_jezika.md",
    "05_pogon_umjetne_inteligencije.md",
    "06_od_modela_do_partnera.md",
    "07_izgradnja_partnera.md",
    "08_digitalni_suputnici.md",
]

PATTERN_HR = re.compile(r"^\s*> \*\*Definicija \((.+?)\):\*\* (.+)$", re.MULTILINE)
# English chapters use translated blockquotes: > **Term:** definition text
PATTERN_EN = re.compile(r"^\s*> \*\*([^*]+?):\*\* (.+)$", re.MULTILINE)


def sort_key_hr(item: tuple[str, str]) -> str:
    term = item[0].lower()
    for old, new in [("č", "c"), ("ć", "c"), ("š", "s"), ("ž", "z"), ("đ", "d")]:
        term = term.replace(old, new)
    return term


def sort_key_en(item: tuple[str, str]) -> str:
    return item[0].lower()


def extract_definitions(chapters_dir: Path, language: str) -> list[tuple[str, str]]:
    pat = PATTERN_HR if language == "hr" else PATTERN_EN
    seen_terms: set[str] = set()
    out: list[tuple[str, str]] = []
    for fname in CHAPTER_FILES:
        path = chapters_dir / fname
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for m in pat.finditer(text):
            term = m.group(1).strip()
            body = m.group(2).strip()
            key = term.lower()
            if key in seen_terms:
                continue
            seen_terms.add(key)
            out.append((term, body))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract glossary definitions from chapters 1–8.")
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=PROJECT_ROOT / "manuscript" / "chapters",
        help="Directory containing chapter markdown files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output markdown path (default: <chapters-dir>/10_glosar.md)",
    )
    parser.add_argument(
        "--language",
        choices=("hr", "en"),
        default="hr",
        help="hr = Definicija (Term): pattern; en = **Term:** blockquote pattern",
    )
    args = parser.parse_args()

    chapters_dir = args.chapters_dir.resolve()
    output_path = args.output or (chapters_dir / "10_glosar.md")

    items = extract_definitions(chapters_dir, args.language)
    items.sort(key=sort_key_hr if args.language == "hr" else sort_key_en)

    if args.language == "hr":
        title = "# Glosar"
        intro = (
            "Ovaj odjeljak sadrži abecedni popis ključnih pojmova korištenih u knjizi, s kratkim definicijama. "
            "Definicije su izvučene iz poglavlja 1–8; u tijeku čitanja nalaze se na mjestu prvog spomena."
        )
    else:
        title = "# Glossary"
        intro = (
            "This section lists key terms used in the book with short definitions. "
            "Entries are drawn from chapters 1–8; in the main text they appear at first mention."
        )

    lines = [title, "", intro, "", "---", ""]
    for term, body in items:
        lines.append(f"**{term}** — {body}")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    try:
        rel = output_path.resolve().relative_to(PROJECT_ROOT.resolve())
    except ValueError:
        rel = output_path
    print("Zapisano:", rel, "| Broj definicija:", len(items))


if __name__ == "__main__":
    main()
