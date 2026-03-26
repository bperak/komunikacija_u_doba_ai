#!/usr/bin/env python3
"""
Spaja sva poglavlja i generira:
1. Integralnu HTML verziju knjige (sa SVG dijagramima)
2. PDF verziju putem Chrome headless (sa svim SVG dijagramima)

Obje verzije su potpune i sadrže sve dijagrame.
"""
import re
import subprocess
import sys
import shutil
import base64
import uuid
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional
from urllib.parse import quote

# Ensure Unicode logging works on Windows consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"
DIAGRAMS_DIR = PROJECT_ROOT / "docs" / "diagrams"
OUTPUT_DIR = PROJECT_ROOT / "manuscript"
BOOK_BASENAME = "Perak_Komunikacija_u_doba_AI"

CHAPTER_FILES = [
    "00_naslovnica.md",
    "00b_predgovor.md",
    "01_uvod.md",
    "02_povijest_tehnologija.md",
    "03_veliki_jezicni_modeli.md",
    "04_dekonstrukcija_jezika.md",
    "05_pogon_umjetne_inteligencije.md",
    "06_od_modela_do_partnera.md",
    "07_izgradnja_partnera.md",
    "08_digitalni_suputnici.md",
    "09_referencije.md",
    "10_glosar.md",
    "11_zavrsna_biljeska.md",
]

