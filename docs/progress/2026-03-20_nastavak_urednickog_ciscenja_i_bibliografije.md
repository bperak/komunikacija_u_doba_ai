# Izvještaj rada

Datum: 2026-03-20

## Sažetak

Nastavljeno je uredničko čišćenje rukopisa nakon prethodne regeneracije knjige. Fokus ovoga ciklusa bio je na 2. poglavlju, dodatnom usklađivanju citata i bibliografije te provjeri da se knjiga i dalje uspješno generira u HTML i PDF oblik.

## Što je izmijenjeno

### 1. Tipografsko i stilsko čišćenje teksta

U datoteci `manuscript/chapters/02_povijest_tehnologija.md`:

- ispravljeni su tipografski i kurzivni artefakti:
  - `potkraj1990-ih` -> `potkraj 1990-ih`
  - uklonjeni su zaostali razmaci u izrazima poput `*SixDegrees *`, `*Facebooka *`, `*Instagrama *`, `*Snapchata *`, `*r/funny *`, `*online *zajednice`, `*online *aktivnost`
  - `open-source *projektima` usklađeno je u `*open-source* projektima`
- uklonjen je zaostali znak `*` u sintagmi `asocijativnoga indeksiranja`
- ispravljen je naziv platforme `Courserae` u `Coursera`
- preoblikovan je odlomak o Racteru radi jasnijeg i bibliografski čišćeg oslanjanja na postojeće izvore

### 2. Usklađivanje citata i bibliografije

U datotekama:

- `manuscript/chapters/03_veliki_jezicni_modeli.md`
- `manuscript/chapters/04_dekonstrukcija_jezika.md`
- `manuscript/chapters/06_od_modela_do_partnera.md`
- `manuscript/chapters/08_digitalni_suputnici.md`
- `manuscript/chapters/09_referencije.md`

napravljene su sljedeće korekcije:

- uklonjen je nepokriveni navod `Smith, 2020` u 3. poglavlju
- u 4. poglavlju citat `Vigotski, 1978` usklađen je s bibliografskim zapisom `Vygotsky, 1978`
- u 6. poglavlju nepokriveni navodi `Gao i sur., 2024` i `Barnett i sur., 2024` zamijenjeni su postojećim izvorom `Xu i sur., 2023`
- u 8. poglavlju:
  - `Novak i sur., 2021` zamijenjeno je postojećom referencom `Chen i sur., 2021`
  - uklonjen je nepokriveni navod `Wang et al., 2021`
- u bibliografiju su dodane jedinice potrebne za već prisutne citate:
  - `Berners-Lee, 1990`
  - `Hofstede, 2001`
  - `Howe, 2008`
  - `Leiner i sur., 2009`
  - `Lévy, 1997`
  - `Wooldridge, 2009`
  - `Sundararajan, 2016`

### 3. Provjera preostalih citata

Nakon čišćenja provjerena je podudarnost citata i bibliografskih jedinica. U preostalom automatskom ispisu pojavljuju se samo korporativni autori (`Anthropic`, `OpenAI`, `Palisade Research`), koji su već uredno prisutni u bibliografiji.

## Regeneracija knjige

Build je ponovno pokrenut naredbom:

```bash
python scripts/build_pdf.py
```

Status:

- build uspješno dovršen
- HTML ponovno generiran
- PDF ponovno generiran

## Generirane izlazne datoteke

- `manuscript/Perak_Komunikacija_u_doba_AI.html`
- `manuscript/Perak_Komunikacija_u_doba_AI.pdf`

Vrijeme generiranja:

- HTML: 2026-03-20 11:13:51
- PDF: 2026-03-20 11:13:56

## Napomena

Tijekom ovog ciklusa `git status` nije korišten zbog `dubious ownership` upozorenja, no sadržajne i build provjere odrađene su izravno nad datotekama i generiranim izlazom.
