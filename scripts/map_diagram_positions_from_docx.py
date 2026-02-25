"""
Mapiranje pozicija dijagrama: učitava diagram_captions_from_docx.json i manuscript MD,
za svaki caption pronalazi broj retka u MD; zapisuje manuscript/diagram_placeholder_lines.txt
(jedan broj retka po redu, redoslijed = diag_01 … diag_NN).

--fallback-headings: za pozicije koje ostaju 0, dodijeli sljedeći neiskorišteni redak
koji je naslov (#) ili kratka linija, da se dijagrami ne izgube.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def normalize_line(s: str) -> str:
    """Normalizira tekst za usporedbu: višestruki razmaci u jedan, trim."""
    return re.sub(r"\s+", " ", (s or "").strip())


def clean_caption(s: str) -> str:
    """Ista logika kao u extract: uklanja broj poglavlja, broj stranice, asteriske, leading #."""
    if not s:
        return ""
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"^#+\s*", "", s)
    s = re.sub(r"^\s*\d+(?:\.\d+)*\.?\s*", "", s)
    s = re.sub(r"\s*\d{1,4}\s*$", "", s)
    s = s.strip("*").strip()
    s = re.sub(r"\s+", " ", s).strip()
    return s


def normalize_md_line(line: str) -> str:
    """Za usporedbu s captionom: uklanja ### i broj poglavlja s početka, asteriske, razmake."""
    s = (line or "").strip()
    s = re.sub(r"^#+\s*", "", s)
    s = re.sub(r"^\s*\d+(?:\.\d+)*\.?\s*", "", s)
    s = s.strip("*").strip()
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _candidate_anchor_lines(md_lines: list[str]) -> list[int]:
    """Indeksi redaka koji su naslovi (#) ili kratke linije, u redoslijedu dokumenta."""
    candidates = []
    for i, line in enumerate(md_lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            candidates.append(i)
        elif len(s) <= 120 and not s.startswith("```"):
            candidates.append(i)
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser(description="Mapira captione iz DOCX na retke u MD.")
    parser.add_argument("--fallback-headings", action="store_true", help="Za 0 pozicije dodijeli sljedeći neiskorišteni naslov/kratku liniju.")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    captions_path = project_root / "manuscript" / "diagram_captions_from_docx.json"
    md_path = project_root / "manuscript" / "Ben knjiga lektorirana_za_obradu.md"
    out_path = project_root / "manuscript" / "diagram_placeholder_lines.txt"

    if not captions_path.is_file():
        print("Caption lista ne postoji: manuscript/" + captions_path.name, file=sys.stderr)
        print("Pokrenite prvo: python scripts/extract_mermaid_from_docx.py", file=sys.stderr)
        return 1
    if not md_path.is_file():
        print("Rukopis MD ne postoji: manuscript/" + md_path.name, file=sys.stderr)
        return 1

    with open(captions_path, encoding="utf-8") as f:
        captions_list = json.load(f)

    md_lines = md_path.read_text(encoding="utf-8").splitlines()
    md_normalized = [normalize_line(ln) for ln in md_lines]
    md_for_match = [normalize_md_line(ln) for ln in md_lines]

    placeholder_lines = []
    used_line_indices = set()

    for item in captions_list:
        index = item.get("index", 0)
        caption = (item.get("caption") or "").strip()
        norm_caption = clean_caption(caption)
        if not norm_caption and not caption:
            placeholder_lines.append(0)
            print("Upozorenje: dijagram", index, "nema captiona.", file=sys.stderr)
            continue
        if not norm_caption:
            norm_caption = normalize_line(caption)
        if len(norm_caption) < 3:
            placeholder_lines.append(0)
            continue
        found = None
        for i in range(len(md_lines)):
            if i in used_line_indices:
                continue
            nm = md_for_match[i]
            nl = md_normalized[i]
            if not nm and not nl:
                continue
            if norm_caption == nm or norm_caption == nl:
                found = i + 1
                used_line_indices.add(i)
                break
            if norm_caption in nm or nm in norm_caption:
                found = i + 1
                used_line_indices.add(i)
                break
            if norm_caption in nl or nl in norm_caption:
                found = i + 1
                used_line_indices.add(i)
                break
        if found is None and len(norm_caption) >= 25:
            key = norm_caption[:45].strip()
            for i in range(len(md_lines)):
                if i in used_line_indices:
                    continue
                if key in md_for_match[i] or key in md_normalized[i]:
                    found = i + 1
                    used_line_indices.add(i)
                    break
        if found is None and len(norm_caption) >= 15:
            key = norm_caption[:30].strip()
            for i in range(len(md_lines)):
                if i in used_line_indices:
                    continue
                if key in md_for_match[i] or key in md_normalized[i]:
                    found = i + 1
                    used_line_indices.add(i)
                    break
        placeholder_lines.append(found if found is not None else 0)
        if found is None:
            print("Upozorenje: caption za dijagram", index, "nije pronađen:", (caption[:55] + "...") if len(caption) > 55 else caption, file=sys.stderr)

    if args.fallback_headings:
        candidates = _candidate_anchor_lines(md_lines)
        used = set(used_line_indices)
        cidx = 0
        new_placeholder_lines = []
        for line_num in placeholder_lines:
            if line_num != 0:
                new_placeholder_lines.append(line_num)
                continue
            while cidx < len(candidates) and candidates[cidx] in used:
                cidx += 1
            if cidx < len(candidates):
                new_placeholder_lines.append(candidates[cidx] + 1)
                used.add(candidates[cidx])
                cidx += 1
            else:
                new_placeholder_lines.append(0)
        placeholder_lines = new_placeholder_lines
        filled = sum(1 for n in placeholder_lines if n != 0)
        print("Fallback:", filled, "pozicija (ukupno),", sum(1 for n in placeholder_lines if n == 0), "ostalo 0.", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Broj retka (1-based) gdje umetnuti sliku dijagrama; redoslijed = diag_01, diag_02, ...\n")
        for line_num in placeholder_lines:
            f.write(str(line_num) + "\n")

    print("Zapisano", len(placeholder_lines), "pozicija u manuscript/" + out_path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
