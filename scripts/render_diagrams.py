"""Regenerate SVG diagrams from Mermaid sources in docs/diagrams.

Requires: npm install (beautiful-mermaid), then run from project root:
  python scripts/render_diagrams.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = PROJECT_ROOT / "docs" / "diagrams"
RENDER_SCRIPT = PROJECT_ROOT / "scripts" / "render_mermaid.mjs"
EDGE_LABELS_SCRIPT = PROJECT_ROOT / "scripts" / "svg_edge_labels_along_path.mjs"


def main() -> int:
    if not DIAGRAMS_DIR.exists():
        print("docs/diagrams not found.")
        return 1
    if not RENDER_SCRIPT.exists():
        print("scripts/render_mermaid.mjs not found.")
        return 1

    mmd_files = list(DIAGRAMS_DIR.glob("*.mmd"))
    if not mmd_files:
        print("No .mmd files in docs/diagrams.")
        return 0

    for mmd in mmd_files:
        out_svg = mmd.with_suffix(".svg")
        cmd = ["node", str(RENDER_SCRIPT), "-f", str(mmd), "-o", str(out_svg)]
        try:
            subprocess.run(cmd, cwd=PROJECT_ROOT, check=True)
            print(f"Rendered: {mmd.name} -> {out_svg.name}")
            if EDGE_LABELS_SCRIPT.exists():
                subprocess.run(
                    ["node", str(EDGE_LABELS_SCRIPT), "-f", str(out_svg), "-o", str(out_svg)],
                    cwd=PROJECT_ROOT,
                    check=True,
                    capture_output=True,
                )
                print(f"  -> edge labels along path: {out_svg.name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed {mmd.name}: {e}", file=sys.stderr)
            return 1
        except FileNotFoundError:
            print("Node not found. Install Node.js and run: npm install", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
