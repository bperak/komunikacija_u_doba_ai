from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "promocija" / "plakat_preview.png"
COVER = ROOT / "docs" / "cover_naslovnica.png"
LOGO_FFRI = ROOT / "docs" / "logo-ffri.png"
LOGO_UNIRI = ROOT / "docs" / "logo-uniri.png"

WIDTH = 1240
HEIGHT = 1754
MARGIN = 72


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts") / name,
        Path("C:/Windows/Fonts") / name.lower(),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONT_SANS = load_font("segoeui.ttf", 24)
FONT_SANS_BOLD = load_font("segoeuib.ttf", 24)
FONT_SERIF = load_font("georgia.ttf", 26)
FONT_SERIF_BOLD = load_font("georgiab.ttf", 26)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    font: ImageFont.ImageFont,
    fill: str,
    max_width: int,
    line_gap: int = 8,
) -> int:
    x, y = xy
    words = text.split()
    line = ""
    lines: list[str] = []
    for word in words:
        test = word if not line else f"{line} {word}"
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)

    for item in lines:
        draw.text((x, y), item, font=font, fill=fill)
        bbox = draw.textbbox((x, y), item, font=font)
        y = bbox[3] + line_gap
    return y


def rounded_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int],
    radius: int = 28,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def paste_with_aspect(
    canvas: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
    contain: bool = True,
) -> None:
    x1, y1, x2, y2 = box
    bw, bh = x2 - x1, y2 - y1
    src = image.copy()
    if contain:
        src.thumbnail((bw, bh))
    else:
        src = src.resize((bw, bh))
    ox = x1 + (bw - src.width) // 2
    oy = y1 + (bh - src.height) // 2
    canvas.paste(src, (ox, oy), src if src.mode == "RGBA" else None)


def make_background() -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f5f0e6")
    px = img.load()
    for y in range(HEIGHT):
        t = y / HEIGHT
        base_r = int(245 - 8 * t)
        base_g = int(240 - 10 * t)
        base_b = int(230 - 4 * t)
        for x in range(WIDTH):
            px[x, y] = (base_r, base_g, base_b)
    return img


