# Završni prolaz dijagrama, sadržaja i stražnje naslovnice

Datum: 2026-03-20

## Što je napravljeno

- Svi Mermaid izvori u `docs/diagrams` ponovno su renderirani u ujednačenoj plavkastoj paleti.
- U `scripts/render_mermaid.mjs` dodano je čišćenje Mermaid frontmattera, `%%{init}%%` blokova i starih HTML prijeloma (`<br>`), kako bi i stariji `diag_*` dijagrami izlazili čitljivo i bez doslovno ispisanih oznaka.
- Kartica `Sadržaj` u `scripts/build_pdf.py` rasterećena je manjim unutarnjim marginama i smanjenim desnim uvlakama.
- Završna stranica zamijenjena je stražnjom naslovnicom u `manuscript/chapters/11_zavrsna_biljeska.md`, vizualno usklađenom s naslovnicom.
- U PDF build procesu popravljeno je generiranje Chrome headless profila izvan OneDrive privremenih putanja, kako bi build ponovno prolazio stabilno.
- U numeraciji PDF-a dodano je preskakanje zaglavlja i broja stranice na stražnjoj naslovnici te uklanjanje prazne završne stranice ako nastane kao print-artifakt.

## Provjera

- Vizualno su provjereni `Sadržaj`, reprezentativni stariji `diag_*` dijagrami i nova stražnja naslovnica.
- Potvrđeno je da su stari ljubičasti Mermaid izlazi zamijenjeni novim plavkastim SVG-ovima.
- Potvrđeno je da PDF završava na stražnjoj naslovnici, bez praznog zadnjeg lista.

## Ishod

- Knjiga sada ima ujednačeniji vizualni sustav dijagrama.
- Sadržaj je čitljiviji i manje stisnut u kartici.
- Završetak knjige sada funkcionira kao prava stražnja naslovnica, a ne kao obična tekstualna kartica.
