"""
Automatsko popravljanje oznaka bold (**) i italic (*) u Markdown datoteci.
Spašava uobičajene greške nastale pri konverziji iz Worda (razbijene fraze).
"""
import re
import sys
import os
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def fix_bold_and_italic(text: str) -> str:
    """Primjenjuje sve popravke bold/italic oznaka; ponavlja dok ima promjena."""
    while True:
        prev = text
        # 1. Bold razbijen s **** između: **a** **** **b** -> **a b**
        text = re.sub(r"\*\*([^*]+)\*\*\s*\*\*\*\*\s*\*\*([^*]+)\*\*", r"**\1 \2**", text)
        # 2. Susjedni bold bez razmaka: **a****b** -> **a b**
        text = re.sub(r"\*\*([^*]+)\*\*\*\*([^*]+)\*\*", r"**\1 \2**", text)
        # 3. Italic razbijen s ** u sredini: *a** **b* -> *a b*
        text = re.sub(r"\*([^*]+)\*\*\s*\*\*([^*]+)\*", r"*\1 \2*", text)
        # 3b. Nastavak italic nakon **: *a b* **c* -> *a b c*
        text = re.sub(r"\*([^*]+)\*\s+\*\*([^*]+)\*", r"*\1 \2*", text)
        # 3c. Italic s jednim ** u sredini: *a** b* -> *a b*
        text = re.sub(r"\*([^*]+)\*\* ([^*]+)\*", r"*\1 \2*", text)
        # 3d. Italic s ** na početku drugog dijela: *a **b* -> *a b*
        text = re.sub(r"\*([^*]+) \*\*([^*]+)\*", r"*\1 \2*", text)
        # 3e. Dvostruki razmak unutar bolda: **a  b** -> **a b**
        text = re.sub(r"\*\*([^*]+)  ([^*]+)\*\*", r"**\1 \2**", text)
        # 4. Susjedne bold fraze: **a** **b** -> **a b**
        text = re.sub(r"\*\*([^*]+)\*\*(\s+)\*\*([^*]+)\*\*", r"**\1 \3**", text)
        # 5. Susjedne italic fraze: *a* *b* -> *a b*
        text = re.sub(r"\*([^*]+)\*(\s+)\*([^*]+)\*", r"*\1 \3*", text)
        # 6. Pet asteriska (pogrešan bold+italic): *****word***** -> *word*
        text = re.sub(r"\*\*\*\*\*([^*]+)\*\*\*\*\*", r"*\1*", text)
        if text == prev:
            break
    return text


def fix_standalone_asterisks(text: str) -> str:
    """Redak koji je samo **** ili ** zamijeni s horizontalnim pravilom ili ukloni."""
    lines = text.split("\n")
    out = []
    for line in lines:
        s = line.strip()
        if s == "****" or s == "***" or s == "**":
            out.append("---")  # horizontalno pravilo umjesto praznog označavanja
        else:
            out.append(line)
    return "\n".join(out)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    default_path = os.path.join(
        project_root, "manuscript", "Ben knjiga lektorirana_za_obradu.md"
    )
    path = sys.argv[1] if len(sys.argv) > 1 else default_path
    if not os.path.isabs(path):
        path = os.path.normpath(os.path.join(project_root, path))

    if not os.path.isfile(path):
        print(f"Datoteka ne postoji: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    original = text
    text = fix_bold_and_italic(text)
    text = fix_standalone_asterisks(text)

    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Popravljeno: {path}")
    else:
        print("Nema promjena.")


if __name__ == "__main__":
    main()
