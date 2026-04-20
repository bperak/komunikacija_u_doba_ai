#!/usr/bin/env python3
"""
Translate Croatian chapter markdown into manuscript/en/chapters/ using
newline-bounded chunks (preserves most Markdown structure).
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT = Path(__file__).resolve().parent.parent
HR_DIR = PROJECT / "manuscript" / "chapters"
EN_DIR = PROJECT / "manuscript" / "en" / "chapters"

CHAPTER_ORDER = [
    "01_uvod.md",
    "02_povijest_tehnologija.md",
    "03_veliki_jezicni_modeli.md",
    "04_dekonstrukcija_jezika.md",
    "05_pogon_umjetne_inteligencije.md",
    "06_od_modela_do_partnera.md",
    "07_izgradnja_partnera.md",
    "08_digitalni_suputnici.md",
    "09_referencije.md",
]

POST_SUBSTITUTIONS: list[tuple[str, str]] = [
    ("> **Definicija (", "> **Definition ("),
    ("**Definicija (", "**Definition ("),
    ("*Slika ", "*Figure "),
    ("*Tablica ", "*Table "),
]


def diagram_paths_hr_to_en(text: str) -> str:
    return text.replace("](../../docs/diagrams/", "](../../docs/diagrams_en/")


def translate_one(text: str, primary, sleep_s: float) -> str:
    t = text
    if not t.strip():
        return t
    try:
        out = primary.translate(t)
        time.sleep(sleep_s)
        return out if out else t
    except Exception:
        try:
            from deep_translator import GoogleTranslator

            out = GoogleTranslator(source="auto", target="en").translate(t)
            time.sleep(sleep_s)
            return out if out else t
        except Exception:
            return t


def translate_by_line_blocks(raw: str, primary, sleep_s: float) -> str:
    """Translate consecutive non-special lines in runs up to ~1200 chars."""
    lines = raw.splitlines(keepends=True)
    out: list[str] = []
    in_fence = False
    run: list[str] = []

    def flush_run() -> None:
        nonlocal run
        if not run:
            return
        blob = "".join(run)
        out.append(translate_one(blob, primary, sleep_s))
        run = []

    for line in lines:
        st = line.strip()
        if st.startswith("```"):
            flush_run()
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if st.startswith("![](") or (st.startswith("![") and "](" in st):
            flush_run()
            out.append(line)
            continue
        if st.startswith("|") and st.count("|") >= 2:
            flush_run()
            out.append(line)
            continue

        if not st:
            flush_run()
            out.append(line)
            continue

        cur = "".join(run) + line
        if len(cur) > 1400:
            flush_run()
        run.append(line)

    flush_run()
    return "".join(out)


def post_process(text: str) -> str:
    for a, b in POST_SUBSTITUTIONS:
        text = text.replace(a, b)
    return text


def main() -> None:
    from deep_translator import GoogleTranslator

    parser = argparse.ArgumentParser()
    parser.add_argument("--chapters", nargs="*", default=CHAPTER_ORDER)
    parser.add_argument("--sleep", type=float, default=0.05)
    args = parser.parse_args()

    EN_DIR.mkdir(parents=True, exist_ok=True)
    translator = GoogleTranslator(source="hr", target="en")

    for name in args.chapters:
        src = HR_DIR / name
        if not src.exists():
            print("Skip missing:", name)
            continue
        raw = diagram_paths_hr_to_en(src.read_text(encoding="utf-8"))
        print("Translating", name, "...")
        en = translate_by_line_blocks(raw, translator, args.sleep)
        en = post_process(en)
        (EN_DIR / name).write_text(en, encoding="utf-8")
        print("  wrote", (EN_DIR / name).relative_to(PROJECT))

    print("Done.")


if __name__ == "__main__":
    main()
