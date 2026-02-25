# Bilješka: ch02_nadzor_ciklus.svg

## Što je bilo krivo

1. **Strelica na bridu Prediktivni proizvodi → Ciljanje i manipulacija nije bila vidljiva**  
   Polyline je završavao unutar čvora. Čvor se u SVG-u crta *nakon* polylinea, pa pravokutnik prekrije strelicu.

2. **Labela „vodi ka” bila je uz sam rub čvora**  
   Putanja za textPath bila je vertikalna tik do čvora; trebala je biti na vodoravnom dijelu brida.

3. **Tekst je izgledao prejako (pre bold)**  
   `font-weight="500"` / `"600"` izgledalo je prenaglašeno.

## Kako je popravljeno (u pipelineu)

**Izvornik je .mmd** — ručne izmjene u SVG-u gube se pri ponovnom renderu. Zato je popravak ugrađen u **postproces** `scripts/svg_edge_labels_along_path.mjs`:

1. **Skraćivanje polylinea**  
   Ako kraj linije (zadnja točka) padne unutar nekog čvora (rect s rx="0", visina 35–50 px), skripta skraćuje polyline tako da završava izvan čvora (s malim razmakom ARROW_GAP). Strelica ostaje vidljiva, a putanja za labelu automatski postaje vodoravni segment, pa je labela na bridu, ne uz rub.

2. **Ublaženi font**  
   U postprocesu: `font-weight="600"` → 500 (naslov), `font-weight="500"` → 400 (čvorovi).

**Korištenje:** Nakon renderiranja iz .mmd (`node scripts/render_mermaid.mjs -f docs/diagrams/ch02_nadzor_ciklus.mmd -o ...`) pokreni postproces:  
`node scripts/svg_edge_labels_along_path.mjs -f docs/diagrams/ch02_nadzor_ciklus.svg -o docs/diagrams/ch02_nadzor_ciklus.svg`  
Tada će strelica, labela i font biti ispravni i bez ručnog mijenjanja SVG-a.
