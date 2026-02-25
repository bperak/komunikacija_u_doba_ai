"""
Ujednačavanje stilova Mermaid dijagrama u docs/diagrams/ (knjiga):
- Uklanjanje HTML oznaka (<br>, <i>, <b>, <em>, <strong>)
- Uklanjanje linija 'style ...' (svi čvorovi isti default stil)
- Svi čvorovi u obliku Id[Label] (uglate zagrade, kao usmena_tradicija.mmd)
- Skraćivanje predugačkih labela (čvor i brid) na MAX_LABEL_LENGTH znakova
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_LABEL_LENGTH = 55


def strip_html(s: str) -> str:
    """Uklanja HTML oznake, <br> zamjenjuje razmakom."""
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"</?(?:i|b|em|strong)>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+", " ", s)  # višestruke razmake u jedan
    return s.strip()


def truncate_label(label: str, max_len: int = MAX_LABEL_LENGTH) -> str:
    """Skrati labelu na max_len znakova + '...' ako je predugačka."""
    label = label.strip()
    if len(label) <= max_len:
        return label
    return label[: max_len - 3].rstrip() + "..."


def find_matching(s: str, start: int, open_s: str, close_s: str) -> int | None:
    """Vraća indeks zatvaranja koji odgovara open_s na start, ili None."""
    if not s.startswith(open_s, start):
        return None
    pos = start + len(open_s)
    depth = 1
    while pos < len(s):
        if s[pos : pos + len(close_s)] == close_s:
            depth -= 1
            if depth == 0:
                return pos + len(close_s)
            pos += len(close_s)
        elif s[pos : pos + len(open_s)] == open_s:
            depth += 1
            pos += len(open_s)
        else:
            pos += 1
    return None


def normalize_node_shapes(line: str) -> str:
    """Zamjenjuje (Label), {Label}, ((Label)), [(Label)] s [Label] (čvorovi ujednačeni), skraćuje labele."""
    out = []
    pos = 0
    while pos < len(line):
        # Traži id[( ili id(( ili id{{ ili id{ ili id(
        m = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)(\[\(|\(\(|\{\{|\{|\()", line[pos:])
        if not m:
            out.append(line[pos:])
            break
        end_m = pos + m.end()
        out.append(line[pos : pos + m.start()])
        node_id = m.group(1)
        br = m.group(2)
        if br == "[(":
            open_s, close_s = "[(", ")]"
        elif br == "((":
            open_s, close_s = "((", "))"
        elif br == "{{":
            open_s, close_s = "{{", "}}"
        elif br == "{":
            open_s, close_s = "{", "}"
        else:
            open_s, close_s = "(", ")"
        close_idx = find_matching(line, pos + m.start() + len(node_id), open_s, close_s)
        if close_idx is None:
            out.append(line[pos + m.start() : end_m])
            pos = end_m
            continue
        inner = line[end_m : close_idx - len(close_s)]
        if len(inner) >= 2 and inner.startswith('"') and inner.endswith('"'):
            inner = inner[1:-1]
        inner = truncate_label(inner)
        out.append(node_id + "[" + inner + "]")
        pos = close_idx
    return "".join(out)


def normalize_edge_labels(line: str) -> str:
    """ -- label --> pretvori u -->|label| (pipe sintaksa), skrati predugačke labele."""
    def repl(m: re.Match) -> str:
        label = m.group(1).strip()
        label = truncate_label(label)
        return f" -->|{label}| "
    return re.sub(r" -- (.+?) --> ", repl, line)


def shorten_existing_labels(line: str) -> str:
    """Skrati labele koje su već u obliku Id[Label] ili -->|Label|."""
    # Id[Label] – čvorovi koji su već u uglatim zagradama
    def node_repl(m: re.Match) -> str:
        return m.group(1) + "[" + truncate_label(m.group(2)) + "]"
    line = re.sub(r"\b([A-Za-z_][A-Za-z0-9_]*)\[([^\]]*)\]", node_repl, line)
    # -->|Label| – edge labele u pipe sintaksi
    def edge_repl(m: re.Match) -> str:
        return "-->|" + truncate_label(m.group(1)) + "|"
    line = re.sub(r"-->\|([^|]*)\|", edge_repl, line)
    return line


def unify_mermaid(content: str) -> str:
    """Jedan Mermaid blok: strip HTML, ukloni style linije, normaliziraj čvorove i bridove (pipe)."""
    lines = []
    for raw in content.splitlines():
        s = raw.rstrip()
        if re.match(r"^\s*style\s+\w+", s):
            continue
        s = strip_html(s)
        if not s or s.startswith("%%"):
            if s:
                lines.append(s)
            continue
        s = normalize_node_shapes(s)
        s = normalize_edge_labels(s)
        s = shorten_existing_labels(s)
        if s.rstrip().endswith(";"):
            s = s.rstrip()[:-1]
        lines.append(s)
    return "\n".join(lines).strip()


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    diagrams_dir = script_dir.parent / "docs" / "diagrams"
    if not diagrams_dir.is_dir():
        print("docs/diagrams ne postoji", file=sys.stderr)
        return 1

    mmd_files = sorted(diagrams_dir.glob("diag_*.mmd"))
    for mmd in mmd_files:
        text = mmd.read_text(encoding="utf-8")
        unified = unify_mermaid(text)
        mmd.write_text(unified, encoding="utf-8")
        print("Unified:", mmd.name)

    return 0


if __name__ == "__main__":
    sys.exit(main())
