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
from pathlib import Path
from urllib.parse import quote

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"
DIAGRAMS_DIR = PROJECT_ROOT / "docs" / "diagrams"
OUTPUT_DIR = PROJECT_ROOT / "manuscript"

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
]

BOOK_CSS = """
<style>
@media print {
    @page { size: A4; margin: 2.5cm 2cm 2.5cm 2.5cm; }
    @page:first { size: A4; margin: 0; }
    h1 { page-break-before: always; }
    h1:first-of-type { page-break-before: avoid; }
    blockquote, figure, .img-wrap, pre, table { page-break-inside: avoid; }
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
    max-width: 90%;
    max-height: 500px;
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

.img-wrap svg {
    max-width: 85%;
    max-height: 420px;
    width: auto;
    height: auto;
    display: block;
    margin: 0 auto;
}

/* Pandoc figure element */
figure {
    margin: 1.5em auto;
    text-align: center;
    max-width: 90%;
}

figure img {
    max-width: 100%;
    max-height: 500px;
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
    background: #f8f9fa;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1.5em 2em;
    margin: 2em 0;
}

#TOC ul { list-style: none; padding-left: 1em; }
#TOC > ul { padding-left: 0; }
#TOC li { margin-bottom: 0.3em; }
#TOC a { color: #2a5a8c; }

/* ── Book cover ── */
.book-cover {
    position: relative;
    width: calc(100% + 4rem);
    min-height: 960px;
    margin: -2rem -2rem 0 -2rem;
    overflow: hidden;
    border-radius: 0;
    page-break-after: always;
    background: #0f1932;
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
    color: #d4a843;
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

/* ── Inner title page (naslovni list) ── */
.title-page {
    page-break-before: auto;
    page-break-after: always;
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
    page-break-after: always;
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

/* ── Predgovor ── */
.predgovor-page {
    page-break-before: auto;
    page-break-after: always;
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
    margin-top: 2.5em;
    text-align: right;
    font-style: italic;
    color: #555;
    line-height: 1.6;
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
}

@media print {
    .book-cover {
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
    }
    .predgovor-page {
        min-height: 100vh;
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
    return re.sub(r'^(\*Slika \d+\.\d+: )(.+?)\.\.\.\*$', _fix, md_text, flags=re.MULTILINE)


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

    # 1. Add .img-wrap class to <p> that contains only an <img>
    html_text = re.sub(
        r'<p>(\s*<img [^>]*/?>\s*)</p>',
        r'<p class="img-wrap">\1</p>',
        html_text
    )

    # 2. Add .caption class to <p><em>Slika X.Y: ...</em></p>
    html_text = re.sub(
        r'<p><em>(Slika \d+\.\d+:.*?)</em></p>',
        r'<p class="caption"><em>\1</em></p>',
        html_text
    )

    # 3. Also handle *Slika 0.X* patterns (chapter 0 naslovnica)
    html_text = re.sub(
        r'<p><em>(\*?Slika \d+\.\d+:.*?)</em></p>',
        r'<p class="caption"><em>\1</em></p>',
        html_text
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


def build_html(merged_md: str) -> Path:
    """Build a beautiful standalone HTML from merged markdown using Pandoc."""
    html_path = OUTPUT_DIR / "knjiga_integralna.html"
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

    html_path = OUTPUT_DIR / "knjiga_integralna.html"

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
    html_path.write_text(full_html, encoding="utf-8")
    return html_path


def build_pdf(merged_md: str, html_path: Path = None) -> Path:
    """Build PDF from the HTML file using Chrome headless (includes all SVG diagrams)."""
    pdf_path = OUTPUT_DIR / "knjiga_integralna.pdf"

    if html_path is None or not html_path.exists():
        html_path = OUTPUT_DIR / "knjiga_integralna.html"

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

    cmd = [
        chrome,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={pdf_path}',
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

    if not pdf_path.exists():
        err = result.stderr[:1000] if result.stderr else "nepoznata greska"
        print(f"  PDF greska: {err}")
        return None

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
        if total <= skip_first_pages:
            doc.close()
            return False

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
        current_heading = ""

        for idx, page in enumerate(doc):
            page_no = idx + 1
            if page_no < start_page:
                continue

            rect = page.rect
            page_text = page.get_text("text") or ""
            lines = [ln.strip() for ln in page_text.splitlines() if ln.strip()]
            for ln in lines[:40]:
                if heading_rx.match(ln):
                    current_heading = ln
                    break

            # Running header: left=book title, right=current chapter/section (if detected).
            header_y = 18
            page.insert_text(
                fitz.Point(24, header_y),
                book_title,
                fontname="helv",
                fontsize=8,
                color=(0.45, 0.45, 0.45),
                overlay=True,
            )
            if current_heading:
                chapter_text = current_heading
                if len(chapter_text) > 60:
                    chapter_text = chapter_text[:57] + "..."
                ch_w = fitz.get_text_length(chapter_text, fontname="helv", fontsize=8)
                ch_x = max(24, rect.width - 24 - ch_w)
                page.insert_text(
                    fitz.Point(ch_x, header_y),
                    chapter_text,
                    fontname="helv",
                    fontsize=8,
                    color=(0.45, 0.45, 0.45),
                    overlay=True,
                )

            label = str(page_no - start_page + 1)
            width = fitz.get_text_length(label, fontname="helv", fontsize=9)
            x = (rect.width - width) / 2
            y = rect.height - 18
            page.insert_text(
                fitz.Point(x, y),
                label,
                fontname="helv",
                fontsize=9,
                color=(0.35, 0.35, 0.35),
                overlay=True,
            )

        tmp_pdf = pdf_path.with_name(f"{pdf_path.stem}._numbered{pdf_path.suffix}")
        doc.save(str(tmp_pdf), deflate=True)
        doc.close()
        tmp_pdf.replace(pdf_path)
        print(f"  Numeracija dodana od Uvoda: PDF {start_page} -> logička stranica 1.")
        return True
    except Exception as exc:
        print(f"  Upozorenje: numeracija stranica nije uspjela ({exc}).")
        return False


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
        add_page_numbers(pdf_path, skip_first_pages=1)
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
