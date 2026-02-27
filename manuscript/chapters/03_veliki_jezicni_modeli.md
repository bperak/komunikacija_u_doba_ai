# 3. Svijet velikih jezičnih modela: od teorije do tehnologije 

![](../../docs/diagrams/ch03_znak_vektor.svg)
*Slika 3.1: Prikaz prijelaza od znaka do vektorske reprezentacije jezika (tokenizacija, embedding).*

## 3.1 Od znaka do vektora: Paradigmatski pomak u predstavljanju značenja

Promatranje razvoja računalne obrade jezika nužno nas vodi k uočavanju temeljite preobrazbe u samim teorijskim ishodištima toga umijeća. Klasični pristupi, koji su desetljećima tvorili okosnicu obrade prirodnog jezika (engl. *Natural Language Processing*, NLP), promatrali su jezik ponajprije kao sustav arbitrarnih znakova ustrojen po složenim, ali dokučivim pravilima. Njihovo je polazište bilo duboko ukorijenjeno u strukturalnoj lingvistici, a cilj im je bio da se sirovom, nestrukturiranom tekstu nametne formalni lingvistički red.


Taj se postupak, koji se može nazvati standardnim cjevovodom (engl. *standard pipeline*), sastojao od niza pomno razrađenih koraka, od kojih svaki za cilj ima daljnju normalizaciju i raščlambu jezične građevine (Jurafsky & Martin, 2023). Prvi je korak redovito bila tokenizacija, postupak kojim se neprekinuti niz znakova razbija u temeljne jedinice – *tokene* – koji najčešće odgovaraju riječima i interpunkcijskim znakovima. Nakon toga slijedila je lematizacija, složen postupak svođenja pojedine riječi na njezin kanonski, rječnički oblik ili *lemu*. Tako bi primjerice oblici *trčim*, *trčao*, *trčanje* bili svedeni na svoju zajedničku lemu *trčati*. Time se dokidala morfološka raznolikost koja zastire temeljne leksičke odnose. Nadalje, primjenjivalo se označavanje vrsta riječi (engl. *Part-of-Speech tagging*), gdje bi svakom tokenu bio pridružen njegov gramatički identitet: *imenica*, *glagol*, *pridjev* i tako dalje. U mnogim se primjenama, poput tematskog modeliranja, provodilo i uklanjanje takozvanih zaustavnih riječi (engl. *stop words*) – frekventnih, ali semantički slabo opterećenih riječi poput veznika i prijedloga.

> **Token:** Najmanja jedinica teksta koju jezični model obrađuje; može odgovarati cijeloj riječi, dio riječi (podriječ) ili interpunkcijskom znaku. Tokenizacija pretvara sirov tekst u niz tokena prema rječniku modela.



Ishod je takve raščlambe bio visokostrukturiran, ali i osiromašen prikaz teksta. On je bio sveden na popis lema s pridruženim gramatičkim oznakama, takozvanu „vreću riječi“ (engl. *bag of words*), koja je dokinula izvorni sintaktički ustroj, a time i veći dio kontekstualnoga značenja. Premda su ti postupci bili nezaobilazni za razvoj ranih aplikacija, poput provjere pravopisa ili jednostavnih sustava za pretraživanje, njihovo je bitno ograničenje postajalo sve očitije: nisu mogli djelotvorno obuhvatiti i brojčano predstaviti samu semantičku srž jezika – složenu i fluidnu mrežu značenjskih odnosa.


