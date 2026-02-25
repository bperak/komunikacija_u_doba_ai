# Rukopis i poglavlja

## Izvor

- **Originalni rukopis (samo čitanje):** `Ben knjiga lektorirana_za_obradu.md` u ovoj mapi.
- **Razdvajanje:** rukopis se razdvaja u 10 datoteka u podmapu `chapters/` (00–09); dodatno postoji `10_glosar.md`, generiran skriptom za glosar. LLM obrađuje **1 poglavlje po 1** unutar svog konteksta.

## Mapa chapters/

U `manuscript/chapters/` nalaze se:

| Datoteka | Sadržaj |
|----------|--------|
| `00_naslovnica.md` | Naslovnica (redci 1–48 izvornika) |
| `01_uvod.md` … `08_digitalni_suputnici.md` | Poglavlja 1–8 (granice po naslovu `# 1` … `# 8`) |
| `09_referencije.md` | Od "# Referencije" do kraja |
| `10_glosar.md` | Glosar (abecedni popis definicija; generira `scripts/extract_glossary.py`) |

**Putanje do slika:** U datotekama u `chapters/` putanja do dijagrama je `../../docs/diagrams/` (dva nivoa gore od `chapters/`). U izvornom rukopisu u `manuscript/` putanja je `../docs/diagrams/`.

## Naredbe (korijen projekta)

- **Razdvajanje (split):**  
  `python scripts/split_manuscript_to_chapters.py`  
  Čita `manuscript/Ben knjiga lektorirana_za_obradu.md`, piše 10 datoteka u `manuscript/chapters/` i prilagodi putanje slika.

- **Spajanje (merge):**  
  `python scripts/merge_chapters_to_manuscript.py`  
  Spaja 11 datoteka iz `chapters/` (00–10, uključujući Glosar) u jedan MD. Izlaz: `manuscript/Ben knjiga lektorirana_za_obradu_from_chapters.md` (original se **ne** prepisuje).

- **Glosar:**  
  `python scripts/extract_glossary.py`  
  Izvlači sve blokove `> **Definicija (Pojam):** …` iz poglavlja 01–08 i piše abecedni popis u `manuscript/chapters/10_glosar.md`. Pokrenuti nakon dodavanja novih definicija u poglavlja; zatim ponovno merge.

- **Captioni (nakon splita):**  
  `python scripts/add_captions_to_chapters.py`  
  Dodaje ispod svake slike u `chapters/` caption u formatu *Slika X.Y: …* (X = poglavlje 0–9, Y = redni broj slike). Ako ponovno pokreneš split, captione treba ponovno dodati ovom skriptom.

## Cilj: 1 poglavlje = 1 LLM kontekst

Razdvajanje omogućuje da se rukopis obrađuje po poglavljima: umjesto cijele knjige u jednom koraku, LLM prima jednu datoteku (npr. `03_veliki_jezicni_modeli.md`), što stane u kontekst i omogućuje kvalitetnu obradu ilustracija, captiona i definicija za to poglavlje.

## Definicije i captioni

- **Definicije:** format u MD-u: blok citata, npr. `> **Definicija (Pojam):** Tekst.` Umetnute su u svim poglavljima 1–8. Popis po poglavljima: 1 (indeksni znak, simbol, agent, gramatika, zajednička intencionalnost, teorija uma, LLM, komunikacijski agent, AGI), 2 (artefakt, usmena predaja, živi arhiv), 3 (token, embedding, korpus, transformer, emergentne sposobnosti, RLHF, predtreniranje, fino podešavanje, MLOps, temeljni model, poravnanje, pristranost, suparnički napad, model nagrade, PEFT, LoRA, kvantizacija, obrezivanje, skupna inferencija, inferencija u stvarnom vremenu, edge computing, resursna intenzivnost, zakon skaliranja, TPU, troškovi učenja i troškovi zaključivanja, računalni jaz), 4 (dekonstrukcija jezika u kontekstu AI, jezični čin, mentalna mapa, semantički trokut, problem usidrenja, emergentno ponašanje, društvena konstrukcija zbilje, antropomorfizacija, parasocijalna interakcija, algoritamska leća, pomaknuto referiranje, intersubjektivna stvarnost), 5 (Mooreov zakon, GPU, inferencija, digitalni kolektiv, halucinacija, afektivno računalstvo, agentska neusklađenost), 6 (API, personalizacija, emocionalna inteligencija, CRM, oblikovanje uputa, kontekstualni prozor, korištenje alata / Tool Use, RAG), 7 (chatbot, virtualni asistent, sentiment analiza), 8 (digitalni suputnik, jaz u djelatnosti, višeagentski sustav, ambijentalna inteligencija). Ukupno 71 definicija.
- **Glosar:** sve definicije sakupljene su u `10_glosar.md` (abecedni popis); generira se skriptom `extract_glossary.py`.
- **Captioni:** ispod svake slike u chapters koristi se format *Slika X.Y: …* (dodaje skripta `add_captions_to_chapters.py`).

Detalje vidi u planu u `.cursor/plans/` (rukopis u poglavlja i naslovnica).

---

## Za sljedećeg agenta

- **Plan i handoff:** `.cursor/plans/rukopis_u_poglavlja_i_naslovnica_1377e05e.plan.md` — na dnu je sekcija „Handoff za sljedećeg agenta” sa stanjem, putanjama, naredbama i sljedećim koracima (ilustracije, captioni, definicije, glosar).
- **Testovi:** `tests/test_split_manuscript_to_chapters.py` — 9 testova za split i merge; pokretanje: `python -m pytest tests/test_split_manuscript_to_chapters.py -v`.
- **Original se ne dira:** izvor istine je `Ben knjiga lektorirana_za_obradu.md`; iz `chapters/` se spaja u `Ben knjiga lektorirana_za_obradu_from_chapters.md`.
