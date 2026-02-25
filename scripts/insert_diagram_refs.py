"""
Umetanje referenci na SVG dijagrame u manuscript/Ben knjiga lektorirana_za_obradu.md.
Nakon retka s opisom (caption) umetne ![alt](../docs/diagrams/diag_NN.svg).
Broj referenci = min(broj dijagrama u docs/diagrams, broj redaka u listi).
Lista redaka: ugrađeno PLACEHOLDER_LINES (33) ili datoteka manuscript/diagram_placeholder_lines.txt (jedan broj retka po redu).
"""

from __future__ import annotations

from pathlib import Path

# Redci (1-based) na kojima je caption za dijagram, redoslijed = diag_01, diag_02, ...
PLACEHOLDER_LINES = [
    85, 98, 115, 148, 163, 181, 196, 209, 240, 273, 304, 320, 399,
    672, 685, 706, 847, 918, 1022, 1036, 1083, 1267, 1276, 1404, 1572,
    1759, 1873, 1898, 1944, 2050, 2131, 2161, 2200,
]


def get_placeholder_lines(project_root: Path) -> list[int]:
    """Ako postoji manuscript/diagram_placeholder_lines.txt, učitaj brojeve redaka; inače ugrađena lista."""
    path = project_root / "manuscript" / "diagram_placeholder_lines.txt"
    if path.is_file():
        lines = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    lines.append(int(line))
                except ValueError:
                    pass
        if lines:
            return lines
    return PLACEHOLDER_LINES.copy()


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    md_path = project_root / "manuscript" / "Ben knjiga lektorirana_za_obradu.md"
    diagrams_dir = project_root / "docs" / "diagrams"

    if not md_path.is_file():
        print("Rukopis ne postoji: manuscript/" + md_path.name)
        return 1

    # Broj dijagrama = diag_01.mmd .. diag_NN.mmd u docs/diagrams
    diag_mmd = sorted(diagrams_dir.glob("diag_*.mmd"))
    n_diagrams = len(diag_mmd)
    placeholder_lines = get_placeholder_lines(project_root)
    n_placeholders = len(placeholder_lines)
    n_insert = min(n_diagrams, n_placeholders)

    if n_diagrams > n_placeholders:
        print(
            f"Upozorenje: ima {n_diagrams} dijagrama, a samo {n_placeholders} pozicija (redaka). "
            f"Umetnut će se {n_insert} referenci. Za sve dodajte brojeve redaka u manuscript/diagram_placeholder_lines.txt",
            file=__import__("sys").stderr,
        )

    lines = md_path.read_text(encoding="utf-8").splitlines(keepends=True)
    # Ime dijagrama: diag_01..diag_99 (2 znamenke), diag_100.. (3 znamenke) – usklađeno s docs/diagrams/diag_*.mmd
    def diag_name_for(index: int) -> str:
        return f"diag_{index:02d}" if index < 100 else f"diag_{index}"
    inserted = 0
    # Umetanje od kraja prema početku da se indeksi ne pomaknu
    for i in range(n_insert - 1, -1, -1):
        line_num = placeholder_lines[i]
        diag_name = diag_name_for(i + 1)
        idx = line_num - 1
        if idx < 0 or idx >= len(lines):
            continue
        # Preskoči ako već postoji referenca na dijagram nakon ovog retka (bez duplikata)
        next_idx = idx + 1
        if next_idx < len(lines) and "](../docs/diagrams/diag_" in lines[next_idx]:
            continue
        caption = lines[idx].strip().rstrip("\n")
        if len(caption) > 80:
            alt = caption[:77] + "..."
        else:
            alt = caption.replace("\n", " ").replace("]", "\\]")
        insert = "\n\n![" + alt + "](../docs/diagrams/" + diag_name + ".svg)\n"
        lines.insert(idx + 1, insert)
        inserted += 1

    md_path.write_text("".join(lines), encoding="utf-8")
    print("Umetnuto referenci na dijagrame:", inserted)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