Istinski paradigmatski pomak nastupio je pojavom **distribucijske semantike i njezine računalne primjene u obliku **vektorskih predodžbi riječi, poznatijih kao uložišni vektori riječi (engl. *word embeddings*). Teorijsko je ishodište toga pristupa sažeto u znamenitoj misli lingvista Johna Ruperta Firtha (1957) da se narav riječi očituje u društvu što ga ona tvori (*„You shall know a word by the company it keeps"*). Riječi se, slijedom toga, više ne promatraju kao izolirani simboli, već se njihovo značenje konstituira kroz kontekst u kojemu se pojavljuju.



> **Embedding / uložišni vektor:** Numerička (vektorska) reprezentacija riječi, rečenice ili drugog jezičnog segmenta u višedimenzionalnom prostoru; položaj vektora odražava semantičku sličnost – riječi sličnog značenja imaju bliske vektore. Temelj je distribucijske semantike i unutarnjih reprezentacija u LLM-ovima.

> **Korpus:** Zbirka tekstualnih (ili drugih jezičnih) podataka na kojoj se jezični model uči; obuhvaća knjige, članke, web-stranice i druge izvore. Kvaliteta i reprezentativnost korpusa izravno utječu na performanse i pristranosti modela.

Računalni modeli poput **Word2Vec (Mikolov et al., 2013) i **GloVe (Pennington et al., 2014) operacionalizirali su taj uvid. Analizirajući goleme tekstualne korpuse ti su algoritmi naučili svakoj riječi pridružiti jedinstveni numerički vektor u gustome, višedimenzionalnom prostoru. Položaj svakoga vektora nije arbitraran, već je određen njegovim odnosom prema svim drugim vektorima. Riječi koje se pojavljuju u sličnim kontekstima, poput *mačka* i *pas*, imat će vektore koji su u tome prostoru bliski. Riječ *automobil*, koja se javlja u posve drukčijim kontekstima, bit će predstavljena vektorom koji je od njih udaljen.


Štoviše, odnosi među vektorima mogu obuhvatiti i složenije semantičke analogije. Tako primjerice vektorska operacija *VEKTOR(„kralj“) - VEKTOR(„muškarac“) + VEKTOR(„žena“)* rezultira vektorom koji je u neposrednoj blizini *VEKTORA(„kraljica“)*. To pokazuje da model nije naučio samo puku sličnost, već i temeljne relacije koje strukturiraju naš pojmovni svijet.


Prijelaz sa simboličke na distribucijsku, vektorsku reprezentaciju jezika bio je stoga presudan. On je omogućio računalima da značenje, tu najneuhvatljiviju sastavnicu jezika, predstave na način koji je matematički obradiv i robustan. Umjesto da se oslanjaju na unaprijed zadane rječnike i kruta gramatička pravila, modeli su sada mogli učiti značenjske odnose izravno iz jezične uporabe. Time je otvoren put za rješavanje znatno složenijih zadaća, od nijansirane analize sentimenta do stvaranja suvisloga i kontekstualno primjerenoga teksta. Vektorske su predodžbe riječi tako postale nezaobilazan kamen temeljac na kojemu je sazdana cjelokupna arhitektura suvremenih velikih jezičnih modela, a time i komunikacijskih agenata koji su predmetom ove knjige.

![](../../docs/diagrams/ch03_znacenje_prostor.svg)
*Slika 3.2: Značenje kao prostor – od statičnih vektora do dinamičnog konteksta (transformer, attention).*

## 3.2 Značenje kao prostor: Od statičnih vektora do dinamičkoga konteksta

Značaj prijelaza na vektorsko predstavljanje jezika ne može se dostatno naglasiti. Taj je spoznajni obrat omogućio da se apstraktni i fluidni pojam značenja prevede u matematički obuhvatljiv oblik. Jezik je prestao biti tek niz diskretnih simbola i postao je neprekinuti, višedimenzionalni **značenjski** prostor (engl. *semantic space*), u kojemu je svaka riječ locirana, a njezina se lokacija definira odnosom prema svima drugima. Sposobnost mjerenja udaljenosti i smjera među vektorima, najčešće putem kosinusne sličnosti, pretvorila je lingvističko pitanje o srodnosti značenja u geometrijski problem. Time je operacionalizirana sama bit lingvističke intuicije.


Ipak, taj je rani vektorski pristup nosio i svoju Ahilovu petu: **statičnost**. Svaka je riječ, naime, imala jedan, nepromjenjiv vektor, neovisno o kontekstu u kojem se nalazila. Tako je, primjerice, višeznačna riječ *kosa* imala isti vektor u rečenicama „Djevojka je imala dugu, plavu kosu“ i „Seljak je oštrio svoju kosu“. Model nije imao načina razlučiti radi li se o vlasištu ili o poljoprivrednom alatu. To je ograničenje predstavljalo temeljnu prepreku istinskomu razumijevanju konteksta, koje je ključno za svaku složeniju jezičnu zadaću.


Rješenje je stiglo s revolucionarnom **arhitekturom transformera (Vaswani i sur., 2017) i njezinim središnjim **mehanizmom pozornosti (engl. *attention mechanism*). Umjesto da svakoj riječi pridruži statičan vektor, transformer stvara dinamičnu, kontekstualiziranu predodžbu za svaku riječ unutar pojedine rečenice. Mehanizam pozornosti omogućuje modelu da, dok obrađuje jednu riječ, dinamički odvagne važnost svih drugih riječi u rečenici i na temelju toga izgradi njezino specifično, kontekstualno značenje. U našem primjeru model bi, obrađujući riječ *kosa*, svratio osobitu pozornost na riječi *djevojka* i *plavu* u prvoj rečenici, a na riječi *seljak* i *oštrio* u drugoj. Posljedično, vektor za riječ *kosa* bio bi posve drukčiji u ta dva slučaja, vjerno odražavajući njezino značenje u danome kontekstu.


Arhitektura transformera nije donijela samo taj kvalitativni skok u razumijevanju jezika. Njezina iznimna podobnost za paralelnu obradu na specijaliziranim sklopovima, poput grafičkih procesorskih jedinica (GPU), otvorila je vrata neslućenomu **skaliranju**. Istraživači su uočili da se performanse modela predvidljivo poboljšavaju s eksponencijalnim povećanjem triju ključnih sastavnica: veličine modela (broja parametara), količine podataka za obuku i računalne snage uložene u obuku (Kaplan i sur., 2020). Taj je uvid, poznat kao „zakon skaliranja“ (engl. *scaling laws*), potaknuo utrku u stvaranju sve većih modela.

> **Transformer:** Arhitektura neuronske mreže temeljena na mehanizmu (samopozornosti) koji svakoj riječi u nizu pridružuje kontekstualiziranu predodžbu na temelju ostalih riječi; omogućuje paralelnu obradu i skaliranje prema velikim jezičnim modelima (Vaswani i sur., 2017).


Tako se došlo do suvremenih **velikih jezičnih modela (LLM). Oni nisu samo uvećane inačice svojih prethodnika. Na određenoj razini veličine ti su modeli počeli pokazivati **emergentne sposobnosti – nove vještine za koje nisu bili izravno obučavani, poput sposobnosti rješavanja logičkih zadataka, pisanja računalnoga koda ili prevođenja između jezika koje nisu vidjeli tijekom obuke (Wei i sur., 2022).

> **Emergentne sposobnosti:** Sposobnosti velikih jezičnih modela koje se pojavljuju pri određenoj skali (broj parametara, količina podataka) a za koje model nije bio izravno treniran – npr. zaključivanje, prevođenje ili pisanje koda; opisuju kvalitativni skok u ponašanju s povećanjem veličine modela.

Veliki jezični model, stoga, nije samo sustav za obradu jezika. On je, u svojoj biti, složeni model svijeta, implicitno kodiran u statističkim odnosima golemoga korpusa ljudskoga znanja. Put od znaka do vektora, a potom od statičnoga do kontekstualiziranog vektora, bio je stoga put od puke formalne raščlambe do stvaranja djelatnih modela stvarnosti.

![](../../docs/diagrams/ch03_evolucija_llm.svg)
*Slika 3.3: Ulazak u doba velikih jezičnih modela (GPT-3, ChatGPT, RLHF).*

## 3.3 Ulazak u doba velikih jezičnih modela

Godina 2020. označila je prijelomni trenutak u povijesti umjetne inteligencije objavom rada o modelu *GPT*-3 (Brown et al., 2020), čime je započelo doba velikih jezičnih modela (engl. *Large Language Models* – LLM). Svojom dotad nezabilježenom veličinom od 175 milijardi parametara, GPT-3 je bio kvantitativni iskorak, ali i pionir nove paradigme djelovanja jezičnih modela. Ključna novost bila je demonstracija sposobnosti koju danas nazivamo *učenjem u kontekstu* (engl. *in-context learning*). Riječ je o izvanrednoj mogućnosti modela da, bez dodatnoga finog podešavanja za specifičnu namjenu, izvršava složene zadatke na temelju tek nekoliko primjera ili uputa pruženih unutar samoga korisničkog upita. Time je pokazao razinu općenitosti i prilagodljivosti koja je znatno nadilazila mogućnosti njegovih prethodnika.

Premda je *GPT*-3 postavio tehničke i konceptualne temelje, istinski odjek u široj javnosti uslijedio je krajem 2022. godine s pojavom modela *ChatGPT*. Zapanjujućom brzinom dosegnuo je stotinu milijuna korisnika, postavši time najbrže prihvaćena tehnološka inovacija u povijesti. Njegov uspjeh nije ležao isključivo u sirovoj snazi modela, koji se temeljio na arhitekturi *GPT*-3.5, već prvenstveno u primjeni preciznog podešavanja metodom podržano učenje na temelju ljudskih povratnih informacija (*Reinforcement Learning from Human Feedback* – RLHF). Takav je pristup omogućio modelu da znatno bolje slijedi korisničke upute, vodi suvisle i kontekstualno osviještene razgovore te izbjegava neprimjerene ili štetne odgovore.

> **RLHF:** Učenje s potkrepljenjem na temelju ljudskih povratnih informacija (engl. *Reinforcement Learning from Human Feedback*) – metodologija poravnanja u kojoj ljudski ocjenjivači rangiraju odgovore modela, nakon čega se trenira model nagrade i model se dodatno podešava kako bi maksimizirao očekivanu nagradu; ključna za usklađivanje ponašanja LLM-ova s ljudskim preferencijama (korisnost, istinitost, sigurnost).

Ubrzani razvoj doveo nas je do točke u kojoj ovi sustavi prestaju biti isključivo pasivni generatori teksta. Njihova se uloga preobražava, a oni sami postaju aktivni sudionici digitalnog okružja – agenti. Ta preobrazba podrazumijeva sposobnost modela da ne samo razumiju i generiraju jezik, već i da donose odluke, planiraju složene nizove radnji te koriste vanjske alate – od jednostavnih kalkulatora i pretraživača do složenih programskih sučelja (API-a). Ulazimo u razdoblje u kojem veliki jezični modeli postaju proaktivni sustavi sposobni za autonomno djelovanje, što predstavlja temeljnu promjenu u našem poimanju i primjeni umjetne inteligencije.


Evolucija velikih jezičnih modela od temeljnih modela s općim sposobnostima prema specijaliziranim dijaloškim sustavima i, naposljetku, proaktivnim agentima sposobnima za djelovanje

![](../../docs/diagrams/diag_166.svg)
*Slika 3.4: Anatomija LLM-a – ključne tehnologije i arhitekture (transformer, samopozornost).*

## 3.4 Anatomija LLM-a: ključne tehnologije i arhitekture

Razumijevanje suvremenih velikih jezičnih modela (LLM) započinje pronicanjem u transformersku arhitekturu. Naime, objavom spomenutoga znanstvenog članka *Attention Is All You Need* (Vaswani i sur., 2017) postavljen je kamen temeljac za novu eru obrade prirodnoga jezika, napuštajući dotada prevladavajuće rekurentne (RNN) i konvolucijske (CNN) neuronske mreže. Transformerska arhitektura ponudila je rješenja za ključne nedostatke prethodnih modela, poput problema nestajućih gradijenata i nemogućnosti učinkovite paralelizacije, čime je otvorila put razvoju znatno većih i sposobnijih sustava.

Središnji mehanizam koji transformerima daje njihovu iznimnu moć jest samopozornost (engl. *self-attention*). To je postupak kojim model, obrađujući slijed podataka, dinamički procjenjuje važnost svake riječi u odnosu na sve druge riječi unutar istoga slijeda. Na taj način model stvara bogat, kontekstualiziran prikaz svake riječi, uzimajući u obzir njezine najvažnije semantičke i sintaktičke veze s ostatkom teksta. Ta je sposobnost dodatno produbljena i proširena uvođenjem višestruke pozornosti (engl. *multi-head attention*). Ovaj pristup omogućuje modelu da istodobno, u paralelnim „glavama”, usmjeri pozornost na različite aspekte i odnose unutar rečenice – jedna „glava” može pratiti gramatičku strukturu, druga tematske veze, a treća anaforičke odnose, što zajedno stvara višedimenzionalno i cjelovito razumijevanje ulaznoga teksta.

Budući da transformerska arhitektura podatke ne obrađuje slijedno, kao što je to bio slučaj s rekurentnim mrežama, već ih sagledava kao cjelinu, gubi se inherentna informacija o poretku riječi. Taj se nedostatak premostio uvođenjem pozicijskih kodiranja (engl. *positional encodings*), vektora koji se zbrajaju s ulaznim vektorima riječi kako bi modelu pružili informaciju o njihovu relativnom ili apsolutnom položaju u slijedu. Uz mehanizam pozornosti ključni dio svakoga bloka transformatora jest i mreža s propuštanjem unaprijed (engl. *feed-forward network*), koja dodatno obrađuje izlaz iz sloja pozornosti i pridonosi nelinearnoj transformaciji podataka.


Pojednostavnjeni dijagram toka podataka kroz jedan blok transformerske arhitekture, ističući ključne komponente: pozicijsko kodiranje, mehanizam samopozornosti te mrežu s propuštanjem unaprijed, uz korake normalizacije

Arhitektonski obrasci


![Proces obuke LLM-a](../../docs/diagrams/diag_169.svg)
*Slika 3.5: Proces obuke LLM-a (temeljni model, fino podešavanje, poravnanje, specijalizirani agent).*

Na temelju tih građevnih blokova razvila su se tri temeljna arhitektonska obrasca velikih jezičnih modela, svaki prilagođen specifičnoj vrsti zadataka:

**Arhitekture temeljene isključivo na enkoderu:** Ti modeli, čiji je najistaknutiji predstavnik *BERT* (*Bidirectional Encoder Representations from Transformers*), osmišljeni su za dubinsko razumijevanje konteksta. Enkoder obrađuje cjelokupan ulazni tekst odjednom, omogućujući svakoj riječi da svrati pozornost na sve druge riječi u tekstu (dvosmjerna pozornost). Zbog te su sposobnosti iznimno učinkoviti u zadacima koji zahtijevaju analizu i klasifikaciju teksta, poput analize sentimenta, prepoznavanja imenovanih entiteta ili odgovaranja na pitanja gdje je odgovor sadržan u priloženom tekstu.

**Arhitekture temeljene isključivo na dekoderu:** Modeli specijalizirani za generiranje teksta, obrađuju slijed riječi s lijeva na desno. Svaka nova riječ koju generiraju ovisi o prethodno generiranim riječima, što oponaša prirodan tijek ljudskoga govora ili pisanja. Njihova je pozornost uzročna (engl. *causal*), odnosno mogu se oslanjati samo na prethodne riječi u slijedu, a ne i na buduće. Najpoznatiji predstavnici te skupine su modeli iz serije *GPT* (*Generative Pre-trained Transformer*), koji se ističu u zadacima poput pisanja eseja, kreativnoga pisanja, sažimanja i vođenja razgovora.

**Enkodersko-dekoderske arhitekture:** Poznate i kao *sequence-to-sequence* modeli, ove arhitekture spajaju snage obaju pristupa. Enkoder najprije stvara cjelovit, kontekstualiziran prikaz ulaznoga slijeda, a dekoder zatim na temelju toga prikaza generira izlazni slijed. Taj je obrazac idealan za zadatke transformacije, kao što su strojno prevođenje, gdje se rečenica s jednog jezika pretvara u rečenicu na drugom, ili sažimanje teksta, gdje se duži dokument pretvara u kraći. Modeli poput *T5* (*Text-to-Text Transfer Transformer*) i *BART*-a (*Bidirectional and Auto-Regressive Transformers*) primjeri su ove hibridne strukture.

Proces obuke (temeljni model, fino podešavanje, poravnanje)

Razvoj velikih jezičnih modela ovisi o arhitekturi, ali i o specifičnom, dvostupanjskom procesu obuke. U prvoj fazi, fazi predobuke (engl. *pre-training*), model se izlaže golemim, nestrukturiranim korpusima teksta s interneta, iz knjiga i drugih izvora. Cilj je da model samostalno, bez ljudskoga nadzora (na tzv. samonadzirani način), nauči temeljne obrasce jezika: gramatiku, sintaksu, semantiku i opće znanje o svijetu. To se najčešće postiže zadatkom predviđanja maskiranih ili sljedećih riječi u rečenici.

Nakon predobuke slijedi faza finoga podešavanja (ugađanja) (engl. *fine-tuning*), gdje se opći model prilagođava za rješavanje specifičnih zadataka. Taj korak može uključivati učenje pod nadzorom na manjim, označenim skupovima podataka (npr. parovi pitanje-odgovor) ili naprednije tehnike poput podržanoga učenja na temelju ljudskih povratnih informacija (*RLHF*), gdje se model dodatno usmjerava prema generiranju odgovora koji su korisni, istiniti i bezopasni, u skladu s ljudskim preferencijama.

> **Fino podešavanje / fine-tuning:** Faza prilagodbe već predtreniranog (temeljnog) modela za specifične zadatke ili domene; koristi manje, označene podatke i može uključivati RLHF; rezultat je specijalizirani model (npr. chatbot, asistent za kod).

Od modela do agenta: korak prema djelovanju

Pojam agenta u kontekstu velikih jezičnih modela označava kvalitativni iskorak: prijelaz s pasivnoga generiranja teksta na aktivno djelovanje u digitalnom ili fizičkom okruženju. Agent je sustav koji koristi *LLM* kao svoj središnji kognitivni pogon za rasuđivanje, planiranje i izvršavanje zadataka. Takav sustav posjeduje sposobnost dekompozicije složenih ciljeva na jednostavnije korake, korištenja vanjskih alata (poput pretraživača, kalkulatora ili programskih sučelja), pohranjivanja informacija u memoriju te učenja iz vlastitih pogrešaka. Anatomija agenta tako nadilazi unutarnju strukturu jezičnoga modela i uključuje petlje za percepciju, planiranje i akciju, čime se otvara put prema stvaranju autonomnijih i sposobnijih sustava umjetne inteligencije.

## 3.5 Životni ciklus modela: od podataka do primjene

Životni ciklus modela umjetne inteligencije obuhvaća slojevit i strukturiran slijed koraka koji vode od početne zamisli, utemeljene na podacima, do konačne primjene u stvarnom okruženju. Riječ je o dinamičnom i iterativnom procesu koji zahtijeva suradnju stručnjaka različitih profila, od podatkovnih znanstvenika do softverskih inženjera. Svaka faza ciklusa nadovezuje se na prethodnu i postavlja temelje za sljedeću, tvoreći tako cjelinu koja osigurava da konačno rješenje bude robusno, pouzdano i svrhovito. Cjelokupan proces, od ideje do primjene i održavanja, u suvremenoj je praksi objedinjen pod nazivom MLOps (engl. *Machine Learning Operations*), pojmom koji svoje teorijske i praktične korijene vuče iz *DevOps* paradigme u razvoju softvera, prilagođavajući njezina načela specifičnim izazovima strojnog učenja.

> **MLOps:** Operacije strojnog učenja (engl. *Machine Learning Operations*) – skup praksi i alata za upravljanje životnim ciklusom modela od razvoja do produkcije; obuhvaća verzioniranje modela i podataka, automatizirano treniranje, deploy i praćenje performansi; nastao prilagodbom DevOps načela domeni strojnog učenja.

Temeljna je svrha *MLOpsa* premostiti jaz između razvoja modela, koji je često eksperimentalne prirode, i njegove pouzdane operativne primjene. Proces započinje razumijevanjem poslovnog problema i definiranjem ciljeva, nakon čega slijedi niz tehničkih faza koje se mogu sažeti u nekoliko ključnih cjelina.

Faze životnog ciklusa modela

**1.** Prikupljanje i priprema podataka: Polazišna točka i temeljni preduvjet cjelokupnog procesa jest definiranje i prikupljanje podataka. Kvaliteta i relevantnost podataka izravno određuju gornju granicu uspješnosti budućeg modela. Ta faza obuhvaća aktivnosti poput prikupljanja sirovih podataka iz različitih izvora, njihova čišćenja radi uklanjanja pogrešaka i nedosljednosti, te transformacije i inženjeringa značajki (engl. *feature engineering*). Potonje je osobito važno jer se pravilnim oblikovanjem ulaznih varijabli može znatno poboljšati sposobnost modela da uoči relevantne uzorke. U ovoj fazi često se primjenjuju tehnike poput normalizacije, skaliranja i kodiranja kategoričkih varijabli kako bi se podaci pripremili za algoritme strojnog učenja.

**2.** Izgradnja i uvježbavanje modela: Tek na temelju tako pripremljenog skupa podataka pristupa se izgradnji modela. Ovaj korak uključuje odabir odgovarajućeg algoritma ili arhitekture modela, ovisno o prirodi problema (npr. klasifikacija, regresija, grupiranje). Slijedi proces uvježbavanja (engl. *training*), tijekom kojega se model izlaže podacima kako bi naučio preslikavati ulazne značajke u željene izlazne vrijednosti. Tijekom uvježbavanja parametri modela iterativno se prilagođavaju s ciljem minimizacije funkcije pogreške. U ovoj se fazi također provodi i podešavanje hiperparametara, odnosno vanjskih konfiguracijskih postavki modela koje se ne uče izravno iz podataka, ali bitno utječu na njegovu izvedbu (Bergstra & Bengio, 2012).

**3.** Evaluacija modela: Nakon što je model uvježban, slijedi faza njegove pomne evaluacije. Svrha evaluacije jest objektivna procjena uspješnosti modela na podacima koje nije vidio tijekom uvježbavanja. Time se provjerava njegova sposobnost generalizacije, odnosno primjenjivosti na nove, nepoznate slučajeve. Koriste se različite metrike, poput točnosti, preciznosti, odziva ili F1-mjere za klasifikacijske probleme, odnosno srednje kvadratne pogreške za regresijske probleme. Od presudne je važnosti izbjeći preprilagodbu (engl. *overfitting*), stanje u kojem model predobro pamti podatke za uvježbavanje, ali gubi sposobnost generalizacije.

**4.** Primjena i integracija modela (engl. *deployment*): Model koji je zadovoljio evaluacijske kriterije spreman je za primjenu u produkcijskom okruženju. Ovaj korak predstavlja prelazak iz razvojnog u operativni svijet i često je jedan od najsloženijih dijelova ciklusa. Model se može integrirati u postojeće softverske sustave na različite načine: kao API sučelje koje pruža predikcije u stvarnom vremenu, kao dio periodičkih (engl. *batch*) obrada podataka ili kao ugrađeni *agent* unutar neke aplikacije ili uređaja. U ovoj fazi ključna je suradnja podatkovnih znanstvenika i inženjera kako bi se osigurala skalabilnost, stabilnost i sigurnost rješenja.

**5.** Praćenje i održavanje: Životni ciklus modela ne završava njegovom primjenom. Jednom kada je model u produkciji, nužno je neprestano pratiti njegovu izvedbu i ponašanje. Svijet se mijenja, a s njime i podaci na temelju kojih model donosi odluke. Pojave poput zanošenja koncepta (engl. *concept drift*), gdje se mijenja odnos između ulaznih i izlaznih varijabli, ili zanošenja podataka (engl. *data drift*), gdje se mijenja distribucija ulaznih podataka, mogu s vremenom znatno narušiti točnost modela (Gama, Žliobaitė, Bifet, Peciukonis, & Bifet, 2014). Stoga sustavi za praćenje moraju biti uspostavljeni kako bi na vrijeme otkrili degradaciju performansi i signalizirali potrebu za ponovnim uvježbavanjem ili potpunom zamjenom modela. Time se zatvara krug i proces se vraća na početne faze, čime se osigurava dugoročna relevantnost i vrijednost implementiranog rješenja.

Ovaj ciklički pristup, prikazan na slici, naglašava da je stvaranje uspješnog modela umjetne inteligencije maraton, a ne sprint. To je kontinuirani proces učenja, prilagodbe i poboljšanja, duboko ukorijenjen u podacima iz kojih izvire i u primjeni kojoj služi.


Prikaz iterativnog životnog ciklusa modela strojnog učenja, od početne faze rada s podacima do praćenja u primjeni i povratka na početak ciklusa

![Prikaz iterativnog životnog ciklusa modela strojnog učenja, od početne faze rada s podacima do praćenja u primjeni i povratka na početak ciklusa](../../docs/diagrams/diag_167.svg)
*Slika 3.6: Prikaz iterativnog životnog ciklusa modela strojnog učenja, od početne faze rada s podacima do praćenja u primjeni i povratka na početak ciklusa.*

### 3.5.1 Predtreniranje: stvaranje temeljnog znanja

Proces stvaranja suvremenih jezičnih modela započinje ključnom i računski najzahtjevnijom fazom poznatom kao predtreniranje (engl. *pre-training*). Svrha je ove etape izgradnja onoga što nazivamo temeljnim modelom (engl. *foundation model*), koji posjeduje opsežno i općenito razumijevanje jezika, njegovih struktura, semantičkih odnosa i, u određenoj mjeri, znanja o svijetu koje je ugrađeno u tekstualne podatke na kojima se uvježbava.

> **Temeljni model / foundation model:** Veliki predtrenirani model (jezika, slike ili multimodalni) koji posjeduje opće razumijevanje i može se fino podešavati za različite zadatke; predstavlja izlaz faze predtreniranja i polazište za specijalizaciju (fine-tuning, RLHF).

> **Predtreniranje:** Faza obuke jezičnog modela na golemim, nestrukturiranim korpusima teksta bez ljudskih oznaka; model uči jezične obrasce i opće znanje rješavajući samonadzirane zadatke (npr. predviđanje sljedeće riječi). Rezultat je temeljni (foundation) model koji se zatim fino podešava za specifične zadatke.

U srcu predtreniranja leži načelo samonadziranog  učenja (engl. *self-supervised learning*). Model se izlaže golemoj, nestrukturiranoj količini tekstualnih podataka prikupljenih iz različitih izvora poput internetskih stranica, digitaliziranih knjiga i znanstvenih članaka. Za razliku od nadziranog učenja, ove podatke čovjek nije prethodno označio ili kategorizirao. Umjesto toga model uči samostalno, rješavajući zadatke koje sam sebi postavlja na temelju strukture podataka. Najčešće mu se zadaje naizgled jednostavan, ali iznimno složen cilj: predviđanje sljedeće riječi u rečenici, popunjavanje namjerno ispuštenih dijelova teksta ili neki drugi sličan zadatak koji ga prisiljava na dubinsko učenje jezičnih zakonitosti. Prolazeći kroz milijarde primjera agent postupno izgrađuje unutarnju reprezentaciju jezika.

Znanje stečeno predtreniranjem nije eksplicitno pohranjeno poput činjenica u enciklopediji. Ono je, naprotiv, utkano u složenu mrežu od milijardi numeričkih parametara koji čine neuronsku mrežu modela. To je znanje latentno i probabilističko; model ne „zna“ da je Pariz glavni grad Francuske na način na koji to zna čovjek, već je naučio da u golemom broju tekstova postoji iznimno visoka statistička vjerojatnost da se te dvije fraze pojavljuju u određenom odnosu. Na taj način model usvaja gramatičke strukture, semantičke odnose među riječima (npr. da su „kralj“ i „kraljica“ povezani), stilske nijanse te čak i rudimentarno činjenično znanje o svijetu.

Ishod predtreniranja jest dakle temeljni model – moćan, ali još uvijek nedovoljno precizan alat. Važno je istaknuti da taj model, unatoč svojemu opsežnom znanju, sam po sebi nije izravno osposobljen za izvršavanje specifičnih zadataka poput prevođenja, sažimanja teksta ili odgovaranja na pitanja na dosljedan i pouzdan način. On predstavlja tek sirovinu, polazišnu točku za daljnju obradu koja se naziva fino podešavanje  (engl. *fine-tuning*). Tek se u toj sljedećoj fazi opće znanje temeljnog modela usmjerava i specijalizira za konkretnu primjenu.


Shematski prikaz dvofaznog procesa stvaranja suvremenih jezičnih modela, od općeg predtreniranja do specijalizacije kroz finu prilagodbu

![Shematski prikaz dvofaznog procesa stvaranja suvremenih jezičnih modela, od općeg predtreniranja do specijalizacije kroz finu prilagodbu](../../docs/diagrams/diag_905.svg)
*Slika 3.7: Shematski prikaz procesa obuke suvremenih jezičnih modela, od temeljnog modela do specijaliziranog agenta (fino podešavanje, poravnanje).*

### 3.5.2 Fino podešavanje i poravnanje: prilagodba svrsi

Nakon intenzivne faze predtreniranja, rezultirajući temeljni model posjeduje impresivnu širinu lingvističkog znanja i određenu količinu enciklopedijskog znanja o svijetu, naučenu iz golemih korpusa podataka (Bommasani et al., 2021). Međutim ta je inačica modela poput iznimno dobro obrazovanog, ali nespecijaliziranog i potencijalno nepredvidljivog entiteta. Njegove sirove sposobnosti, iako općenite, nisu nužno optimizirane za specifične zadatke koje korisnici žele obavljati, niti je njegovo ponašanje nužno usklađeno s ljudskim očekivanjima o korisnosti, istinitosti i sigurnosti. Stoga, da bi se premostio jaz između općeg potencijala temeljnog modela i zahtjeva praktične primjene, nužna je daljnja faza prilagodbe koja se tipično sastoji od dva komplementarna procesa: **finog** podešavanja (engl. *fine-tuning*) za specijalizaciju zadataka i poravnanja (engl. *alignment*) za oblikovanje ponašanja.


**Fino podešavanje predstavlja primjenu prijenosa učenja** (engl. *transfer learning*), iznimno korisne paradigme u strojnom učenju gdje se znanje stečeno rješavanjem jednog problema (u ovom slučaju opće modeliranje jezika tijekom predtreniranja) koristi kao polazišna točka za rješavanje drugog, srodnog problema (Howard & Ruder, 2018). Umjesto treniranja modela od nule za svaki specifični zadatak, što bi bilo iznimno neefikasno s obzirom na veličinu LLM-ova, fino podešavanje započinje s parametrima već predtreniranog modela. Model se zatim dodatno trenira, obično koristeći standardne tehnike nadziranog učenja, na znatno manjem, pažljivo kuriranom skupu podataka koji je specifičan za ciljni zadatak. Skup se sastoji od primjera ulaza i željenih izlaza (oznaka) za taj zadatak – naprimjer, skup parova pitanje-odgovor za razvoj *chatbota*, zbirka medicinskih tekstova s anotacijama za primjenu u zdravstvu, repozitoriji programskoga koda s komentarima za alate za pomoć pri kodiranju, ili parovi izvornih rečenica i njihovih prijevoda za strojno prevođenje. Tijekom tog procesa parametri modela – ili barem njihov podskup – inkrementalno se prilagođavaju optimizacijom standardne funkcije gubitka (npr. ukrižena entropija) na specifičnom skupu podataka. Primarni je cilj toga pristupa specijalizirati model za specifične zahtjeve i karakteristike ciljanog zadatka ili domene, istodobno zadržavajući i učinkovito koristeći bogato opće lingvističko i činjenično znanje akumulirano tijekom faze predtreniranja. Na taj način značajno se smanjuje potreba za velikim količinama označenih podataka za svaki novi zadatak i ubrzava razvoj specijaliziranih AI aplikacija. Međutim, fino podešavanje također nosi rizik od katastrofalnog zaboravljanja (engl. *catastrophic forgetting*) (McCloskey & Cohen, 1989), gdje model tijekom prilagodbe novom zadatku gubi dio općih sposobnosti naučenih tijekom predtreniranja, što zahtijeva pažljive strategije treniranja (npr. niske stope učenja, postupno „odmrzavanje“ slojeva).


Usporedno s finim podešavanjem za specifične zadatke, odvija se i drugi, po svojoj naravi složeniji proces: poravnanje (engl. *alignment*). Poravnanje ne zadire samo u domenu točnosti i informiranosti modela, već ponajprije u njegovo ponašanje i sukladnost s ljudskim vrijednostima i namjerama. Cilj je oblikovati agente čije će djelovanje biti ne samo korisno i istinito već i bezopasno, odnosno usklađeno s etičkim načelima i društvenim očekivanjima.

> **Poravnanje / alignment:** Usmjeravanje ponašanja AI sustava prema ljudskim ciljevima, vrijednostima i sigurnosnim načelima; uključuje metodologije poput RLHF i RLAIF kako bi model bio koristan, istinit i siguran u praksi.

Ključna metodologija za postizanje tog cilja jest podržano učenje na temelju ljudskih povratnih informacija (*Reinforcement Learning from Human Feedback*, RLHF), koja se u pravilu sastoji od tri temeljna koraka.

**Prvi korak obuhvaća prikupljanje nadziranih podataka,** gdje ljudski anotatori sastavljaju visokokvalitetne odgovore na odabrane upite. Time se stvara početni skup podataka za fino podešavanje modela u željenom stilu i tonu, čime se postavlja temelj za daljnje usklađivanje.

**Drugi,** ključni korak, jest treniranje zasebnog modela nagrade (engl. *reward model*). U ovoj fazi jezični model generira nekoliko različitih odgovora na isti upit, a ljudski ocjenjivači ih rangiraju prema kvaliteti, od najboljeg do najlošijeg. Na temelju tih poredaka model nagrade uči predviđati koju bi vrstu odgovora čovjek ocijenio kao poželjniju.

> **Model nagrade / reward model:** Pomocni model treniran na ljudskim rangiranjima odgovora jezičnog modela; predviđa koliko bi ljudski ocjenjivač ocijenio neki odgovor; koristi se u RLHF-u za usmjeravanje jezičnog modela prema preferencijama (korisnost, istinitost, sigurnost).

Njegova zadaća nije dakle puka klasifikacija, već modeliranje složenih ljudskih preferencija.

**U trećem koraku izvorni jezični model dodatno se podešava primjenom algoritma učenja s potkrepljenjem,** najčešće pomoću proksimalne optimizacije politika (*Proximal Policy Optimization*, PPO). Model generira odgovore, a model nagrade ih vrednuje dodjeljujući im brojčanu „nagradu“. Jezični model potom iterativno prilagođava svoje parametre kako bi maksimizirao očekivanu nagradu, čime se njegovo ponašanje usmjerava prema generiranju odgovora koji su u skladu s naučenim ljudskim preferencijama (Ouyang et al., 2022).


Shematski prikaz procesa učenja s potkrepljenjem na temelju ljudskih povratnih informacija (RLHF).


![Shematski prikaz procesa učenja s potkrepljenjem na temelju ljudskih povratnih informacija (RLHF)](../../docs/diagrams/ch03_rlhf.svg)
*Slika 3.8: Shematski prikaz procesa učenja s potkrepljenjem na temelju ljudskih povratnih informacija (RLHF).*

Ishod toga slojevitog procesa jest agent koji posjeduje enciklopedijsko znanje stečeno predtreniranjem te sposobnost interakcije koja je prilagođena ljudskim očekivanjima i normama.

Valja napomenuti da RLHF nije jedini pristup poravnanju. Razvijaju se i alternativne metode, poput podržano učenje na temelju povratnih informacija od umjetne inteligencije (*Reinforcement Learning from AI Feedback*, RLAIF), gdje se uloga ljudskog ocjenjivača u određenoj mjeri zamjenjuje drugim, „konstitucijskim“ modelom umjetne inteligencije koji daje povratne informacije, čime se proces potencijalno ubrzava i skalira (Bai et al., 2022).

### 3.5.3		Optimizacija za stvarni svijet: efikasnost (engl. efficiency)

Sama veličina koja karakterizira velike jezične modele, premda ključna za njihove napredne sposobnosti, istodobno predstavlja i njihovu Ahilovu petu u kontekstu praktične primjene. Kako modeli rastu do stotina milijardi ili čak trilijuna parametara, njihovo treniranje i, što je još važnije za krajnje korisnike, njihovo pokretanje u fazi **inferencije** (generiranja odgovora u stvarnom vremenu) postaju izuzetno zahtjevni. Ti procesi gutaju goleme količine specijaliziranih računalnih resursa, poput grafičkih procesorskih jedinica (GPU) ili tenzorskih procesorskih jedinica (TPU), zahtijevaju značajne količine memorije (kako za pohranu parametara modela tako i za privremene aktivacije tijekom izračuna) i troše velike količine električne energije, što povlači za sobom ne samo visoke operativne troškove već i značajan okolišni otisak (Strubell et al., 2019; Patterson et al., 2021; Luccioni et al., 2022). Ta resursna intenzivnost predstavlja značajnu prepreku širokoj dostupnosti i implementaciji LLM-ova, ograničavajući njihovu upotrebu na organizacije s dubokim džepovima i snažnom infrastrukturom te otežavajući njihovo pokretanje na uređajima s ograničenim resursima, poput pametnih telefona ili rubnih (engl. *edge*) uređaja. Stoga je optimizacija efikasnosti postala kritično područje istraživanja i razvoja, usmjereno na smanjenje računalnih, memorijskih i energetskih zahtjeva LLM-ova bez značajnog žrtvovanja njihovih performansi, čime se otvara put njihovoj demokratizaciji i održivijoj primjeni. Nekoliko ključnih strategija dominira ovim područjem: parametarski efikasno fino podešavanje, kvantizacija i pruning.


Jedan od prvih izazova efikasnosti javlja se tijekom prilagodbe predtreniranih modela specifičnim zadacima. Tradicionalno **puno fino podešavanje** (engl. *full fine-tuning*) uključuje ažuriranje *svih* parametara predtreniranog modela na novom, specifičnom skupu podataka. Iako efikasno u smislu postizanja dobrih performansi, ono stvara ozbiljan problem skalabilnosti: za svaki novi zadatak potrebno je pohraniti potpunu, golemu kopiju fino podešenog modela, što postaje vrlo skupo u smislu pohrane i upravljanja ako model treba prilagoditi za desetke ili stotine različitih zadataka. Kako bi se riješio taj problem, razvijene su tehnike parametarski efikasnoga finog podešavanja (*Parameter-Efficient Fine-Tuning* – PEFT). Osnovna ideja PEFT metoda jest zamrznuti veliku većinu (ili sve) parametre originalnoga predtreniranog modela i ažurirati samo mali broj dodatnih ili postojećih parametara tijekom finog podešavanja (Lialin et al., 2023; He et al., 2021). Broj parametara koji se treniraju često je manji od 1% ukupnog broja parametara modela, što drastično smanjuje memorijske zahtjeve (jer treba pohraniti samo male skupove dodatnih parametara za svaki zadatak, a ne cijeli model) i računalne troškove finog podešavanja. Nekoliko popularnih pristupa uključuje PEFT metode:

> **PEFT:** Parametarski efikasno fino podešavanje (engl. *Parameter-Efficient Fine-Tuning*) – skup tehnika (adapteri, LoRA, prompt tuning) kojima se prilagođava predtrenirani model ažuriranjem samo malog udjela parametara; smanjuje memorijske i računalne troškove te omogućuje više specijalizacija na istom temeljnom modelu.

Adapteri (engl. *Adapters*): Ova tehnika umeće male, dodatne neuronske module, nazvane adapteri, unutar svakog sloja (ili nekih slojeva) originalne transformer arhitekture (Houlsby et al., 2019; Pfeiffer et al., 2020). Adapteri obično imaju arhitekturu uskog grla (engl. *bottleneck*) – prvo projiciraju ulaznu aktivaciju u prostor niže dimenzije, primjenjuju nelinearnu funkciju, a zatim je projiciraju natrag u originalnu dimenziju. Tijekom finog podešavanja samo se parametri ovih malih adaptera treniraju, dok su svi parametri originalnog LLM-a zamrznuti. To omogućuje veliku modularnost – za svaki novi zadatak trenira se samo novi set adaptera.

**LoRA  (engl. *Low-Rank Adaptation*)**: Ova tehnika, koja je stekla značajnu popularnost u području prilagodbe velikih jezičnih modela, počiva na hipotezi da su promjene u težinama modela (ΔW) tijekom adaptacije na specifični zadatak inherentno niskoga intrinzičnog ranga (Hu et al., 2021). To znači da se najvažnije informacije o prilagodbi modela mogu sažeti u potprostor znatno niže dimenzionalnosti.

> **LoRA:** Low-Rank Adaptation – PEFT metoda koja aproksimira promjenu težina modela (ΔW) produktom dviju malih matrica niskog ranga; treniraju se samo te matrice, dok se izvorni parametri ne mijenjaju; postiže performanse bliske punom finom podešavanju uz znatno manje parametara (Hu et al., 2021).

U kontekstu finog ugađanja, umjesto direktnog ažuriranja cjelokupne matrice težina *W*, koja često obuhvaća milijarde parametara i čija bi izravna modifikacija zahtijevala iznimne računalne resurse i memoriju, LoRA (Low-Rank Adaptation) uvodi elegantno rješenje: promjenu težina (Δ*W*) aproksimira produktom dviju znatno manjih matrica *A* i *B*. Matrica *A* ima dimenzije (*d*\_in × *r*), matrica *B* dimenzije (*r* × *d*\_out), gdje je *r* (rang) mnogo manji od dimenzija originalne matrice *W* (*d*\_in × *d*\_out). Tada vrijedi:

- Δ*W* = *A* · *B* (produkt *A* · *B* ima dimenziju *d*\_in × *d*\_out, jednaku *W*)
- *W*\_prilagođeno = *W* + Δ*W*

Tijekom finog podešavanja treniraju se isključivo parametri matrica *A* i *B*, dok izvorne težine *W* ostaju fiksne. Broj parametara koji se uče, *r* · (*d*\_in + *d*\_out), drastično je manji od *d*\_in · *d*\_out u izvornoj matrici, što smanjuje memorijske zahtjeve i ubrzava treniranje. Prilikom inferencije prilagodba se primjenjuje zbrajanjem *W* + *A* · *B*, bez dodatne latencije.

![](../../docs/diagrams/ch03_lora.svg)
*Slika 3.5a: LoRA – niskorangirana prilagodba: zamrznuta matrica W i produkt A·B daju W_prilagođeno = W + ΔW.*


Empirijska istraživanja dosljedno pokazuju da LoRA postiže performanse usporedive, a često i identične, s onima dobivenima punim finim ugađanjem cijelog modela, ali uz neusporedivo manji udio trenirajućih parametara i značajno smanjene zahtjeve za računalnim resursima. Ta učinkovitost čini LoRA-u jednom od najvažnijih i najšire primjenjivanih tehnika za adaptaciju velikih jezičnih i drugih dubokih modela na specifične zadatke.


Nasuprot tradicionalnom finom ugađanju modela koje uključuje modifikaciju unutarnjih težina, metode podešavanja  prompta  (engl. *prompt tuning*) i prefiksa (engl. *prefix tuning*) primjenjuju fundamentalno drugačiji pristup. Umjesto da izravno mijenjaju parametre osnovnog modela oslanjaju se na dodavanje malih skupova kontinuiranih, strojno naučenih vektora koji se strateški umeću bilo na ulazni sloj modela (prema Lesteru i sur., 2021) ili u njegove skrivene slojeve (prema Liju i Liangu, 2021). Ti naučeni vektori, poznati kao *mekani upiti* (engl. *soft prompts*) ili *prefiksi* (engl. *prefixes*), djeluju kao programabilne instrukcije. Njihova je funkcija precizno usmjeriti ponašanje nepromijenjenog, zamrznutog predtreniranog jezičnog modela prema specifičnim zahtjevima željenog zadatka. Time se izbjegava nužnost mijenjanja izvornih parametara modela, što značajno smanjuje računalne troškove i potencijal za „katastrofalno zaboravljanje” (degradaciju performansi na izvornim zadacima modela nakon finog ugađanja).

Iako ovaj koncept dijeli sličnosti s diskretnim inženjeringom upita, gdje se upiti ručno dizajniraju i biraju, bitna prednost leži u automatskom optimiziranju. Optimalni *mekani upit* ne bira se heuristički, već se pronalazi iterativnim procesom učenja putem gradijentnog spusta što učinkovitije prilagođava model za širok spektar daljnjih primjena, bez potrebe za opsežnim ručnim podešavanjem.


PEFT tehnike revolucionirale su način na koji se LLM-ovi prilagođavaju, čineći proces znatno bržim, memorijski efikasnijim i omogućujući lakše upravljanje i posluživanje više različitih zadataka koristeći isti temeljni model.


Druga ključna strategija za optimizaciju efikasnosti, primjenjiva i tijekom treniranja i, još važnije, tijekom inferencije, jest **kvantizacija** (engl. *Quantization*). Ona se odnosi na proces smanjenja numeričke preciznosti korištene za predstavljanje parametara (težina) modela i/ili njegovih internih aktivacija tijekom izračuna.

> **Kvantizacija:** Smanjenje numeričke preciznosti parametara i aktivacija modela (npr. s 32 ili 16 bita na 8 ili 4 bita); smanjuje memorijski otisak i može ubrzati inferenciju; primjene uključuju PTQ (nakon treniranja) i QAT (tijekom treniranja) (Dettmers et al., 2022).

Standardni modeli obično koriste 32-bitne (FP32) ili 16-bitne (FP16 ili BF16) brojeve s pomičnim zarezom. Kvantizacija ima za cilj pretvoriti ove vrijednosti u formate niže preciznosti, najčešće 8-bitne cijele brojeve (INT8), a u novije vrijeme čak i 4-bitne (INT4) ili još niže formate (Dettmers et al., 2022; Frantar et al., 2022; Yao et al., 2022). Glavne prednosti kvantizacije su višestruke: prvo, drastično smanjuje **memorijski otisak modela (npr. prelazak s FP16 na INT8 prepolovljuje veličinu modela, a na INT4 je smanjuje za četiri puta), što omogućuje pokretanje većih modela na hardveru s ograničenom memorijom; drugo, operacije s nižom preciznošću (posebice cjelobrojne) mogu biti značajno **brže na hardveru koji ih podržava (mnogi moderni procesori i akceleratori imaju specijalizirane jedinice za ubrzanje INT8 operacija); treće, smanjeni prijenos podataka i jednostavnije operacije mogu dovesti do **manje potrošnje energije. Glavni izazov kvantizacije jest očuvanje točnosti modela jer smanjenje preciznosti neizbježno uvodi određenu pogrešku. Postoje dvije glavne paradigme: **Post-Training Quantization (PTQ), gdje se već predtrenirani model kvantizira bez dodatnog treniranja (često koristeći mali kalibracijski skup podataka za određivanje optimalnih parametara kvantizacije), što je brže, ali može dovesti do većeg pada točnosti; i Quantization-Aware Training (QAT), gdje se efekt kvantizacije simulira tijekom procesa finog podešavanja ili čak predtreniranja, omogućujući modelu da se prilagodi nižoj preciznosti i tako zadrži višu razinu točnosti (Jacob et al., 2018). Zahvaljujući napretku u kvantizacijskim tehnikama danas je često moguće postići značajnu kompresiju (npr. na 4 bita) uz vrlo mali ili gotovo nikakav gubitak performansi na nizvodnim zadacima, čineći kvantizaciju iznimno popularnom metodom za efikasnu implementaciju LLM-ova.

Treća važna tehnika optimizacije je **obrezivanje** (engl. *pruning*), koja se temelji na ideji da su mnogi veliki neuronski modeli preparametrizirani, odnosno sadrže značajan broj parametara (težina) ili čak cijelih strukturalnih komponenti koje su redundantne ili ne doprinose značajno konačnim performansama modela. Obrezivanje ima za cilj identificirati i trajno ukloniti te manje važne elemente, čime se smanjuje veličina modela i potencijalno ubrzava inferencija (LeCun et al., 1990; Han et al., 2015).

> **Obrezivanje / pruning:** Uklanjanje manje važnih parametara ili cijelih struktura (neuroni, slojevi, glave pozornosti) iz modela kako bi se smanjila veličina i ubrzala inferencija; može biti nestrukturirano (pojedinačne težine) ili strukturirano (cijele jedinice); često se kombinira s dodatnim finim podešavanjem (LeCun et al., 1990; Han et al., 2015).

Razlikujemo dva glavna tipa obrezivanja: nestrukturirano i strukturirano.

**Nestrukturirano obrezivanje** (engl. *unstructured*) uklanja pojedinačne težine iz matrica težina modela, obično na temelju nekog kriterija važnosti (npr. uklanjanje težina s najmanjom apsolutnom vrijednošću – engl. *magnitude pruning*). Iako može postići vrlo visoke stope prorjeđivanja (npr. ukloniti 90% ili više težina) uz zadržavanje točnosti, rezultirajuće matrice težina postaju rijetke (engl. *sparse*) s nepravilnim uzorcima nula. Standardni hardver (GPU, CPU) često nije optimiziran za efikasno iskorištavanje ovakve strukture, pa postignuto smanjenje broja parametara ne mora nužno dovesti do značajnog ubrzanja inferencije u praksi, osim ako se ne koristi specijalizirani hardver ili softverske biblioteke.

**Strukturirano obrezivanje** (engl. *structured*) uklanja cijele, pravilne strukturalne jedinice modela, kao što su pojedinačni neuroni, kanali u konvolucijskim mrežama, ili, u kontekstu transformera, cijele glave pažnje (engl. *attention heads*) ili čak cijeli slojevi (Li et al., 2016; Voita et al., 2019; Michel et al., 2019). Budući da se uklanjaju cijeli blokovi, rezultirajući model je manji, ali i dalje ima gustu strukturu koja se može efikasno izvršavati na standardnom hardveru, često dovodeći do stvarnih ubrzanja inferencije uz smanjenje broja parametara. Određivanje koje strukture ukloniti obično se temelji na procjeni njihove važnosti za performanse modela.

Obrezivanje se često izvodi iterativno: model se trenira, dio parametara se obreže, a zatim se model dodatno fino podešava kako bi se oporavio od potencijalnog pada točnosti uzrokovanog obrezivanjem. Zanimljiva poveznica je **Hipoteza** lutrijskog listića (engl. *Lottery Ticket Hypothesis*) (Frankle & Carbin, 2019), koja postulira da unutar velikih, nasumično inicijaliziranih neuronskih mreža postoje male podmreže („dobitni listići“) koje, kada se treniraju u izolaciji od samog početka s istom inicijalizacijom, mogu postići performanse usporedive s originalnom velikom mrežom. Iako pronalaženje tih *listića* nije trivijalno, ova hipoteza dodatno podupire ideju da su veliki modeli inherentno redundantni i da postoje znatno manje, efikasnije arhitekture koje čekaju da budu otkrivene ili ekstrahirane. Tehnike poput destilacije znanja (engl. *knowledge distillation*) (Hinton et al., 2015), gdje se znanje velikog *učiteljskog* modela prenosi na manji *učenički* model, također se često koriste, ponekad u kombinaciji s pruningom, za stvaranje manjih i bržih modela (npr. DistilBERT (Sanh et al., 2020)).

Tehnike poput parametarski efikasnog finog podešavanja, kvantizacije i pruninga, često korištene i u kombinaciji, predstavljaju ključne alate za premošćivanje jaza između teorijskih sposobnosti velikih jezičnih modela i zahtjeva praktične primjene u stvarnom svijetu. One čine LLM-ove ne samo izvedivijima za implementaciju u širem rasponu scenarija, uključujući one s ograničenim resursima, već i smanjuju njihove ekonomske i ekološke troškove, doprinoseći njihovoj demokratizaciji i otvarajući put prema održivijoj budućnosti umjetne inteligencije.


### 3.5.4 Mjerenje uspjeha: evaluacija (engl. evaluation)

Evaluacija predstavlja ključan, ali i slojevit postupak u razvoju i razumijevanju inteligentnih sustava, nadilazeći puko kvantitativno mjerenje kako bi obuhvatila i kritičku prosudbu njihove svrhovitosti i djelotvornosti. U kontekstu umjetne inteligencije i autonomnih agenata, evaluacija je nezaobilazna sastavnica cjelokupnoga istraživačkog i razvojnog ciklusa. Njezina temeljna svrha jest pružiti objektivan uvid u performanse agenta, pri čemu se njezina vrijednost ne iscrpljuje u pukom utvrđivanju uspješnosti. Naprotiv, smislena evaluacija nastoji proniknuti u razloge koji stoje iza određenog ishoda, objašnjavajući zašto i pod kojim uvjetima agent djeluje uspješno ili neuspješno. Time se otvara put prema ciljanim poboljšanjima i dubljem znanstvenom razumijevanju promatranih pojava (Smith, 2020).

U teorijskom i praktičnom smislu, uobičajeno je razlikovati dvije temeljne razine evaluacije, koje se međusobno ne isključuju, već nadopunjuju. To su interna i eksterna evaluacija.

**Interna evaluacija usredotočena je na analizu pojedinih sastavnica ili modula unutar samog agenta.** Njezin je cilj procijeniti djelotvornost specifičnih algoritama, modela ili mehanizama od kojih je agent sazdan. Primjerice, kod agenta zaduženog za obradu prirodnog jezika, interna evaluacija mogla bi zasebno mjeriti točnost modula za prepoznavanje entiteta ili uspješnost algoritma za semantičku analizu. Takav pristup omogućuje precizno lociranje nedostataka i optimizaciju pojedinih dijelova sustava neovisno o njegovu konačnom zadatku.

**Eksterna evaluacija,** s druge strane, promatra agenta kao cjelovitu, monolitnu cjelinu te mjeri njegovu uspješnost u izvršavanju konačnog, njemu namijenjenog zadatka unutar zadanog okruženja. U tom se pristupu zanemaruju unutarnji mehanizmi, a pozornost se usmjerava isključivo na ishod. Primjerice, ako je riječ o agentu za igranje šaha, eksterna evaluacija mjerila bi njegov postotak pobjeda protiv drugih igrača ili programa. Kod agenta za korisničku podršku mjerio bi se stupanj zadovoljstva korisnika ili vrijeme potrebno za rješavanje upita (Jones, 2021). Taj pristup daje konačnu ocjenu praktične uporabljivosti agenta.

Da bi evaluacijski postupak bio znanstveno utemeljen i vjerodostojan, mora počivati na nekoliko ključnih načela. Prije svega, evaluacija mora biti objektivna, što podrazumijeva korištenje jasno definiranih i mjerljivih metrika koje su neovisne o subjektivnoj prosudbi istraživača. Nadalje, ona mora biti ponovljiva (engl. *repeatable*), što znači da drugi istraživači, koristeći iste podatke, postavke i metodologiju, moraju moći dobiti istovjetne ili statistički usporedive rezultate. To načelo jamči provjerljivost i pouzdanost znanstvenih spoznaja. Jednako je važna i reproducibilnost (engl. *reproducible*), širi pojam koji podrazumijeva mogućnost da drugi timovi, polazeći od opisa metode, samostalno implementiraju sustav i provedu sličan eksperiment te dođu do sukladnih zaključaka.

U konačnici, evaluaciju ne valja shvatiti kao statičan čin presuđivanja, već kao dinamičan i integralan dio razvojnog procesa. Ona tvori povratnu spregu koja omogućuje kontinuirano poboljšanje. Rezultati evaluacije, bilo da su pozitivni ili negativni, pružaju dragocjene informacije koje usmjeravaju daljnji razvoj, ispravljanje pogrešaka i usavršavanje agenta. Time se uspostavlja iterativni ciklus koji je u samoj srži napretka u području umjetne inteligencije.


Iterativni razvojni ciklus agenta, gdje se nakon evaluacije i analize rezultata donosi odluka o poboljšanju i ponovnom razvoju ili završetku ciklusa


### 3.5.5	Model u akciji: inferencija 

Nakon što je model umjetne inteligencije uspješno obučen i vrednovan, on prelazi iz razvojne faze u fazu primjene. U toj fazi njegova temeljna svrha postaje djelovanje na novim podacima kako bi se stvorila vrijednost za korisnika ili sustav. Taj se proces, u kojemu model na temelju novih, prethodno neviđenih ulaznih podataka generira predviđanja, naziva inferencijom  (engl. *inference*). Ona predstavlja vrhunac cjelokupnog procesa razvoja modela, trenutak u kojemu se apstraktna znanja, stečena tijekom obučavanja, pretvaraju u konkretne i korisne odgovore.

Za razliku od postupka obučavanja, gdje se parametri modela dinamički prilagođavaju kako bi se što bolje preslikali ulazni podaci u željene izlazne vrijednosti, tijekom inferencije model ostaje statičan. Njegova naučena unutarnja struktura i parametri fiksirani su te se primjenjuju na nove podatke bez daljnjih izmjena (vidi npr. Goodfellow et al., 2016). Agent, bio on čovjek ili softverski sustav, unosi podatke u model – primjerice, sliku za klasifikaciju, rečenicu za prijevod ili skup senzorskih očitanja. Model potom, primjenjujući svoje naučene unutarnje reprezentacije, obrađuje te podatke i kao izlaz pruža relevantnu informaciju – predviđanje, klasifikaciju, sažetak ili neki drugi oblik strukturiranog odgovora.

![](../../docs/diagrams/ch03_inferencija.svg)
*Slika 3.5b: Osnovni tijek procesa inferencije, gdje se novi ulazni podatak provodi kroz statični, prethodno obučeni model kako bi se generirao izlaz.*

### 3.5.6. Načini i okruženja izvođenja inferencije

S tehničkog stajališta, inferencija se može provoditi na dva temeljna načina: skupno (engl. *batch*) i u stvarnom vremenu (engl. *real-time* ili *online*).

**Skupna inferencija podrazumijeva obradu velikih količina podataka odjednom,** u unaprijed definiranim ciklusima. Taj je pristup prikladan za primjene kod kojih trenutni odgovor nije presudan, kao što je generiranje dnevnih poslovnih izvješća, analiza tržišnih trendova na tjednoj bazi ili obrada arhivskih podataka. Glavna prednost toga načina jest visoka propusnost i učinkovitost obrade velikih skupova podataka.

> **Skupna inferencija / batch inference:** Način izvođenja modela u kojem se velike količine podataka obrađuju odjednom u unaprijed definiranim ciklusima; pogodan kada latencija nije kritična (izvješća, analize, arhiva); omogućuje visoku propusnost i učinkovitost.


**Inferencija u stvarnom vremenu pak odnosi se na obradu pojedinačnih ili malih skupina podataka čim postanu dostupni,** s naglaskom na minimalnoj latenciji, odnosno vremenu potrebnom za dobivanje odgovora. Takav je pristup nužan u sustavima kod kojih je brza reakcija ključna, primjerice u detekciji prijevara pri kartičnim transakcijama, sustavima za preporuke sadržaja na mrežnim stranicama ili u upravljanju autonomnim vozilima.

> **Inferencija u stvarnom vremenu:** Način izvođenja modela (engl. *real-time* ili *online* inferencija) u kojem se pojedinačni ili mali skupovi podataka obrađuju odmah po dostupnosti, s naglaskom na minimalnu latenciju; nužan u sustavima za detekciju prijevara, preporuke, autonomnu vožnju i slične primjene.


Izbor između skupne i inferencije u stvarnom vremenu usko je povezan s arhitekturom sustava i okruženjem u kojem se model izvršava. Modeli se često postavljaju na poslužitelje u oblaku (engl. *cloud*), što omogućuje skalabilnost i pristup velikim računskim resursima, ali može uvoditi latenciju zbog mrežne komunikacije. S druge strane, kako bi se latencija smanjila i osigurala privatnost podataka, modeli se sve češće izvode na rubnim uređajima (engl. *edge computing*), poput pametnih telefona, industrijskih senzora ili automobila, ili na lokalnoj infrastrukturi (engl. *on-premise*).

> **Edge computing:** Izvođenje računalne obrade i modela na rubnim uređajima (telefoni, senzori, vozila) umjesto isključivo u centralnom oblaku; smanjuje latenciju i potrebu za prijenosom podataka, pogodno za privatnost i aplikacije u stvarnom vremenu.

Inferencija je dakle trenutak u kojemu apstraktni matematički model postaje konkretan alat, sposoban donositi odluke, automatizirati procese i pružati uvide u stvarnom svijetu. Ona je most između teorije strojnog učenja i njegove praktične primjene.

## 3.6 Izazovi i ograničenja: sjene u digitalnom ogledalu

Dok veliki jezični modeli demonstriraju sve impresivnije sposobnosti u razumijevanju i generiranju jezika, otvarajući vrata transformativnim primjenama u gotovo svim sferama ljudskog djelovanja, njihov brzi razvoj i implementacija neizbježno su praćeni nizom ozbiljnih izazova i inherentnih ograničenja koja bacaju sjenu na njihov potencijal. Pitanja vezana uz **sigurnost njihovog korištenja, **pouzdanost informacija koje generiraju, te potencijal za zlouporabu njihovih moćnih sposobnosti, predstavljaju kritične prepreke koje se ne smiju zanemariti. 


> **Pristranost / bias:** Sistemsko odstupanje u ponašanju algoritma ili modela koje proizlazi iz podataka za obuku – npr. društvenih predrasuda, stereotipa ili nedovoljne zastupljenosti određenih skupina; može dovesti do diskriminacije u odlukama (zapošljavanje, kredit, kazneni postupci) i perpetuiranja nepravde (O'Neil, 2016).

Jedna od temeljnih poteškoća, ukorijenjena u samoj biti strojnog učenja, jest pitanje algoritamske pristranosti. Sustavi umjetne inteligencije uče na temelju podataka koje im čovjek pruža, a ti podaci nerijetko odražavaju postojeće društvene predrasude, stereotipe i nejednakosti. Algoritam, kao matematički nepristran entitet, ne može sam od sebe ispraviti ljudske manjkavosti utkane u podatkovne skupove; on ih, štoviše, može pojačati i automatizirati, stvarajući tako sustave koji sustavno diskriminiraju određene skupine ljudi pri zapošljavanju, odobravanju kredita ili čak u kaznenopravnim postupcima (O'Neil, 2016.). Time se tehnologija, umjesto da bude oruđe za postizanje pravednosti, pretvara u sredstvo za perpetuiranje i legitimiranje nepravde.

Na to se izravno nadovezuje problem transparentnosti i objašnjivosti, često sažet u pojmu „ crne kutije “ (engl. *black box*). Mnogi napredni modeli umjetne inteligencije, poput dubokih neuronskih mreža, djeluju na način koji je iznimno teško ili čak nemoguće u potpunosti protumačiti. Iako sustav može donijeti iznimno preciznu odluku ili predviđanje, put kojim je do te odluke došao ostaje skriven unutar složenih slojeva matematičkih operacija. Taj manjak transparentnosti postavlja ozbiljne prepreke, osobito u područjima visokog rizika kao što su medicina ili autonomna vožnja. Kako vjerovati odluci stroja ako ne razumijemo njezinu logiku? Tko snosi odgovornost kada takav neobjašnjiv sustav pogriješi? Nemogućnost uvida u rezoniranje agenta potkopava povjerenje i onemogućuje učinkovitu kontrolu i ispravljanje pogrešaka (Pasquale, 2015.).

Osim tehničkih zapreka, primjena umjetne inteligencije postavlja i duboke društvene i ekonomske izazove. Automatizacija, pokretana sve sposobnijim inteligentnim agentima, prijeti transformacijom tržišta rada na dosad neviđenoj razini. Dok su prethodne industrijske revolucije uglavnom zamjenjivale manualni rad, današnja tehnologija sve više zadire i u kognitivne zadatke koji su se smatrali isključivo ljudskom domenom. Postavlja se pitanje masovnog gubitka radnih mjesta i posljedičnog rasta ekonomske nejednakosti. Stvaranje novih poslova možda neće ići ukorak s nestajanjem starih, što može dovesti do produbljivanja digitalnog jaza – ne samo u pristupu tehnologiji, već i u vještinama potrebnima za snalaženje u novom ekonomskom poretku.

U središtu ovih tehnoloških i društvenih mijena stoji čovjek, čija se privatnost, autonomija i dobrobit nalaze pred novim iskušenjima. Djelovanje inteligentnih sustava počiva na prikupljanju i obradi golemih količina podataka, često osobnih. Time se brišu granice između privatnog i javnog, a mogućnosti nadzora postaju gotovo neograničene. Stalno praćenje digitalnih tragova, koje provode i korporacije i državni aparati, otvara vrata manipulaciji, od suptilnog utjecaja na potrošačke navike do oblikovanja političkog mišljenja unutar personaliziranih informacijskih mjehurića i jeka (Zuboff, 2019). Čovjekova autonomija u donošenju odluka time je ugrožena, a njegova izloženost algoritamskom upravljanju sve veća.

Nadalje, valja upozoriti i na opasnost od pretjeranog oslanjanja na tehnologiju i postupnog gubitka ljudskih vještina. Prepustimo li kritičko razmišljanje, pamćenje ili čak kreativnost strojevima, riskiramo vlastitu kognitivnu atrofiju. Sposobnost strojeva da generiraju uvjerljiv tekst, slike i zvukove postavlja i pitanje autentičnosti i istine. U svijetu u kojem je sve teže razlikovati stvarno od lažnog, a dezinformacije se šire brzinom svjetlosti, povjerenje u institucije i u sam medijski prostor biva duboko poljuljano.

Naposljetku, svi navedeni izazovi upućuju na temeljnu potrebu za uspostavom čvrstih etičkih okvira i regulatornih mehanizama. Razvoj tehnologije daleko nadmašuje brzinu kojom se donose zakoni, stvarajući regulatorni vakuum u kojem se odluke o budućnosti čovječanstva prepuštaju tehnološkim tvrtkama vođenima profitnim interesima. Pitanje odgovornosti, globalna priroda umjetne inteligencije koja izmiče nacionalnim zakonodavstvima te opasnost od njezine zlouporabe u vojne svrhe i stvaranja autonomnog oružja samo su neki od problema koji zahtijevaju hitnu i usklađenu međunarodnu suradnju.

Suočavanje sa sjenama u digitalnom ogledalu nije poziv na odbacivanje tehnologije već na njezin promišljen i odgovoran razvoj. Prepoznavanje izazova prvi je korak prema njihovu rješavanju – korak koji zahtijeva suradnju stručnjaka iz različitih područja, od tehničkih znanosti do filozofije i prava, kako bi se osiguralo da umjetna inteligencija uistinu služi dobrobiti cijelog čovječanstva, a ne samo uskom krugu povlaštenih.

### 3.6.1 Sigurnost, pouzdanost i zlouporaba

Svako cjelovito promišljanje o dosezima i primjeni autonomnih agenata neizbježno dotiče tri ključna i međusobno isprepletena područja: sigurnost sustava, njegovu pouzdanost u djelovanju te mogućnosti zlouporabe. Ta tri elementa tvore temeljni okvir za procjenu održivosti, etičnosti i praktične uporabljivosti bilo kojeg agentskog sustava, jer zanemarivanje ijednoga od njih može dovesti do ozbiljnih tehničkih, društvenih ili sigurnosnih posljedica.

#### Sigurnost

Sigurnost se, u kontekstu autonomnih agenata, odnosi na zaštitu sustava, njegovih podataka i procesa od neovlaštenog pristupa, izmjena ili uništenja. Ona obuhvaća tehničke mjere kojima se osigurava cjelovitost i povjerljivost sustava, ali i njegova otpornost na vanjske napade. Zlonamjerni akteri mogu pokušati iskoristiti ranjivosti u programskom kodu, arhitekturi sustava ili komunikacijskim protokolima kako bi preuzeli kontrolu nad agentom, ukrali osjetljive podatke s kojima agent barata ili ga onemogućili u radu.

Poseban izazov u području umjetne inteligencije predstavljaju takozvani *suparnički napadi* (engl. *adversarial attacks*), gdje se ulazni podaci (primjerice, slika ili tekst) suptilno mijenjaju na način koji je čovjeku neprimjetan, ali koji agenta navodi na potpuno pogrešan zaključak ili djelovanje (Goodfellow et al., 2014).

> **Suparnički napad / adversarial attack:** Namjerna izmjena ulaznih podataka (slike, teksta) suptilna za ljudsko oko, ali koja navodi model na pogrešnu klasifikaciju ili odluku; zahtijeva robusne modele i mehanizme provjere izvan tradicionalne informacijske sigurnosti (Goodfellow et al., 2014).

Zaštita od takvih napada zahtijeva robusne modele i mehanizme provjere koji nadilaze tradicionalne metode informacijske sigurnosti. Sigurnosni propust ne ugrožava samo funkcionalnost agenta, već izravno potkopava povjerenje korisnika i otvara vrata daljnjim zlouporabama.

#### Pouzdanost

Usko povezana sa sigurnošću jest i pouzdanost, koja označava dosljednost i predvidljivost u radu agenta. Dok se sigurnost bavi zaštitom od vanjskih prijetnji, pouzdanost se usredotočuje na unutarnju ispravnost i robusnost sustava. Pouzdan agent mora dosljedno izvršavati svoje zadaće u skladu s definiranim parametrima i ciljevima, čak i u nepredviđenim okolnostima ili pri susretu s novim, neočekivanim podacima.

Sustav koji je pouzdan nije krhak; on je otporan na pogreške uzrokovane rubnim slučajevima, šumom u podacima ili vlastitim unutarnjim ograničenjima. Jedan od ključnih problema pouzdanosti u suvremenim jezičnim modelima jest fenomen „halucinacija“, gdje agent generira uvjerljive, ali činjenično netočne ili besmislene informacije (Ji et al., 2023). Osiguravanje pouzdanosti stoga podrazumijeva rigorozno testiranje, validaciju i uspostavu mehanizama za detekciju i ispravljanje anomalija u ponašanju agenta. Nepouzdan agent, čak i ako je savršeno siguran, gubi svoju praktičnu vrijednost jer se na njegove odluke i ishode nije moguće osloniti.

#### Zlouporaba

Naposljetku, treći član toga trojstva jest zlouporaba, koja se odnosi na namjerno korištenje agenta u štetne, neetične ili nezakonite svrhe. Za razliku od sigurnosnih propusta koje iskorištavaju vanjski napadači, zlouporaba podrazumijeva da se agent koristi onako kako je dizajniran, ali za postizanje zlonamjernih ciljeva. Paradoksalno, upravo one značajke koje agente čine moćnima – autonomija, sposobnost učenja, prilagodbe i vođenja složenih interakcija – ujedno otvaraju i vrata njihovoj zlouporabi.

Mogućnosti zlouporabe su mnogostruke: od automatiziranog širenja dezinformacija i propagande, preko izvođenja sofisticiranih napada socijalnog inženjerstva i krađe identiteta, do koordinacije zlonamjernih aktivnosti u digitalnom ili fizičkom svijetu. Agent se može upotrijebiti za stvaranje lažnog sadržaja (engl. *deepfakes*), zaobilaženje sigurnosnih provjera ili automatizaciju procesa koji štete pojedincima ili organizacijama. Problem zlouporabe nadilazi isključivo tehničku domenu i zalazi duboko u etička i pravna pitanja, postavljajući pred društvo izazov uspostave normi i regulativa koje će umanjiti potencijalne štete.

Ta tri aspekta – sigurnost, pouzdanost i zlouporaba – nisu neovisne kategorije, već čine dinamičan i povezan sustav. Slaba sigurnost olakšava zlouporabu, dok niska pouzdanost može stvoriti nepredviđene sigurnosne ranjivosti. Učinkovito suočavanje s tim izazovima zahtijeva holistički pristup koji objedinjuje tehničke inovacije u području robusnosti i zaštite, s jasnim etičkim smjernicama i pravnim okvirima za odgovoran razvoj i primjenu tehnologije autonomnih agenata.



Međusobna povezanost sigurnosti, pouzdanosti i zlouporabe. Slabosti u jednom području izravno utječu na druga dva, stvarajući ciklus u kojem se rizici međusobno pojačavaju

### 3.6.2 Pristranost, privatnost i etika podataka: tamna strana digitalnih ogledala

Digitalni sustavi, napose oni utemeljeni na umjetnoj inteligenciji i strojnomu učenju, često se poimaju kao objektivna, neutralna ogledala koja odražavaju svijet onakvim kakav jest. Ta metafora, premda zavodljiva, prikriva dublju i složeniju istinu. Ogledala koja stvaramo nisu savršeno ravna niti besprijekorno čista; ona su izobličena, a odrazi koje nude nose u sebi sjene pristranosti, narušene privatnosti i etičkih dvojbi koje proistječu iz samih temelja na kojima su sazdana – iz podataka. Promatranje tamne strane tih digitalnih ogledala ključno je za razumijevanje njihova stvarnog utjecaja na društvo.

Temeljni problem proizlazi iz prirode podataka kojima se algoritmi napajaju. Suprotno raširenomu, gotovo mitskomu uvjerenju o objektivnosti stroja, algoritamska pristranost nije intrinzična mana koda, već neizbježan odraz podataka kojima se algoritam „hrani“. Ti podaci nisu apstraktni entiteti već destilirano ljudsko iskustvo, sa svim svojim povijesnim nepravdama, društvenim nejednakostima i predrasudama. Kada algoritam uči iz podataka o zapošljavanju koji odražavaju desetljeća diskriminacije prema ženama u određenim sektorima, on ne uči o objektivnim kvalifikacijama, već o povijesnoj stvarnosti. Njegov će model, posljedično, perpetuirati tu istu diskriminaciju, ne iz zlobe, već iz logike naučenog obrasca. Sustavi za prepoznavanje lica koji pokazuju znatno nižu točnost za osobe tamnije puti ili žene nisu rezultat lošeg programiranja već nedovoljne i nereprezentativne zastupljenosti tih skupina u podatkovnim setovima za obuku (Buolamwini & Gebru, 2018). Time digitalno ogledalo ne samo da odražava postojeću društvenu manu nego je i pojačava, dajući joj privid tehnološke neupitnosti i stvarajući opasan začarani krug.





![Shematski prikaz ciklusa u kojem pristrani podaci vode do pristranih modela, čije odluke potom jačaju i legitimiraju početne društvene pristranosti](../../docs/diagrams/diag_200.svg)
*Slika 3.9: Shematski prikaz ciklusa u kojem pristrani podaci vode do pristranih modela, čije odluke potom jačaju i legitimiraju početne društvene pristranosti.*

Uz problem pristranosti jednako se tako ozbiljno postavlja i pitanje privatnosti. Doba velikih podataka (engl. *Big Data*) iznjedrilo je ekonomiju nadzora (engl. *surveillance capitalism*), u kojoj se osobni podaci smatraju sirovinom, najvrednijim resursom novoga doba (Zuboff, 2019). Svaki naš digitalni trag – od pretraga na internetu, preko lokacijskih podataka i komunikacije na društvenim mrežama, do biometrijskih informacija – postaje predmetom prikupljanja, obrade i monetizacije. Granica između privatne i javne sfere postaje sve propulzivnija, a pristanak koji korisnici daju često je tek iluzija, skriven iza neprobojnih pravnih formulacija i nepreglednih korisničkih uvjeta. Posljedice takva stanja sežu dublje od ciljanog oglašavanja. Gubitak privatnosti ugrožava samu srž osobne autonomije, slobodu izražavanja i mogućnost djelovanja bez straha od stalnog nadzora i prosuđivanja. Kada podaci o našemu zdravlju, političkim uvjerenjima ili intimnim odnosima postanu dostupni trećim stranama – bilo da je riječ o korporacijama, državnim tijelima ili zlonamjernim *agentima* – otvara se prostor za manipulaciju, ucjenu i društvenu kontrolu nesagledivih razmjera.

Naposljetku, pristranost i privatnost stapaju se u jedinstven i slojevit etički izazov. Tko snosi odgovornost za štetu koju počini pristran algoritam? Je li to programer koji je napisao kôd, tvrtka koja je sustav implementirala, korisnik koji je nekritički prihvatio njegovu odluku ili pak društvo koje je stvorilo podatke opterećene nepravdom? Tradicionalni modeli odgovornosti, osmišljeni za ljudske aktere i predvidljive uzročno-posljedične lance, pokazuju se nedostatnima u svijetu u kojem autonomni *agenti* donose odluke s dalekosežnim posljedicama. To od nas zahtijeva razvoj novih etičkih okvira koji će moći obuhvatiti složenost digitalnog ekosustava. Potrebna je korjenita promjena paradigme: od reaktivnog ispravljanja pogrešaka prema proaktivnom, etički utemeljenom dizajnu (engl. *Ethics by Design*). To podrazumijeva transparentnost u radu algoritama, pravo na objašnjenje automatiziranih odluka te uspostavu neovisnih tijela za nadzor i reviziju.

Digitalna ogledala stoga nisu pasivni promatrači, već aktivni sudionici u preoblikovanju naše stvarnosti, često na načine koji su suptilni, ali duboko utjecajni. A izazov koji stoji pred nama nije u tome da ta ogledala razbijemo, već da naučimo kako ih graditi s mudrošću i održavati s osjećajem odgovornosti, svjesni da odraz koji u njima vidimo nije samo slika svijeta kakav jest, već i nacrt svijeta kakav bi, našim djelovanjem ili nedjelovanjem, mogao postati.

### 3.6.3 Resursna intenzivnost: cijena inteligencije

Svako očitovanje inteligencije, bilo ono biološko ili umjetno stvoreno, sa sobom nosi neizbježan trošak. U domeni umjetne inteligencije, napose u području dubokih neuronskih mreža i velikih jezičnih modela, taj trošak poprima goleme razmjere, očitujući se ne samo u financijskim izdacima, već i u potrošnji materijalnih i energetskih resursa. Stremljenje k sve naprednijim i sposobnijim agentima stvorilo je paradigmu u kojoj se složenost i performanse modela izravno povezuju s količinom uloženih računalnih resursa. Ta resursna intenzivnost postala je stoga ključno obilježje suvremenog razvoja umjetne inteligencije, namećući temeljna pitanja o njezinoj održivosti, dostupnosti i ekološkim posljedicama.

> **Resursna intenzivnost:** Zahtjevnost razvoja i primjene AI modela u smislu računalne snage, memorije, energije i financijskih troškova; posebno izražena kod velikih jezičnih modela čiji treninzi i inferencija zahtijevaju masivne klastere GPU/TPU, što ograničava dostupnost i ima ekološke posljedice.

Temeljni pokretač te iznimne računalne gladi jest paradigma skaliranja, empirijski potvrđena zakonitost prema kojoj se performanse modela poboljšavaju predvidljivom stopom s porastom broja parametara, veličine skupa podataka za učenje i količine računalne snage uložene u proces učenja (Kaplan et al., 2020).

> **Zakon skaliranja / scaling laws:** Empirijski uvid prema kojemu performanse jezičnih modela predvidljivo rastu s povećanjem tri faktora: broja parametara modela, količine podataka za učenje i količine računalne snage; potaknuo je utrku u izgradnji sve većih modela (Kaplan et al., 2020).

Ta je spoznaja potaknula svojevrsnu utrku u izgradnji sve većih modela, čije arhitekture sadrže stotine milijardi, pa i trilijune, parametara. Učenje takvih kolosalnih struktura zahtijeva dugotrajne i složene izračune na specijaliziranim sklopovima, poput grafičkih procesorskih jedinica (GPU) i tenzorskih procesorskih jedinica (TPU), organiziranih u masivne klastere koji djeluju tjednima ili čak mjesecima bez prestanka.

> **TPU:** Tenzorska procesorska jedinica (engl. *Tensor Processing Unit*) – čip dizajniran za ubrzanje operacija strojnog učenja, posebno matričnih izračuna u dubokim mrežama; optimiziran za visoku propusnost i energetsku učinkovitost u treniranju i inferenciji velikih modela.
 Troškovi takvog pothvata dosežu desetke, a ponekad i stotine milijuna dolara samo za jedan ciklus učenja, obuhvaćajući cijenu hardvera, električne energije i održavanja.

Izravna posljedica te goleme potrošnje energije jest značajan ekološki otisak. Proces učenja velikih modela umjetne inteligencije jedan je od energetski najintenzivnijih računalnih zadataka. Studije koje su nastojale kvantificirati taj utjecaj dale su zabrinjavajuće rezultate. Primjerice, procjenjuje se da je proces učenja jednoga velikog jezičnog modela s pretraživanjem arhitekture proizveo količinu ugljičnog dioksida koja je usporediva s pet prosječnih životnih ciklusa automobila, uključujući i njihovu proizvodnju (Strubell et al., 2019). Ta spoznaja stavlja tehnološki napredak u izravan sukob s globalnim naporima za smanjenje emisija stakleničkih plinova, namećući etičku dilemu istraživačima i tvrtkama koje djeluju u tome području.



Povećanje veličine modela i podataka vodi eksponencijalnom rastu računalnih zahtjeva, rezultirajući visokim financijskim troškovima, velikom potrošnjom energije te preprekama za demokratizaciju i značajnim ekološkim otiskom

Nadalje, visoka cijena računalnih resursa stvara dubok jaz i postavlja ozbiljne prepreke za demokratizaciju tehnologije. Razvoj najnaprednijih modela postaje isključivo područje djelovanja malog broja tehnoloških divova i nacionalnih laboratorija koji posjeduju dostatan kapital i infrastrukturu. Akademske institucije, neovisni istraživači i manje tvrtke sve teže mogu pratiti taj tempo, što dovodi do konsolidacije moći i utjecaja u rukama nekolicine. > **Računalni jaz:** Asimetrija u pristupu računalnim resursima (GPU/TPU, energija, kapital) potrebnim za razvoj i pokretanje velikih AI modela; ograničava koji akteri mogu sudjelovati u razvoju, što vodi konsolidaciji moći i pristranostima u tehnologiji.

Takav „računalni jaz“ ograničava raznolikost ideja, usporava znanstvenu recenziju i replikaciju rezultata te otvara prostor za pristranosti koje odražavaju vrijednosti i interese onih koji mogu sebi priuštiti razvoj takvih sustava.

Važno je razlikovati i troškove učenja (engl. *training costs*) od troškova primjene, odnosno zaključivanja (engl. *inference costs*).

> **Troškovi učenja i troškovi zaključivanja:** Troškovi učenja (engl. *training costs*) – jednokratni, ali iznimno visoki troškovi treniranja modela (hardver, energija, vrijeme). Troškovi zaključivanja (engl. *inference costs*) – kontinuirani operativni troškovi primjene već naučenog modela na svaki upit; na milijardama upita dnevno kumulativno mogu biti golemi.

Dok je učenje jednokratan, ali iznimno intenzivan proces, zaključivanje se odnosi na kontinuiranu uporabu već naučenog modela za obavljanje konkretnih zadataka. Iako je potrošnja resursa za pojedinačno zaključivanje znatno manja od one za učenje, kumulativni trošak može biti golem kada se model primjenjuje na milijunima ili milijardama upita dnevno, kao što je slučaj s popularnim digitalnim pomoćnicima ili prevoditeljskim uslugama. Stoga, u ukupnu cijenu inteligencije treba ubrojiti investicije potrebne za njezino stvaranje, kao i trajni operativni trošak njezina postojanja i djelovanja. Suočavanje s tim višeslojnim izazovom zahtijeva pomak prema razvoju energetski učinkovitijih algoritama, optimiziranih hardverskih rješenja i transparentnijem izvještavanju o stvarnoj cijeni napretka u području umjetne inteligencije.

## 3.7 Transformacija komunikacije: primjene i perspektive

Pojava i sve šira primjena umjetne inteligencije, a napose velikih jezičnih modela, unosi korjenite promjene u samu srž ljudske komunikacije, preobličujući njezine temeljne paradigme i otvarajući neslućene mogućnosti, ali i postavljajući nove izazove. Svjedočimo razdoblju u kojem se tehnologija prestaje poimati isključivo kao pasivni kanal ili alat i poprima obilježja aktivnoga sudionika, pa čak i sukreatora komunikacijskih procesa. Ta transformacija iz temelja mijenja način na koji pojedinci, organizacije i čitava društva stvaraju, razmjenjuju i tumače informacije.

Jedna od najistaknutijih primjena očituje se u mogućnosti stvaranja hiperpersonaliziranih sadržaja, gdje se komunikacijske poruke kroje prema specifičnim potrebama, interesima i prethodnom ponašanju pojedinog korisnika. U području marketinga i oglašavanja to omogućuje dostavljanje relevantnih ponuda koje znatno povećavaju angažman potrošača, nadilazeći tradicionalne, masovne pristupe (Chen i sur., 2021). Slična se načela primjenjuju i u medijima, gdje algoritmi predlažu vijesti i članke u skladu s čitateljevim navikama, stvarajući jedinstveno informacijsko iskustvo za svakog pojedinca.

Ta se načela personalizacije protežu i na područje korisničke podrške, koje doživljava temeljitu preobrazbu. Nekoć ograničeni i skriptirani *chatboti* ustupaju mjesto naprednim konverzacijskim agentima koji su sposobni voditi složene dijaloge, razumjeti kontekst i pružati rješenja za širok spektar korisničkih upita u stvarnom vremenu. Takvi sustavi ne samo da povećavaju učinkovitost i smanjuju operativne troškove već i poboljšavaju korisničko zadovoljstvo pružanjem trenutačne i stalno dostupne podrške (Kumar i sur., 2022).

Nadalje, umjetna inteligencija postaje nezaobilazan čimbenik u samom procesu stvaranja sadržaja. Veliki jezični modeli danas se koriste za sastavljanje marketinških tekstova, novinskih izvješća, objava za društvene mreže, pa čak i za pisanje programskoga koda ili kreativnih književnih djela. Uloga ljudskoga stvaratelja time se mijenja – on sve više postaje urednik, kustos ili suradnik koji usmjerava i dorađuje sadržaj koji generira stroj. Takav suradnički odnos otvara goleme stvaralačke mogućnosti, ali istodobno pokreće i složena pitanja o autorstvu, izvornosti i vjerodostojnosti informacija (Liang i sur., 2023).

Promatrano u dugoročnoj perspektivi, razvoj autonomnih agenata predstavlja možda i najdublju promjenu koja se nazire na obzoru. Ti sofisticirani softverski entiteti, osnaženi umjetnom inteligencijom, zamišljeni su tako da djeluju proaktivno uime svojih korisnika, obavljajući složene zadatke koji zahtijevaju planiranje i interakciju s drugim sustavima i ljudima. Agent bi, primjerice, mogao samostalno organizirati poslovno putovanje, pregovarati o uvjetima ugovora ili upravljati korisnikovim digitalnim identitetom. U takvom scenariju komunikacija se više ne odvija samo između ljudi ili između čovjeka i stroja već i između samih autonomnih agenata koji zastupaju ljudske interese.


Evolucijski tijek komunikacijskih paradigmi pod utjecajem umjetne inteligencije

Naposljetku, valja istaknuti kako ova tehnološka revolucija sa sobom nosi i znatne etičke i društvene implikacije. Mogućnost generiranja uvjerljivih, ali lažnih informacija (engl. *deepfakes*) predstavlja ozbiljnu prijetnju društvenom povjerenju i demokratskim procesima. Automatizacija komunikacijskih uloga postavlja pitanja o budućnosti radnih mjesta, dok sveprisutna posredovanost tehnologijom potiče rasprave o otuđenju i gubitku autentičnosti u međuljudskim odnosima (Brynjolfsson i McAfee, 2018). Stoga, usporedno s tehnološkim napretkom, od presudne je važnosti razvijati i snažne etičke okvire te mehanizme nadzora koji će osigurati da transformacija komunikacije služi dobrobiti čovječanstva, a ne njegovu potkopavanju. Budućnost komunikacije bit će neizbježno oblikovana suigrom ljudske ingenioznosti i umjetne inteligencije, a ishod te suigre ovisit će o mudrosti kojom budemo upravljali njezinim razvojem.