BOOK_CSS = """
<style>
@media print {
    @page { size: A4; margin: 2.5cm 2cm 2.5cm 2.5cm; }
    @page :first { size: A4; margin: 0; }
    @page fullbleed { size: A4; margin: 0; }
    h1 { page-break-before: always; }
blockquote, figure, .img-wrap, pre, table { page-break-inside: avoid; }
.figure-block { page-break-inside: avoid; break-inside: avoid-page; }
    body { font-size: 11pt; }
    body {
        max-width: none;
        margin: 0;
        padding: 0;
    }
}

body {
    font-family: Georgia, 'Times New Roman', Cambria, serif;
    font-size: 12pt;
    line-height: 1.7;
    color: #1a1a1a;
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}

h1 {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.8em;
    font-weight: 700;
    color: #1a3a5c;
    margin-top: 3em;
    margin-bottom: 0.8em;
    line-height: 1.25;
    text-align: left;
    border-bottom: 2px solid #1a3a5c;
    padding-bottom: 0.3em;
}

h2 {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.4em;
    font-weight: 600;
    color: #2a5a8c;
    margin-top: 2em;
    margin-bottom: 0.6em;
    text-align: left;
}

h3 {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.2em;
    font-weight: 600;
    color: #3a6a9c;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    text-align: left;
}

h4 {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.05em;
    font-weight: 600;
    color: #4a7aac;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    text-align: left;
}

p { margin: 0 0 0.6em 0; }

blockquote {
    margin: 1em 0;
    padding: 0.8em 1em;
    background: #f0f4f8;
    border-left: 4px solid #2a5a8c;
    font-size: 0.92em;
    line-height: 1.55;
    color: #2a2a2a;
    border-radius: 0 4px 4px 0;
}

blockquote p { margin: 0 0 0.3em 0; }
blockquote p:last-child { margin-bottom: 0; }

/* --- Images: centered, constrained size --- */
img {
    max-width: 100%;
    max-height: 560px;
    width: auto;
    height: auto;
    display: block;
    margin: 0.5em auto;
}

/* Paragraphs that contain only an image or SVG */
.img-wrap {
    text-align: center;
    margin: 1.2em 0 0.3em 0;
}

.figure-block {
    text-align: center;
    margin: 1.2em 0 1.2em 0;
    page-break-inside: avoid;
    break-inside: avoid-page;
}

.figure-block .img-wrap {
    margin: 0 0 0.3em 0;
    page-break-inside: avoid;
    break-inside: avoid-page;
}

.img-wrap svg {
    max-width: 100%;
    max-height: 520px;
    width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

/* Slika 2.4 (diag_902): držati unutar margina — plave kućice ne smiju izlaziti */
.img-wrap svg[viewBox*="807.9375 410"] {
    max-width: 100%;
    max-height: none;
}

.img-wrap.slika24 svg,
.img-wrap.slika24 img {
    max-width: 100% !important;
    width: 100% !important;
    height: auto !important;
    margin-left: 0 !important;
}

/* Slika 2.11 (diag_10), Slika 2.12 (ch02_reformacija_znanost): povećati */
.img-wrap.slika211 svg,
.img-wrap.slika211 img,
.img-wrap.slika212 svg,
.img-wrap.slika212 img {
    max-width: 100% !important;
    width: 100% !important;
}

/* Slika 3.5 (diag_169): dovoljno visine da se labele u kućicama ne trimaju */
.img-wrap.slika35 svg {
    max-height: 520px !important;
    overflow: visible !important;
}
.img-wrap.slika35 {
    padding-bottom: 0.5em;
}

/* Pandoc figure element */
figure {
    margin: 1.5em auto;
    text-align: center;
    max-width: 100%;
}

figure img {
    max-width: 100%;
    max-height: 560px;
    margin: 0 auto;
}

/* --- Captions: centered, smaller, gray --- */
figcaption {
    text-align: center;
    font-size: 0.88em;
    color: #555;
    font-style: italic;
    margin-top: 0.4em;
    margin-bottom: 0.3em;
    line-height: 1.4;
}

.caption {
    text-align: center;
    font-size: 0.88em;
    color: #555;
    font-style: italic;
    margin-top: 0;
    margin-bottom: 1.2em;
    line-height: 1.4;
}

.figure-block .caption {
    margin-bottom: 0;
    page-break-inside: avoid;
    break-inside: avoid-page;
}

code {
    font-family: Consolas, 'Courier New', monospace;
    font-size: 0.88em;
    background: #f5f5f5;
    padding: 2px 5px;
    border-radius: 3px;
}

pre {
    font-family: Consolas, 'Courier New', monospace;
    font-size: 0.85em;
    background: #f5f5f5;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow-x: auto;
    white-space: pre-wrap;
    line-height: 1.45;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 0.92em;
}

th, td {
    border: 1px solid #ccc;
    padding: 0.4em 0.6em;
    text-align: left;
}

th {
    background: #f0f4f8;
    font-weight: 600;
    color: #1a3a5c;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 2em 0;
}

a { color: #2a5a8c; text-decoration: none; }
a:hover { text-decoration: underline; }

ul, ol { margin: 0.5em 0 0.5em 1.5em; }
li { margin-bottom: 0.2em; }

strong { font-weight: 700; }
em { font-style: italic; }

/* Table of contents */
#TOC {
    background: #fbfcfe;
    border: 1px solid #d7e1ec;
    border-radius: 8px;
    padding: 1.1em 1.2em 1.2em 1.15em;
    margin: 1.4em 0 2em 0;
}

#TOC ul {
    list-style: none;
    padding-left: 0.7em;
    margin: 0;
}
#TOC > ul { padding-left: 0; }
#TOC li {
    margin-bottom: 0.22em;
    padding-left: 0;
}
#TOC li ul {
    padding-left: 0.9em;
    margin-top: 0.18em;
}
#TOC a { color: #2a5a8c; }

/* ── Book cover ── */
.book-cover,
.back-cover {
    position: relative;
    width: calc(100% + 4rem);
    min-height: 960px;
    margin: -2rem -2rem 0 -2rem;
    overflow: hidden;
    border-radius: 0;
    page-break-after: always;
    background: #0f1932;
}

.back-cover {
    page-break-after: auto;
}

.cover-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.cover-img {
    width: 100% !important;
    height: 100% !important;
    max-width: none !important;
    max-height: none !important;
    object-fit: cover;
    display: block;
    margin: 0 !important;
}

.cover-bg::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        180deg,
        rgba(15, 25, 50, 0.50) 0%,
        rgba(15, 25, 50, 0.20) 30%,
        rgba(15, 25, 50, 0.10) 50%,
        rgba(15, 25, 50, 0.20) 70%,
        rgba(15, 25, 50, 0.55) 100%
    );
    z-index: 1;
}

.cover-content {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 960px;
    padding: 3.5rem 3rem 2.5rem 3rem;
    color: #ffffff;
    text-align: center;
}

.cover-top {
    padding-top: 0.5rem;
}

.cover-author {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.65em;
    font-weight: 400;
    letter-spacing: 0.2em;
    color: #ffffff;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.cover-middle {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem 0;
}

.cover-title {
    font-family: Georgia, 'Times New Roman', Cambria, serif !important;
    font-size: 2.5em !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    color: #ffffff !important;
    text-align: center !important;
    border-bottom: none !important;
    margin: 0 0 0.5em 0 !important;
    padding: 0 !important;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.5);
}

.cover-subtitle {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.4em;
    font-weight: 300;
    line-height: 1.5;
    color: #ffffff;
    text-shadow: 0 1px 8px rgba(0, 0, 0, 0.5);
    letter-spacing: 0.04em;
}

.cover-bottom {
    padding-bottom: 1rem;
}

.cover-institution {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 0.92em;
    font-weight: 400;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.85);
    border-top: 1px solid rgba(212, 168, 67, 0.4);
    display: inline-block;
    padding-top: 0.5em;
    margin-bottom: 0.3em;
}

.cover-year {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 0.92em;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.65);
    letter-spacing: 0.15em;
}

.back-cover {
    page-break-before: always;
    page-break-after: auto;
    margin: 0 -2rem -2rem -2rem;
}

.back-cover .cover-content {
    justify-content: center;
    text-align: center;
}

.back-cover .cover-middle {
    max-width: 620px;
    margin: 0 auto;
}

.back-cover-kicker {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 0.95em;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(219, 234, 254, 0.9);
    margin-bottom: 1.2em;
}

.back-cover-title {
    margin-bottom: 0.55em !important;
}

.back-cover-subtitle {
    font-size: 1.18em;
    line-height: 1.7;
    letter-spacing: 0.01em;
}

.back-cover-link {
    margin-top: 1.8em;
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 0.98em;
    letter-spacing: 0.04em;
    color: rgba(219, 234, 254, 0.95);
}

/* ── Inner title page (naslovni list) ── */
.title-page {
    page-break-before: auto;
    page-break-after: auto;
    min-height: 900px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 3rem 2rem;
}

.title-page-author {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.4em;
    font-weight: 300;
    letter-spacing: 0.15em;
    color: #2a2a2a;
    margin-bottom: 3em;
}

.title-page-title {
    font-family: Georgia, 'Times New Roman', Cambria, serif;
    font-size: 2.2em;
    font-weight: 700;
    line-height: 1.25;
    color: #1a3a5c;
    margin-bottom: 0.5em;
}

.title-page-subtitle {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.15em;
    font-weight: 300;
    line-height: 1.4;
    color: #555;
    letter-spacing: 0.03em;
    margin-bottom: 4em;
}

.title-page-bottom {
    margin-top: auto;
    padding-top: 3em;
}

.title-page-publisher {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1em;
    font-weight: 400;
    color: #333;
    margin-bottom: 0.3em;
}

.title-page-place {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 0.95em;
    font-weight: 300;
    color: #666;
    letter-spacing: 0.05em;
}

/* ── Impresum / Colophon page ── */
.impresum-page {
    page-break-before: auto;
    page-break-after: auto;
    min-height: 860px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 3rem 2rem 2rem 2rem;
}

.impresum-content {
    max-width: 520px;
}

.impresum-section {
    margin-bottom: 1.2em;
    font-size: 0.92em;
    line-height: 1.55;
    color: #333;
}

.impresum-label {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-weight: 600;
    font-size: 0.85em;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #2a5a8c;
    margin-bottom: 0.15em;
}

.impresum-isbn {
    margin-top: 2em;
    margin-bottom: 1.5em;
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1em;
    font-weight: 600;
    color: #1a3a5c;
    letter-spacing: 0.02em;
}

.impresum-copyright {
    margin-bottom: 2em;
    font-size: 0.82em;
    line-height: 1.5;
    color: #666;
    font-style: italic;
}

.impresum-cite {
    margin-top: 1em;
    padding-top: 1em;
    border-top: 1px solid #ccc;
    font-size: 0.88em;
    line-height: 1.55;
    color: #333;
}

.impresum-author-note {
    margin-top: 1.25em;
    padding-top: 1em;
    border-top: 1px solid #e0e0e0;
}

.impresum-author-note p {
    margin: 0 0 0.65em 0;
    text-align: justify;
}

.impresum-author-note p:last-child {
    margin-bottom: 0;
}

.impresum-author-note a {
    color: #1a3a5c;
    word-break: break-all;
}

/* ── Predgovor ── */
.predgovor-page {
    page-break-before: auto;
    page-break-after: auto;
    max-width: 700px;
    margin: 0 auto;
    padding: 2em 1em;
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    line-height: 1.8;
    color: #333;
}

.predgovor-page h2 {
    font-size: 1.8em;
    font-weight: 700;
    color: #1a3a5c;
    margin-top: 1.5em;
    margin-bottom: 1em;
    padding-bottom: 0.3em;
    border-bottom: 2px solid #1a3a5c;
}

.predgovor-page p {
    text-align: justify;
    margin-bottom: 1em;
    font-size: 1em;
}

.predgovor-signature {
    margin-top: 1.5em;
    text-align: right;
    font-style: italic;
    color: #555;
    line-height: 1.6;
    page-break-before: avoid;
}

/* Glosar */
.glossary-page {
    max-width: 760px;
    margin: 0 auto;
    padding: 0.5em 0 1em 0;
}

.glossary-page h1 {
    margin-top: 2em;
}

.glossary-page p {
    text-align: left;
    hyphens: none;
    -webkit-hyphens: none;
    line-height: 1.55;
    margin-bottom: 0.5em;
    font-size: 0.96em;
}

.glossary-page hr {
    margin: 1.2em 0 1.4em;
}

/* ── TOC heading ── */
.toc-heading {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 1.8em;
    font-weight: 700;
    color: #1a3a5c;
    text-align: left;
    margin-top: 2em;
    margin-bottom: 0.8em;
    padding-bottom: 0.3em;
    border-bottom: 2px solid #1a3a5c;
    page-break-before: always;
}

@media print {
    .book-cover,
    .back-cover {
        width: 100%;
        margin: 0;
        page-break-after: always;
        page-break-inside: avoid;
        break-inside: avoid-page;
        min-height: 296mm;
        height: 296mm;
        overflow: hidden;
        box-sizing: border-box;
    }
    .back-cover {
        page: fullbleed;
        page-break-after: auto !important;
        width: 100%;
        margin: 0;
    }
    .cover-content {
        min-height: 100%;
        height: 100%;
        padding: 1.2rem 1.4rem 1.2rem 1.4rem;
        box-sizing: border-box;
    }
    .cover-top,
    .cover-middle {
        padding: 0;
    }
    .cover-author {
        font-size: 1.35em;
        letter-spacing: 0.14em;
    }
    .cover-title {
        font-size: 2.0em !important;
        line-height: 1.15 !important;
        margin-bottom: 0.35em !important;
    }
    .cover-subtitle {
        font-size: 1.15em;
        line-height: 1.35;
    }
    .cover-institution {
        font-size: 0.82em;
        letter-spacing: 0.1em;
        white-space: nowrap;
    }
    .cover-year {
        font-size: 0.8em;
    }
    .cover-bottom {
        display: none;
    }
    .title-page {
        min-height: 225mm;
        height: 225mm;
        padding: 1.5rem 1rem;
        justify-content: space-between;
        page-break-inside: avoid;
        break-inside: avoid-page;
    }
    .title-page-author {
        margin-bottom: 1.8em;
    }
    .title-page-title {
        font-size: 2em;
        margin-bottom: 0.4em;
    }
    .title-page-subtitle {
        margin-bottom: 1.8em;
    }
    .title-page-bottom {
        margin-top: 0;
        padding-top: 0;
    }
    .impresum-page {
        min-height: 100vh;
        page-break-inside: avoid;
        break-inside: avoid-page;
    }
    .impresum-content {
        page-break-inside: avoid;
        break-inside: avoid-page;
    }
    .predgovor-page {
        page-break-inside: avoid;
        min-height: 0;
        max-height: none;
        padding: 1.5em 1em 1em;
    }
    .predgovor-signature {
        margin-top: 1em;
        page-break-inside: avoid;
        page-break-before: avoid;
        break-before: avoid-page;
    }
    .back-cover {
        page: fullbleed;
        page-break-before: always;
        min-height: 297mm;
        height: 297mm;
        width: 100%;
        margin: 0;
        page-break-inside: avoid;
        break-inside: avoid-page;
    }
    .back-cover .cover-content {
        min-height: 100%;
        height: 100%;
        padding: 1.4rem 1.4rem 1.2rem 1.4rem;
    }
    .back-cover-kicker {
        font-size: 0.82em;
        letter-spacing: 0.14em;
        margin-bottom: 1em;
    }
    .back-cover-title {
        font-size: 2.05em !important;
        line-height: 1.15 !important;
    }
    .back-cover-subtitle {
        font-size: 1.05em;
        line-height: 1.55;
    }
    .back-cover-link {
        font-size: 0.88em;
    }
}
</style>
"""


