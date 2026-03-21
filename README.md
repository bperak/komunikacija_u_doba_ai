# Komunikacija u doba umjetne inteligencije

**Razvoj velikih jezičnih modela i komunikacijskih agenata**

*Benedikt Perak*

Filozofski fakultet, Sveučilište u Rijeci · Rijeka, 2025.

ISBN (elektroničko izdanje): 978-953-361-147-1

![Naslovnica knjige](https://raw.githubusercontent.com/bperak/komunikacija_u_doba_ai/main/docs/cover_naslovnica.png)

---

## O knjizi

Ova knjiga istražuje razvoj komunikacijskih tehnologija od usmene predaje do velikih jezičnih modela i autonomnih agenata umjetne inteligencije. Namijenjena je studentima i svima koji promišljaju nove trendove u komunikaciji sa strojevima sa sve razvijenijim jezičnim sposobnostima.

### Agentno obnavljajuća knjiga

Ovo izdanje ima novi oblik — **agentno obnavljajuće knjige**. Prvo izdanje bit će dopunjavano korištenjem agentnih postupaka pretrage informacija, dopuna novih *state-of-the-art* tehnoloških rješenja i problematizacije njihovih implikacija za komunikacijske i kulturološke fenomene. Nove inačice periodično se objavljuju na ovom repozitoriju.

---

## Preuzimanje knjige

### Službeno izdanje (izdavač)

Elektroničko izdanje dostupno je na **izdavačkoj stranici Filozofskog fakulteta** u Rijeci — to je primarni kanal za citiranje i dijeljenje kad je stranica objavljena. *(Umetni ovdje točan URL kad bude na FFRI webu.)*

### GitHub (izvor + arhiv izdanja)

| Što | Opis |
|-----|------|
| **Zadnji build** | Release **[latest](https://github.com/bperak/komunikacija_u_doba_ai/releases/tag/latest)** — automatski se ažurira pri pushu PDF/HTML na `main`; praktičan za razvoj, ne zamjenjuje službeni broj izdanja. |
| **Označena izdanja** | Pojedina izdanja (npr. `v1.0.0`, `v1.1.0`) — trajni zapisi za arhiv i stabilne poveznice. **Kad FFRI objavi novo izdanje**, napravi novi Release s novim tagom. Upute: [docs/IZDANJE_GITHUB.md](docs/IZDANJE_GITHUB.md). |

| Format | Preuzmi (grana `main`) |
|--------|-------------------------|
| **PDF** | [⬇ Perak_Komunikacija_u_doba_AI.pdf](https://github.com/bperak/komunikacija_u_doba_ai/raw/main/manuscript/Perak_Komunikacija_u_doba_AI.pdf) |
| **HTML** | [⬇ Perak_Komunikacija_u_doba_AI.html](https://github.com/bperak/komunikacija_u_doba_ai/raw/main/manuscript/Perak_Komunikacija_u_doba_AI.html) |

[📦 Svi releasei](https://github.com/bperak/komunikacija_u_doba_ai/releases)

---

## Sadržaj knjige

1. **Uvod: Komunikacija i razvoj civilizacije**
2. **Povijest i evolucija komunikacijskih tehnologija** — od usmene predaje, pisma i tiska do elektroničke komunikacije i interneta
3. **Veliki jezični modeli** — arhitektura, obuka, fino podešavanje i poravnanje
4. **Dekonstrukcija jezika** — tokenizacija, ugradbe, semantički prostori
5. **Pogon umjetne inteligencije** — transformerska arhitektura, mehanizam pažnje
6. **Od modela do partnera** — tehnike upućivanja, lanci misli, memorija i kontekst
7. **Izgradnja komunikacijskog partnera** — RAG, agentura, alati
8. **Digitalni suputnici** — višeagentski sustavi, etički izazovi, budućnost
9. **Referencije**
10. **Index**

---

## Struktura repozitorija

```
├── manuscript/
│   ├── chapters/          # Markdown poglavlja knjige
│   ├── Perak_Komunikacija_u_doba_AI.pdf
│   └── Perak_Komunikacija_u_doba_AI.html
├── docs/
│   └── diagrams/          # Mermaid izvori (.mmd) i SVG dijagrami
├── scripts/
│   ├── build_pdf.py      # Generiranje HTML/PDF knjige
│   ├── export_cover_png.py
│   └── ostale skripte (formatting, split, dijagrami, glosar)
├── book_builder/         # Agentni alati za izgradnju knjige
├── tests/                # Testovi
├── dodatno/              # Arhiva: stari rukopisi, planiranje, opcionalne skripte
├── requirements.txt
└── package.json
```

## Izgradnja knjige iz izvora

### Preduvjeti

- **Python 3.10+**
- **Pandoc** (za konverziju Markdown → HTML/PDF)
- **Google Chrome / Microsoft Edge** (headless print za PDF)
- **Node.js** (za regeneriranje Mermaid dijagrama, opcionalno)

### Koraci

```bash
# 1. Kloniraj repozitorij
git clone https://github.com/bperak/komunikacija_u_doba_ai.git
cd komunikacija_u_doba_ai

# 2. Instaliraj Python ovisnosti
pip install -r requirements.txt

# 3. (Opcionalno) Instaliraj Node.js ovisnosti za dijagrame
npm install

# 4. Generiraj HTML i PDF
python scripts/build_pdf.py
```

Generirane datoteke nalaze se u `manuscript/` direktoriju.

PDF izlaz je podešen bez browser header/footer artefakata (datum, URL, vrijeme), s
running headerom i numeracijom koja kreće od poglavlja **Uvod**.

---

## Citiranje (APA 7)

> Perak, Benedikt (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci.

---

## Licenca

© 2025 Benedikt Perak, Filozofski fakultet, Sveučilište u Rijeci.

Sva prava pridržana. Niti jedan dio ovog izdanja ne može biti objavljen, pretiskan ili distribuiran bez prethodne suglasnosti izdavača.
