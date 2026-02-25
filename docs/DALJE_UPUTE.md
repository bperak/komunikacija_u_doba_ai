# Što dalje – upute za nastavak projekta

## Krajnji cilj procesa

**U jednoj rečenici:** Sustav (više agenata) treba pomoći u **doradi i poliranju znanstvene knjige** – da na temelju tvog lektoriranog rukopisa (`Ben knjiga lektorirana_za_obradu.docx`) predlaže poboljšanja, provjerava stil i citate, po želji pretražuje izvore, i na kraju da dobiješ **doradenu, spremnu verziju** teksta (po poglavljima ili cijelu knjigu).

**Što to u praksi znači:**
- **Ulaz:** tvoja knjiga (Word → Markdown), npr. lektorirani rukopis.
- **Proces:** orchestrator šalje tekst specijalistima (stil, citati, proofreader, web/RAG kad ih uključiš); oni predlažu izmjene ili vraćaju doraden tekst.
- **Izlaz:** doradena verzija poglavlja/knjige (spremna za daljnju obradu ili objavu), s mogućnošću spremanja verzija u bazu i kasnije web sučelja za pokretanje zadataka.

Cilj nije automatski “napisati knjigu umjesto tebe”, nego **pomoć u redakciji, lektoriranju i provjeri** – da ti agenti rade kao tim koji predlaže i provjerava, a ti odlučuješ što prihvaćaš.

---

## Od lektoriranog rukopisa do krajnje verzije

Knjiga je **već lektorirana** (`Ben knjiga lektorirana_za_obradu.docx`). Krajnja verzija = ono što šalješ izdavaču ili u tisak (finalni Word ili PDF, s naslovnicom, sadržajem, konzistentnim formatiranjem).

**Dva moguća puta:**

### A) Najjednostavnije (bez ovog projekta)

1. Otvori `manuscript/Ben knjiga lektorirana_za_obradu.docx` u Wordu.
2. U Wordu doradi: naslovnica, stranica s sadržajem (TOC), eventualno numeracija stranica i zaglavlja.
3. Spremi kao finalni Word i/ili **Izradi PDF** (Datoteka → Spremi kao → PDF) i to pošalji izdavaču.

To je već **krajnja verzija** ako ti ne treba automatska dorada teksta.

### B) S ovim projektom (opcionalno)

Ako želiš još jedan **lagani automatizirani prolaz** (provjera tipfelera, konzistentnost termina, citati) prije izvoza:

1. **Word → Markdown** (već imaš): `python scripts/convert.py` → dobiješ `manuscript/Ben knjiga lektorirana_za_obradu.md`.
2. **Opcionalno: jedan prolaz agenata** (kad bude povezano): orchestratoru daš markdown; proofreader/stil agenti predlože male izmjene; ti prihvaćaš u Wordu ili u .md.
3. **Markdown → finalni format:** Word (otvoriš .md u Wordu ili Pandoc: `pandoc knjiga.md -o knjiga_final.docx`); PDF (u Wordu "Spremi kao PDF" ili Pandoc: `pandoc knjiga.md -o knjiga_final.pdf`).
4. U finalnom Wordu/PDF-u doradiš naslovnicu, sadržaj, stranice – kao u A).

**Sažetak:** Za skoro gotovu, lektoriranu knjigu krajnju verziju najčešće napraviš tako da u Wordu dovršiš naslovnicu i sadržaj te izvezeš PDF (put A). Projekt s agentima koristiš ako želiš još jedan automatizirani provjeravajući prolaz prije toga (put B).

---

Kratki pregled sljedećih koraka prema `TASK.md` i `PLANNING.md`.

---

## Odmah (Faza 1 – bez novih API ključeva)

1. **Provjeri da orchestrator radi**  
   Iz roota projekta:
   ```bash
   python -m book_builder.agents.orchestrator
   ```
   U `.env` mora biti postavljen `OPENAI_API_KEY`.

2. **Konvertiraj lektorirani rukopis u Markdown**  
   ```bash
   python scripts/convert.py
   ```
   Zadano: `manuscript/Ben knjiga lektorirana_za_obradu.docx` → isti naziv s nastavkom `.md` u `manuscript/`.

3. **CLI za unos**  
   Dodati mogućnost unosa teksta ili naslova poglavlja iz naredbenog retka ili iz datoteke (npr. iz generiranog Markdowna).

4. **Povezati knjigu s orchestratorom**  
   Omogućiti da se kao ulaz orchestratoru preda Markdown iz konverzije (npr. izlaz od `scripts/convert.py` za `Ben knjiga lektorirana_za_obradu.docx`) – za doradu/lektoriranje teksta putem agenata.

5. **Proširiti testove**  
   Test za CLI; test da orchestrator prima markdown ulaz (mock).

6. **Dijagrami (Mermaid)**  
   Instalirano: [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid). U rootu: `npm install`. Izvori: `docs/diagrams/*.mmd`. Regeneriraj SVG: `python scripts/render_diagrams.py` ili pojedinačno: `node scripts/render_mermaid.mjs -f docs/diagrams/architecture.mmd -o docs/diagrams/architecture.svg`. Arhitektura agenata je u `docs/diagrams/architecture.mmd`.

---

## Kad imaš dodatne API ključeve (Faza 2)

7. **Web pretraga** – zamijeniti stub u `book_builder/tools/core.py` pravim API-jem (npr. SerpAPI ili Tavily); ključ iz `.env`.
8. **RAG** – vektorska baza (npr. Chroma/FAISS) nad markdown poglavljima knjige; `retrieve_facts` koristi pravi retrieval.
9. **Citati** – integracija s Zotero ili provjera formata (npr. IEEE); opcionalno `check_citation` s pravom logikom.

---

## Kasnije (Faza 3)

10. **Baza** – SQLModel za nacrte, verzije poglavlja i citate; spremanje outputa orchestratora.
11. **FastAPI + WebSockets** – REST API za pokretanje zadatka, WebSockets za stream outputa; po želji jednostavan front-end.

---

## Preporučeni redoslijed za “odmah”

| Redoslijed | Što | Zašto |
|------------|-----|--------|
| 1 | Pokreni orchestrator i convert | Provjera da sve radi s postojećim `.env`. |
| 2 | CLI za unos (tekst / datoteka) | Orchestrator može primati konkretan tekst ili putanju do Markdowna. |
| 3 | Povezati knjigu (markdown → orchestrator) | Lektorirani rukopis (`Ben knjiga lektorirana_za_obradu.docx` → md) postaje ulaz za doradu. |
| 4 | Testovi za CLI i markdown input | Stabilnost pri promjenama. |
| 5 | Dijagrami (opcionalno) | `npm install` pa `python scripts/render_diagrams.py` – arhitektura u `docs/diagrams/`. |

Detalji arhitekture: `docs/PLANNING.md` i dijagram `docs/diagrams/architecture.svg` (izvor: `architecture.mmd`).  
Detalji zadataka: `docs/TASK.md`.
