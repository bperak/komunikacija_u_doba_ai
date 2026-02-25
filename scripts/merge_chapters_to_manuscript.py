#!/usr/bin/env python3
"""
Spaja 11 datoteka iz manuscript/chapters/ (00–09 + 10_glosar) natrag u jedan MD.
Izlaz: manuscript/Ben knjiga lektorirana_za_obradu_from_chapters.md (original se ne prepisuje).
Putanje slika: ../../docs/diagrams/ -> ../docs/diagrams/ (za konzistentnost s rukopisom u manuscript/).
Kodiranje: UTF-8.
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"
OUTPUT_PATH = PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu_from_chapters.md"

CHAPTER_FILES = [
    "00_naslovnica.md",
    "01_uvod.md",
    "02_povijest_tehnologija.md",
    "03_veliki_jezicni_modeli.md",
    "04_dekonstrukcija_jezika.md",
    "05_pogon_umjetne_inteligencije.md",
    "06_od_modela_do_partnera.md",
    "07_izgradnja_partnera.md",
    "08_digitalni_suputnici.md",
    "09_referencije.md",
    "10_glosar.md",
]


def revert_image_paths(text: str) -> str:
    """Za ispis u manuscript/: ../../docs/diagrams/ -> ../docs/diagrams/"""
    return text.replace("](../../docs/diagrams/", "](../docs/diagrams/")


def main() -> None:
    parts = []
    for fname in CHAPTER_FILES:
        path = CHAPTERS_DIR / fname
        if not path.exists():
            raise SystemExit(f"Nedostaje: {path}")
        parts.append(path.read_text(encoding="utf-8"))

    merged = "".join(parts)
    merged = revert_image_paths(merged)
    OUTPUT_PATH.write_text(merged, encoding="utf-8")
    print("Zapisano:", OUTPUT_PATH.name)
    print("Broj redaka:", len(merged.splitlines()))


if __name__ == "__main__":
    main()
