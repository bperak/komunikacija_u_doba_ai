#!/usr/bin/env python3
"""
Izvlači sve blokove > **Definicija (Pojam):** Tekst. iz manuscript/chapters/ (01–08)
i piše Glosar u manuscript/chapters/10_glosar.md, sortirano abecedno po pojmu.
Kodiranje: UTF-8.
"""
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"
OUTPUT_PATH = CHAPTERS_DIR / "10_glosar.md"

# Poglavlja u kojima tražimo definicije (01–08)
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

# Format: > **Definicija (Pojam):** Tekst.
PATTERN = re.compile(r"^\s*> \*\*Definicija \((.+?)\):\*\* (.+)$", re.MULTILINE)


def extract_definitions() -> list[tuple[str, str]]:
    seen_terms = set()
    out = []
    for fname in CHAPTER_FILES:
        path = CHAPTERS_DIR / fname
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for m in PATTERN.finditer(text):
            term = m.group(1).strip()
            body = m.group(2).strip()
            # Jedan pojam samo jednom (prva pojavnica)
            key = term.lower()
            if key in seen_terms:
                continue
            seen_terms.add(key)
            out.append((term, body))
    return out


def sort_key(item: tuple[str, str]) -> str:
    """Sortiranje po pojmu, case-insensitive, hrvatska abeceda približno."""
    term = item[0].lower()
    # Zamjena za hrvatsko sortiranje (opcionalno: č->c, š->s, ž->z za stabilan red)
    for old, new in [("č", "c"), ("ć", "c"), ("š", "s"), ("ž", "z"), ("đ", "d")]:
        term = term.replace(old, new)
    return term


def main() -> None:
    items = extract_definitions()
    items.sort(key=sort_key)

    lines = [
        "# Glosar",
        "",
        "Ovaj odjeljak sadrži abecedni popis ključnih pojmova korištenih u knjizi, s kratkim definicijama. Definicije su izvučene iz poglavlja 1–8; u tijeku čitanja nalaze se na mjestu prvog spomena.",
        "",
        "---",
        "",
    ]
    for term, body in items:
        lines.append(f"**{term}** — {body}")
        lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print("Zapisano: 10_glosar.md | Broj definicija:", len(items))


if __name__ == "__main__":
    main()
