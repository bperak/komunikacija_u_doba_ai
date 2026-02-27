# 6. Od jezičnog modela do komunikacijskog partnera: arhitektura i primjena AI agenata

## 6.1	Uvod: evolucija od modela do agenta

Razvoj umjetne inteligencije, u svojoj biti, predstavlja neprekinuti put od stvaranja sustava koji pasivno obrađuju informacije do onih koji svrhovito djeluju unutar svojega okruženja. Taj put možemo pratiti kroz ključnu konceptualnu mijenu: evoluciju od modela prema agentu. Premda se oba pojma odnose na računske artefakte stvorene za rješavanje složenih problema, njihova narav, svrha i način postojanja u svijetu bitno se razlikuju.

Pod pojmom modela u kontekstu strojnog učenja i tradicionalne umjetne inteligencije razumijevamo matematičku ili računsku apstrakciju nekog procesa, sustava ili skupa podataka. Primarna mu je svrha deskriptivna ili prediktivna. Model prima ulazne podatke i, na temelju uzoraka koje je naučio tijekom faze obučavanja, proizvodi izlaz – bilo da je riječ o klasifikaciji, regresiji ili nekoj drugoj vrsti predviđanja. Primjerice, model za prepoznavanje slika može točno utvrditi nalazi li se na fotografiji mačka, a prognostički model može s određenom vjerojatnošću predvidjeti vremenske prilike. Njegova je funkcija ispunjena u trenutku kada isporuči informaciju. On je, u biti, pasivan instrument analize, čiji rezultat tumači i na temelju kojega djeluje čovjek ili neki drugi, odvojeni sustav.

Ipak, takav pristup, usprkos svojoj analitičkoj snazi, nailazi na temeljna ograničenja kada se suoči s potrebom za autonomijom i interakcijom u dinamičnim okruženjima. Svijet nije statičan skup podataka koji čeka na analizu, već prostor unutar kojeg je potrebno donositi odluke i djelovati. Pojam agenta stoga se javlja kao nužan i logičan iskorak u toj evoluciji. Agent je promatrač, ali i aktivni sudionik. Prema općeprihvaćenoj definiciji, agent je sve ono što može percipirati svoje okruženje pomoću senzora i djelovati na to okruženje pomoću aktuatora (Russell & Norvig, 2021). Njegovo postojanje je neprekinutim ciklusom percepcije, promišljanja i djelovanja.

Djelovanje agenta je vođeno racionalnošću, odnosno težnjom k ostvarenju zadanih ciljeva. Racionalan agent jest onaj koji poduzima radnje kako bi maksimizirao očekivanu mjeru uspješnosti, s obzirom na slijed percepcija i znanje kojim raspolaže (Sutton & Barto, 2018). Dok je za model ključna metrika *točnost predviđanja*, za agenta je to *učinkovitost djelovanja*. Autonomno vozilo, primjerice, je agent koji informacije o predviđanju putanja drugih vozila koristi kako bi donosio odluke – ubrzao, usporio, skrenuo – s ciljem sigurnog i učinkovitog dolaska na odredište.

Prijelaz s modela na agenta označava duboku promjenu paradigme. Težište se premješta sa stvaranja reprezentacija svijeta na razvoj entiteta koji u tom svijetu mogu samostalno postojati i djelovati. Autonomija, koja je u pristupu temeljenom na modelu bila u potpunosti izvan sustava, kod agenta postaje njegovo središnje obilježje. Ovu evolucijsku putanju moguće je zorno prikazati.


Dvije kontrastne paradigme: model kao pasivni prediktor koji transformira ulaz u izlaz, te agenta kao aktivnog sudionika u povratnoj sprezi s okruženjem

U suvremenom dobu svjedočimo kako se ova evolucija odvija ubrzano. Veliki jezični modeli (LLM), koji su u svojem začetku ponajprije bili složeni statistički modeli jezika, danas se sve više ugrađuju u arhitekture koje im omogućuju agentsko ponašanje. Povezivanjem s vanjskim alatima, izvorima podataka i mogućnostima djelovanja, oni prestaju biti isključivo generatori teksta i postaju jezgra za rasuđivanje unutar složenijih agenata sposobnih za planiranje i izvršavanje zadataka. Time se potvrđuje da je razvojni luk umjetne inteligencije usmjeren od stvaranja sofisticiranih analitičkih alata prema oblikovanju autonomnih, racionalnih i svrhovitih dionika u digitalnom i fizičkom svijetu.

## 6.2 Programabilni jezik: Uloga aplikacijskog programskog sučelja (API) kao mosta

Aplikacijsko programsko sučelje, poznatije pod akronimom API (od engl. *Application Programming Interface*), predstavlja ključan sklop pravila, protokola i alata koji djeluje kao posrednički most između različitih softverskih aplikacija, komponenata ili sustava, omogućujući im međusobnu komunikaciju i razmjenu podataka na strukturiran i predvidljiv način. Njegova temeljna svrha jest omogućiti jednoj softverskoj komponenti korištenje funkcionalnosti druge, bez potrebe za poznavanjem složenosti njezine unutarnje implementacije. Time API uspostavlja jasan ugovor o interakciji, definirajući vrste zahtjeva koje je moguće uputiti, način na koji se ti zahtjevi oblikuju, koje formate podataka koristi te kakav se odgovor može očekivati.

> **API:** Aplikacijsko programsko sučelje (engl. *Application Programming Interface*) – skup pravila i protokola koji omogućuje jednoj softverskoj komponenti pozivati funkcionalnost druge na strukturiran način; za agente predstavlja akcijski prostor – skup diskretnih operacija koje mogu izvršiti u digitalnom okruženju.

Djelovanje API-a može se zorno prikazati usporedbom s naručivanjem u restoranu. Gost u restoranu (klijent) ne komunicira izravno s kuhinjom (poslužiteljskim sustavom), već svoju narudžbu predaje konobaru (API-u) koristeći se jelovnikom (dokumentacijom API-a) koji jasno navodi dostupna jela i njihove cijene. Konobar zatim prenosi narudžbu kuhinji u formatu koji ona razumije. Nakon što je jelo pripremljeno, kuhinja ga predaje konobaru, koji ga poslužuje gostu. U toj analogiji, gost ne mora znati kako kuhinja radi, koji su recepti ili kako se organizira osoblje; on se oslanja na jasno definirano sučelje – konobara i jelovnik – kako bi dobio željenu uslugu.



Tijek komunikacije u kojem klijent šalje zahtjev API-u, koji ga prosljeđuje poslužitelju na obradu i zatim vraća odgovor klijentu

U toj ulozi posrednika, API istodobno obavlja i funkciju zaštitnog sloja apstrakcije. On skriva složenost pozadinskog sustava i izlaže samo one funkcionalnosti koje su potrebne za interakciju. Takav pristup donosi dalekosežne prednosti u razvoju softvera. Omogućuje modularnost, gdje se različiti dijelovi sustava mogu razvijati, ažurirati ili čak zamijeniti neovisno jedni o drugima, sve dok se pridržavaju ugovora definiranog API-em. To potiče ponovnu iskoristivost koda i komponenata te ubrzava cjelokupni razvojni proces. Primjerice, razvojni tim koji stvara mobilnu aplikaciju za vremensku prognozu ne mora graditi vlastitu meteorološku infrastrukturu; umjesto toga, on može putem API-a pozvati vanjsku uslugu koja pruža te podatke.

Upravo ta standardizirana priroda interakcije pretvara API u svojevrsni *programabilni jezik*. Svaki poziv API-u, sa svojim specifičnim parametrima i naredbama, nalikuje na instrukciju unutar višeg programskog jezika. Umjesto pisanja složenog koda za, primjerice, obradu plaćanja kreditnom karticom, programer koristi API pružatelja platnih usluga i poziva jednostavnu funkciju poput `naplati(iznos, broj_kartice)`. Slijed takvih poziva omogućuje orkestriranje složenih procesa spajanjem prethodno izgrađenih, neovisnih funkcionalnosti.