def fix_nested_image_syntax(md_text: str) -> str:
    r"""Fix broken nested image syntax like ![![\](path)](path)."""
    md_text = re.sub(r'!\[!\[\\?\]\([^)]*\)\]\(([^)]+)\)', r'![](\1)', md_text)
    return md_text


def clear_image_alt_text(md_text: str) -> str:
    """Clear alt text from images to prevent Pandoc from creating duplicate figcaptions.
    The proper captions are in *Slika X.Y:* lines below each image.
    Also prevents truncated alt text (ending with '...') from showing.
    """
    return re.sub(r'!\[[^\]]*\]\(', '![](', md_text)


def fix_truncated_captions(md_text: str) -> str:
    """Fix captions truncated with '...' — trim to last complete word, add period.
    Only acts on lines matching *Slika X.Y: ...text...*  (ending with '...*').
    If '...' is glued to a word (no space before), the word is partial and trimmed.
    If '...' follows a space, the last word is kept intact.
    """
    def _fix(m):
        prefix = m.group(1)          # e.g. '*Slika 6.1: '
        body = m.group(2)            # text before '...*'
        # If body ends with space(s), last word was complete — just strip spaces
        if body != body.rstrip():
            body = body.rstrip()
        else:
            # '...' was glued to a partial word — trim to last whole word
            if body and body[-1].isalpha():
                last_space = body.rfind(' ')
                if last_space > 0:
                    body = body[:last_space]
        # Clean trailing punctuation debris and ensure single period
        body = body.rstrip(' ,;:.')
        return f'{prefix}{body}.*'
    return re.sub(r'^(\*Slika \d+\.\d+[a-z]?: )(.+?)\.\.\.\*$', _fix, md_text, flags=re.MULTILINE)


def fix_caption_newlines(md_text: str) -> str:
    """Ensure a blank line between image and caption so they render as separate blocks."""
    lines = md_text.splitlines()
    result = []
    for i, line in enumerate(lines):
        result.append(line)
        # If current line is an image and next line is a caption, insert blank line
        if (line.strip().startswith("![")
                and i + 1 < len(lines)
                and lines[i + 1].strip().startswith("*Slika")):
            result.append("")
    return "\n".join(result)


