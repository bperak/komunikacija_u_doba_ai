# Komunikacija u doba umjetne inteligencije

**Razvoj velikih jezičnih modela i komunikacijskih agenata**

*Benedikt Perak*

Filozofski fakultet, Sveučilište u Rijeci · Rijeka, 2025.

ISBN (elektroničko izdanje): 978-953-361-147-1

---

## O knjizi

Ova knjiga istražuje razvoj komunikacijskih tehnologija od usmene predaje do velikih jezičnih modela i autonomnih agenata umjetne inteligencije. Namijenjena je studentima i svima koji promišljaju nove trendove u komunikaciji sa strojevima sa sve razvijenijim jezičnim sposobnostima.

### Agentno obnavljajuća knjiga

Ovo izdanje ima novi oblik — **agentno obnavljajuće knjige**. Prvo izdanje bit će dopunjavano korištenjem agentnih postupaka pretrage informacija, dopuna novih *state-of-the-art* tehnoloških rješenja i problematizacije njihovih implikacija za komunikacijske i kulturološke fenomene. Nove inačice periodično se objavljuju na ovom repozitoriju.

---

## Preuzimanje knjige

| Verzija | Opis | Preuzmi |
|---------|------|---------|
| **Najnovija** | Zadnje izdanje knjige | [⬇ Preuzmi najnoviju verziju](https://github.com/bperak/komunikacija_u_doba_ai/releases/latest) |
| Sve verzije | Arhiva svih prošlih izdanja | [📦 Sve verzije](https://github.com/bperak/komunikacija_u_doba_ai/releases) |

Knjiga je dostupna u **HTML** i **PDF** formatu.

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

---

## Struktura repozitorija

```
├── manuscript/
│   └── chapters/          # Markdown poglavlja knjige
├── docs/
│   └── diagrams/          # Mermaid izvori (.mmd) i SVG dijagrami
├── scripts/
│   └── build_pdf.py       # Skripta za generiranje HTML/PDF knjige
├── book_builder/          # Agentni alati za izgradnju knjige
├── tests/                 # Testovi
├── requirements.txt       # Python ovisnosti
└── package.json           # Node.js ovisnosti (Mermaid dijagrami)
```

## Izgradnja knjige iz izvora

### Preduvjeti

- **Python 3.10+**
- **Pandoc** (za konverziju Markdown → HTML/PDF)
- **XeLaTeX** (MiKTeX ili TeX Live, za PDF generiranje)
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

---

## Citiranje (APA 7)

> Perak, Benedikt (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci.

---

## Licenca

© 2025 Benedikt Perak, Filozofski fakultet, Sveučilište u Rijeci.

Sva prava pridržana. Niti jedan dio ovog izdanja ne može biti objavljen, pretiskan ili distribuiran bez prethodne suglasnosti izdavača.
