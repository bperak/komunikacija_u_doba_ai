"""English manuscript tree: all chapter files, diagrams_en links, build_pdf locale."""
import importlib.util
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EN_CH = PROJECT_ROOT / "manuscript" / "en" / "chapters"
DIAGRAMS_EN = PROJECT_ROOT / "docs" / "diagrams_en"

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


def test_en_chapters_dir_has_all_expected_files():
    assert EN_CH.exists(), "manuscript/en/chapters missing"
    for name in CHAPTER_FILES:
        p = EN_CH / name
        assert p.is_file(), f"missing {p.relative_to(PROJECT_ROOT)}"


def test_en_chapters_reference_diagrams_en_not_hr_diagrams():
    """Chapters 01–08 should point to docs/diagrams_en for SVG assets (not diagrams/)."""
    skip = {
        "00_naslovnica.md",
        "00b_predgovor.md",
        "09_referencije.md",
        "10_glosar.md",
        "11_zavrsna_biljeska.md",
    }
    hr_diag = "../../docs/diagrams/"
    en_diag = "../../docs/diagrams_en/"
    for name in CHAPTER_FILES:
        if name in skip:
            continue
        text = (EN_CH / name).read_text(encoding="utf-8")
        assert hr_diag not in text, f"{name} must not use {hr_diag!r}"
        assert en_diag in text, f"{name} should reference {en_diag!r}"


def test_diagrams_en_has_string_translations_manifest():
    manifest = DIAGRAMS_EN / "string_translations.json"
    assert manifest.is_file(), "diagrams_en/string_translations.json missing"


@pytest.mark.parametrize("svg_name", ["ch02_mcluhan.svg", "diag_01.svg", "ch03_rlhf.svg"])
def test_sample_diagrams_en_svg_exists(svg_name):
    p = DIAGRAMS_EN / svg_name
    assert p.is_file(), p


def test_build_pdf_configure_locale_en():
    spec = importlib.util.spec_from_file_location(
        "build_pdf", PROJECT_ROOT / "scripts" / "build_pdf.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    mod.configure_build_locale("en")
    assert mod.CHAPTERS_DIR == PROJECT_ROOT / "manuscript" / "en" / "chapters"
    assert mod.BOOK_BASENAME == "Perak_Communication_in_the_Age_of_AI"
    assert mod.COVER_README_BASENAME == "cover_naslovnica_en"
    mod.configure_build_locale("hr")
    assert mod.CHAPTERS_DIR == PROJECT_ROOT / "manuscript" / "chapters"


def test_extract_glossary_en_writes_file(tmp_path):
    """Smoke: EN glossary pattern runs without error when chapters exist."""
    import subprocess
    import sys

    out = tmp_path / "glossary_en.md"
    r = subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "scripts" / "extract_glossary.py"),
            "--language",
            "en",
            "--chapters-dir",
            str(EN_CH),
            "--output",
            str(out),
        ],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    assert r.returncode == 0, r.stderr
    assert out.read_text(encoding="utf-8").startswith("# Glossary")