def remove_duplicate_caption_paragraphs(md_text: str) -> str:
    """Remove standalone paragraphs that duplicate the caption of the image below.

    Some chapter sources contain a short summary sentence immediately before an
    image, followed by the proper `*Slika X.Y:*` caption under the image. When
    the sentence substantially repeats that caption, it should not appear in the
    running text.
    """
    lines = md_text.splitlines()
    ranges_to_remove: list[tuple[int, int]] = []

    def _normalize(text: str) -> str:
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'^\*?Slika \d+\.\d+[a-z]?:\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'[^0-9A-Za-zčćžšđČĆŽŠĐ\s-]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip().lower()
        return text

    for i, line in enumerate(lines):
        if not line.strip().startswith("!["):
            continue

        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines) or not lines[j].strip().startswith("*Slika "):
            continue

        k = i - 1
        while k >= 0 and not lines[k].strip():
            k -= 1
        if k < 0:
            continue
        para_end = k
        while k >= 0 and lines[k].strip():
            k -= 1
        para_start = k + 1

        paragraph_lines = lines[para_start:para_end + 1]
        if not paragraph_lines:
            continue

        paragraph = " ".join(part.strip() for part in paragraph_lines).strip()
        if not paragraph or paragraph.startswith(("#", ">", "*", "-", "<")):
            continue
        if re.search(r'\([A-ZČĆŽŠĐ][^)]*\d{4}[a-z]?\)', paragraph):
            continue

        caption = lines[j].strip().strip("*")
        paragraph_norm = _normalize(paragraph)
        caption_norm = _normalize(caption)
        if len(paragraph_norm) < 80 or len(paragraph_norm) > 360:
            continue
        if len(caption_norm) < 80:
            continue

        similarity = SequenceMatcher(None, paragraph_norm, caption_norm).ratio()
        if similarity >= 0.82:
            ranges_to_remove.append((para_start, para_end))

    if not ranges_to_remove:
        return md_text

    remove_idx = {
        idx
        for start, end in ranges_to_remove
        for idx in range(start, end + 1)
    }
    cleaned_lines = [line for idx, line in enumerate(lines) if idx not in remove_idx]
    return "\n".join(cleaned_lines)


def fix_image_paths_for_manuscript(md_text: str) -> str:
    """Convert relative diagram paths: from chapters/ perspective to manuscript/ perspective.
    chapters/ uses ../../docs/diagrams/ -> manuscript/ needs ../docs/diagrams/
    """
    def replace_img(m):
        alt = m.group(1)
        rel_path = m.group(2)
        if "../../docs/diagrams/" in rel_path:
            new_path = rel_path.replace("../../docs/diagrams/", "../docs/diagrams/")
            return f"![{alt}]({new_path})"
        if "../../docs/" in rel_path:
            new_path = rel_path.replace("../../docs/", "../docs/")
            return f"![{alt}]({new_path})"
        return m.group(0)

    # Fix both markdown images and HTML img src
    md_text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_img, md_text)
    md_text = md_text.replace('src="../../docs/', 'src="../docs/')
    return md_text


