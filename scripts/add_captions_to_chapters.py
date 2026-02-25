#!/usr/bin/env python3
"""
Dodaje captione u formatu "Slika X.Y: ..." ispod svake slike u manuscript/chapters/.
X = broj poglavlja (0=naslovnica, 1-8=poglavlja, 9=referencije), Y = redni broj slike u poglavlju.
Ako slika već ima caption (redak koji počinje s "Slika" ili "Prikaz"), preskače se.
Kodiranje: UTF-8.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"

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
]

# Slika: ![alt](path) — tražimo putanju koja sadrži diagrams; alt ne smije sadržavati ]
RE_IMAGE_LINE = re.compile(r"!\[([^\]]*)\]\([^)]*diagrams/[^)]*\)")
RE_ALREADY_CAPTION = re.compile(r"^\*?(Slika|Prikaz)\s+\d", re.IGNORECASE)
MAX_CAPTION_LEN = 120


def extract_alt(line: str) -> str:
    m = RE_IMAGE_LINE.search(line)
    if not m:
        return "Dijagram"
    alt = m.group(1).strip()
    if not alt:
        return "Dijagram"
    alt = re.sub(r"\s+", " ", alt)
    if len(alt) > MAX_CAPTION_LEN:
        alt = alt[: MAX_CAPTION_LEN - 3].rstrip() + "..."
    return alt


def process_file(path: Path, chapter_num: int) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    new_lines = []
    img_count = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        if RE_IMAGE_LINE.search(line):
            img_count += 1
            next_stripped = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not RE_ALREADY_CAPTION.match(next_stripped):
                alt = extract_alt(line)
                caption = f"*Slika {chapter_num}.{img_count}: {alt}*"
                new_lines.append(caption + "\n")
        i += 1
    path.write_text("".join(new_lines), encoding="utf-8")
    return img_count


def main() -> None:
    if not CHAPTERS_DIR.is_dir():
        raise SystemExit("manuscript/chapters/ ne postoji.")
    total = 0
    for idx, filename in enumerate(CHAPTER_FILES):
        path = CHAPTERS_DIR / filename
        if not path.is_file():
            print(f"Preskačem (nema datoteke): {filename}")
            continue
        n = process_file(path, idx)
        total += n
        print(f"{filename}: {n} captiona")
    print(f"Ukupno: {total} captiona.")


if __name__ == "__main__":
    main()