def main() -> None:
    img = make_background().convert("RGBA")
    draw = ImageDraw.Draw(img)

    teal = (15, 106, 115, 255)
    amber = (213, 141, 42, 255)
    ink = (24, 33, 38, 255)
    muted = (83, 96, 102, 255)
    white_panel = (255, 255, 255, 192)
    line = (24, 33, 38, 24)

    draw.ellipse((860, -90, 1350, 390), fill=(15, 106, 115, 26))
    draw.ellipse((-120, 1330, 380, 1830), fill=(213, 141, 42, 30))

    draw.text((MARGIN, MARGIN), "NOVA KNJIGA / BESPLATNO ELEKTRONICKO IZDANJE", font=load_font("segoeuib.ttf", 20), fill=teal)
    title_y = draw_wrapped(
        draw,
        "Komunikacija u doba umjetne inteligencije",
        (MARGIN, MARGIN + 36),
        load_font("georgiab.ttf", 50),
        "#182126",
        760,
        6,
    )
    draw.text((MARGIN, title_y + 8), "Razvoj velikih jezicnih modela i komunikacijskih agenata", font=load_font("segoeui.ttf", 28), fill=muted)

    flag_box = (960, 70, 1150, 130)
    rounded_panel(draw, flag_box, white_panel, line, radius=18)
    draw.text((995, 86), "PDF + HTML", font=load_font("segoeuib.ttf", 20), fill=teal)

    cover_box = (MARGIN, 290, 430, 1090)
    rounded_panel(draw, cover_box, (255, 255, 255, 180), line, radius=28)
    cover = Image.open(COVER).convert("RGBA")
    paste_with_aspect(img, cover, (MARGIN + 18, 308, 412, 1072))

    note_box = (MARGIN, 1125, 430, 1338)
    rounded_panel(draw, note_box, white_panel, line, radius=24)
    note_text = (
        "Knjiga je namijenjena studentima, nastavnicima, istrazivacima i siroj publici "
        "koja trazi ozbiljan uvod u odnos jezika, kulture i umjetne inteligencije."
    )
    draw_wrapped(draw, note_text, (MARGIN + 22, 1150), load_font("segoeui.ttf", 21), "#536066", 340, 6)

    right_x = 485
    draw.text((right_x, 302), "Benedikt Perak", font=load_font("segoeuib.ttf", 30), fill=ink)

    lead = (
        "Od usmene predaje i pisma do velikih jezicnih modela i komunikacijskih agenata: "
        "knjiga prati kako se mijenja komunikacija i sto te promjene znace za znanje, "
        "obrazovanje, kulturu i drustvene odnose."
    )
    lead_y = draw_wrapped(draw, lead, (right_x, 360), load_font("georgia.ttf", 33), "#182126", 660, 10)

    panel1 = (right_x, lead_y + 20, 1160, lead_y + 258)
    rounded_panel(draw, panel1, white_panel, line, radius=28)
    draw.text((right_x + 24, lead_y + 42), "O KNJIZI", font=load_font("segoeuib.ttf", 20), fill=teal)
    text1 = (
        "Komunikacija u doba umjetne inteligencije povezuje povijest komunikacijskih tehnologija "
        "s aktualnim razvojem umjetne inteligencije. U sredistu su veliki jezicni modeli, agentni "
        "sustavi i pitanje kako AI postaje novi sudionik komunikacije."
    )
    draw_wrapped(draw, text1, (right_x + 24, lead_y + 78), load_font("segoeui.ttf", 22), "#182126", 620, 8)

    panel2_y = panel1[3] + 22
    panel2 = (right_x, panel2_y, 1160, panel2_y + 260)
    rounded_panel(draw, panel2, white_panel, line, radius=28)
    draw.text((right_x + 24, panel2_y + 22), "TEME", font=load_font("segoeuib.ttf", 20), fill=teal)
    topics = [
        "povijest komunikacijskih tehnologija",
        "LLM-ovi i komunikacijski agenti",
        "jezik, kultura i proizvodnja znanja",
        "etika, pristranost i drustvene posljedice AI-a",
    ]
    tx_positions = [(right_x + 24, panel2_y + 72), (right_x + 340, panel2_y + 72), (right_x + 24, panel2_y + 156), (right_x + 340, panel2_y + 156)]
    for (tx, ty), topic in zip(tx_positions, topics):
        draw.line((tx, ty - 10, tx + 250, ty - 10), fill=(24, 33, 38, 30), width=2)
        draw_wrapped(draw, topic, (tx, ty), load_font("segoeui.ttf", 22), "#182126", 265, 4)

    meta_y = panel2[3] + 24
    meta_boxes = [
        (right_x, meta_y, right_x + 320, meta_y + 116, "Izdavac", "Filozofski fakultet u Rijeci"),
        (right_x + 340, meta_y, right_x + 660, meta_y + 116, "Mjesto i godina", "Rijeka, 2025."),
        (right_x, meta_y + 136, right_x + 320, meta_y + 252, "ISBN", "978-953-361-147-1"),
        (right_x + 340, meta_y + 136, right_x + 660, meta_y + 252, "Dostupno", "PDF i HTML izdanje"),
    ]
    for x1, y1, x2, y2, label, value in meta_boxes:
        rounded_panel(draw, (x1, y1, x2, y2), (255, 255, 255, 210), line, radius=20)
        draw.text((x1 + 18, y1 + 18), label.upper(), font=load_font("segoeuib.ttf", 18), fill=muted)
        draw_wrapped(draw, value, (x1 + 18, y1 + 48), load_font("segoeuib.ttf", 22), "#182126", (x2 - x1) - 36, 4)

    cta_y = meta_y + 286
    cta_box = (right_x, cta_y, 920, cta_y + 180)
    rounded_panel(draw, cta_box, (15, 106, 115, 235), (15, 106, 115, 235), radius=28)
    draw.text((right_x + 26, cta_y + 24), "PREUZIMANJE I PREGLED", font=load_font("segoeuib.ttf", 20), fill="white")
    draw.text((right_x + 26, cta_y + 64), "Glavni link za dijeljenje knjige:", font=load_font("segoeui.ttf", 24), fill="white")
    draw_wrapped(draw, "github.com/bperak/komunikacija_u_doba_ai", (right_x + 26, cta_y + 102), load_font("segoeuib.ttf", 26), "white", 380, 6)

    qr_box = (950, cta_y, 1160, cta_y + 180)
    draw.rounded_rectangle(qr_box, radius=28, fill=(255, 255, 255, 170), outline=(15, 106, 115, 120), width=3)
    draw.text((1005, cta_y + 26), "QR KOD", font=load_font("segoeuib.ttf", 20), fill=teal)
    qr_text = "Dodaj QR koji vodi na glavni URL ili sluzbenu FFRI stranicu."
    draw_wrapped(draw, qr_text, (974, cta_y + 70), load_font("segoeui.ttf", 18), "#536066", 160, 4)

    footer_y = 1605
    draw.line((MARGIN, footer_y, WIDTH - MARGIN, footer_y), fill=(24, 33, 38, 36), width=2)

    logo_ffri = Image.open(LOGO_FFRI).convert("RGBA")
    logo_uniri = Image.open(LOGO_UNIRI).convert("RGBA")
    paste_with_aspect(img, logo_ffri, (MARGIN, footer_y + 20, MARGIN + 150, footer_y + 70))
    paste_with_aspect(img, logo_uniri, (MARGIN + 170, footer_y + 20, MARGIN + 320, footer_y + 70))

    footer = (
        "Lokalni preview plakata za pregled. U verziju za dogadaj mozes dodati datum, "
        "vrijeme i mjesto promocije."
    )
    draw_wrapped(draw, footer, (760, footer_y + 18), load_font("segoeui.ttf", 18), "#536066", 400, 4)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, quality=95)


if __name__ == "__main__":
    main()