def merge_chapters() -> str:
    """Read and merge all chapter markdown files."""
    parts = []
    for fname in CHAPTER_FILES:
        path = CHAPTERS_DIR / fname
        if not path.exists():
            print(f"  UPOZORENJE: Nedostaje: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        parts.append(text)
        print(f"  + {fname} ({len(text.splitlines())} red.)")
    return "\n\n".join(parts)


def extract_cover_metadata() -> dict[str, str]:
    """Read cover text from the source chapter so HTML and PDF covers stay aligned."""
    cover_path = CHAPTERS_DIR / "00_naslovnica.md"
    defaults = {
        "author": "Benedikt Perak",
        "title": "Komunikacija u doba umjetne inteligencije",
        "subtitle": "Razvoj velikih jezičnih modela\ni komunikacijskih agenata",
    }
    if not cover_path.exists():
        return defaults

    text = cover_path.read_text(encoding="utf-8")

    def _extract(pattern: str, default: str) -> str:
        match = re.search(pattern, text, flags=re.DOTALL)
        if not match:
            return default
        value = match.group(1).strip()
        value = re.sub(r'<br\s*/?>', '\n', value, flags=re.IGNORECASE)
        value = re.sub(r'<[^>]+>', '', value)
        value = re.sub(r'[ \t]+\n', '\n', value)
        value = re.sub(r'\n[ \t]+', '\n', value)
        value = re.sub(r'[ \t]{2,}', ' ', value)
        value = re.sub(r'\n{3,}', '\n\n', value)
        value = value.strip()
        return value or default

    return {
        "author": _extract(r'<div class="cover-author">(.*?)</div>', defaults["author"]),
        "title": _extract(r'<h1 class="cover-title">(.*?)</h1>', defaults["title"]),
        "subtitle": _extract(r'<div class="cover-subtitle">(.*?)</div>', defaults["subtitle"]),
    }


def _extract_div(html_text: str, css_class: str):
    """Extract a top-level div by CSS class and return (extracted_html, remaining_html)."""
    marker = f'<div class="{css_class}">'
    start = html_text.find(marker)
    if start < 0:
        return None, html_text
    depth = 0
    i = start
    end = -1
    while i < len(html_text):
        if html_text[i:i+4] == '<div':
            depth += 1
        elif html_text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                break
        i += 1
    if end < 0:
        return None, html_text
    extracted = html_text[start:end]
    remaining = html_text[:start] + html_text[end:]
    return extracted, remaining


def inline_svg_images(html_text: str, base_dir: Path) -> str:
    """Replace <img src="...svg"> with inline SVG content for a self-contained HTML."""
    def _replace_svg_img(m):
        full_tag = m.group(0)
        src = m.group(1)
        if not src.endswith('.svg'):
            return full_tag
        # Chapter 6 custom SVGs render correctly as external files, but Chrome
        # can mix up their content when many inline SVGs with repeated internal
        # ids live in the same long HTML document.
        if "/ch06_" in src or "\\ch06_" in src or src.split("/")[-1].startswith("ch06_"):
            return full_tag
        svg_path = (base_dir / src).resolve()
        if not svg_path.exists():
            return full_tag
        try:
            svg_content = svg_path.read_text(encoding='utf-8')
            svg_start = svg_content.find('<svg')
            if svg_start < 0:
                return full_tag
            svg_content = svg_content[svg_start:]
            # Strip fixed width/height so CSS can control sizing via viewBox
            svg_content = re.sub(r'\s+width="[^"]*"', '', svg_content, count=1)
            svg_content = re.sub(r'\s+height="[^"]*"', '', svg_content, count=1)
            # Remove any existing inline max-width style from Mermaid
            svg_content = re.sub(
                r'style="[^"]*max-width:\s*[\d.]+px[^"]*"',
                '',
                svg_content, count=1
            )
            return svg_content
        except Exception:
            return full_tag

    html_text = re.sub(r'<img\s+src="([^"]+\.svg)"[^>]*/?\s*>', _replace_svg_img, html_text)
    return html_text


def inline_cover_image(html_text: str, base_dir: Path) -> str:
    """Inline cover image as data URI for reliable print rendering."""
    candidates = [
        Path("../docs/book_cover_bg.jpg"),
        Path("../../docs/book_cover_bg.jpg"),
        Path("docs/book_cover_bg.jpg"),
        Path("../docs/book_cover_bg.png"),
        Path("../../docs/book_cover_bg.png"),
        Path("docs/book_cover_bg.png"),
    ]
    cover_path = None
    for rel in candidates:
        p = (base_dir / rel).resolve()
        if p.exists():
            cover_path = p
            break
    if not cover_path:
        return html_text

    try:
        b64 = base64.b64encode(cover_path.read_bytes()).decode("ascii")
        mime = "image/jpeg" if cover_path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
        data_uri = f"data:{mime};base64,{b64}"
        html_text = html_text.replace("../docs/book_cover_bg.jpg", data_uri)
        html_text = html_text.replace("../../docs/book_cover_bg.jpg", data_uri)
        html_text = html_text.replace("docs/book_cover_bg.jpg", data_uri)
        html_text = html_text.replace("../docs/book_cover_bg.png", data_uri)
        html_text = html_text.replace("../../docs/book_cover_bg.png", data_uri)
        html_text = html_text.replace("docs/book_cover_bg.png", data_uri)
    except Exception:
        return html_text
    return html_text


def postprocess_html(html_text: str) -> str:
    """Add CSS classes to image paragraphs and caption paragraphs in generated HTML."""

    # 0. Extract front-matter divs from wherever Pandoc placed them
    cover_html, html_text = _extract_div(html_text, "book-cover")
    title_html, html_text = _extract_div(html_text, "title-page")
    impr_html, html_text = _extract_div(html_text, "impresum-page")
    predgovor_html, html_text = _extract_div(html_text, "predgovor-page")

    # Insert them right after <body> in the correct order:
    # cover → inner title page → impresum → predgovor → (Pandoc title + TOC + content)
    front_matter = '\n'.join(part for part in [cover_html, title_html, impr_html, predgovor_html] if part)
    if front_matter:
        html_text = html_text.replace('<body>', '<body>\n' + front_matter, 1)

    # 0b. Remove the Pandoc-generated <h1> title (duplicate of cover)
    html_text = re.sub(
        r'<h1 class="title"[^>]*>.*?</h1>\s*',
        '',
        html_text,
        count=1,
        flags=re.DOTALL,
    )

    # 0c. Add "Sadržaj" heading before the TOC nav
    html_text = html_text.replace(
        '<nav id="TOC"',
        '<div class="toc-heading">Sadržaj</div>\n<nav id="TOC"',
        1,
    )

    # 0d. Keep cover image as direct child (no paragraph wrapper).
    html_text = re.sub(
        r'<p>\s*(<img [^>]*class="cover-img"[^>]*>)\s*</p>',
        r'\1',
        html_text,
        flags=re.DOTALL,
    )

    # 1. Add .img-wrap class to <p> that contains only an <img>
    #    Skip cover image, which must keep its absolute layout.
    html_text = re.sub(
        r'<p>(\s*<img (?![^>]*class="cover-img")[^>]*/?>\s*)</p>',
        r'<p class="img-wrap">\1</p>',
        html_text
    )
    # 1b. Slika 2.11 (diag_10), Slika 2.12 (ch02_reformacija_znanost): add class so CSS can enlarge
    html_text = re.sub(
        r'<p class="img-wrap">(\s*<img [^>]*src="[^"]*diag_10\.svg[^"]*"[^>]*/?>\s*)</p>',
        r'<p class="img-wrap slika211">\1</p>',
        html_text
    )
    html_text = re.sub(
        r'<p class="img-wrap">(\s*<img [^>]*src="[^"]*ch02_reformacija_znanost\.svg[^"]*"[^>]*/?>\s*)</p>',
        r'<p class="img-wrap slika212">\1</p>',
        html_text
    )

    # 2. Add .caption class to <p><em>Slika X.Y: ...</em></p>
    html_text = re.sub(
        r'<p><em>(Slika \d+\.\d+[a-z]?:.*?)</em></p>',
        r'<p class="caption"><em>\1</em></p>',
        html_text
    )

    # 3. Also handle *Slika 0.X* patterns (chapter 0 naslovnica)
    html_text = re.sub(
        r'<p><em>(\*?Slika \d+\.\d+[a-z]?:.*?)</em></p>',
        r'<p class="caption"><em>\1</em></p>',
        html_text
    )

    # 4. Wrap image + caption pairs into a single block so Chrome does not
    #    place the caption on the next page during PDF pagination.
    html_text = re.sub(
        r'(<p class="img-wrap(?: [^"]+)?">.*?</p>\s*<p class="caption">.*?</p>)',
        r'<div class="figure-block">\1</div>',
        html_text,
        flags=re.DOTALL,
    )

    return html_text


def find_exe(name: str, extra_paths=None) -> str:
    """Find executable on PATH or in common locations."""
    found = shutil.which(name)
    if found:
        return found
    for p in (extra_paths or []):
        if Path(p).exists():
            return str(p)
    return None


def find_unicode_font() -> Path | None:
    """Pick an installed font with Croatian diacritics support."""
    candidates = [
        Path(r"C:\Windows\Fonts\segoeui.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\calibri.ttf"),
        Path(r"C:\Windows\Fonts\tahoma.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def build_html(merged_md: str) -> Path:
    """Build a beautiful standalone HTML from merged markdown using Pandoc."""
    html_path = OUTPUT_DIR / f"{BOOK_BASENAME}.html"
    md_path = OUTPUT_DIR / "_temp_build.md"
    header_path = OUTPUT_DIR / "_temp_header.html"

    md_path.write_text(merged_md, encoding="utf-8")
    header_path.write_text(BOOK_CSS, encoding="utf-8")

    pandoc = find_exe("pandoc", [
        r"C:\Users\Benedikt\AppData\Local\Pandoc\pandoc.exe",
        r"C:\Program Files\Pandoc\pandoc.exe",
    ])

    if not pandoc:
        raise FileNotFoundError("Pandoc nije pronaden!")

    cmd = [
        pandoc,
        str(md_path),
        "-o", str(html_path),
        "--from=markdown",
        "--to=html5",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--metadata", "title=Komunikacija u doba umjetne inteligencije",
        "--metadata", "lang=hr",
        "--include-in-header", str(header_path),
        "--wrap=none",
    ]

    print(f"  Pandoc: {pandoc}")
    result = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
    )

    # Cleanup temp files
    md_path.unlink(missing_ok=True)
    header_path.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"  Pandoc greska: {result.stderr[:1000]}")
        return build_html_manual(merged_md)

    if result.stderr:
        warnings = [l for l in result.stderr.splitlines() if "warn" in l.lower()]
        if warnings:
            print(f"  Upozorenja: {len(warnings)}")

    # Post-process: add classes for images and captions
    raw_html = html_path.read_text(encoding="utf-8")
    processed = postprocess_html(raw_html)
    processed = inline_svg_images(processed, OUTPUT_DIR)
    processed = inline_cover_image(processed, OUTPUT_DIR)
    html_path.write_text(processed, encoding="utf-8")
    print("  Post-processing: klase za slike i opise dodane.")
    print("  SVG dijagrami ugrađeni inline u HTML.")

    return html_path


def build_html_manual(merged_md: str) -> Path:
    """Fallback: build HTML manually with Python markdown library."""
    try:
        import markdown
    except ImportError:
        print("  Instaliram markdown paket...")
        subprocess.run([sys.executable, "-m", "pip", "install", "markdown", "-q"])
        import markdown

    html_path = OUTPUT_DIR / f"{BOOK_BASENAME}.html"

    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
        'markdown.extensions.smarty',
    ]
    html_body = markdown.markdown(merged_md, extensions=extensions, output_format='html5')

    full_html = f"""<!DOCTYPE html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Komunikacija u doba umjetne inteligencije</title>
{BOOK_CSS}
</head>
<body>
{html_body}
</body>
</html>"""

    full_html = postprocess_html(full_html)
    full_html = inline_svg_images(full_html, OUTPUT_DIR)
    full_html = inline_cover_image(full_html, OUTPUT_DIR)
    html_path.write_text(full_html, encoding="utf-8")
    return html_path


