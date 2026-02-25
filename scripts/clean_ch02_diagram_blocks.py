#!/usr/bin/env python3
"""Remove redundant 'Dijagram' image+caption blocks from 02_povijest_tehnologija.md."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "manuscript" / "chapters" / "02_povijest_tehnologija.md"
text = path.read_text(encoding="utf-8")

# Remove block: image line + caption "*Slika 2.XX: Dijagram*" (with flexible newlines)
pattern = re.compile(
    r'\n+!\[\]\(../../docs/diagrams/diag_\d+\.svg\)\s*\n\*Slika 2\.\d+: Dijagram\*\s*\n*',
    re.MULTILINE
)
new_text = pattern.sub("\n\n", text)
# Collapse excessive newlines (more than 2 in a row -> 2)
new_text = re.sub(r'\n{4,}', '\n\n\n', new_text)

path.write_text(new_text, encoding="utf-8")
print("Removed Dijagram blocks. Before:", text.count("*Slika 2."), "After:", new_text.count("*Slika 2."))
