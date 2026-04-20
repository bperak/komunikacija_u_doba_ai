"""Insert blank line after *Figure N.M:...* when the next line starts a body paragraph."""
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
EN_DIR = PROJECT / "manuscript" / "en" / "chapters"

# Caption then single newline then body or heading — Pandoc needs a blank line before ATX headings too
PAT_BODY = re.compile(r"(\*Figure \d+\.\d+[^*\n]*\*)\n([A-Za-z])")
PAT_HEADING = re.compile(r"(\*Figure \d+\.\d+[^*\n]*\*)\n(#{1,6}\s)")


def main() -> None:
    for path in sorted(EN_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        new = PAT_HEADING.sub(r"\1\n\n\2", raw)
        new = PAT_BODY.sub(r"\1\n\n\2", new)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print(path.name)


if __name__ == "__main__":
    main()