def build_pdf(merged_md: str, html_path: Path = None) -> Path:
    """Build PDF from the HTML file using Chrome headless (includes all SVG diagrams)."""
    pdf_path = OUTPUT_DIR / f"{BOOK_BASENAME}.pdf"
    tmp_pdf_path = OUTPUT_DIR / f"{BOOK_BASENAME}._fresh.pdf"
    profile_root = Path.home() / ".codex" / "memories" / "chrome-headless-profiles"
    user_data_dir = profile_root / f"profile-{uuid.uuid4().hex}"

    if html_path is None or not html_path.exists():
        html_path = OUTPUT_DIR / f"{BOOK_BASENAME}.html"

    if not html_path.exists():
        print("  HTML fajl ne postoji - PDF se ne može generirati!")
        return None

    chrome = None
    for candidate in [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]:
        if Path(candidate).exists():
            chrome = candidate
            break

    if not chrome:
        chrome = shutil.which("chrome") or shutil.which("google-chrome")

    if not chrome:
        print("  Chrome/Edge nije pronađen! PDF se ne može generirati.")
        print("  Koristite HTML verziju -> Ctrl+P -> Spremi kao PDF")
        return None

    print(f"  Browser: {chrome}")
    print(f"  Generiranje PDF-a iz HTML-a (sa svim dijagramima)...")

    file_url = html_path.resolve().as_uri()
    if tmp_pdf_path.exists():
        tmp_pdf_path.unlink()
    user_data_dir.mkdir(parents=True, exist_ok=False)
    cmd = [
        chrome,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-crash-reporter',
        '--disable-crashpad',
        f'--user-data-dir={user_data_dir}',
        f'--print-to-pdf={tmp_pdf_path}',
        '--no-pdf-header-footer',
        '--print-to-pdf-no-header',
        file_url,
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=120,
        )
    except subprocess.TimeoutExpired:
        print("  TIMEOUT: PDF generiranje prekinuto nakon 2 min")
        return None
    finally:
        shutil.rmtree(user_data_dir, ignore_errors=True)

    if result.returncode != 0 or not tmp_pdf_path.exists():
        err = result.stderr[:1000] if result.stderr else "nepoznata greska"
        print(f"  PDF greska: {err}")
        return None

    if pdf_path.exists():
        pdf_path.unlink()
    tmp_pdf_path.replace(pdf_path)
    return pdf_path


