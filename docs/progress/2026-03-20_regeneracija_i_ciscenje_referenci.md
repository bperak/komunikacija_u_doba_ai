# Izvještaj rada

Datum: 2026-03-20

## Sažetak

Provedeno je uredničko čišćenje uvoda i bibliografije, nakon čega je knjiga ponovno generirana pomoću postojećeg postupka iz `README.md` i skripte `scripts/build_pdf.py`.

## Što je izmijenjeno

### 1. Uvod

U datoteci `manuscript/chapters/01_uvod.md`:

- usklađen je stil citiranja u odlomku o velikim jezičnim modelima
- uklonjeni su nepotpuni ili bibliografski nepokriveni navodi (`Gemini (Google)`, `Llama (Meta AI, 2024)`)
- vraćen je uredan citat za Milenu Žic-Fuchs: `(Žic-Fuchs, 1991)`
- usklađena je terminologija: `višeagentski sustavi` / `agentski rojevi`
- dosljedno su oblikovane oznake `Poglavlje 6` i `Poglavlje 7`

### 2. Reference

U datoteci `manuscript/chapters/09_referencije.md`:

- dodana je referenca:
  - `Žic-Fuchs, M. (1991). Znanje o jeziku i znanje o svijetu...`
- ispravljena je Guardian referenca o Cambridge Analytici punom poveznicom
- `Harari (2014)` je pretvoren u standardnu bibliografsku jedinicu
- uklonjene su uredničke napomene unutar bibliografskih zapisa
- uklonjeni su generički ili eksplicitno hipotetski zapisi koji nisu prikladni za završnu bibliografiju
- uklonjeni su zaostali prazni naslovi i prazni redci na kraju bibliografije

### 3. Usklađivanje citata u ostalim poglavljima

U datotekama:

- `manuscript/chapters/02_povijest_tehnologija.md`
- `manuscript/chapters/05_pogon_umjetne_inteligencije.md`
- `manuscript/chapters/06_od_modela_do_partnera.md`
- `manuscript/chapters/08_digitalni_suputnici.md`

napravljene su sljedeće korekcije:

- uklonjeni su citati koji su upućivali na generičke ili nepostojeće reference
- zamijenjeni su bibliografski problematični navodi stvarnim izvorima gdje je to bilo moguće
- u 5. poglavlju:
  - `Pester, 2025` i `Ladish, 2025` zamijenjeni su referencom `Palisade Research (2025)`
  - `Tang i sur., 2024` zamijenjeno je referencom `Pan i sur., 2024`

## Regeneracija knjige

Build je pokrenut naredbom:

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

- HTML: 2026-03-20 11:02:49
- PDF: 2026-03-20 11:02:54

## Napomena

Tijekom provjere stanja repozitorija `git` je prijavio `dubious ownership`, pa za ovaj ciklus nije korišten `git status` kao izvor izvještavanja. Sadržajne i build provjere odrađene su izravno nad datotekama i build izlazom.
