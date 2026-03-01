"""Export first page of built PDF to docs/cover_naslovnica.png for README."""
from pathlib import Path

try:
    import fitz
except ImportError:
    raise SystemExit("pip install pymupdf")

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
PDF = ROOT / "manuscript" / "Perak_Komunikacija_u_doba_AI.pdf"
OUT = ROOT / "docs" / "cover_naslovnica.png"

if not PDF.exists():
    raise SystemExit(f"PDF not found: {PDF}")

doc = fitz.open(str(PDF))
OUT.parent.mkdir(parents=True, exist_ok=True)
doc[0].get_pixmap(dpi=150, alpha=False).save(str(OUT))
doc.close()
print(f"Saved: {OUT}")