def add_page_numbers(pdf_path: Path, skip_first_pages: int = 1) -> bool:
    """Add clean running headers and page numbers to PDF."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("  Instaliram PyMuPDF za numeraciju stranica...")
        install = subprocess.run(
            [sys.executable, "-m", "pip", "install", "pymupdf", "-q"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        if install.returncode != 0:
            print("  Upozorenje: PyMuPDF nije instaliran, preskačem numeraciju stranica.")
            return False
        import fitz

    try:
        doc = fitz.open(str(pdf_path))
        total = len(doc)
        last_page_original_text = (doc[-1].get_text("text") or "").strip() if total else ""
        if total <= skip_first_pages:
            doc.close()
            return False
        unicode_font = find_unicode_font()
        font_kwargs = {"fontname": "helv"}
        if unicode_font:
            font_kwargs = {"fontname": "F0", "fontfile": str(unicode_font)}

        # Numbering starts from the first page that contains "1. Uvod".
        start_page = None
        uvod_rx = re.compile(r"\b1\.?\s+Uvod\b", re.IGNORECASE)
        for i, page in enumerate(doc):
            txt = page.get_text("text")
            lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
            if lines and uvod_rx.match(lines[0]):
                start_page = i + 1
                break

        if start_page is None:
            for i, page in enumerate(doc):
                txt = page.get_text("text")
                if uvod_rx.search(txt):
                    start_page = i + 1
                    break

        if start_page is None:
            start_page = max(1, skip_first_pages + 1)
            print(f"  Upozorenje: '1. Uvod' nije pronađen, numeracija kreće od stranice {start_page}.")

        book_title = "Komunikacija u doba umjetne inteligencije"
        heading_rx = re.compile(r"^\d+(?:\.\d+)*\.?\s+.+")
        special_headings = {"Predgovor", "Referencije", "Glosar", "Kazalo pojmova", "Index", "Bilješka o izdanju"}
        current_heading = ""

        def normalize_heading(text: str) -> str:
            return re.sub(r"\s+", " ", text).strip().rstrip(".")

        def fit_header_fontsize(text: str, available_width: float, base_size: float = 6.8) -> float:
            """Shrink long running headers just enough to fit, without trimming."""
            if available_width <= 0:
                return base_size
            text_width = fitz.get_text_length(text, fontname="helv", fontsize=base_size)
            if text_width <= available_width:
                return base_size
            scaled = base_size * (available_width / max(text_width, 1))
            return max(4.8, min(base_size, scaled))

        def wrap_header_text(text: str, available_width: float, fontsize: float) -> str:
            """Wrap long running headers into two balanced lines."""
            words = text.split()
            if len(words) < 3:
                return text

            best = text
            best_score = float("inf")
            for i in range(1, len(words)):
                line1 = " ".join(words[:i])
                line2 = " ".join(words[i:])
                width1 = fitz.get_text_length(line1, fontname="helv", fontsize=fontsize)
                width2 = fitz.get_text_length(line2, fontname="helv", fontsize=fontsize)
                overflow = max(0, width1 - available_width) + max(0, width2 - available_width)
                balance = abs(width1 - width2)
                score = overflow * 1000 + balance
                if score < best_score:
                    best_score = score
                    best = f"{line1}\n{line2}"
            return best

        def detect_heading(page) -> str:
            blocks = page.get_text("dict").get("blocks", [])
            candidates = []
            for idx, block in enumerate(blocks):
                block_lines = []
                block_sizes = []
                block_fonts = []
                min_y = None
                bbox = block.get("bbox", [0, 0, 0, 0])
                for line in block.get("lines", []):
                    spans = line.get("spans", [])
                    if not spans:
                        continue
                    text = normalize_heading("".join(span.get("text", "") for span in spans))
                    if not text:
                        continue
                    block_lines.append(text)
                    block_sizes.extend(span.get("size", 0) for span in spans)
                    block_fonts.extend(span.get("font", "") for span in spans)
                    line_min_y = min(span.get("bbox", [0, 0, 0, 0])[1] for span in spans)
                    min_y = line_min_y if min_y is None else min(min_y, line_min_y)
                if not block_lines:
                    continue
                first_line = block_lines[0]
                if not (heading_rx.match(first_line) or first_line in special_headings):
                    continue
                max_size = max(block_sizes) if block_sizes else 0
                if max_size < 13:
                    continue
                text = normalize_heading(" ".join(block_lines))
                fonts = " ".join(block_fonts)
                block_x0, _, _, block_y1 = bbox

                # Some long headings are split into a second PDF block on the next line.
                for next_block in blocks[idx + 1: idx + 4]:
                    next_lines = []
                    next_sizes = []
                    next_bbox = next_block.get("bbox", [0, 0, 0, 0])
                    for line in next_block.get("lines", []):
                        spans = line.get("spans", [])
                        if not spans:
                            continue
                        next_text = normalize_heading("".join(span.get("text", "") for span in spans))
                        if next_text:
                            next_lines.append(next_text)
                            next_sizes.extend(span.get("size", 0) for span in spans)
                    if not next_lines or not next_sizes:
                        break
                    next_max_size = max(next_sizes)
                    next_x0, next_y0, _, _ = next_bbox
                    next_text = normalize_heading(" ".join(next_lines))
                    if heading_rx.match(next_text) or next_text in special_headings:
                        break
                    if next_max_size < 13 or abs(next_max_size - max_size) > 1.0:
                        break
                    if next_y0 - block_y1 > 18 or abs(next_x0 - block_x0) > 24:
                        break
                    text = normalize_heading(f"{text} {next_text}")
                    block_y1 = next_bbox[3]

                candidates.append((min_y or 0, -max_size, "bold" not in fonts.lower() and "semibold" not in fonts.lower(), text))
            if not candidates:
                return ""
            candidates.sort()
            return candidates[0][3]

        for idx, page in enumerate(doc):
            page_no = idx + 1
            if page_no < start_page:
                continue

            rect = page.rect
            page_text = page.get_text("text")
            if (
                "ZAVRŠNA BIL" in page_text
                or "Ova knjiga završava, ali ostaje" in page_text
                or "github.com/bperak/komunikacija_u_doba_ai" in page_text
            ):
                continue
            if (
                "Bilješka o izdanju" in page_text
                or "BIL JEŠKA O IZDANJU" in page_text
                or "Ova knjiga ostaje otvorena za" in page_text
            ):
                detected_heading = "Bilješka o izdanju"
            else:
                detected_heading = detect_heading(page)
            if detected_heading:
                current_heading = detected_heading

            # Running header: centered group with book title + current chapter/section.
            header_left = 32
            header_right = rect.width - 32
            header_width = header_right - header_left
            header_color = (0.45, 0.45, 0.45)
            divider_color = (0.76, 0.80, 0.86)
            divider_y = 27

            if current_heading:
                chapter_text = normalize_heading(current_heading)
                combined_header = f"{book_title} · {chapter_text}"
                combined_fontsize = fit_header_fontsize(combined_header, header_width, 6.4)
                combined_width = fitz.get_text_length(combined_header, fontname="helv", fontsize=combined_fontsize)

                if combined_width <= header_width:
                    page.insert_textbox(
                        fitz.Rect(header_left, 7, header_right, 20),
                        combined_header,
                        fontsize=combined_fontsize,
                        color=header_color,
                        overlay=True,
                        align=1,
                        **font_kwargs,
                    )
                    divider_y = 27
                else:
                    title_fontsize = 6.5
                    chapter_fontsize = 5.2
                    wrapped_heading = wrap_header_text(chapter_text, header_width, chapter_fontsize)
                    page.insert_textbox(
                        fitz.Rect(header_left, 4, header_right, 15),
                        book_title,
                        fontsize=title_fontsize,
                        color=header_color,
                        overlay=True,
                        align=1,
                        **font_kwargs,
                    )
                    page.insert_textbox(
                        fitz.Rect(header_left, 13, header_right, 30),
                        wrapped_heading,
                        fontsize=chapter_fontsize,
                        color=header_color,
                        overlay=True,
                        align=1,
                        **font_kwargs,
                    )
                    divider_y = 33 if "\n" in wrapped_heading else 29
            else:
                page.insert_textbox(
                    fitz.Rect(header_left, 7, header_right, 20),
                    book_title,
                    fontsize=6.5,
                    color=header_color,
                    overlay=True,
                    align=1,
                    **font_kwargs,
                )
                divider_y = 27

            shape = page.new_shape()
            divider_half = rect.width * 0.16
            shape.draw_line(
                fitz.Point(rect.width / 2 - divider_half, divider_y),
                fitz.Point(rect.width / 2 + divider_half, divider_y),
            )
            shape.finish(color=divider_color, width=0.6)
            shape.commit(overlay=True)

            label = str(page_no - start_page + 1)
            y = rect.height - 18
            page.insert_textbox(
                fitz.Rect(0, y - 10, rect.width, y + 8),
                label,
                fontsize=9,
                color=(0.35, 0.35, 0.35),
                overlay=True,
                align=1,
                **font_kwargs,
            )

        if len(doc) > 1 and len(last_page_original_text) < 8:
            doc.delete_page(len(doc) - 1)

        tmp_pdf = pdf_path.with_name(f"{pdf_path.stem}._numbered{pdf_path.suffix}")
        doc.save(str(tmp_pdf), deflate=True)
        doc.close()
        tmp_pdf.replace(pdf_path)
        print(f"  Numeracija dodana od Uvoda: PDF {start_page} -> logička stranica 1.")
        return True
    except Exception as exc:
        print(f"  Upozorenje: numeracija stranica nije uspjela ({exc}).")
        return False


def normalize_front_matter_cover(pdf_path: Path) -> bool:
    """Replace page 1 with clean full-bleed cover and remove top strip on page 2."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return False

    cover_img = None
    for candidate in [PROJECT_ROOT / "docs" / "book_cover_bg.jpg", PROJECT_ROOT / "docs" / "book_cover_bg.png"]:
        if candidate.exists():
            cover_img = candidate
            break
    if not cover_img:
        return False

    try:
        src = fitz.open(str(pdf_path))
        if len(src) < 2:
            src.close()
            return False
        cover_meta = extract_cover_metadata()
        unicode_font = find_unicode_font()
        font_kwargs = {"fontname": "helv"}
        if unicode_font:
            font_kwargs = {"fontname": "F0", "fontfile": str(unicode_font)}

        new = fitz.open()
        first_rect = src[0].rect
        first = new.new_page(width=first_rect.width, height=first_rect.height)
        first.insert_image(first.rect, filename=str(cover_img), keep_proportion=False, overlay=True)

        # Rebuild title typography on top of the cover background.
        white = (0.96, 0.96, 0.96)
        first.insert_textbox(
            fitz.Rect(0, 34, first_rect.width, 90),
            cover_meta["author"],
            fontsize=18,
            align=1,
            color=white,
            **font_kwargs,
        )
        first.insert_textbox(
            fitz.Rect(54, first_rect.height * 0.40, first_rect.width - 54, first_rect.height * 0.58),
            cover_meta["title"],
            fontsize=28,
            align=1,
            color=white,
            **font_kwargs,
        )
        first.insert_textbox(
            fitz.Rect(70, first_rect.height * 0.56, first_rect.width - 70, first_rect.height * 0.66),
            cover_meta["subtitle"],
            fontsize=15,
            align=1,
            color=white,
            **font_kwargs,
        )

        # Logos UNIRI + FFRI u podnožju, centrirano
        docs_dir = PROJECT_ROOT / "docs"
        logo_h = 28
        gap = 16
        logos = []
        for name in ["logo-uniri.png", "logo-ffri.png"]:
            p = docs_dir / name
            if p.exists():
                logos.append(p)
        if logos:
            try:
                total_w = 0
                rects = []
                for fp in logos:
                    img = fitz.open(str(fp))
                    r = img[0].rect
                    img.close()
                    w = r.width * (logo_h / r.height)
                    rects.append((fp, w))
                    total_w += w
                total_w += gap * (len(rects) - 1)
                x_start = (first_rect.width - total_w) / 2
                y_bottom = first_rect.height - 40
                x_cur = x_start
                for fp, w in rects:
                    r = fitz.Rect(x_cur, y_bottom - logo_h, x_cur + w, y_bottom)
                    first.insert_image(r, filename=str(fp), keep_proportion=True)
                    x_cur += w + gap
            except Exception:
                pass

        # Copy the rest as-is.
        new.insert_pdf(src, from_page=1, to_page=len(src) - 1)
        src.close()

        # Drop accidental "strip" page: page 2 often has only a thin colored bar
        # (print artifact from title-page/heading) and is otherwise blank.
        # Remove if empty or very little text (e.g. < 80 chars = strip-only).
        if len(new) > 1:
            p2_text = (new[1].get_text("text") or "").strip()
            if len(p2_text) < 80:
                new.delete_page(1)

        tmp_pdf = pdf_path.with_name(f"{pdf_path.stem}._frontmatter{pdf_path.suffix}")
        new.save(str(tmp_pdf), deflate=True)
        new.close()
        tmp_pdf.replace(pdf_path)
        print("  Naslovnica normalizirana (full-bleed + bez trake na 2. stranici).")
        return True
    except Exception as exc:
        print(f"  Upozorenje: normalizacija naslovnice nije uspjela ({exc}).")
        return False


