"""
Testovi za split_manuscript_to_chapters: 10 datoteka (00–09) + 10_glosar u manuscript/chapters/,
granice naslovnica/poglavlja/referencije, putanje slika ../../docs/diagrams/, merge uključuje Glosar.
"""
import re
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "manuscript" / "chapters"
EXPECTED_FILES_SPLIT = [
    "00_naslovnica.md",
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
EXPECTED_FILES = EXPECTED_FILES_SPLIT + ["10_glosar.md"]


@pytest.fixture(scope="module")
def run_split_first():
    """Pokreće split, zatim extract_glossary ako treba, da chapters/ ima 00–10."""
    import subprocess
    if not CHAPTERS_DIR.exists() or len(list(CHAPTERS_DIR.glob("*.md"))) < 10:
        subprocess.run(
            ["python", str(PROJECT_ROOT / "scripts" / "split_manuscript_to_chapters.py")],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )
    if not (CHAPTERS_DIR / "10_glosar.md").exists():
        subprocess.run(
            ["python", str(PROJECT_ROOT / "scripts" / "extract_glossary.py")],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )


def test_chapters_dir_has_expected_files(run_split_first):
    """U manuscript/chapters/ mora biti 11 MD datoteka (00–09 + 10_glosar)."""
    assert CHAPTERS_DIR.exists(), "manuscript/chapters/ ne postoji"
    files = sorted(f.name for f in CHAPTERS_DIR.glob("*.md"))
    assert files == EXPECTED_FILES, f"Očekivano {EXPECTED_FILES}, dobiveno {files}"


def test_naslovnica_ends_before_chapter_one(run_split_first):
    """Naslovnica (redci 1-48) ne smije sadržavati naslov poglavlja 1 '# 1 Uvod'."""
    path = CHAPTERS_DIR / "00_naslovnica.md"
    text = path.read_text(encoding="utf-8")
    assert "# 1 Uvod" not in text, "00_naslovnica ne smije sadržavati '# 1 Uvod'"


def test_01_uvod_starts_with_chapter_one(run_split_first):
    """01_uvod.md počinje s '# 1 Uvod'."""
    text = (CHAPTERS_DIR / "01_uvod.md").read_text(encoding="utf-8")
    assert text.strip().startswith("# 1 "), "01_uvod mora počinjati s '# 1 '"


def test_09_referencije_starts_with_referencije(run_split_first):
    """09_referencije.md počinje s '# Referencije'."""
    text = (CHAPTERS_DIR / "09_referencije.md").read_text(encoding="utf-8")
    assert re.match(r"^#\s*Referencije", text.strip(), re.IGNORECASE), "09_referencije mora počinjati s '# Referencije'"


def test_08_ends_before_referencije(run_split_first):
    """08_digitalni_suputnici.md ne smije sadržavati '# Referencije'."""
    text = (CHAPTERS_DIR / "08_digitalni_suputnici.md").read_text(encoding="utf-8")
    lines = text.strip().split("\n")
    for line in lines:
        if re.match(r"^#\s*Referencije\s*$", line.strip(), re.IGNORECASE):
            pytest.fail("08 ne smije sadržavati redak '# Referencije'")


def test_chapters_use_relative_diagram_paths(run_split_first):
    """U chapter datotekama (00–09) putanja do slika mora biti ../../docs/diagrams/, ne ../docs/diagrams/."""
    wrong = "](../docs/diagrams/"
    for fname in EXPECTED_FILES_SPLIT:
        text = (CHAPTERS_DIR / fname).read_text(encoding="utf-8")
        assert wrong not in text, f"{fname} ne smije sadržavati ](../docs/diagrams/"


def test_chapters_have_diagram_links_where_expected(run_split_first):
    """Barem neke chapter datoteke (00–09) imaju link na ../../docs/diagrams/ (provjera zamjene)."""
    right = "](../../docs/diagrams/"
    count = 0
    for fname in EXPECTED_FILES_SPLIT:
        count += (CHAPTERS_DIR / fname).read_text(encoding="utf-8").count(right)
    assert count > 0, "Očekivani barem neki linkovi na ../../docs/diagrams/ u chapters"


def test_merge_produces_file_with_correct_paths():
    """Nakon merge, izlazna datoteka ima putanje ../docs/diagrams/ (za manuscript/)."""
    import subprocess
    merge_script = PROJECT_ROOT / "scripts" / "merge_chapters_to_manuscript.py"
    if not CHAPTERS_DIR.exists() or len(list(CHAPTERS_DIR.glob("*.md"))) < 11:
        if len(list(CHAPTERS_DIR.glob("*.md"))) < 10:
            subprocess.run(
                ["python", str(PROJECT_ROOT / "scripts" / "split_manuscript_to_chapters.py")],
                cwd=str(PROJECT_ROOT),
                check=True,
                capture_output=True,
            )
        if not (CHAPTERS_DIR / "10_glosar.md").exists():
            subprocess.run(
                ["python", str(PROJECT_ROOT / "scripts" / "extract_glossary.py")],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )
    subprocess.run(
        ["python", str(merge_script)],
        cwd=str(PROJECT_ROOT),
        check=True,
        capture_output=True,
    )
    out_path = PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu_from_chapters.md"
    assert out_path.exists(), "Merge mora kreirati from_chapters.md"
    text = out_path.read_text(encoding="utf-8")
    assert "](../docs/diagrams/" in text, "Merge izlaz mora imati putanju ../docs/diagrams/"
    assert "](../../docs/diagrams/" not in text, "Merge izlaz ne smije imati ../../ u chapters stilu"


def test_merge_line_count_near_original():
    """Broj redaka spojenog rukopisa približno jednak originalu; merge može imati više redaka (captioni/definicije) ili manje ako su u chapters uklonjeni suvišni blokovi slika."""
    import subprocess
    if not (PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu_from_chapters.md").exists():
        subprocess.run(
            ["python", str(PROJECT_ROOT / "scripts" / "merge_chapters_to_manuscript.py")],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
        )
    orig = (PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu.md").read_text(encoding="utf-8")
    merged = (PROJECT_ROOT / "manuscript" / "Ben knjiga lektorirana_za_obradu_from_chapters.md").read_text(encoding="utf-8")
    no_orig, no_merged = len(orig.splitlines()), len(merged.splitlines())
    # Merge ne smije biti znatno kraći (sadržaj iz chapters mora biti uključen); dopušteno do ~250 manje ako su uklonjeni suvišni blokovi slika
    assert no_merged >= no_orig - 250, f"Merge ima premalo redaka: original {no_orig}, merge {no_merged}"
