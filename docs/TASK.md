# TASKS

## 2024-06-11
- [x] Scaffold Scientific Book Builder multi-agent system (folders, agents, tools, tests, planning).  
  - Created `book_builder` package with tools and agents.  
  - Added `PLANNING.md` with architecture.  
  - Added unit tests and requirements.

## Discovered During Work
- Integrate real web search and RAG once API keys and vector store are available.
- Persist drafts to DB.

---

## KORACI ZA NASTAVAK PROJEKTA

### Faza 1 – Odmah (bez novih API ključeva)
1. **Pokrenuti sustav i provjeriti da radi** – `python -m book_builder.agents.orchestrator` (orchestrator učitava `.env` s `OPENAI_API_KEY`).
2. **CLI za unos** – omogućiti unos teksta/naslova poglavlja iz naredbenog retka ili iz datoteke (npr. iz Markdowna nakon `python scripts/convert.py`).
3. **Povezati knjigu s orchestratorom** – opcija da se kao input da izlaz iz `scripts/convert.py` (Markdown poglavlja iz `manuscript/Ben knjiga lektorirana_za_obradu.docx`) za doradu/lektoriranje.
4. **Proširiti testove** – test za CLI, test da orchestrator prima markdown input (mock).

### Faza 2 – Stvarne integracije (kad imaš API ključeve)
5. **Web pretraga** – zamijeniti stub u `book_builder/tools/core.py` s pravim API-jem (npr. SerpAPI ili Tavily); ključ iz `.env`.
6. **RAG** – vektorska baza (npr. Chroma/FAISS) nad markdown poglavljima knjige; `retrieve_facts` koristi pravi retrieval.
7. **Citati** – integracija s Zotero ili jednostavna provjera formata (IEEE); opcionalno `check_citation` s pravom logikom.

### Faza 3 – Perzistencija i UI
8. **Baza** – SQLModel za nacrte, verzije poglavlja i citate; spremanje outputa orchestratora.
9. **FastAPI + WebSockets** – REST API za pokretanje zadatka, WebSockets za stream outputa; jednostavan front-end (opcionalno). 