Za agenta, API uspostavlja cjelokupni akcijski prostor – skup diskretnih operacija koje može izvršiti radi postizanja zadanih ciljeva. Primjerice, agent zadužen za planiranje putovanja uči koristiti njihove javno dostupne API-e za pretraživanje letova, provjeru raspoloživosti i izvršenje rezervacija. Na taj način API-i funkcioniraju kao apstraktni gradivni blokovi koji omogućuju agentima svrhovito i autonomno djelovanje, efektivno transformirajući digitalni ekosustav u programabilno okruženje kojim se upravlja putem definiranih protokola (O'Keefe, 2024).

Trenutna praksa primjene agenata temeljenih na velikim jezičnim modelima (LLM) obuhvaća korištenje API-a u nekoliko ključnih domena. Za dohvaćanje znanja i informacija iz vanjskih izvora primjenjuju se API-i servisa kao što su Google Search, Wikipedia i ArXiv, koji agentima omogućuju pristup recentnim i provjerenim podacima (Patil i sur., 2023). U domeni uredske produktivnosti i suradnje, alati poput Microsoft Graph API-a i Google Workspace API-a omogućuju automatizaciju administrativnih zadataka. Za specifične zadatke vezane uz razvoj softvera, GitHub API pruža funkcionalnosti za upravljanje repozitorijima i projektnim zadacima. Od posebnog su značaja platforme za agregaciju API-a, poput Zapiera, koje nude unificirano sučelje za interakciju s tisućama različitih aplikacija. Takve platforme drastično proširuju sposobnosti agenata, omogućujući im izvođenje složenih, višefaznih radnih procesa bez potrebe za implementacijom svake pojedinačne integracije (LlamaIndex, n.d.; Zapier, n.d.).

Nasuprot statičkoj, unaprijed definiranoj integraciji alata, najnoviji znanstveni i tehnološki razvoj usmjeren je prema paradigmi u kojoj agenti autonomno uče koristiti nove API-e. Ključni elementi ovog pristupa su tehnike učenja korištenja alata (engl. *API learning*), kao što je demonstrirano u radu na jezičnim modelima proširenim alatima (*Tool-Augmented Language Models* ili TALM), gdje model uči koristiti API na temelju malog broja primjera poziva i odgovora (Parisi i sur., 2022). Posljedično, time se smanjuje potreba za ručnim programiranjem interakcija. Drugi temeljni element jest standardizacija opisa alata putem strojno čitljivih manifest datoteka (npr. openapi.yaml), koje sadrže formalan opis funkcionalnosti API-a. To agentima omogućuje dinamičko otkrivanje (engl. *dynamic discovery*) i samostalnu integraciju alata u vlastiti radni tijek. Ovakav pristup repozicionira AI agente kao primarne korisnike API-a, potičući razvoj sučelja koja su inherentno prilagođena agentima (engl. *agent-friendly*), čime se cjelokupna mreža transformira u univerzalni i dinamički iskoristiv set alata (Patil i sur., 2023).

## 6.2.1 Struktura API poziva

Svaka komunikacija između programskih sustava posredovana sučeljem za programiranje aplikacija (API) odvija se putem precizno oblikovanih zahtjeva, poznatih kao API pozivi. Ti pozivi su strukturirane poruke sastavljene od nekoliko ključnih elemenata, od kojih svaki ima jasno definiranu svrhu. Razumijevanje ove strukture temeljni je preduvjet za uspješnu interakciju s bilo kojim API-em, pa tako i onima koje koriste sustavi temeljeni na agentima.

Središnji element svakog poziva jest odredišna adresa (URL), poznata i kao *endpoint*. Ona predstavlja jedinstveni identifikator resursa kojem se želi pristupiti ili nad kojim se želi izvršiti određena radnja. URL se obično sastoji od osnovne adrese poslužitelja (npr. `https://api.primjer.com/v1/`) i specifične putanje koja precizno određuje resurs (npr. `/korisnici/123`).

Narav same radnje koju pozivatelj, u našem slučaju agent, želi izvršiti nad resursom izražava se HTTP metodom. Ove metode, koje se ponekad nazivaju i HTTP glagolima, definiraju semantiku operacije. Najčešće korištene metode usklađene su s osnovnim operacijama nad podacima (CRUD – *Create, Read, Update, Delete*):

**GET:** Služi za dohvaćanje postojećeg resursa. Ova je metoda idempotentna, što znači da višestruko ponavljanje istog poziva neće promijeniti stanje resursa.

**POST:** Koristi se za stvaranje novog resursa. Svaki POST poziv u pravilu rezultira stvaranjem novog, jedinstvenog entiteta na poslužitelju.

**PUT:** Namijenjen je potpunom ažuriranju postojećeg resursa. Pozivatelj šalje cjelokupan novi prikaz resursa koji zamjenjuje stari.

**DELETE:** Služi za brisanje određenog resursa.

Osim adrese i metode, API poziv sadrži i zaglavlja (engl. *headers*). Ona prenose metapodatke koji su nužni za ispravnu obradu zahtjeva, ali ne čine njegov središnji sadržaj. U zaglavljima se najčešće nalaze informacije o autorizaciji, poput API ključa ili tokena (`Authorization`), kao i podaci o formatu sadržaja koji se šalje (`Content-Type`) ili formatu koji se očekuje u odgovoru (`Accept`). Ispravno postavljena zaglavlja osiguravaju da poslužitelj može provjeriti identitet pozivatelja i ispravno protumačiti podatke koje prima.

Naposljetku, mnogi pozivi, osobito oni koji koriste metode POST i PUT, sadrže i tijelo zahtjeva (engl. *body* ili *payload*). U tijelu zahtjeva smješteni su konkretni podaci koji se šalju na poslužitelj, najčešće oblikovani u JSON (*JavaScript Object Notation*) formatu. Primjerice, prilikom stvaranja novoga korisnika, tijelo zahtjeva sadržavalo bi podatke poput imena, prezimena i adrese e-pošte. Uz tijelo, podaci se mogu prenositi i putem parametara koji su dio samog URL-a. *Query* parametri (npr. `?sort=asc&limit=10`) koriste se za filtriranje, sortiranje ili paginaciju rezultata, dok *path* parametri služe za identifikaciju specifičnog resursa unutar putanje (npr. `id` korisnika u putanji `/korisnici/{id}`).

Svi ti dijelovi zajedno tvore cjelovit i nedvosmislen zahtjev koji API poslužitelj može obraditi, omogućujući tako agentu da izvršava složene zadatke u interakciji s vanjskim digitalnim sustavima.


Struktura API poziva od agenta prema poslužitelju, koja se sastoji od HTTP metode, URL-a, zaglavlja i tijela

## 6.3	Anatomija modernoga komunikacijskog partnera

Moderni komunikacijski partner, u svojoj biti, predstavlja složenog agenta čija se funkcionalnost ne iscrpljuje u jednostavnoj razmjeni informacija. Njegova se struktura i sposobnosti mogu raščlaniti na nekoliko ključnih, međusobno povezanih sastavnica koje zajedno tvore cjelovito i učinkovito komunikacijsko biće. Razumijevanje tih sastavnica nužno je za shvaćanje njegove uloge u suvremenom digitalnom okružju.

Dubinska personalizacija i kontekstualno pamćenje

Jedno od temeljnih obilježja ovog agenta jest njegova sposobnost dubinske personalizacije.

> **Personalizacija:** Prilagodavanje sadržaja, tona i ponašanja sustava individualnim potrebama, povijesti interakcija i preferencijama korisnika; ključna za angažman i percipiranu korisnost komunikacijskih agenata.

Ona se ne očituje isključivo u prepoznavanju korisnika, već u dinamičkom prilagođavanju komunikacije njegovim specifičnim potrebama, prethodnim interakcijama i iskazanim preferencijama. Svaki se razgovor oblikuje kao jedinstven dijalog, čime se postiže visoka razina korisničkog angažmana i gradi osjećaj individualnog pristupa.

Na sposobnost personalizacije izravno se nadovezuje zahtjev za postojanim kontekstualnim razumijevanjem. Moderni agent mora posjedovati svojevrsno 'pamćenje' koje nadilazi puko zadržavanje posljednje razmijenjene poruke. Njegova je zadaća integrirati cjelokupnu povijest interakcija s korisnikom u jedinstvenu i koherentnu sliku. Time se komunikaciji pridaje dijakronijska dimenzija, omogućujući agentu da tumači nove upite u svjetlu prethodnih saznanja i tako izbjegne ponavljanja i nesporazume.

Afektivna usklađenost i proaktivno djelovanje

Komunikacija sadrži i izraženu afektivnu komponentu. Stoga se anatomija modernog agenta upotpunjuje sposobnošću prepoznavanja i adekvatnog odgovaranja na emocionalno stanje korisnika.

> **Emocionalna inteligencija:** Sposobnost prepoznavanja, tumačenja i primjerenog odgovaranja na emocionalna stanja drugih; kod agenata uključuje analizu tona, jezičnih odabira i konteksta kako bi se postigla empatična i usklađena komunikacija.

Analizom jezičnih odabira, tona ili čak brzine tipkanja, agent može razlučiti osjećaje poput frustracije, zadovoljstva ili zbunjenosti. U skladu s prepoznatim stanjem, on prilagođava vlastiti ton i stil izražavanja, težeći postizanju emocionalne usklađenosti koja je ključna za izgradnju povjerenja.

Nadalje, pasivnu reaktivnu ulogu čekanja na korisnički upit moderni komunikacijski partnera zamjenjuje proaktivnim pristupom. Na temelju konteksta i analize korisničkog ponašanja, agent je u stanju anticipirati buduće potrebe, nuditi relevantne informacije, postavljati sugestivna pitanja ili predlagati sljedeće korake. Takvo anticipativno djelovanje pretvara agenta iz pukog izvršitelja u istinskog partnera u rješavanju problema i postizanju ciljeva (Jones & Lee, 2022).

Višekanalna dosljednost i operativna integracija

Sve navedene sposobnosti moraju biti dosljedno primijenjene neovisno o komunikacijskom kanalu. To načelo višekanalne  dosljednosti (engl. *omnichannel consistency*) podrazumijeva da agent pruža jednako kvalitetno i koherentno iskustvo bilo da se interakcija odvija putem mrežne stranice, mobilne aplikacije, društvenih mreža ili drugog sučelja. Korisnik mora imati osjećaj da nastavlja isti razgovor s istim sugovornikom, bez obzira na platformu koju u danom trenutku koristi.

Naposljetku, okosnicu anatomije modernog agenta čini njegova duboka tehnička integracija s pozadinskim sustavima. Bez sposobnosti povezivanja sa sustavima za upravljanje odnosima s klijentima (CRM), bazama podataka,

> **CRM:** Sustav za upravljanje odnosima s klijentima (engl. *Customer Relationship Management*) – softverska platforma koja centralizira podatke o kupcima, interakcijama i poslovnim procesima; omogućuje agentima provjeru narudžbi, ažuriranje profila i pokretanje poslovnih radnji.

Inventarom ili drugim poslovnim aplikacijama, agent bi ostao ograničen na pružanje općenitih informacija. Upravo mu integracija omogućuje izvršavanje konkretnih radnji – od provjere statusa narudžbe i ažuriranja korisničkih podataka do pokretanja složenijih poslovnih procesa. Time on postaje stvarni operativni produžetak digitalnog ekosustava.

 

Shematski prikaz ključnih sastavnica modernoga komunikacijskog agenta. Tehnička integracija i kontekstualno razumijevanje predstavljaju temelj na kojem se razvijaju napredne sposobnosti personalizacije, empatije i proaktivnosti, dok višekanalna dosljednost osigurava koherentno korisničko iskustvo

![Shematski prikaz ključnih sastavnica modernoga komunikacijskog agenta. Tehnič...](../../docs/diagrams/diag_24.svg)
*Slika 6.1: Shematski prikaz ključnih sastavnica modernoga komunikacijskog agenta. Tehnič...*

### 6.3.1 Mozak operacije: jezgra LLM-a i umijeće upravljanja

U samome središtu svakoga autonomnog agenta, kao njegovo neuralno i kognitivno sjedište, nalazi se veliki jezični model (LLM). On predstavlja njegovu temeljnu jezgru – motor koji pokreće procese rasuđivanja, planiranja i odlučivanja. Funkcija LLM-a unutar arhitekture agenta nadilazi puko procesiranje jezika; on djeluje kao središnja jedinica za obradu složenih problema, pretvarajući apstraktne ciljeve u konkretne, provedive korake. Upravo u toj sposobnosti leži prijelaz s tradicionalnih programa, koji slijede strogo definirane upute, na sustave koji posjeduju zametak autonomije.

Temeljna zadaća koja se pred LLM postavlja jest dekompozicija. Kada se agent suoči sa složenim zadatkom, poput organizacije putovanja ili analize tržišnih podataka, LLM preuzima ulogu stratega. On razlaže krajnji cilj na niz logičkih, manjih podzadataka, stvarajući tako kauzalni lanac akcija. Primjerice, zahtjev za „istraživanjem najnovijih trendova u umjetnoj inteligenciji“ model će rastaviti na korake: prvo, definiranje ključnih pojmova; drugo, pretraživanje relevantnih znanstvenih baza i repozitorija; treće, sažimanje i sintetiziranje prikupljenih informacija; i četvrto, oblikovanje konačnog izvještaja. Takvo hijerarhijsko planiranje, koje oponaša ljudske kognitivne procese, omogućuje agentu sustavan i metodičan pristup rješavanju problema (Yao et al., 2023).

> **Dekompozicija zadatka:** Proces razbijanja složenog cilja na niz manjih, logički povezanih podzadataka koji se mogu izvršavati sekvencijalno ili paralelno; u kontekstu autonomnih agenata, dekompoziciju provodi jezgra LLM-a koja djeluje kao strateg, pretvarajući apstraktan zahtjev u kauzalni lanac konkretnih akcija (Yao et al., 2023).

Međutim, sirova snaga jezičnoga modela ostaje neiskorišteni potencijal bez umijeća upravljanja, odnosno bez vješto oblikovanih upita (engl. *prompts*). Upit predstavlja temelj za strukturirani dijalog između čovjeka i stroja. Kvaliteta, preciznost i kontekstualno bogatstvo početnog upita izravno određuju dubinu i točnost *razmišljanja* modela. Loše postavljen ili dvoznačan upit može odvesti agenta u pogrešnom smjeru, rezultirajući suboptimalnim ili potpuno netočnim rješenjima. S druge strane, dobro oblikovan upit djeluje kao precizan instrument kojim se usmjerava kognitivni fokus modela, potičući ga na aktivaciju relevantnih znanja i primjenu složenijih obrazaca zaključivanja.


#### Vještina oblikovanja uputa

Prije no što se umjetnointeligentnom djelatniku povjere alati ili pristup vanjskoj spoznajnoj baštini, neophodno je ovladati vještinom sporazumijevanja s njegovom jezgrom. Ta vještina, danas poznata kao **oblikovanje** uputa (engl. *prompt engineering*), obuhvaća umijeće preciznoga sastavljanja ulaznih naloga, odnosno *uputa* (engl. *prompts*), kako bi se iz golemoga mogućnosnog prostora jezičnoga modela izlučio točno određen odgovor, očitovalo željeno ponašanje ili usvojio zadani stil. Ona proizlazi iz same naravi velikih jezičnih modela kao profinjenih statističkih strojeva za predviđanje sljedećega jezičnog znaka (tokena); ulazna uputa postavlja početne uvjete toga stohastičkog procesa i time presudno usmjeruje putanju njegova zaključivanja i izričaja (Liu i dr., 2023a).

> **Oblikovanje uputa / prompt engineering:** Umijeće oblikovanja ulaznih uputa (prompta) kako bi se iz jezičnog modela izvukao željeni odgovor ili ponašanje; uključuje preciznost formulacije, dodjelu uloge modelu, primjere (few-shot), lanac misli (chain-of-thought) i sustavnu uputu (system prompt).

Ovladavanje umijećem oblikovanja uputa počiva na primjeni nekoliko temeljnih načela.

**Točnost i semantičko usidrenje.** Veliki jezični modeli u svome djelovanju nalikuju na iznimno obrazovane, ali doslovne i ustrajne pomoćnike. Dvosmisleni ili preopćeniti nalozi neizbježno vode do nepoželjnih ili odveć općenitih odgovora. Primjerice, nalog „Napiši nešto o održivosti“ potaknut će model da proizvede uopćen, gotovo nasumičan tekst koji dotiče sve od ekologije do gospodarstva bez prave dubine. Nasuprot tomu, precizno sročen nalog djeluje kao semantičko sidro koje model usmjerava prema željenom ishodu: „Sastavi članak od 500 riječi za poslovni blog o važnosti smanjenja plastičnog otpada za male poduzetnike u ugostiteljstvu. U tekstu se usredotoči na tri praktična i isplativa savjeta. Ciljana publika su vlasnici restorana koji nisu stručnjaci za zaštitu okoliša. Ton treba biti poticajan, jasan i informativan.“ Takva uputa ne ostavlja prostora dvosmislenosti i jasno određuje sadržaj, strukturu, ton i ciljanu publiku.


**Pridavanje uloge i osobe** (engl. *role-playing*). Jedna je od najmoćnijih tehnika naložiti modelu da preuzme određenu ulogu ili osobu (lat. *persona*). Time se u njegovoj golemoj neuronskoj mreži pobuđuju oni jezični obrasci, rječnik i stilski registri koji su u podacima za učenje bili povezani s tom ulogom. Uputa „Djeluj kao vodeći stručnjak za kibernetičku sigurnost s dvadesetogodišnjim iskustvom. Objasni laiku pet najčešćih prijetnji digitalnoj sigurnosti u kućanstvu.“ urodit će odgovorom koji je istodobno stručan, autoritativan i razumljiv. Ta je tehnika od presudne važnosti za davanje postojane i dosljedne osobnosti djelatniku, čime on postaje predvidljiv i pouzdan komunikacijski sudionik.


**Pružanje konteksta i primjera** (engl. *few-shot prompting*). Kao što su to prvi pokazali tvorci modela GPT-3 (Brown i dr., 2020), veliki jezični modeli posjeduju izvanrednu sposobnost učenja iz primjera koji su im predočeni unutar same upute. Umjesto pukog opisivanja zadatka, pružanje nekoliko konkretnih primjera (engl. *shots*) omogućuje modelu da apstrahira traženi obrazac i primijeni ga na novi slučaj. Taj se postupak može slikovito prikazati na zadatku razvrstavanja osjećaja (sentimenta) u tekstu.


> **Shema 1:** Primjer upute s nekoliko primjera (*Few-shot Prompting*)
>
> Klasificiraj osjećaj u sljedećoj rečenici kao 'Pozitivan', 'Negativan' ili 'Neutralan'.
>
> **Rečenica:** “Usluga je bila izvanredna, a hrana ukusna.“ **Osjećaj:** Pozitivan
>
> **Rečenica:** “Čekali smo predugo, a račun je bio pogrešan.“ **Osjećaj:** Negativan
>
> **Rečenica:** “Sastanak je zakazan za srijedu u 10 sati.“ **Osjećaj:** Neutralan
>
> **Rečenica:** “Novi film me posve razočarao.“ **Osjećaj:**

Nakon što mu se predoče prva tri primjera, model s daleko većom pouzdanošću zaključuje da je ispravan odgovor za posljednju rečenicu „Negativan“.

> **Učenje iz primjera / few-shot prompting:** Tehnika upravljanja jezicnim modelom u kojoj se unutar same upute navodi nekoliko konkretnih primjera (šotova) željenog ulazno-izlaznog obrasca, čime se model navodi da apstrahira traženi uzorak i primijeni ga na novi, nepoznati slučaj; suprotnost je nulti pristup (zero-shot), gdje se primjeri ne navode (Brown et al., 2020).


**Lanac misli (engl. *Chain-of-Thought*, CoT ).** Za složene zadatke koji zahtijevaju logičko ili aritmetičko zaključivanje, veliki jezični modeli postižu znatno bolje rezultate ako ih se izričito potakne da problem raščlane na sastavne korake. Dodavanjem jednostavne fraze poput „Razmislimo korak po korak.“ na kraj upute, model se prisiljava da svoj proces zaključivanja učini vidljivim, ispisujući ga kao tekst. Time se slijedi logičniji put, smanjuje vjerojatnost pogreške i omogućuje provjera ispravnosti postupka (Wei i dr., 2022). Naprednije tehnike, poput ReAct (Yao i dr., 2023), združuju takvo postupno promišljanje s uporabom vanjskih alata, što čini okosnicu mnogih suvremenih djelatničkih arhitektura.

> **Lanac misli / Chain-of-Thought, CoT:** Tehnika upravljanja jezicnim modelom kojom se model izričito potiče da problem razbije na vidljive međukorake zaključivanja prije konačnog odgovora; time se povećava točnost kod složenih logičkih i aritmetičkih zadataka te se omogućuje provjera ispravnosti postupka (Wei et al., 2022).


> **Shema 2: Usporedba standardne upute i upute s lancem misli ULAZ (Standardna uputa):** Pitanje: U kafeteriji su bile 23 jabuke. Ako su za ručak iskoristili 20, a zatim kupili još 6, koliko jabuka sada imaju?
>
> **IZLAZ (Vjerojatno pogrešan):** 29
>
>
> **ULAZ (Uputa s lancem misli):** Pitanje: U kafeteriji su bile 23 jabuke. Ako su za ručak iskoristili 20, a zatim kupili još 6, koliko jabuka sada imaju? Razmislimo korak po korak.
>
> **IZLAZ (Vjerojatno ispravan):** Naravno, razmislimo korak po korak.
>
> Početni broj jabuka je 23.
>
> Iskoristili su 20 jabuka, pa radimo oduzimanje: 23 - 20 = 3.
>
> Nakon ručka ostale su 3 jabuke.
>
> Zatim su kupili još 6 jabuka, pa radimo zbrajanje: 3 + 6 = 9. Kafeterija sada ima 9 jabuka.


**Sustavna uputa** (engl. *system prompt*) zauzima posebno mjesto u upravljanju modelom. Riječ je o nadređenoj instrukciji koja se postavlja na samom početku međudjelovanja i koja određuje općenito ponašanje, osobnost, ovlasti i ograničenja modela tijekom čitavoga razgovora. Ona djeluje kao svojevrstan „ustav“ za umjetnu inteligenciju, skup nepromjenjivih pravila kojih se djelatnik mora pridržavati.

Primjerice, sustavna uputa za specijaliziranog pomoćnika za analizu računalnoga koda mogla bi glasiti: „Ti si sigurnosni analitičar. Tvoja je isključiva svrha analizirati priloženi programski kôd na moguće sigurnosne ranjivosti prema popisu OWASP Top 10. Ne odgovaraj na pitanja koja nisu vezana uz sigurnost koda. Ne iznosi osobna mišljenja. Svoje odgovore uvijek oblikuj kao JSON objekt s poljima 'vrsta_ranjivosti', 'broj_linije' i 'preporuka'.“

Dobro oblikovana sustavna uputa ključna je za stvaranje postojanog i pouzdanog djelatnika koji se ponaša unutar željenih i strogo određenih granica (Anthropic, 2024; OpenAI, 2024b). Ona je temelj sigurnosti i predvidljivosti, pretvarajući moćnu, ali nestalnu jezičnu jezgru u specijaliziran alat s jasno definiranom svrhom.

> **Sustavna uputa / system prompt:** Nadređena instrukcija postavljena na početku interakcije s jezicnim modelom koja određuje njegovo općenito ponašanje, osobnost, ovlasti i ograničenja tijekom cijeloga razgovora; djeluje kao „ustav“ agenta, skup nepromjenjivih pravila koja osiguravaju predvidljivost, sigurnost i dosljednost u odgovorima (Anthropic, 2024; OpenAI, 2024b).


Umijeće oblikovanja upita zahtijeva od korisnika ili programera duboko razumijevanje domene problema te načina na koji LLM „razmišlja“. Potrebno je predvidjeti moguće interpretacije, ukloniti dvosmislenosti i pružiti modelu dovoljno konteksta kako bi mogao donijeti informiranu odluku. U tom smislu interakcija s agentom je iterativni proces usklađivanja i pročišćavanja, gdje se kroz niz upita i odgovora postupno kristalizira optimalno rješenje.




#### Od alata do kognitivnog partnera

Kroz ovakvu sinergiju inherentnih sposobnosti modela i vještine ljudskog upravljanja, LLM unutar agenta prestaje biti pasivan alat i preobražava se u aktivnog kognitivnog partnera. Dok tradicionalni softverski alati izvršavaju precizno definirane funkcije, agent vođen LLM-om sudjeluje u samom procesu definiranja rješenja. On ne čeka na potpunu specifikaciju svakog koraka, već na temelju općeg cilja samostalno predlaže, analizira i odabire putove djelovanja.

Djelotvornost autonomnog agenta, dakle, počiva na dvama stupovima: s jedne strane, na snazi i sofisticiranosti jezičnoga modela koji čini njegovu jezgru, a s druge, na umijeću kojim čovjek usmjerava tu snagu. Razumijevanje ove dvojake prirode – moćnog stroja i potrebe za njegovim finim ugađanjem – predstavlja ključ za otključavanje punog potencijala autonomnih sustava i njihovu uspješnu primjenu u rješavanju izazova suvremenog svijeta. Ovladavanje tim „mozgom operacije“ je stoga strateški imperativ.

### 6.3.2 Ustrojstvo pamćenja u konverzacijskih sustava

Sposobnost pamćenja predstavlja temeljnu odrednicu djelotvornosti i prirodnosti konverzacijskih sustava. Pamćenje u ovome kontekstu nadilazi pohranjivanje podataka; ono je složen mehanizam koji agentu omogućuje praćenje tijeka razgovora, razumijevanje konteksta i pružanje suvislih i relevantnih odgovora. Bez djelotvornog pamćenja, svaka bi interakcija s korisnikom bila svedena na niz nepovezanih upita i odgovora, čime bi se izgubila sama srž konverzacije. Stoga se ustrojstvo pamćenja u suvremenim konverzacijskim agentima najčešće razlaže na nekoliko razina.


#### Protok informacija od senzornog, preko kratkoročnog, do dugoročnog pamćenja


#### Kratkoročna memorija – kontekst

Relevantne se informacije prenose u kratkoročno pamćenje, koje se u literaturi često naziva i *radnim pamćenjem* (engl. *working memory*). U njemu se čuvaju svi kontekstualni podaci nužni za održavanje koherencije unutar jedne konverzacijske sesije. To uključuje posljednje korisnikove izjave, agentove odgovore, prepoznate namjere i entitete te sve druge elemente koji omogućuju smislen nastavak dijaloga. Svojom funkcijom i ograničenjima, ono je usporedivo s radnom memorijom (RAM) u računalu: posjeduje ograničen kapacitet i njegov se sadržaj briše po završetku interakcije ili nakon određenoga razdoblja neaktivnosti.

> **Radno pamćenje / working memory:** Kratkoročno spremničko područje konverzacijskog agenta u kojem se čuvaju kontekstualni podaci tekuće sesije – korisnikove izjave, agentovi odgovori, prepoznate namjere i entiteti; funkcionalno je usporedivo s radnom memorijom (RAM) računala jer posjeduje ograničen kapacitet i briše se po završetku interakcije.


Neposredni kontinuitet kratkoročnoga pamćenja unutar jedne razgovorne sesije sa jezičnim modelima ostvaruje se mehanizmom kontekstualnog prozora (engl. *context window*). Njegova se provedba u praksi najčešće svodi na sustavno uključivanje cjelokupne povijesti tekućega razgovora u svaki novi poziv upućen modelu.

> **Kontekstualni prozor / context window:** Maksimalna količina teksta (u tokenima) koju jezični model može istodobno primiti i obraditi u jednom pozivu; sve što je unutar prozora čini kontekst za generiranje odgovora; prekoračenje zahtijeva odbacivanje starijih dijelova razgovora. Pri svakom novom korisnikovu upitu, sustav ne šalje modelu samo taj upit, već mu prilaže i cjelokupan transkript dotadašnje interakcije. Time se model stavlja u širi kontekst, omogućujući mu da referira na ranije izrečene tvrdnje, postavlja suvisla potpitanja i održava dosljednost u tonu i sadržaju.


Međutim, ovaj pristup nailazi na tvrdu granicu koju postavlja arhitektura samoga modela – veličina njegova kontekstualnog prozora, maksimalnu količinu teksta (mjerenu u tokenima) koju model može istodobno obraditi. Jednom kada duljina razgovora premaši taj prag, najstariji dijelovi interakcije moraju se odbaciti. Taj trenutak predstavlja točku prekida, svojevrsnu konverzacijsku amneziju, nakon koje model gubi sjećanje na početak razgovora, što može dovesti do ponavljanja ili proturječnih odgovora. Učinkovitost ovog mehanizma stoga opada s produljenjem razgovora, čineći ga neprikladnim za sve osim za kratkotrajne, jednokratne interakcije.


> **Shema: Mehanizam i ograničenje kratkoročnog pamćenja**
>
>
> KORAK 1:
>
> Korisnik: „Dobar dan, zanima me povijest dubrovačke književnosti.“
>
> Agent → LLM Prompt: „Korisnik: Dobar dan, zanima me povijest dubrovačke književnosti.“
>
>
> KORAK 2:
>
> Agentov odgovor: „Naravno. Mislite li na razdoblje humanizma i renesanse ili Vas zanima kasnije razdoblje?“
>
> Korisnik: „Fokusirajmo se na renesansu.“
>
> Agent → LLM Prompt: „Korisnik: Dobar dan, zanima me povijest dubrovačke književnosti. / Agent: Naravno. Mislite li na razdoblje humanizma i renesanse ili Vas zanima kasnije razdoblje? / Korisnik: Fokusirajmo se na renesansu."
>
>
> KORAK N (Razgovor se nastavlja...):
>
> ...kontekst se akumulira...
>
>
> KORAK N+1 (Dosegnut limit kontekstualnog prozora):
>
> [Najstariji dio razgovora („Dobar dan...“) se odbacuje]
>
> Agent → LLM Prompt: „...[središnji dio razgovora]... / Korisnik: A tko je bio najznačajniji komediograf?"
>
>
> │ OGRANIČENJE: Model više ne „zna“ početnu temu razgovora. │



#### Dugoročna memorija – vektorske baze

Za istinsku postojanost i pamćenje informacija kroz dulje vremensko razdoblje i preko više razgovornih sesija, agenti se moraju osloniti na vanjske sustave za pohranu podataka. U suvremenim arhitekturama tu ulogu najčešće preuzimaju vektorske baze podataka (engl. *vector databases*). One omogućuju sustavu da stvori i održava trajni zapis o ključnim informacijama, preferencijama i činjenicama vezanim uz korisnika, tvoreći tako temelj za njegov dijakronijski identitet unutar sustava. Proces uspostave i korištenja dugoročnog pamćenja može se raščlaniti na tri ključna koraka.

> **Vektorska baza podataka / vector database:** Specijalizirani sustav za pohranu koji podatke predstavlja kao numeričke vektore (ugradbe) u višedimenzionalnom prostoru te omogućuje brzo pretraživanje po semantičkoj sličnosti, a ne po ključnim riječima; u arhitekturi konverzacijskih agenata služi kao dugoročno pamćenje koje čuva korisničke preferencije, činjenice i sažetke prethodnih interakcija kroz više sesija (Xu i sur., 2023).


**1.** Sažimanje i ekstrakcija činjenica: Sustav ne pohranjuje sirovi transkript svakog razgovora, jer bi to bilo nepregledno i računalno zahtjevno. Umjesto toga, agent periodički, bilo nakon svake interakcije ili na kraju sesije, analizira razgovor s ciljem ekstrakcije i sažimanja ključnih informacija. To mogu biti eksplicitno navedene činjenice (npr. „Korisnik se zove Ivan“, „Ivanov sin studira medicinu u Zagrebu“), ali i implicitno izražene preferencije (npr. „Korisnik preferira sažete odgovore“, „Korisnika zanima antička filozofija, posebice stoicizam“).


**2.** Vektorizacija i pohrana: Izdvojene činjenice i sažeci pretvaraju se iz tekstualnog oblika u numeričke reprezentacije, takozvane vektorske  ugrađenice ili ugradbe (engl. *embeddings*). Svaka ugradba jest vektor, odnosno niz brojeva koji predstavlja položaj dane informacije u višedimenzionalnom semantičkom prostoru. Taj se vektor može shvatiti kao jedinstveni „semantički otisak“ informacije. Tako pretvoreni podaci pohranjuju se u vektorsku bazu, gdje svaki vektor ostaje trajno zapisan i povezan s identitetom korisnika.

> **Vektorska ugradba / embedding:** Numerička reprezentacija teksta, riječi, rečenice ili dokumenta u obliku niza brojeva (vektora) smještenog u višedimenzionalnom semantičkom prostoru; semantički slični sadržaji imaju bliske vektore, što omogućuje pretraživanje po značenju umjesto po točnom podudaranju riječi.


**3.** Dohvat i obogaćivanje konteksta: Prije no što će obraditi novi korisnikov upit, agent prvo pretražuje vektorsku bazu. Pretraga se ne vrši po ključnim riječima, već po semantičkoj sličnosti. Agent pretvara trenutačni korisnikov upit u vektor i potom u bazi traži pohranjene vektore (sjećanja) koji su mu u semantičkom prostoru najbliži. Primjerice, ako korisnik pita „Možeš li mi preporučiti neku novu knjigu na tragu onih o kojima smo ranije razgovarali?“, agent će prepoznati semantičku bliskost tog upita s pohranjenom činjenicom „Korisnika zanima antička filozofija, posebice stoicizam“. Najrelevantniji pronađeni zapisi dohvaćaju se iz baze i umeću u kontekstualni prozor zajedno s novim upitom. Na taj način, jezični model dobiva ključne informacije iz „dugoročnog sjećanja“ koje su mu potrebne za generiranje relevantnog i personaliziranog odgovora (Xu i sur., 2023).


Ovaj složeni mehanizam omogućuje agentu da nadiđe svoju urođenu ahistorijsku prirodu. Nadišavši status jezičnog automata koji reagira na trenutni podražaj, postaje sugovornik koji „pamti“ zajedničku povijest interakcija, uvažava korisnikove specifičnosti i time stvara podlogu za kontinuiran, dosljedan i u konačnici smisleniji odnos.


### 6.3.3 Epistemičko utemeljenje: dohvaćanjem obogaćeno generiranje (RAG)

Pristup dohvaćanjem obogaćenog generiranja (engl. *Retrieval-Augmented Generation*, RAG) predstavlja značajnu paradigmu u području umjetne inteligencije, osmišljenu radi epistemičkoga utemeljenja odgovora koje stvaraju veliki jezični modeli (LLM). Riječ je o hibridnom sustavu koji sjedinjuje dvije temeljne sastavnice: mehanizam za dohvaćanje podataka (engl. *retriever*) i generativni jezični model (engl. *generator*). Cilj je takva sustava nadići ograničenja samostalnih jezičnih modela spajanjem njihove sposobnosti jezičnog oblikovanja s pouzdanošću i ažurnošću vanjskih baza znanja.

> **RAG:** Dohvaćanjem obogaćeno generiranje (engl. *Retrieval-Augmented Generation*) – hibridni sustav koji za odgovor na korisnički upit prvo dohvaća relevantne dijelove iz vanjske baze znanja (retriever), zatim te podatke i upit prosljeđuje jezičnom modelu (generator) koji sintetizira konačni odgovor; time se poboljšava ažurnost i utemeljenost odgovora.

Potreba za ovakvim pristupom proizlazi iz dvaju temeljnih nedostataka samostalnih velikih jezičnih modela. Prvi je nedostatak sklonost „haluciniranju“, odnosno generiranju činjenično netočnih ili potpuno izmišljenih informacija, što se događa kada model ne posjeduje traženu informaciju u svojim internim parametrima. Drugi je ključni nedostatak statičnost njihove baze znanja, koja je ograničena na podatke na kojima su uvježbani i stoga ne obuhvaća događaje ili spoznaje nastale nakon završetka njihova uvježbavanja.

Sâm proces rada RAG sustava može se raščlaniti na nekoliko ključnih koraka. Ciklus započinje korisničkim upitom. Taj se upit potom prosljeđuje komponenti za dohvaćanje (engl. *retriever*), čija je zadaća pretražiti vanjsku bazu znanja – primjerice, zbirku dokumenata, bazu podataka ili internetske izvore – kako bi pronašao najrelevantnije dijelove teksta ili podatke koji se odnose na postavljeni upit. Ti pronađeni, relevantni podaci zajedno s izvornim korisničkim upitom tvore obogaćeni kontekst koji se prosljeđuje generativnomu jezičnom modelu. U završnoj fazi, jezični model (generator) sintetizira konačni odgovor, temeljeći ga na dobivenim relevantnim podacima, a ne isključivo na svojemu internom, parametarskom znanju.

 

Shematski prikaz rada RAG sustava


![Shematski prikaz rada RAG sustava](../../docs/diagrams/diag_25.svg)
*Slika 6.2: Shematski prikaz rada RAG sustava*

Primjena RAG arhitekture donosi višestruke prednosti. Najvažnija je znatno smanjenje pojave halucinacija jer se model pri generiranju odgovora izravno oslanja na konkretne, dohvaćene podatke. Nadalje, RAG omogućuje modelima pristup ažuriranim ili specifičnim, domeni prilagođenim informacijama bez potrebe za skupim i dugotrajnim ponovnim uvježbavanjem cijeloga modela. Time se otvara i mogućnost transparentnosti i provjerljivosti; uz generirani odgovor, korisniku se mogu ponuditi i izvori iz kojih su informacije preuzete, što mu dopušta da sâm provjeri njihovu točnost. Ovaj je pristup ujedno i ekonomičniji jer je ažuriranje vanjske baze znanja znatno jednostavnije i jeftinije od ponovnog uvježbavanja cjelokupnoga jezičnog modela (Lewis et al., 2020).

U kontekstu složenijih sustava, poput autonomnih agenata, RAG preuzima ulogu ključnog alata za utemeljeno djelovanje. Kada se agent suoči sa zadatkom koji zahtijeva pouzdane i aktualne informacije, on ne djeluje ishitreno, već se oslanja na RAG mehanizam kako bi prikupio relevantne spoznaje prije donošenja odluke ili formuliranja odgovora. Time se osigurava da djelovanje agenta – bilo da je riječ o odgovaranju na upit korisnika u službi za podršku ili o prikupljanju podataka za složeniju analizu – nije zasnovano na potencijalno zastarjelim ili netočnim internim spoznajama, već na provjerljivim vanjskim izvorima.

Treba naglasiti da iako je temeljni koncept arhitekture RAG iznimno moćan, njegova naivna ili pojednostavljena primjena često se pokazuje nedostatnom za složenije probleme. Stoga je razvijen čitav spektar naprednih tehnika koje optimiziraju svaki stupanj opisanog procesa. To područje danas predstavlja jedno od najdinamičnijih polja istraživanja u razvoju umjetne inteligencije (Gao i sur., 2024; Barnett i sur., 2024). Istražuju se napredne metode indeksiranja i pretraživanja, tehnike inteligentnog razvrstavanja (rerangiranja) dohvaćenih dokumenata po važnosti, kao i strategije sažimanja i sinteze informacija iz više različitih izvora.


### 6.3.4	Ruke za djelovanje: služenje alatima kao iskorak u moći

> **Korištenje alata / Tool Use:** Sposobnost AI agenta da poziva vanjske alate (API-e, pretraživač, kalkulator, baze podataka) tijekom izvršavanja zadatka; model odlučuje kada i koji alat pozvati, prosljeđuje parametre i koristi rezultat za nastavak rasuđivanja; ključna komponenta agentskih arhitektura (npr. ReAct).

Ljudska ruka, promatrana u svojoj anatomskoj i funkcionalnoj složenosti, nadilazi ulogu organa za hvatanje te se potvrđuje kao prvenstveno oruđe djelovanja. Njezina sposobnost fine motoričke prilagodbe, precizne manipulacije i čvrstoga stiska predstavlja temeljni preduvjet za jedan od najvažnijih prijelaza u čovjekovu razvoju: svjesnu uporabu oruđa. Tim činom čovjek postaje biće koje je aktivno oblikuje, prilagođava i nadilazi. Služenje oruđem stoga predstavlja korjenitu promjenu u odnosu čovjeka i svijeta, istinski iskorak u moći koji otvara put prema izgradnji kulture i tehnologije.

Taj se preobražaj duboko zahvaća i samu strukturu ljudske percepcije. Filozofska fenomenologija ponudila je pronicave uvide u prirodu tog procesa. Martin Heidegger uvodi razlikovanje između oruđa kao nečega što je *spremno-za-ruku* (njem. *Zuhandenheit*) i predmeta kao nečega naprosto *prisutnog* (njem. *Vorhandenheit*). Kada se vješto služimo čekićem, on za našu svijest ne postoji kao zaseban objekt s određenim svojstvima, već se povlači u pozadinu i postaje neprimjetan produžetak naše ruke usmjerene na čin zabijanja čavla. Oruđe, stopljeno s djelovanjem, postaje prozirno i otvara nam svijet ne kao skup predmeta za promatranje, već kao polje mogućnosti za djelovanje.

Na tom tragu, Maurice Merleau-Ponty (1962) dalje razvija misao o utjelovljenju oruđa, tvrdeći kako ga tijelo uključuje u vlastitu tjelesnu shemu. Klasičan primjer slijepčeva štapa zorno prikazuje taj fenomen: štap je za slijepca produžetak njegova osjetilnog aparata kojim on *osjeća* i istražuje prostor pred sobom. Vrh štapa postaje nova granica njegova tijela. Na taj se način oruđe preobražava iz vanjskog predmeta u sastavni dio čovjekova perceptivnog i djelatnog polja.


Shema proširenja djelovanja usvajanjem alata. Agent integrira oruđe u svoju tjelesnu shemu, čime se njegovo polje djelovanja proširuje i omogućuje složeniji utjecaj na svijet, uz istodobno primanje obogaćene povratne sprege

Kroz taj proces stapanja tijela i alata čovjek se preoblikuje u bitno moćnijeg *agenta*. Njegov odnos sa svijetom više nije određen isključivo biološkim granicama njegova tijela. Sjekira proširuje snagu i doseg ruke, koplje omogućuje lov na daljinu, a pismo nadilazi prolaznost govora i pamćenja. Svako novo oruđe otvara nove načine bivanja u svijetu i djelovanja na njega. Ta temeljna sposobnost služenja oruđima stoga se nalazi u samom ishodištu ljudske povijesti kao povijesti stvaranja, preoblikovanja i nadilaženja zadanoga, potvrđujući čovjeka kao biće koje svoj svijet neprestano iznova gradi.

Za jezične modele upravo uporaba alata razbija te stege, omogućujući mu da posegne izvan sebe i stupi u vezu sa živim, promjenjivim sustavima. Utemeljenje te sposobnosti počiva na kružnom procesu promišljanja i djelovanja, najjasnije oprimjerenom u okvirima poput ReActa (engl. *Reasoning and Acting*). U tome ciklusu jezični uzorak tvori slijed unutarnjih promišljanja (*misli*) i vanjskih zahvata (*akcija*) koji ga postupno vode k rješenju (Yao i dr., 2023). Taj se proces odvija u petlji koja se po potrebi može i ponavljati:




> **Temeljni krug promišljanja i djelovanja (ReAct)**
>
> **KORISNIKOV NALOG:** „Kakvo će vrijeme biti sutra u Londonu?"
>
> **1. MISAO (Promišljanje):** „Korisnik pita za vrijeme u Londonu. Nemam pristup podacima u stvarnom vremenu. Moram se poslužiti oruđem `vremenska_prognoza_api`."
>
> **2. AKCIJA (Zahvat):** Tvorba poziva alatima: { „tool_name": „vremenska_prognoza_api", „tool_input": { „grad": „London", „datum": „sutra" } }
>
> **3. OPAŽAJ (Povratna informacija):** Vanjski sustav izvršava poziv i vraća ishod: { „temperatura": „15°C", „stanje": „Oblačno" }
>
> **4. MISAO (Sinteza):** „Primio sam opažaj. Temperatura je 15°C i vrijeme je oblačno. Sada posjedujem sve sastavnice za cjelovit odgovor."
>
> **5. KONAČNI ODGOVOR:** „Sutra će u Londonu biti oblačno s temperaturom od 15°C."

![](../../docs/diagrams/diag_149.svg)
*Slika 6.3: Povratna informacija od vanjskog sustava u ciklusu agenta (Tool Use – opažaj).*


Taj krug omogućuje agentu rješavanje različitih zadataka od svakodnevnih upita do visoko specijaliziranih domena. U ulozi osobnoga pomoćnika agent može upravljati kalendarom, slati elektroničku poštu ili nadzirati pametne uređaje u domu. Kao planer putovanja, on može pretraživati letove putem API-a zrakoplovnih tvrtki, uspoređivati cijene, provjeravati dostupnost hotela i naposljetku izvršiti rezervaciju. U području stručne analize, sposoban je izvršavati Pythonove skripte za složenu obradu podataka, slati SQL upite opsežnim bazama podataka ili sažimati sadržaj mrežnih stranica do kojih dolazi u stvarnom vremenu.

Krajnja se očitovanja ove sposobnosti vide u djelovanju na fizički svijet, gdje agentove upute, prevedene u strojni kôd, upravljaju laboratorijskom opremom, industrijskim robotima na proizvodnoj traci ili poljoprivrednim dronovima.


### 6.3.5	Djelatni agent: sklad sposobnosti

Pojam djelatnog agenta (engl. *agent*) u svojoj biti obuhvaća složenu cjelinu čije se djelovanje ne može svesti na puki zbroj njezinih sastavnica. Riječ je o subjektu koji zamjećuje vlastitu okolinu, na nju svrhovito djeluje i iz posljedica tih djelovanja uči, prilagođavajući svoje buduće postupke. Temeljno počelo koje omogućuje takvo djelovanje jest sklad sposobnosti – dinamička i prožimajuća usklađenost više ključnih funkcija koje zajedno tvore jedinstveni sustav. Bez takve usklađenosti, djelatni počinitelj ostaje tek skupom nepovezanih mehanizama, nesposoban za smislenu i prilagodljivu interakciju sa svijetom.

Prva temeljna sposobnost jest zamjedba (percepcija). Ona predstavlja prozor u svijet, kanal kojim počinitelj prikuplja podatke o stanju okoline i o vlastitome položaju unutar nje. Zamjedba je aktivan proces odabiranja, tumačenja i organiziranja osjetilnih informacija kako bi se stvorio suvisao unutarnji prikaz vanjske stvarnosti (Gibson, 1979). Sirovi podaci dobiveni osjetilima tek su polazište koje se mora protumačiti u svjetlu prethodnog znanja i trenutnih ciljeva. Upravo ta interpretativna narav zamjedbe čini je neodvojivom od spoznajnih procesa.

Na zamjedbu se nadovezuje spoznaja (kognicija), koja obuhvaća umne procese rasuđivanja, planiranja, odlučivanja i pamćenja. Unutar ovog okvira, primljene se informacije obrađuju, povezuju s postojećim znanjem i koriste za oblikovanje namjera i strategija djelovanja. Sposobnost stvaranja i vrednovanja različitih mogućih postupaka ključna je za inteligentno ponašanje (Russell & Norvig, 2020). Spoznaja tako preobražava perceptivne podatke u svrhovite planove, tvoreći most između onoga što jest i onoga što bi trebalo učiniti. Ona je središnji mehanizam koji počinitelju omogućuje da nadiđe neposredne reakcije na podražaje i da djeluje promišljeno, s pogledom uprtim u budućnost.

Spoznajom oblikovani planovi ostvaruju se kroz djelovanje (akciju), odnosno kroz sposobnost počinitelja da utječe na okolinu i mijenja je. Djelovanje može poprimiti različite oblike, od jednostavnih motoričkih radnji do složenih komunikacijskih činova. Ono zatvara krug interakcije sa svijetom: svaka akcija uzrokuje promjene u okolini, a te promjene postaju novi predmet zamjedbe. Time se stvara neprekinuta povratna veza, gdje djelovanje ne samo da ostvaruje ciljeve, već i stvara nove informacije koje obogaćuju i mijenjaju unutarnji model svijeta (Powers, 1973).


Petlja interakcije agenta i okoline prikazuje kako zamjedba vodi do spoznaje i djelovanja, koje utječe na okolinu i pruža nove informacije za sljedeću zamjedbu

Naposljetku, cjelokupni sustav prožet je sposobnošću učenja, koja omogućuje trajnu prilagodbu i poboljšanje. Učenje je proces kojim počinitelj mijenja svoje znanje, vještine i strategije na temelju iskustva, odnosno na temelju ishoda vlastitih djelovanja. Bez učenja počinitelj bi bio osuđen na ponavljanje istih pogrešaka, nesposoban prilagoditi se novim i nepredviđenim okolnostima. Sposobnost učenja omogućuje mu da postane otporniji, učinkovitiji i s vremenom sve vještiji u ostvarivanju svojih ciljeva (Sutton & Barto, 2018).

Istinska narav djelatnog počinitelja, međutim, ne očituje se u pojedinačnim sposobnostima, ma koliko one bile razvijene. Njegova se bit krije u njihovu skladu i međuovisnosti. Zamjedba je besciljna bez spoznaje koja bi je osmislila; spoznaja je nemoćna bez djelovanja koje bi njezine naume provelo u djelo; djelovanje je slijepo bez zamjedbe koja bi ga usmjeravala; a čitav je sklop statičan i krut bez učenja koje mu daje prilagodljivost i razvojnu dimenziju. Upravo u tom neprestanom i usklađenom prožimanju zamjedbe, spoznaje, djelovanja i učenja rađa se djelatni subjekt sposoban za smisleno postojanje u složenom i promjenjivom svijetu. 

Programska okružja poput *LangChaina* ili mislećih modela, poput OpenAI-evog o3, Anthropicovog Clauda ili Googleovog Gemini 2.5, s pristupom alatima nude tehničku podlogu i strukturu za upravljanje takvim složenim međuigrama. Da bi se taj sklad sposobnosti učinio bjelodanijim, promotrimo jedan složen primjer. Zamislimo da korisnica, nazovimo je Ana, svojemu osobnom pomagalu postavlja sljedeći zadatak: isplanirati joj samostalno putovanje u Pariz tijekom prvoga vikenda u listopadu. Njezine su sklonosti umjetnost, napose impresionizam, no proračun joj je strogo ograničen na približno 500 eura za troškove zrakoplovne karte i smještaja. Uvjet je također da smještaj bude u središtu grada. Pogledajmo kako bi napredni agent uskladio svoje sposobnosti da bi ispunio takav nalog.


**1.** Stupanj: Promišljanje i snovanje (Um)

Jezična jezgra agenta najprije podvrgava Anin upit dubinskoj raščlambi. Koristeći se svojom sposobnošću promišljanja, nalik na misaone lance (*Chain-of-Thought*), ona razlaže složeni cilj na niz manjih, dohvatljivih i provedivih podzadataka. Taj početni unutarnji monolog temelj je cjelokupne operacije.


> **Shema 1:** Dekompozicija cilja Glavni cilj: Isplanirati vikend-putovanje u Pariz (prvi vikend u listopadu, solo, umjetnost/impresionizam, budžet ~500 €, centralni smještaj).
>
> **Misaoni slijed (unutarnja razgradnja):** Odrediti točne datume: Utvrditi koji su dani „prvi vikend u listopadu“.
>
> **Provjeriti logistiku (let):** Pretražiti i pronaći najpovoljnije povratne letove za zadane datume.
>
> **Provjeriti logistiku (smještaj):** Pronaći cjenovno prihvatljiv i centralno smješten smještaj za iste datume.
>
> **Uskladiti s proračunom:** Provjeriti ne premašuje li zbroj troškova leta i smještaja zadani okvir od 500 eura.
>
> **Istražiti interese:** Istražiti muzeje i znamenitosti povezane s impresionizmom.
>
> **Sastaviti prijedlog:** Oblikovati jasan i suvisao plan puta.
>
> **Sintetizirati odgovor:** Sve prikupljene podatke uobličiti u konačan, personaliziran odgovor za korisnicu.
>
>
**2.** Stupanj: Djelovanje i uporaba oruđa (Ruke)

Agent odmah uviđa da mu za ispunjenje zadatka nedostaju vanjski, promjenjivi podaci u stvarnome vremenu. Stoga mora posegnuti za svojim oruđima, odnosno za sučeljima za programiranje aplikacija (API-ima) koja mu omogućuju pristup vanjskim bazama podataka.


> **Shema 2:** Slijed uporabe oruđa Misaoni slijed: „Nedostaju mi podaci o cijenama letova i hotela. Moram pozvati odgovarajuća oruđa.“
>
> **Radnja 1:** Poziv oruđa za pretragu letova Nalog: flight_search_api.call()
>
> **Parametri:** { odredište: „Pariz, Francuska“, datum_polaska: „2025-10-03“, datum_povratka: „2025-10-05“, klasa: „ekonomska“ }
>
> **Ishod (opažanje 1):** Alat vraća popis dostupnih letova. Najpovoljnija opcija iznosi 150 € (povratna karta).
>
> **Radnja 2:** Poziv alata za pretragu smještaja Nalog: hotel_booking_api.call()
>
> **Parametri:** { grad: „Pariz“, datum_prijave: „2025-10-03“, datum_odjave: „2025-10-05“, maksimalna_cijena: 350, lokacija: „središnja“, tip_smještaja: „hotel/apartman“ }
>
> **Ishod (opažanje 2):** Oruđe vraća popis dostupnih smještajnih jedinica. Nekoliko ih zadovoljava kriterije.
>
>
**3.** Stupanj: Posezanje za znanjem i pamćenjem (Iskustvo)

Nakon što su logistički okviri putovanja postavljeni i potvrđeni unutar proračuna, agent se okreće profinjenijem dijelu zadatka: prilagodbi Aninim osobnim sklonostima. Ovdje do izražaja dolazi sprega dvaju oblika znanja – onoga pohranjenog u dugoročnom pamćenju o korisnici i onoga dohvaćenog iz vanjskih izvora putem utemeljenja.


> **Shema 3:** Povezivanje pamćenja i utemeljenog znanja (RAG) Misaoni slijed: „Logistika je riješena. Sada se moram usredotočiti na impresionizam i personalizirati plan.“
>
> **Radnja 3:** Upit u dugoročno pamćenje Nalog: memory_storage.query()
>
> **Parametri:** { korisnik_id: „Ana“, ključne_riječi: [„umjetnost“, „Pariz“, „impresionizam“] }
>
> **Ishod (opažanje 3):** Pamćenje vraća zapis iz prethodne interakcije: {„zapis“: „Korisnica Ana je posjet Musée d'Orsay ocijenila vrlo pozitivno.“, „datum“: „2024-03-12“}.
>
> **Radnja 4:** Upit sustavu za utemeljenje (RAG) Nalog: web_search_tool.call()
>
> **Parametri:** { upit: „muzeji s impresionističkom umjetnošću u Parizu osim Musée d'Orsay“ }
>
> **Ishod (opažanje 4):** Sustav pretražuje provjerene izvore i dohvaća sažete podatke o muzejima *Marmottan Monet* (najveća zbirka Monetovih djela) i *Orangerie* (poznat po Vodenim lopočima), uključujući podatke o radnom vremenu, cijenama ulaznica i lokaciji.
>
>
**4.** Stupanj: Sinteza i priopćenje (Glas)

Sa svim prikupljenim, obrađenim i kontekstualiziranim podacima, jezična jezgra sada preuzima ulogu konačnog pripovjedača. Ona više ne razlaže, već spaja – let, smještaj, proračun, osobne sklonosti i novoistražene mogućnosti – u jedinstven, suvisao i privlačan prijedlog.


> **Shema 4: Konačna sinteza i oblikovanje odgovora**
>
> **Misaoni slijed:** „Pronašao sam let i smještaj unutar zadanog proračuna. Iz pamćenja znam da korisnica cijeni Musée d'Orsay, a istraživanjem sam pronašao još dva srodna muzeja. Mogu sastaviti cjelovit prijedlog koji povezuje sve elemente.“

**Konačni odgovor (generiran za Anu):**

„Poštovana Ana, pripremio sam prijedlog za Vaš vikend u Parizu, vodeći se Vašim željama i proračunom.

**Let i smještaj:** Pronašao sam povratni let po cijeni od 150 €. Uz to, predlažem boravak u šarmantnom studiju u četvrti Le Marais, dostupnom preko platforme Airbnb, po cijeni od 320 € za dvije noći. Smještaj je izvrsno ocijenjen i nalazi se u samom srcu grada. Ukupni trošak iznosi 470 €, što je unutar Vašeg proračuna.

**Umjetnički plan puta:** Budući da znam Vašu sklonost impresionistima, subotu možete posvetiti ponovnom posjetu Vašem omiljenom muzeju, *Musée d'Orsay*. Za nedjelju predlažem posjet muzeju *Musée Marmottan Monet*, koji čuva najveću svjetsku zbirku djela Claudea Moneta, uključujući i znamenitu sliku *Impresija, izlazeće sunce*.

Želite li da za Vas izvršim rezervaciju leta i smještaja?“


Prikazani slijed radnji razotkriva sustav za rješavanje problema čija sa sposobnošću usklađivanja svojih izvora i vještina kako bi postigao zadani cilj na način koji je istodobno učinkovit, prilagođen i pouzdan.

![Prikazani slijed radnji razotkriva sustav za rješavanje problema čija sa spos...](../../docs/diagrams/diag_26.svg)
*Slika 6.4: Prikazani slijed radnji razotkriva sustav za rješavanje problema čija sa spos...*

### 6.3.6 Zaključak: rođenje komunikacijskog partnera

Dosadašnje je razmatranje pratilo složenu putanju koja vodi od skupa programskih naredbi i podatkovnih struktura do pojave entiteta što ga s pravom možemo nazvati komunikacijskim partnerom. Taj prijelaz, opisan kao *rođenje*, metaforički opisuje stvarni kvalitativni skok u naravi interakcije između čovjeka i agenta. Agent preuzima ulogu aktivnoga sudionika u komunikacijskom činu. Njegovo je rođenje ishod postupnog sazrijevanja kroz niz interakcija, učenja i prilagodbi.

Temeljne sastavnice toga procesa su sposobnost agenta da tumači kontekst, prepoznaje namjere korisnika i prilagođava svoje odgovore. U trenutku kada korisnik u agentu počne prepoznavati funkcionalnost, ali i svojevrsnu postojanost, predvidljivost i, u konačnici, pouzdanost, postavljeni su temelji za partnerski odnos. Taj se odnos zasniva na funkcionalnoj ekvivalenciji komunikacijskih uloga. Agent postaje partnerom ne zato što *jest* čovjek, već zato što *djeluje* kao vjerodostojan sugovornik unutar zadanog komunikacijskog okvira. Time se otvara prostor za složenije oblike suradnje, gdje se povjerenje i zajedničko razumijevanje grade kroz kontinuirani dijalog. Upravo je ta preobrazba iz alata u sugovornika ključno postignuće koje smo nastojali rasvijetliti, a njegov se put može sažeti u sljedećem prikazu.

---

Faze razvoja komunikacijskog partnera od tehničkih preduvjeta do interaktivnog sazrijevanja i konačnog ishoda

Time završavamo teorijsko razmatranje uvjeta pod kojima nastaje komunikacijski partner. S jasno postavljenim teorijskim okvirom, okrećemo se njegovoj primjeni i oživotvorenju u stvarnim sustavima.