def export_cover_for_readme(pdf_path: Path) -> Optional[Path]:
    """Export first page of PDF to docs/cover_naslovnica.png for README (full cover with text)."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    out = PROJECT_ROOT / "docs" / "cover_naslovnica.png"
    try:
        doc = fitz.open(str(pdf_path))
        if len(doc) == 0:
            doc.close()
            return None
        page = doc[0]
        pix = page.get_pixmap(dpi=150, alpha=False)
        out.parent.mkdir(parents=True, exist_ok=True)
        pix.save(str(out))
        doc.close()
        print(f"  Naslovnica za README: {out.name}")
        return out
    except Exception as exc:
        print(f"  Upozorenje: export naslovnice za README nije uspio ({exc}).")
        return None


def main():
    print("=" * 60)
    print(" GENERIRANJE INTEGRALNE VERZIJE KNJIGE")
    print("=" * 60)

    # Step 1: Merge
    print(f"\n[1/3] Spajanje {len(CHAPTER_FILES)} poglavlja...")
    merged = merge_chapters()
    total_lines = len(merged.splitlines())
    print(f"  Ukupno: {total_lines} redaka\n")

    # Step 2: Fix syntax
    print("[2/3] Priprema teksta...")
    merged = fix_nested_image_syntax(merged)
    merged = clear_image_alt_text(merged)
    merged = fix_truncated_captions(merged)
    merged = fix_caption_newlines(merged)
    merged = remove_duplicate_caption_paragraphs(merged)
    merged_for_html = fix_image_paths_for_manuscript(merged)
    print("  Putanje slika popravljene.")
    print("  Alt-tekst slika obrisan (sprječava duple opise).")
    print("  Skraćeni opisi (s '...') popravljeni.")
    print("  Opisi slika odvojeni u zasebne retke.\n")

    # Step 3: Build HTML (with images)
    print("[3/3] Generiranje izlaznih datoteka...\n")

    print("  --- HTML (sa SVG dijagramima) ---")
    html_path = build_html(merged_for_html)
    if html_path and html_path.exists():
        size_kb = html_path.stat().st_size / 1024
        print(f"  HTML GOTOV: {html_path.name} ({size_kb:.0f} KB)")
    else:
        print("  HTML generiranje nije uspjelo!")

    print()
    print("  --- PDF (sa SVG dijagramima, Chrome headless) ---")
    pdf_path = build_pdf(merged_for_html, html_path)
    if pdf_path and pdf_path.exists():
        normalize_front_matter_cover(pdf_path)
        add_page_numbers(pdf_path, skip_first_pages=1)
        export_cover_for_readme(pdf_path)
        size_mb = pdf_path.stat().st_size / (1024 * 1024)
        print(f"  PDF GOTOV: {pdf_path.name} ({size_mb:.1f} MB)")
    else:
        print("  PDF nije generiran. Koristite HTML verziju:")
        print(f"  Otvorite HTML u pregledniku -> Ctrl+P -> Spremi kao PDF")

    print(f"\n{'=' * 60}")
    print(f" GOTOVO!")
    if html_path and html_path.exists():
        print(f" HTML: {html_path}")
    if pdf_path and pdf_path.exists():
        print(f" PDF:  {pdf_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
