#!/usr/bin/env python3
"""
Razdvaja rukopis manuscript/Ben knjiga lektorirana_za_obradu.md u 10 datoteka
u manuscript/chapters/: naslovnica, 8 poglavlja, referencije.
Granice: ^# [0-9] za poglavlja 1-8, ^# Referencije za referencije.
Putanje slika: ](../docs/diagrams/ -> ](../../docs/diagrams/ u chapter datotekama.
Kodiranje: UTF-8. Originalni rukopis se ne mijenja.
"""

import re
from pathlib import Path

# Putanje (od korijena projekta)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_PATH = PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu.md"
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"

# Mapiranje: redni broj izlaza -> (ime datoteke, opis)
OUTPUT_FILES = [
    (0, "00_naslovnica.md", "Naslovnica (redci 1–48)"),
    (1, "01_uvod.md", "Poglavlje 1"),
    (2, "02_povijest_tehnologija.md", "Poglavlje 2"),
    (3, "03_veliki_jezicni_modeli.md", "Poglavlje 3"),
    (4, "04_dekonstrukcija_jezika.md", "Poglavlje 4"),
    (5, "05_pogon_umjetne_inteligencije.md", "Poglavlje 5"),
    (6, "06_od_modela_do_partnera.md", "Poglavlje 6"),
    (7, "07_izgradnja_partnera.md", "Poglavlje 7"),
    (8, "08_digitalni_suputnici.md", "Poglavlje 8"),
    (9, "09_referencije.md", "Referencije"),
]

# Regex: početak retka, #, razmak, znamenka (poglavlja 1–8)
RE_CHAPTER_HEADER = re.compile(r"^#\s+[0-9]")
# Regex: # pa eventualno razmaci pa "Referencije"
RE_REFERENCIJE = re.compile(r"^#\s*Referencije\s*$", re.IGNORECASE)


def find_boundaries(lines: list[str]) -> tuple[list[int], int | None]:
    """
    Vraća (lista redaka gdje počinju poglavlja 1–8, redak za Referencije ili None).
    Redci su 0-based.
    """
    chapter_starts: list[int] = []
    referencije_line: int | None = None
    for i, line in enumerate(lines):
        if RE_REFERENCIJE.match(line.strip()):
            referencije_line = i
            break
        if RE_CHAPTER_HEADER.match(line.strip()):
            chapter_starts.append(i)
    return chapter_starts, referencije_line


def adapt_image_paths(text: str) -> str:
    """Zamjena putanja slika za chapters: ](../docs/diagrams/ -> ](../../docs/diagrams/"""
    return text.replace("](../docs/diagrams/", "](../../docs/diagrams/")


def main() -> None:
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    content = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    chapter_starts, ref_line = find_boundaries(lines)
    if len(chapter_starts) < 8:
        raise SystemExit(
            f"Očekivano 8 početaka poglavlja (^# [0-9]), pronađeno: {len(chapter_starts)}"
        )
    if ref_line is None:
        raise SystemExit("Nije pronađen redak '# Referencije'.")

    # Granice (0-based): naslovnica 0..48-1, ch1 48..ch2-1, ... ch8 .. ref-1, ref..end
    bounds = [0, 48]  # naslovnica 1–48 -> indeksi 0..47
    for i in range(8):
        bounds.append(chapter_starts[i])
    bounds.append(ref_line)
    bounds.append(len(lines))

    # Segmenti za svaku od 10 datoteka: [start, end) u indeksima
    segments: list[tuple[int, int]] = []
    segments.append((0, 48))  # 00_naslovnica: redci 1–48
    for i in range(8):
        start = chapter_starts[i]
        end = chapter_starts[i + 1] if i + 1 < 8 else ref_line
        segments.append((start, end))
    segments.append((ref_line, len(lines)))  # 09_referencije

    for (idx, filename, _), (start, end) in zip(OUTPUT_FILES, segments):
        chunk_lines = lines[start:end]
        chunk_text = "".join(chunk_lines)
        chunk_text = adapt_image_paths(chunk_text)
        out_path = CHAPTERS_DIR / filename
        out_path.write_text(chunk_text, encoding="utf-8")
        print(f"Zapisano: {out_path.name} (redci {start + 1}–{end})")

    print("Gotovo. 10 datoteka u manuscript/chapters/")


if __name__ == "__main__":
    main()
