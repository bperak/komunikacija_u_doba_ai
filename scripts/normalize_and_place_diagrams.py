"""
Parsira manuscript/mermaid_diagrami.md, izvlači sve Mermaid blokove s 'graph',
normalizira sintaksu (graph TD, pipe labele), zapisuje docs/diagrams/diag_01.mmd .. diag_NN.mmd.
N = broj svih graph blokova u katalogu (bez ograničenja).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def parse_mermaid_blocks_from_md(md_path: Path) -> list[str]:
    """Izvadi sve ```mermaid ... ``` blokove čiji sadržaj sadrži 'graph '."""
    text = md_path.read_text(encoding="utf-8")
    blocks = []
    pattern = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)
    for m in pattern.finditer(text):
        code = m.group(1).strip()
        if "graph " in code:
            blocks.append(code)
    return blocks


def normalize_mermaid(code: str) -> str:
    """
    Ujednači sintaksu prema PROCEDURI: graph TD, -->|label|, subgraph "title".
    """
    lines = code.split("\n")
    out = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("%%"):
            if s:
                out.append(s)
            continue
        # graph LR -> graph TD (za pouzdane edge labele); ukloni ; na kraju
        if re.match(r"^graph\s+(?:LR|TD|BT|RL)\b", s, re.IGNORECASE):
            s = re.sub(r"^graph\s+LR\b", "graph TD", s, flags=re.IGNORECASE)
            s = re.sub(r";\s*$", "", s)
        # --"label"--> -> -->|label|
        s = re.sub(r'--\s*"([^"]*)"\s*-->', r'-->|\1|', s)
        s = re.sub(r'--\s*"([^"]*)"\s*--', r'--|\1|', s)
        out.append(s)
    return "\n".join(out).strip()


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Normalizira Mermaid blokove iz mermaid_diagrami.md u docs/diagrams/diag_NN.mmd.")
    parser.add_argument("--max", type=int, default=None, help="Ograniči na prvih N dijagrama (npr. --max 87 za 87 iz DOCX-a)")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    catalog = project_root / "manuscript" / "mermaid_diagrami.md"
    diagrams_dir = project_root / "docs" / "diagrams"

    if not catalog.is_file():
        print("Katalog ne postoji:", catalog.as_posix(), file=sys.stderr)
        return 1

    blocks = parse_mermaid_blocks_from_md(catalog)
    total_in_catalog = len(blocks)
    print("Pronadeno graph blokova u katalogu:", total_in_catalog)
    if args.max is not None:
        blocks = blocks[: args.max]
        print("Ograničeno na prvih", len(blocks), "dijagrama (--max", args.max, ").")
    n = len(blocks)
    if n == 0:
        print("Nema graph blokova za zapis.", file=sys.stderr)
        return 1

    diagrams_dir.mkdir(parents=True, exist_ok=True)
    for i, code in enumerate(blocks, 1):
        normalized = normalize_mermaid(code)
        name = f"diag_{i:02d}"
        mmd_path = diagrams_dir / f"{name}.mmd"
        mmd_path.write_text(normalized, encoding="utf-8")
        print("Zapisano:", mmd_path.name)

    print("Ukupno zapisano dijagrama:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
