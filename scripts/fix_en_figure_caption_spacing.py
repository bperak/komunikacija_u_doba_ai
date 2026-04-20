"""Insert blank line after *Figure N.M:...* when the next line starts a body paragraph."""
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
EN_DIR = PROJECT / "manuscript" / "en" / "chapters"

# Caption line then single newline then letter (paragraph) — needs an extra blank line
PAT = re.compile(r"(\*Figure \d+\.\d+[^*\n]*\*)\n([A-Za-z])")


def main() -> None:
    for path in sorted(EN_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        new = PAT.sub(r"\1\n\n\2", raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print(path.name)


if __name__ == "__main__":
    main()
