# Označavanje novog izdanja knjige na GitHubu

**Službeno izdanje** (bibliografski kanon, izdavač): stranica Filozofskog fakulteta u Rijeci — kad je knjiga tamo objavljena, taj URL je primarni za citiranje i promociju.

**GitHub** služi kao:

- **automatski „zadnji build“** — Release označen tagom `latest` (ažurira se workflowom pri pushu PDF/HTML na `main`);
- **trajno označena izdanja** — svaki put kad FFRI (ili ti) objaviš **novo izdanje** knjige, na GitHubu napravi **novi Release s verzijom u tagu**, npr. `v1.0.0`, `v1.1.0`, `v2.0.0`.

Tako u [Releases](https://github.com/bperak/komunikacija_u_doba_ai/releases) ostaje vidljiva povijest: koje je datoteke bilo u kojem izdanju, bez da `latest` zamjenjuje značenje „izdanja 2“.

## Kada napraviti novo označeno izdanje?

- Nova verzija objavljena ili najavljena na **izdavačkoj stranici FFRI**.
- Značajnije izmjene sadržaja (npr. novo poglavlje, ispravak kruga referenci).
- Želiš **stabilan link** na točno taj PDF/HTML za citate ili arhiv (permalink na Release asset).

## Koraci (ručno, GitHub web)

1. Pushaj na `main` ažurirani `manuscript/Perak_Komunikacija_u_doba_AI.pdf` i `.html` kad su finalni za to izdanje.
2. Otvori repozitorij → **Releases** → **Draft a new release**.
3. **Choose a tag**: upiši novi tag, npr. `v1.1.0` → *Create new tag*.
4. **Release title**: npr. `Izdanje 1.1` ili `Komunikacija u doba AI — izdanje 2026`.
5. **Opis**: kratko što je novo (1–3 rečenice), opcionalno poveznica na FFRI stranicu tog izdanja.
6. Priloži iste datoteke kao assete (ili se osloni na snapshot grane u tom trenutku — asseti su najjasniji za preuzimanje).
7. Objavi (**Publish release**).

Tag `latest` i dalje pokazuje zadnji automatski build; **verzionirani tagovi** (`v1.0.0`, …) ostaju nepomični.

## Semver (kratko)

- **v1.0.0** — prvo javno označeno izdanje na GitHubu.
- **v1.1.0** — manja nadogradnja (dopune, ispravci).
- **v2.0.0** — veća preinaka ili novo izdanje u izdavačkom smislu.

Uskladi broj s napomenom na naslovnici / kod izdavača ako postoji službena numeracija.
