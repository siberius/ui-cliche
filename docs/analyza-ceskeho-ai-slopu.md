# Hloubková analýza AI klišé v češtině a metodika tvorby anti-slop skillu

Texty generované velkými jazykovými modely (LLM) v češtině i strojové lokalizace z angličtiny vykazují předvídatelnou síť lexikálních, syntaktických a typografických vzorců, která se v komunitním i odborném diskurzu označuje jako **AI slop** (v češtině volně překládané jako *AI břečka* nebo *AI balast*)¹. Hloubková analýza českého prostředí ukazuje, že tento jev nevzniká pouze nadužíváním přeložených anglických buzzwordů (jako „v dnešní dynamické době“, „hraje klíčovou roli“, „ponořit se do tématu“ či „bohatá tapiserie“), ale především strukturálním střetem anglické pravděpodobnostní distribuce tokenů s českou mluvnicí¹. Empirické srovnání 18 světových modelů v projektu **cestina.ai** vzdělávací společnosti Scio (říjen 2026) ukázalo, že bez explicitního pokynu ke stručnosti píší modely v češtině zhruba o třetinu delší texty než lidé, přičemž jejich míra přirozenosti dosahuje podle evaluačního modelu pouze $37\text{--}57\ \%$ oproti $86\ \%$ u původních lidských textů⁵. V e-commerce lokalizacích pak podle analýzy lokalizační platformy LocoGlobal (na vzorku $141\,113$ produktů v $72$ jazycích) doslovný AI překlad bez kontextu a glosáře způsobuje terminologický chaos a propad lokálního SEO na průměrných $56$ bodů ze $100$, což e-shopy připravuje o $20\text{--}30\ \%$ tržního potenciálu⁷.

Zatímco v angličtině se proti generickému stylu AI prosadily open-source instrukční soubory (`SKILL.md`) z repozitářů jako `no-ai-slop` (autor Peter Yang)⁸ nebo `stop-slop` (autor Azayzel)¹⁰ vycházející z komunitního katalogu Wikipedie *Signs of AI writing* (`WP:AISIGNS`)¹², prostý překlad těchto pravidel do češtiny nestačí. Český anti-slop systém musí kromě univerzálních nešvarů (negativní paralelismus „nejde jen o X, ale o Y“, pravidlo tří, alibistické odvolávání na nejmenované odborníky a kompulzivní shrnutí) řešit také **morfosyntaktické kalky z angličtiny**. Patří sem zejména porušování aktuálního členění větného (funkční větné perspektivy), nadužívání přivlastňovacích zájmen (*váš/jeho/její*) na úkor českého zvratného *svůj* (nebo jejich úplného vypuštění), toporný opisný trpný rod a falešná agencie neživotných podmětů¹¹. Neméně kritická je rovina české typografie podle normy **ČSN 01 6910**, kde AI modely pravidelně chybují v používání anglických či rovných uvozovek (`" "` místo `„ “`), čtverčíkových pomlček (`—`) či spojovníků (`-`) místo půlčtverčíkových pomlček (`–`), v chybném sázení procent bez mezery (`50%` místo `50 %`) a v absenci pevných mezer za neslabičnými předložkami¹⁷.

Tato zpráva předkládá taxonomii českého AI slopu, komparativní rozbor selhání v autorském psaní i lokalizaci a na jejich základě definuje metodiku i kompletní produkční šablonu souboru `SKILL.md` pro AI agenty (Claude Code, Cursor, Codex, Gemini CLI, OpenClaw)²⁰. Navržený skill je rozdělen do dvou provázaných pilířů: **Obecné sekce** (univerzální strukturální, rétorická a obsahová pravidla vycházející z metodik `no-ai-slop` a `stop-slop`) a **Sekce lokalizace a českých specifik** (pravidla pro přirozený český slovosled, slovesnou valenci, typografickou normu a konverzní adaptaci textu)¹⁶.

---

## Empirická anatomie AI břečky (AI Slop) a limity detekce v českém prostředí

Pojem *AI slop* (česky břečka či balast) se začal masově šířit v květnu 2024, kdy jej uživatel `@deepfates` a následně vývojář Simon Willison přirovnali k tomu, čím je nevyžádaný spam pro e-mailovou komunikaci, a v roce 2025 byl zvolen slovem roku institucemi Merriam-Webster, American Dialect Society i Macquarie Dictionary¹. V odborné praxi se termín používá ve dvou rovinách: v širším významu označuje masově produkovaný digitální obsah s minimem lidské práce, který na první pohled působí hotově, ale čtenáři nepřináší žádnou přidanou hodnotu. V užším, technickém významu označuje specifické statistické a stylistické tiky velkých jazykových modelů. 

Na tuto terminologii navazuje širší ekosystém pojmů mapujících dopady syntetického balastu, jak je shrnuje přehledová studie Daniela Votruby (dfriends.cz, říjen 2026)¹:
* **Workslop** označuje uhlazené, ale prázdné pracovní výstupy přesouvající dřinu na příjemce (podle průzkumu BetterUp Labs a Stanford Social Media Lab publikovaného v *Harvard Business Review* v září 2025 na vzorku $1\,150$ amerických zaměstnanců se s ním měsíčně setkalo přibližně $40\ \%$ pracovníků, přičemž každý incident stál v průměru $1$ hodinu a $56$ minut času, resp. $186\ \text{USD}$ měsíčně na zaměstnance)¹.
* **Botshit** popisuje neověřené halucinace chatbotů použité pro firemní rozhodování¹.
* **Sycophancy** označuje podlézavost modelů (kvůli níž OpenAI v dubnu 2025 stáhlo přehnaně vstřícnou aktualizaci GPT-4o a Anthropic v květnu 2025 zakázal modelu Claude 4 v systémovém promptu úvodní pochvaly)¹.
* **Model collapse** postihuje degradaci modelů trénovaných rekurzivně na syntetických datech (popsanou Shumailovem a kol. v časopise *Nature* v červenci 2024)¹.

Z pohledu matematické lingvistiky vzniká AI slop tím, že jazykové modely generují text predikcí statisticky nejpravděpodobnějšího následujícího tokenu vzhledem k předchozímu kontextu³. Tento mechanismus vede ke dvěma vlastnostem, na nichž staví moderní detektory AI: **nízké perplexitě** (míra nepředvídatelnosti volby slov je u modelu nízká, protože vybírá nejčastější kolokace) a **nízké burstiness** (nízká variabilita délky a rytmu vět)³. Zatímco lidské psaní přirozeně střídá krátké, úderné oznamovací věty se složitými souvětími podle emocionální váhy sdělení, neupravený text z AI má metronomický rytmus, v němž se věty shlukují kolem stejné střední délky a jednotné syntaktické kostry³. Benchmark **EQ-Bench** kvantifikuje tuto šablonovitost pomocí metriky *Slop Score*, v níž $60\ \%$ váhy tvoří nadužívaná slova, $25\ \%$ váhy kontrastní konstrukce typu „not just X, but Y“ („nejde jen o X, ale o Y“) a $15\ \%$ váhy nadužívané tříslovné fráze¹. Studie autorů Sun a kol. (ICML 2025) navíc pomocí TF-IDF analýzy ukázala, že jednotlivé modely lze podle jejich lexikálních a formátovacích tiků identifikovat s přesností $97{,}1\ \%$: modely rodiny ChatGPT (OpenAI) statisticky nadužívají dlouhé pomlčky a výrazy *certainly*, *overall* a *typically*, zatímco modely Claude (Anthropic) preferují opatrné obraty (*according to*, *based on*, *appears to*) a používají výrazně méně tučného písma i podnadpisů¹.

---

### [GRAF 1] České AI texty jsou o třetinu delší a ztrácejí až 49 procentních bodů přirozenosti
*Empirická anatomie generovaného textu v češtině (Scio cestina.ai), globální váhy AI klišé (EQ-Bench) a chybovost detektorů*

#### 1. Přirozenost a relativní délka českých textů
*(Benchmark Scio cestina.ai, říjen 2026, srovnání 18 modelů)*

| Ukazatel / Skupina modelů | Skóre přirozenosti / Délka | Vizuální znázornění | Poznámka |
| :--- | :--- | :--- | :--- |
| **Lidský originál (baseline)** | **$86\ \%$** | `█████████████████░░░` | Reálné e-maily, dopisy a interní zprávy před érou ChatGPT |
| **Špičkové AI modely (maximum)** | **$57\ \%$** | `███████████░░░░░░░░░` | Např. Muse Wonder Full, Gemini 4 Argon, GPT-6 Astra, Claude Fable 5.1 |
| **Průměrné / slabší AI modely (minimum)** | **$37\ \%$** | `███████░░░░░░░░░░░░░` | Spodní hranice testovaných modelů v češtině |
| **Relativní délka: Lidský originál** | **$100\ \%$** | `███████████████░░░░░` | Výchozí délka lidského textu (baseline) |
| **Relativní délka: AI modely (bez pokynu)** | **$133\ \%$ ($+33\ \%$)** | `████████████████████` | Průměrný nárůst délky českého AI textu oproti člověku |

#### 2. Z čeho se skládá metrika EQ-Bench Slop Score
*(Podíl váhových složek při měření repetitivních vzorců LLM – $100\ \%$ celkem)*

| Složka Slop Score | Váha | Vizuální podíl | Popis složky |
| :--- | :--- | :--- | :--- |
| **Nadužívaná klišé slova** | **$60\ \%$** | `████████████░░░░░░░░` | Slovníková vata a nadužívaná adjektiva/slovesa typická pro LLM (např. *klíčový, fascinující, ponořit se*). |
| **Negativní paralelismus** | **$25\ \%$** | `█████░░░░░░░░░░░░░░░` | Kontrastní šablona „not just X, but Y“ / „nejde jen o X, ale o Y“. |
| **Nadužívané tříslovné fráze** | **$15\ \%$** | `███░░░░░░░░░░░░░░░░░` | Opakující se trigramy typu „hraje klíčovou roli“ či „v dnešní době“. |

#### 3. Spolehlivost a chybovost AI detektorů na českých textech
*(Experimentální test redakce Seznam Zprávy, vzorek 20 textů)*

| Detektor a měřený jev | Výsledek | Vizuální znázornění | Hodnocení v testu |
| :--- | :--- | :--- | :--- |
| **Copyleaks** (Správně určené texty) | **$75\ \%$** | `███████████████░░░░░` | Nejlepší výsledek v testu SZ |
| **OpenAI Detector** (Falešně pozitivní lidské texty) | **$50\ \%$** | `██████████░░░░░░░░░░` | Riziko křivého obvinění (polovina lidských textů označena za AI) |
| **GPTZero** (Odhalené české AI texty) | **$0\ \%$** | `░░░░░░░░░░░░░░░░░░░░` | Úplné selhání v češtině |

> **Shrnutí grafu:** Srovnání empirických měření kvality generovaného textu. V projektu Scio cestina.ai (říjen 2026, 18 modelů) dosáhly původní lidské texty průměrné přirozenosti $86\ \%$, zatímco modely AI se pohybovaly mezi $37\ \%$ a $57\ \%$ a bez instrukce ke stručnosti generovaly o $33\ \%$ delší výstupy. Globální metrika EQ-Bench Slop Score přisuzuje $60\ \%$ váhy nadužívaným slovům a $25\ \%$ kontrastní vazbě „nejde jen o X, ale o Y“. Nezávislé testy na českých textech zároveň ukazují, že běžné detektory buď selhávají (GPTZero $0\ \%$ odhalených českých AI textů), nebo generují až $50\ \%$ falešně pozitivních obvinění u lidských textů.
> *Zdroje dat: Cysnews.cz / Scio cestina.ai, NexusMag.eu, dfriends.cz (analýza AI slop & EQ-Bench), Seznam Zprávy.*

---

V českém jazykovém prostředí naráží analýza AI slopu na důležité metodologické rozlišení mezi měřenými korpusovými daty a pozorováním z praxe. Jak upozorňuje rozbor Daniela Votruby (dfriends.cz), české marketingové a copywriterské příručky (např. sBranding, Jecas.cz či blogy agentur, z nichž část prodává školení nebo nástroje) sice shodně uvádějí znaky jako dlouhá pomlčka, fráze „V dnešní digitální době“, stejnoměrná délka vět či opakování nadpisu v závěru, avšak žádná z těchto příruček frekvenci jednotlivých frází neměřila na formálním českém korpusu¹. Prvním rozsáhlým empirickým benchmarkem zaměřeným na samostatnou tvůrčí psanou řeč v češtině (na rozdíl od dřívějšího benchmarku BenCzechMark orientovaného na porozumění textu, matematické úlohy a obecné znalosti) se stal projekt **cestina.ai**, spuštěný společností Scio v říjnu 2026⁵.

Analytici Scio v projektu cestina.ai shromáždili autentické lidské texty (e-maily, dopisy a interní sdělení) napsané před nástupem nástrojů typu ChatGPT, extrahovali z nich klíčová fakta a nechali $18$ světových modelů od $11$ vývojářů vygenerovat vlastní verze na základě totožných faktů⁵. Zjištění projektu odhalují tři klíčové rysy českého AI psaní:
1. **Výrazná inflace délky:** Pokud uživatel nezadá explicitní pokyn ke stručnosti (např. „piš stručně“), generují modely v češtině texty zhruba o třetinu delší než lidé, a teprve po výslovné instrukci se délka srovná s lidským standardem⁵.
2. **Propast v přirozenosti:** Zatímco lidské originály získaly od evaluačního modelu průměrné skóre přirozenosti $86\ \%$, výstupy AI modelů se pohybovaly pouze v rozmezí $37\ \%$ až $57\ \%$⁵. Nejvyšší přirozenosti v psané češtině dosáhl model **Muse Wonder Full** (Meta) při vysokém vynaloženém úsilí na uvažování (*reasoning effort*), těsně následovaný skupinou modelů s drobnými rozdíly v rámci statistické nejistoty měření: **Muse Wonder** (Meta), **Gemini 4 Argon** (Google), **GPT-6 Astra** a **GPT-6.1 Sol** (OpenAI), **Claude Fable 5.1** (Anthropic) a **Grok 4.7** (xAI)⁵.
3. **Pravopis vs. vynechávání faktů:** Modely při zpracování neuspořádaných lidských poznámek s překlepy téměř nikdy nepřebírají pravopisné chyby, ale současně mají tendenci zkracovat fakta a občas zcela vynechat konkrétní číselné údaje⁵.

Tato zjištění vysvětlují, proč jsou automatizované AI detektory v českém prostředí nespolehlivé. Komerční nástroje jako Plagly.ai či Isgen.ai sice ve svých marketingových materiálech uvádějí přesnost $95\text{--}99\ \%$ na neupravených textech delších než $500$ slov (s minimálním doporučeným prahem $250$ slov)³, avšak nezávislé testy a odborné instituce jako Český institut pro AI a data (CIAD) nebo redakce Seznam Zprávy upozorňují na jejich vysokou chybovost v češtině²⁴. V praktickém testu Seznam Zpráv na $20$ různorodých textech dosáhl nejlepší testovaný detektor (Copyleaks) úspěšnosti pouhých $75\ \%$, zatímco populární GPTZero v češtině nerozpoznal ani jeden ($0\ \%$) z vygenerovaných textů a detektor přímo od OpenAI označil polovinu ($50\ \%$) lidských textů jako falešně pozitivní²⁵. Jak uvádějí provozovatelé českého nástroje DetekceGPT, zahraniční detektory na češtině a slovenštině systematicky chybují mimo jiné proto, že neznají přirozenou stavbu českých souvětí²². CIAD proto varuje před využíváním jednoho procentuálního skóre z nástrojů typu Turnitin či ZeroGPT jako důkazu u rozhodnutí s reálnými důsledky (ve školství, HR či redakcích) a doporučuje kombinovat analýzu konkrétních jazykových vzorců s ověřením historie dokumentu (verzování v Google Docs) a ústní obhajobou²⁴. Stejnou filozofii zastává i open-source skill `no-ai-slop`: detektory pouze hádají, zatímco pojmenované vzorce v textu představují ověřitelnou oporu pro úpravu⁹.

---

## Taxonomie AI klišé v českých textech: Od lexikální vaty po falešnou hloubku

Syntéza pravidel z globálních open-source repozitářů `no-ai-slop`⁹, `stop-slop`¹¹, komunitního průvodce Wikipedie *Signs of AI writing* (`WP:AISIGNS`, čítajícího téměř $15\,000$ slov a dvanáct hlavních kategorií)¹² a českých rozborů (DetekceGPT, jaksiporadit.cz, dfriends.cz, CIAD) umožňuje sestavit podrobnou anatomii klišé, jimiž AI zapleveluje české texty. Tyto vzorce nevystupují izolovaně; v neupraveném výstupu tvoří provázanou strukturu, která maskuje absenci reálné zkušenosti (tzv. **E-E-A-T** – *Experience, Expertise, Authoritativeness, Trustworthiness*) a vlastního názoru.

### 1. Lexikální klišé, zakázaná slova a umělé metafory
Jazykové modely mají v angličtině silnou statistickou afinitu k abstraktním slovesům a přídavným jménům, která znějí učeně či manažersky, ale nenesou konkrétní věcný význam (*delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game-changer, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving*). V češtině se tento slovník propisuje jako přímé překladové kalky. Nejčastějším prohřeškem je adjektivum **„klíčový“** (*key/crucial/vital/paramount*), neboť pro AI je v češtině téměř každý prvek klíčový (*klíčové aspekty, klíčové strategie, hraje klíčovou roli*). Místo toho, aby model popsal mechanismus nebo důsledek, proč na dané věci záleží, připojí k ní nálepku důležitosti.

Druhou skupinu tvoří nepřirozené slovesné a jmenné metafory. AI se v českých článcích neustále touží **„ponořit do…“** (*delve into / dive into*), což generuje věty typu „V tomto článku se ponoříme do fascinujícího světa…“ nebo „Pojďme se hlouběji ponořit do tématu“. Kdykoli model popisuje složitější jev, město, kulturu nebo technologický ekosystém, sahá po metaforách **„bohatá tapiserie“**, **„pestrá mozaika“**, **„maják (naděje/inovací)“**, **„labyrint“** nebo **„říše“** (*tapestry, mosaic, beacon, labyrinth, realm*). Jak upozorňují české redakční příručky, pokud autor nepíše o středověkém umění, slovo *tapiserie* do moderního českého textu nepatří. Podobně působí motivační fráze **„odemknout potenciál“** (*unlock potential*) a **„posunout na další úroveň“** (*elevate to the next level*), které nahrazují věcná slovesa jako *zlepšit, využít naplno* či *získat*, a korporátní anglicismy jako **„navigovat výzvy / nejistotu“** (*navigate challenges*), **„rozbalit téma“** (*unpack*) či **„opřít se do diskomfortu“** (*lean into*).

### 2. Úvodní odkašlávání (Throat-clearing openers) a časové vycpávky
Lidský čtenář očekává, že text začne přímo u podstaty problému, konfliktu nebo konkrétního faktu. Jazykový model však na začátku odstavce či článku téměř vždy „odkašlává“ pomocí širokých zobecňujících frází, které posouvají hlavní sdělení až do druhé nebo třetí věty¹. Typickým příkladem jsou časoprostorové vycpávky jako „V dnešní digitální době…“, „V dnešním rychle se měnícím / dynamickém světě…“, „Ve světě, kde…“, „Žijeme v době, kdy je změna jedinou jistotou“ nebo „Umělá inteligence se stává nedílnou součástí našich životů“⁴. Tyto věty neprojdou tzv. **testem přenositelnosti** (*portability test*) z metodiky `no-ai-slop`: pokud lze větu beze změny přesunout do textu jiné firmy, země nebo produktu, jde o prázdnou vatu, kterou je nutné smazat⁹.

Vedle časových klišé modely nadužívají rétorické odkašlávání a nastavení falešné exkluzivity (*faux-insight setups*). Konstrukce typu „Pojďme si říct na rovinu:“ (*Let me be clear*), „Nepříjemnou pravdou je, že…“ (*The uncomfortable truth is*), „Věc se má takto:“ (*Here's the thing:*), „Tohle je část, kterou většina lidí přeskakuje:“ nebo „Co vám nikdo neřekne:“ uměle oznamují hlubokou myšlenku místo toho, aby ji rovnou vyslovily¹¹. Stejně šablonovitě působí v příspěvcích na sociálních sítích (zejména na LinkedInu) otevíráky „Jsem opravdu šťastný, že vám můžu oznámit…“⁴ nebo dopisní fráze „Doufám, že vás tato zpráva zastihne v pořádku“ (*I hope this message finds you well*) vložené doprostřed běžných článků¹³.

### 3. Strukturální a rétorické vzorce (Negativní paralelismus, pravidlo tří a metakomentáře)
Nejodolnější vrstvou AI slopu nejsou jednotlivá slova, ale syntaktické šablony, do nichž modely skládají argumentaci¹.
* **Binární kontrasty a negativní paralelismus:** Prvním a statisticky nejvýznamnějším vzorcem jsou obraty typu „Není to jen o X, je to o Y“ („Není to jen o pohledu na čísla a grafy, je to o…“, „Není to jen o mzdách“, „Otázkou není X. Je jí Y.“, „Ne proto, že X. Ale proto, že Y.“)¹. Tento obrat tvoří $25\ \%$ váhy celkového Slop Score v benchmarku EQ-Bench¹. Model jím vytváří falešné drama tím, že nejprve popře slaměného panáka (X), aby vzápětí dramaticky odhalil zřejmou skutečnost (Y)⁹. Příbuzným nešvarem je negativní výčet („Není to X. Není to Y. Je to Z.“), dvojtečková odhalení („Detail, díky kterému to funguje: známkuje to oddělený agent“) a dramatická fragmentace („Rychlost. Kvalita. Cena. To je celé. O tom to je.“)¹¹.
* **Pravidlo tří (rule of threes) a falešné rozsahy (false ranges):** AI má nutkavou tendenci řadit přídavná jména, slovesa i benefity do trojic („tři rychlé, přehledné a efektivní postupy“, „inovativní, transformativní a přelomový“)¹. Podobně nadužívá falešné škály typu „od intimních setkání po celosvětová hnutí“ (*ranging from X to Y*), které předstírají konkrétní spektrum, ale neposkytují žádné reálné podrobnosti¹³.
* **Interpretativní metadiskurz, vágní autorita a kompulzivní shrnutí:** Modely neustále vystupují z tématu, aby čtenáři říkaly, čeho si má všimnout a jakou váhu tomu má přikládat: „Je důležité zmínit, že…“, „Stojí za zmínku…“, „Je třeba míti na paměti, že…“, „V neposlední řadě…“. Na začátcích odstavců pak mechanicky rotují aditivní konektory „Navíc,“, „Dále,“, „Kromě toho,“²⁴. K zamaskování faktu, že model nemá zdroj (nebo si jej halucinuje), slouží vágní připisování autority („Odborníci se shodují“, „Studie ukazují“, „Průmyslové zprávy naznačují“) bez uvedení konkrétního jména a citace¹. V závěru pak model odmítá zaujmout vyhraněné stanovisko, uchyluje se k vyhýbavým frázím typu „Nakonec záleží na konkrétním případu, jakou cestu zvolíte“ a článek uzavírá návěstím „Závěrem lze říci,“, „Celkově vzato,“ či „Shrnutí:“, které pouze zopakuje nadpis nebo předchozí odstavce¹.

### Přehledová tabulka kategorií AI slopu

| Kategorie AI Slopu | Typické anglické spouštěče (LLM Priors) | České manifestace a klišé v textech | Mechanismus selhání a pokyn k opravě |
| :--- | :--- | :--- | :--- |
| **Úvodní odkašlávání a časové vycpávky** | *In today's fast-paced digital world, In a world where, Here's the thing, Let's dive in* | V dnešní (rychle se měnící) digitální/dynamické době, Žijeme v době, kdy…, Pojďme se ponořit do fascinujícího světa, Pojďme si říct na rovinu | Nulová informační hodnota (selhává v testu přenositelnosti). Kompletně smazat a začít prvním konkrétním faktem či konfliktem¹. |
| **Zakázaná slova a umělé metafory** | *Key/vital/crucial, delve, tapestry, beacon, realm, unlock potential, elevate, game-changer, robust* | Klíčový (hraje klíčovou roli), ponořit se do tématu, tapiserie / mozaika, maják, říše, odemknout potenciál, posunout na další úroveň, přelomový, robustní | Abstraktní nálepky nahrazující důkaz. Nahradit konkrétním mechanismem, číslem nebo prostým slovesem (*zlepšit, využít naplno, získat*). |
| **Negativní paralelismus a binární drama** | *It's not just X, it's Y; The question isn't X, it's Y; Not a X. Not a Y. A Z.* | Není to jen o X, je to o Y; Nejde jen o X, ale o Y; Otázkou není X, ale Y; Ne proto, že X, ale proto, že Y | Tvoří $25\ \%$ váhy Slop Score. Vytváří falešné drama. Vyškrtnout popření X a formulovat přímo kladné tvrzení Y¹. |
| **Metadiskurz a spojovací vata** | *It's worth noting, It is important to mention, Last but not least, Moreover, Furthermore* | Je důležité zmínit, Stojí za zmínku, Je třeba míti na paměti, V neposlední řadě, Navíc / Dále / Kromě toho | Model komentuje vlastní psaní místo předkládání faktů. Smazat uvozovací vatu a nechat holé tvrzení. |
| **Pravidlo tří a falešné rozsahy** | *Innovative, transformative, and groundbreaking; Ranging from X to Y* | Tři rychlé, přehledné a efektivní postupy; Od intimních setkání po celosvětová hnutí | Mechanický rytmus trojic a iluze konkrétnosti. Použít dva prvky místo tří, nebo uvést přesný výčet a reálná čísla. |
| **Vágní autorita a alibistické závěry** | *Studies show, Experts agree, In conclusion, Ultimately, It depends on your specific case* | Odborníci se shodují, Studie ukazují, Závěrem lze říci, Nakonec záleží na konkrétním případu | Zakrývá absenci zdrojů a vyhýbá se názoru. Uvést přesnou citaci (jméno, zdroj), nebo tvrzení smazat; závěrečné shrnutí vypustit¹. |
| **Konverzační artefakty a uvozovací dopisy** | *I hope this helps!, Certainly!, I hope this message finds you well, contentReference[oaicite:1]* | Doufám, že to pomůže!, Jistě, Doufám, že vás tato zpráva zastihne v pořádku, `turn0search0`, `citeturn0news0` | Neopracované zbytky dialogu s asistentem a systémové řetězce. Jednoznačný důkaz nezkontrolovaného kopírování – beze zbytku odstranit¹. |

---

## Česká specifika a chyby v AI lokalizacích: Lingvistika, typografie a byznys kontext

Když globální jazykový model generuje text v češtině nebo překládá z angličtiny, nepracuje s češtinou jako s autonomním systémem, ale promítá do ní anglické syntaktické a typografické vzorce. Výsledkem je text, který sice neobsahuje hrubé pravopisné chyby v koncovkách, ale rodilému mluvčímu zní cize, toporně a „překladově“ – přesně v duchu upozornění českých překladatelů a lokalizátorů, že text bez gramatických chyb ještě nemusí říkat totéž co originál a v prodejní komunikaci často zní stroze „jako návod k pračce“²¹.

### 1. Morfosyntaktická interference (Anglická syntax v českém převleku)
Lingvistická analýza odhaluje pět strukturálních rovin, v nichž angličtina deformuje český AI výstup:

1. **Narušení aktuálního členění větného (Functional Sentence Perspective – FSP)¹⁴:** V angličtině plní slovosled primárně gramatickou funkci – kvůli chudé flexi musí věta dodržovat pevný rámec Podmět – Přísudek – Předmět (SVO), aby bylo zřejmé, kdo je původcem děje. V češtině však syntaktické vztahy určují pádové koncovky, a slovosled je proto volný (flexibilní) a plní funkci aktuálního členění větného, jak jej definoval Vilém Mathesius a rozvinula Pražská škola (Libuše Dušková, Josef Vachek)¹⁴. V přirozené klidné české větě roste výpovědní dynamičnost od **tématu** (východiska, tedy toho, o čem se mluví a co je z kontextu známé) na začátku věty k **rématu** (jádru výpovědi, tedy nové, nejdůležitější informaci) na konci věty. Když angličtina potřebuje zdůraznit novou informaci, pomůže si gramatickou strukturou (pasivem nebo existenční vazbou, např. *There came a moment when everything changed*), zatímco čeština jednoduše přeskupí slovosled a postaví sloveso před podmět (*Nastal okamžik, kdy se všechno změnilo*)¹⁶. AI modely při psaní i překladu často mechanicky kopírují anglické pořadí podmět–přísudek, čímž rozbíjejí přirozenou českou informační perspektivu a důraz¹⁴.
2. **Nadužívání přivlastňovacích zájmen a ignorování zvratného „svůj“:** Angličtina vyžaduje nesamostatná přivlastňovací zájmena (*my, your, his, her, its, our, their*) před podstatným jménem k určení vlastníka a nemá žádné samostatné zvratné přivlastňovací zájmeno¹⁵. Při překladu pro české *svůj* tak angličtina vždy používá přivlastňovací zájmeno pro osobu podmětu (např. *There was John with his girlfriend* – *Byl tam John se svou přítelkyní*)¹⁵. AI modely při překladu do češtiny chybují oběma směry: buď otrocky překládají *his/her/your* jako *jeho/její/váš* i tam, kde se vlastník shoduje s podmětem a česká mluvnice vyžaduje *svůj* („Pokud se přihlásíte přes svůj účet Google“)¹⁵, nebo zaplavují text zájmeny *váš/vaše* tam, kde je přirozená čeština zcela vypouští.
3. **Opisný trpný rod (passive voice) místo činného rodu a zvratného pasiva:** V angličtině se trpný rod vyjadřuje jedním způsobem (*is brewed, is being discussed, was created*) a hojně se využívá v akademických a korporátních textech¹⁵. V češtině však existují dva způsoby tvorby trpného rodu – opisný a zvratný se *se* (např. „V Česku se vaří hodně piva“ oproti anglickému „A lot of beer is brewed in the Czech Republic“) – a tam, kde má angličtina trpný rod, volí čeština velmi často činný rod s konkrétním podmětem (např. podmět *vláda* v činném rodě místo anglického pasiva)¹⁵. Metodiky `no-ai-slop` i `stop-slop` proto nařizují pasivum („X bylo vytvořeno“, „bylo dosaženo rozhodnutí“) nahrazovat konkrétním původcem děje v činném rodě.
4. **Falešná agencie neživotných podmětů (false agency):** Modely milují konstrukce, v nichž abstraktní pojmy nebo neživotné věci vykonávají lidské činnosti, protože se tím vyhýbají nutnosti pojmenovat konkrétního aktéra: „stížnost se stává opravou“ (*a complaint becomes a fix*), „rozhodnutí vyvstává“ (*the decision emerges*), „data nám říkají“ (*the data tells us*), „trh odměňuje“ (*the market rewards*)¹¹. Souběžně s tím nahrazují plnovýznamová slovesa prázdnými verbonominálními vazbami („učinit rozhodnutí“ místo „rozhodnout“, „má schopnost“ místo „umí / dokáže“, „slouží jako centralizovaný uzel“).
5. **Participiální přívěsky (-ing clauses):** Na konce vět AI v angličtině připojuje participia („…, *highlighting/underscoring/reflecting/showcasing*…“), která předstírají vysvětlení významu a v českém překladu vedou k toporným přechodníkům („…, zdůrazňujíc…“) nebo šroubovaným větám s „…, což podtrhuje / odráží…“⁹.

### 2. Česká typografie (ČSN 01 6910) jako okamžitý vizuální detektor AI
I když je text po obsahové stránce upraven, neznalost českých typografických pravidel zakotvených v normě **ČSN 01 6910** (*Úprava dokumentů zpracovaných textovými procesory*) a doporučeních Ústavu pro jazyk český AV ČR okamžitě prozradí, že výstup vygeneroval model bez lidské sazby. Jak upozorňují české typografické příručky, skvěle napsaný text vypadá okamžitě amatérsky, pokud obsahuje rovné anglické uvozovky místo českých oblých, spojovník tam, kde patří pomlčka, nebo zápis `50%` bez mezery¹⁹. U ChatGPT bylo nadužívání dlouhých pomlček natolik výrazné, že Sam Altman dne 14. listopadu 2025 veřejně oznámil úpravu modelu, aby konečně respektoval zákaz pomlček v uživatelských instrukcích¹.

#### Přehledová tabulka pravidel české typografie (ČSN 01 6910)

| Typografický jev | Typická chyba AI výstupu (Anglický / ASCII standard) | Pravidlo české typografie (ČSN 01 6910 a ÚJČ AV ČR) | Konkrétní příklad (Špatně vs. Správně) |
| :--- | :--- | :--- | :--- |
| **Pomlčka ve větě (větná pomlčka)** | Dlouhá čtverčíková pomlčka (`—`, em-dash) nebo krátký spojovník (`-`) místo pomlčky¹. | Krátká půlčtverčíková pomlčka (`–`, en-dash, `Alt+0150`) oddělená z obou stran mezerami; nesmí stát na začátku řádku. Interpunkce přiléhá hned za pomlčku bez mezery¹⁷. | ❌ Vše funguje—až na export. / Vše funguje - až na export.<br>✔️ Vše funguje – až na export.⁴⁹ |
| **Pomlčka pro rozsah a vztah (od–do, versus)** | Spojovník (`1914-1918`, `Praha-Brno`) nebo pomlčka s mezerami u jednoslovných výrazů¹⁸. | Půlčtverčíková pomlčka (`–`) bez mezer u jednoslovných výrazů a čísel. Pokud je alespoň jeden člen víceslovný, sází se s mezerami (` – `)¹⁷. | ❌ v letech 1914-1918, Praha – Brno<br>✔️ v letech 1914–1918, Praha–Brno, *ale* Karlovy Vary – Plzeň, M. Zikmund – J. Hanzelka⁴⁸ |
| **Spojovník (Hyphen)** | Zaměňován s pomlčkou. | Nejkratší čárka (`-`), píše se vždy bez mezer u složených slov, těsných spojení a částice *-li*¹⁷. | ❌ česko - anglický, bude - li<br>✔️ česko-anglický, Praha-Holešovice, bude-li⁴⁹ |
| **Uvozovky** | Rovné (`"text"`) nebo anglické horní (`“text”`)¹⁷. | České kulaté uvozovky: spodní devítkové na začátku a horní šestkové na konci (`„text“`, tvar 99 a 66), vnořené jednoduché (`‚text‘`). Přiléhají těsně bez mezer¹⁷. | ❌ "Cílem je kvalita." / “Cílem je kvalita.”<br>✔️ „Cílem je kvalita.“ a vnořené „Předložil ‚zajímavou‘ teorii.“⁴⁹ |
| **Procenta a měrné jednotky** | Přilepené k číslu bez mezery podle anglického úzu (`50%`)¹⁹. | S pevnou mezerou (`50 %` = padesát procent, `10 km`). Bez mezery pouze jako přídavné jméno (`50%` = padesátiprocentní)¹⁷. | ❌ sleva 50%, úrok se zvýšil o 3%<br>✔️ sleva 50 %, *ale* 50% sleva (padesátiprocentní), 3% úrok¹⁷ |
| **Čísla, desetinné čárky a měny** | Desetinná tečka, čárka pro tisíce, nadbytečné `,-` u celých částek¹⁸. | Desetinná čárka bez mezer (`1,21 Kč`), u čísel s více než 4 číslicemi dělení po trojicích pevnou mezerou (`100 000`), celé částky psát bez `,-`¹⁷. | ❌ 100,000 Kč, 1.21 Kč, 250,- Kč<br>✔️ 100 000 Kč, 1,21 Kč, 250 Kč¹⁸ |
| **Kalendářní datum** | Chybějící mezery po tečkách v běžném textu (`15.10.2026`)¹⁸. | Za řadovou číslovkou se v souvislém textu píše tečka a pevná mezera (`15. 10. 2026` nebo `15. října 2026`). Bez mezer jen u dvoumístného strojového zápisu (`02.08.2020`)¹⁸. | ❌ Dne 15.10.2026 proběhla akce.<br>✔️ Dne 15. 10. 2026 (15. října 2026) proběhla akce.¹⁸ |
| **Pevná mezera a výraz „viz“** | Neslabičné předložky na konci řádku, tečka za slovem `viz.`⁴⁹. | Po předložkách a spojkách *k, s, v, z, o, u, a, i* vkládat nezlomitelnou mezeru (`U+00A0` / `&nbsp;`). Výraz *viz* není zkratka – píše se vždy bez tečky⁴⁹. | ❌ viz. příloha, `v` na konci řádku<br>✔️ viz příloha, `v&nbsp;Praze`⁴⁹ |
| **Velká písmena v nadpisech** | Anglický Title Case (velká písmena na začátku každého slova) a tečka na konci nadpisu¹. | V češtině neplatí anglický Title Case. Za nadpisy a popisky obrazových reprodukcí se nikdy nepíše tečka¹⁷. | ❌ Jak Využít Umělou Inteligenci V Marketingu.<br>✔️ Jak využít umělou inteligenci v marketingu¹ |

### 3. Byznysová, konverzní a procesní úskalí AI lokalizace
Rozdíl mezi prostým strojovým překladem a skutečnou lokalizací spočívá v tom, že **překlad převádí slova, zatímco lokalizace převádí záměr a obchodní kontext**²¹. Jak uvádí specialista na AI nástroje Honza Šilar (září 2026), skutečná lokalizace nastává až ve chvíli, kdy zákazník vůbec nepozná, že původní verze textu vznikla jinde²¹. Firemní analýza platformy LocoGlobal, která zkoumala $141\,113$ produktů přeložených pomocí AI napříč $72$ jazyky, zjistila, že průměrné skóre kvality AI lokalizace dosahuje pouze $70$ bodů ze $100$, kvůli čemuž e-shopy přicházejí o $20\text{--}30\ \%$ potenciálu⁷.

---

### [GRAF 2] Nekontrolovaná AI lokalizace sráží konverze o 86 % a vyžaduje sedm hodin lidské revize

#### 1. Plošný audit kvality (LocoGlobal)
*(Analýza $141\,113$ AI-přeložených produktů v $72$ jazycích)*

| Sledovaná metrika | Hodnota | Kontext a obchodní dopad |
| :--- | :--- | :--- |
| **Průměrné skóre kvality AI lokalizace** | **$70 / 100$** | **Ztráta $20\text{--}30\ \%$ tržního potenciálu.** AI řeší gramatiku a doslovný překlad, ale ignoruje konverzní kontext a místní zvyklosti. |
| **Skóre lokálního SEO u AI překladů** | **$56 / 100$** | Doslovný překlad URL a meta tagů bez analýzy lokální hledanosti klíčových slov (SERP). |
| **Podíl e-shopů nevědoucích o chybách** | **$80\ \%$** | Provozovatelé cílový jazyk neovládají a překlady po hromadném nahrání nekontrolují. |
| **Produkty neviditelné kvůli nejednotným termínům** | **$33\ \%$** | Případ $247$ silikonových řemínků: $3$ různé AI překlady způsobily pokles prodejů kategorie o $15\ \%$. |

#### 2. Obchodní dopad chyb (Případová studie 6 105 textů)
*(Český kosmetický e-shop: Český originál vs. chybná lokalizace v Chorvatsku – při nekontrolovaném importu z CSV selhal překlad a v rozhraní zůstal český fallback text, což vedlo ke ztrátě $-27\,000\text{ Kč}$ měsíčně na trhu)*

| Metrika chování uživatelů | Český originál (ČR) | Chybná lokalizace (HR) | Relativní změna / Dopad |
| :--- | :--- | :--- | :--- |
| **Bounce rate (okamžité opuštění)** | **$34\ \%$** | **$67\ \%$** | Nárůst o $+33\text{ p. b.}$ (dvojnásobek) |
| **Konverzní poměr (Conversion rate)** | **$2{,}1\ \%$** | **$0{,}3\ \%$** | Kritický propad o **$-86\ \%$** |
| **Průměrná doba na stránce** | **$154\text{ s}$** ($2\text{:}34\text{ min}$) | **$12\text{ s}$** | Pokles o **$-92\ \%$** |

#### 3. Procesní realita a kontrola významu (Axecom)
*(Modelové srovnání celkového času End-to-End: Tradiční vs. AI workflow – skutečná úspora je $3{,}5\text{ h}$, nikoli $9{,}5\text{ h}$)*

| Fáze překladového procesu | Tradiční lidský překlad | AI překlad s kontrolou významu | Poznámka k procesu |
| :--- | :--- | :--- | :--- |
| **Tvorba návrhu / AI generování** | $10{,}0\text{ h}$ | $0{,}5\text{ h}$ | Překlad od nuly vs. rychlý surový návrh z AI |
| **Lidská revize významu (korektura)** | $2{,}0\text{ h}$ | $7{,}0\text{ h}$ | U AI nutná 2-fázová kontrola (segment po segmentu + čtivost) |
| **Oprava DTP sazby a formátování** | $0{,}0\text{ h}$ | $1{,}0\text{ h}$ | Oprava rozpadlé sazby a tabulek po AI exportu |
| **CELKOVÝ ČAS (End-to-End)** | **$12{,}0\text{ h}$** | **$8{,}5\text{ h}$** | **Reálná úspora: $3{,}5\text{ h}$** |

> **Shrnutí grafu:** Obchodní a procesní realita AI lokalizací. Horní panel ukazuje závěry auditu $141\,113$ produktů (LocoGlobal), kde lokální SEO u AI překladů dosahuje jen $56/100$ bodů a $80\ \%$ e-shopů o skrytých chybách vůbec neví. Střední panel dokumentuje reálný případ českého kosmetického e-shopu ($6\,105$ textů), kde selhání lokalizace vedlo k nárůstu okamžitého opuštění stránky (bounce rate) ze $34\ \%$ na $67\ \%$ a propadu konverzního poměru z $2{,}1\ \%$ na $0{,}3\ \%$. Spodní panel (data Axecom, říjen 2026) ukazuje, že ačkoliv AI vygeneruje překlad za $0{,}5$ hodiny místo $10$ hodin, nutná dvoufázová kontrola významu ($7\text{ h}$) a oprava sazby ($1\text{ h}$) snižují reálnou úsporu času na $3{,}5$ hodiny.
> *Zdroje dat: LocoGlobal (Audit 141 113 produktů), Axecom (Analýza AI překladového workflow, říjen 2026).*

---

Rozbor chyb v lokalizacích ukazuje čtyři kritická místa selhání, která musejí být ošetřena v instrukcích pro AI agenty:

1. **Slepota vůči lokálnímu SEO:** V auditu LocoGlobal dosáhlo lokální SEO průměrného skóre pouhých $56/100$⁷. AI překládá URL adresy, meta titles a meta descriptions doslovně bez znalosti lokální hledanosti (*search volume*) a zvyklostí v místním SERP. Například při expanzi dětského e-shopu do Německa vygeneroval doslovný AI překlad URL `/kinderwagen-premium-blau-mit-zubehoer` a popis `Kinderwagen Premium in der Farbe Blau mit Zubehör.` místo hledaného výrazu `/kinderwagen-premium` doplněného o nákupní výzvu (*kaufen*) a lokální benefity (doprava zdarma, záruka)⁷. V češtině přitom vyhledávače chápou skloňování i jednotné a množné číslo, takže klíčová slova z referenčních dokumentů je nutné v textu přirozeně skloňovat v různých pádech, případně v těle textu kombinovat s volnějšími synonymy⁵³.
2. **Terminologický chaos při překladu bez kontextu:** Podle dat LocoGlobal tvoří nekonzistence $30\text{--}40\ \%$ všech chyb v produktových katalozích⁷. Protože AI překládá položky izolovaně bez paměti předchozích překladů (CAT) a bez závazného glosáře značky (*Brand Glossary*), přeloží identický produkt pokaždé jinak. V případové studii expanze kuchyňského náčiní ze Slovenska do Maďarska přeložila AI jeden výraz třemi různými způsoby (u $67$, $34$ a $12$ produktů) a u katalogu $247$ silikonových řemínků způsobila roztříštěnost terminologie to, že zákazníci při vyhledávání viděli jen $67\ \%$ nabídky – $33\ \%$ produktů zůstalo neviditelných, což vedlo k poklesu prodejů v kategorii o $15\ \%$⁷. Glosář značky přitom musí jasně definovat výrazy, které se překládají vždy stejně (např. u klienta Notino *parfémovaná voda* vždy jako *Eau de Parfum*), i názvy produktů a tarifů, které se nepřekládají nikdy²¹.
3. **Pravidlo „Informovat vs. Přesvědčovat“ a počeštění systému:** Podle metodiky Honzy Šilara je pro informační a technické texty (manuály, obchodní podmínky, produktové parametry, transakční e-maily) vhodný přesný překladač typu DeepL²¹. Naopak u persvazivních (prodejních) textů (prodejní landing pages, e-mailové sekvence, příspěvky na sociální sítě) doslovný překlad selhává, protože převléká česká či anglická souvětí do cizích slov a z textu vyprchá chuť nakoupit²¹. Prodejní texty je proto nutné pomocí generativního modelu (např. Claude) rovnou nativně psát v cílovém jazyce na základě obchodních podkladů (ceníky, specifikace, ukázky *tone of voice*)²¹. Kritickou slepou skvrnou je rovněž počeštění systému (tlačítka v košíku, chybové hlášky formulářů, potvrzovací e-maily po platbě) a nepřeložené fallback texty při chybách importu CSV, o nichž podle LocoGlobal $80\ \%$ provozovatelů e-shopů neví⁷. V zdokumentovaném případu českého kosmetického e-shopu expandujícího do Chorvatska ($6\,105$ textů), kde kvůli chybě importu zůstal český text („Tento šampon je vyroben z přírodní růžové vody…“), vyskočila míra okamžitého opuštění (*bounce rate*) na $67\ \%$ (oproti $34\ \%$ v ČR), průměrná doba na stránce klesla na $12$ sekund (oproti $2\text{:}34\text{ min}$ v ČR), konverzní poměr se propadl na $0{,}3\ \%$ (oproti $2{,}1\ \%$ v ČR) a e-shop zaznamenal ztrátu $27\,000\text{ Kč}$ měsíčně⁷.
4. **Adaptace reálií a dvoufázová kontrola významu:** Strojový překlad sám nelokalizuje odkazy na zákony (např. ponechání českého § 64 zákona o DPH č. 235/2004 Sb. na polském webu), jména kontaktních osob v podpoře či recenzích (např. ponechání *Eva Svobodová* v chatovacím okně na italském webu), lokální dárky (např. nabídka časopisu *Vogue Czechoslovakia* německým zákazníkům), měny, telefonní předvolby či formáty účtů (variabilní a konstantní symboly)²¹,⁵³. Navíc, jak upozorňuje analýza překladatelské agentury Axecom (říjen 2026) s odkazem na *NIST Generative AI Profile* (červenec 2024), **přirozená plynulost a sebejistý tón českého AI překladu aktivně ztěžují korekturu**: lidský korektor si okamžitě všimne kostrbaté formulace, ale v plynulém textu snadno přehlédne posun významu (např. změnu formulace „doručení obvykle do pěti pracovních dnů“ na garantovanou lhůtu dodání, změnu dávkování či vypuštění kroku v postupu)³⁶. V modelovém srovnání agentury Axecom proto tradiční lidský překlad trvá $12$ hodin ($10\text{ h}$ překlad + $2\text{ h}$ kontrola), zatímco AI překlad sice vygeneruje návrh za $0{,}5$ hodiny, ale vyžaduje $7$ hodin lidské revize významu (ve dvou průchodech: nejprve větu po větě proti originálu, poté souvislé čtení české verze) a $1$ hodinu opravy rozpadlé DTP sazby – celkem $8{,}5$ hodiny, což představuje reálnou úsporu $3{,}5$ hodiny, nikoliv $9{,}5$ hodiny³⁶.

---

## Srovnávací analýza textů: AI Slop a strojový překlad vs. lidská redakce

Pro přesné pochopení toho, jak má navržený `SKILL.md` v praxi transformovat texty, porovnejme na konkrétních ukázkách neupravený výstup modelu (AI Slop / strojový překlad) s profesionální lidskou redakcí.

### Ukázka 1: Původní český marketingový text (Blog / Případová studie)
Následující srovnání vychází z dokumentované ukázky Daniela Votruby (dfriends.cz, říjen 2026) a ukazuje typickou koncentraci šesti vzorců AI břečky v jediném krátkém odstavci¹:

| Verze textu | Znění textu | Diagnostika vzorců a provedených zásahů |
| :--- | :--- | :--- |
| **Před úpravou (Český AI Slop)** | „V dnešní rychle se měnící digitální době hraje personalizace e-mailů klíčovou roli v úspěchu každé značky. V tomto článku se ponoříme do fascinujícího světa e-mailového marketingu a odhalíme tři rychlé, přehledné a efektivní postupy, které posunou vaše kampaně na další úroveň. Odborníci se shodují, že personalizace přináší lepší výsledky. Závěrem lze říci, že se investice do personalizace vždy vyplatí.“ | **Detekované chyby:**<br>1. Časová vycpávka na úvod („V dnešní rychle se měnící digitální době“).<br>2. Zakázané klišé důležitosti („hraje klíčovou roli“).<br>3. Metadiskurz + metafora noření („V tomto článku se ponoříme do fascinujícího světa“).<br>4. Pravidlo tří + motivační vata („tři rychlé, přehledné a efektivní postupy, které posunou vaše kampaně na další úroveň“).<br>5. Vágní autorita bez zdroje („Odborníci se shodují“).<br>6. Kompulzivní shrnutí + líný extrém bez dat („Závěrem lze říci, že se investice… vždy vyplatí“). |
| **Po úpravě (Lidská anti-slop redakce)** | „Když jsme v e-mailech pro `[název klienta]` přestali psát „Dobrý den“ a začali oslovovat podle poslední návštěvy webu, otevíralo je `[číslo]` % příjemců místo dřívějších `[číslo]` %. U `[segment]` to pomohlo, u `[segment]` se nezměnilo nic. Tady je, co jsme upravili a co bychom příště udělali jinak: `[tři konkrétní kroky]`.“ | **Provedené úpravy:**<br>• Kompletně smazáno úvodní odkašlávání i závěrečné shrnutí.<br>• Abstraktní klišé nahrazena konkrétním mechanismem (změna oslovení podle návštěvy webu) a zástupnými poli `[...]` pro reálná interní data z CRM, která model nezná a nesmí si je vymyslet¹.<br>• Přiznána reálná nuance a limitace („u `[segment]` se nezměnilo nic“), což buduje okamžitou důvěryhodnost.<br>• Aplikována správná česká typografie (kulaté uvozovky, mezera před znakem `%`)¹. |

### Ukázka 2: B2B a produktová komunikace (Odstranění binárních kontrastů a žargonu)
Tato komparace demonstruje aplikaci pravidel `no-ai-slop` a `stop-slop` na typický firemní a produktový text zatížený negativním paralelismem, dvojtečkovým dramatem a korporátním žargonem:

| Typ vzorce | AI Slop verze (Před úpravou) | Anti-Slop verze (Po úpravě) | Princip transformace |
| :--- | :--- | :--- | :--- |
| **Odkašlávání + Binární kontrast + Berlička důrazu** | „Pojďme si říct na rovinu: stavět produkty je těžké. Ne proto, že by technologie byla složitá. Ale proto, že složití jsou lidé. Nechte si to projít hlavou.“ (*Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in.*)¹¹ | „Stavět produkty je těžké. Technologii uřídíte, lidi ne.“ (*Building products is hard. Technology is manageable. People aren't.*)¹¹ | Odstraněn otevírák „Pojďme si říct na rovinu:“, rozbit negativní paralelismus „Ne proto, že X. Ale proto, že Y.“ a smazána performativní berlička „Nechte si to projít hlavou.“ |
| **Stack korporátního žargonu** | „V dnešním rychle se měnícím prostředí se musíme opřít do diskomfortu a navigovat nejistotu s jasností. To je důležité, protože vaše konkurence nečeká.“ (*In today's fast-paced landscape, we need to lean into discomfort and navigate uncertainty with clarity. This matters because your competition isn't waiting.*)¹¹ | „Rozhodujte se rychleji. Konkurence nečeká.“ (*Move faster. Your competition is.*)¹¹ | Smazána časová vycpávka, kalky *opřít se do* (*lean into*), *navigovat nejistotu* (*navigate uncertainty*) a metakomentář *to je důležité, protože*¹¹. |
| **Falešně silné sloveso + Participiální přívěsek** | „Aplikace slouží jako centralizovaný uzel pro správu sponzorů, což podtrhuje závazek týmu k lepším pracovním postupům. Nástroj výrazně zvyšuje produktivitu inženýrů.“ | „Aplikace na jednom místě sleduje sponzory, koncepty, termíny a schválení. Nástroj zkrátil čas kontroly kódu z 30 minut na 8.“⁹ | Vágní vazba „slouží jako centralizovaný uzel“ nahrazena výčtem reálných funkcí; participiální chvost („což podtrhuje…“) a obecné tvrzení nahrazeny měřitelným faktem ($30\text{ min} \rightarrow 8\text{ min}$)⁹. |
| **Dramatická fragmentace + Dlouhá pomlčka** | „Rychlost. Kvalita. Cena. Můžete si vybrat jen dvě—to je celé. O tom ten kompromis je.“¹¹ | „Rychlost, kvalita, cena. Vyberte si dvě.“¹¹ | Odstraněno staccato jednoslovných vět, dlouhá pomlčka bez mezer i prázdný metakomentář na konci. |

### Ukázka 3: Lokalizace z angličtiny do češtiny (UI, SaaS a E-commerce)
Následující tabulka ilustruje, jak prostý AI překlad z angličtiny selhává v české syntaxi (FSP, zájmena, pasivum), typografii a obchodní lokalizaci, a jak vypadá výstup po aplikaci českých lokalizačních pravidel:

| Anglický originál (Zdroj) | Doslovný AI překlad (Chybná lokalizace) | Profesionální česká lokalizace (Anti-Slop CZ) | Lingvistický, typografický a byznys rozbor |
| :--- | :--- | :--- | :--- |
| „Unlock Your Team's Potential Today! Log into your account, upload your files—and get a 50% discount on our Pro Plan. Questions? Contact Sarah Jenkins at support.“ | „Odemkněte Potenciál Vašeho Týmu Dnes! Přihlaste se do vašeho účtu, nahrajte vaše soubory—a získejte 50% slevu na náš Pro Plán. Otázky? Kontaktujte Sarah Jenkins na podpoře.“ | „Zrychlete práci celého týmu. Přihlaste se ke svému účtu, nahrajte soubory – a získejte slevu 50 % na tarif Pro. Potřebujete poradit? Napište Evě Svobodové ze zákaznické podpory.“ | 1. **Klišé & Title Case:** Odstraněn Title Case a klišé *Odemkněte potenciál*.<br>2. **Zájmena:** Opraveno *vašeho účtu* na zvratné *svému účtu* a vypuštěno nadbytečné *vaše* u souborů¹⁵.<br>3. **Typografie:** `—` nahrazena ` – `; rozlišena *50% sleva* (padesátiprocentní) vs. *sleva 50 %* (padesát procent)¹⁷.<br>4. **Reálie:** Cizí jméno v podpoře lokalizováno na české jméno pro důvěryhodnost⁵³. |
| „There came a moment when everything changed. A new course was approved by the government.“ | „Přišel okamžik, kdy se všechno změnilo. Nový kurz byl schválen vládou.“ | „Nastal okamžik, kdy se všechno změnilo. Vláda schválila nový kurz.“ | 1. **Aktuální členění větné (FSP):** Přirozená česká inverze podmětu a přísudku (*Nastal okamžik…*) místo anglické existenční vazby¹⁶.<br>2. **Trpný vs. činný rod:** Anglické pasivum (*was approved by the government*) převedeno do přirozeného českého činného rodu s podmětem *vláda* a rématem (*nový kurz*) na konci věty¹⁶. |
| „Delivery is usually within 5 business days. Goods are exempt from tax under Section 64 of the VAT Act.“ | „Doručení je garantováno do 5 pracovních dnů. Zboží je osvobozeno od daně podle §64 zákona o DPH č. 235/2004 Sb.“ | „Zboží obvykle doručujeme do 5 pracovních dnů. *(Pozor: odkaz na § 64 zákona o DPH je nutné před publikací ověřit s právníkem pro danou cílovou zemi.)*“ | 1. **Sémantická chyba:** Změna *usually* (obvykle) na *garantováno* představuje závažnou chybu v rozsahu závazku³⁶.<br>2. **Právní reálie a typografie:** Znak `§` se sází s mezerou před číslem (`§ 64`); legislativní odkaz nelze převzít z jiného státu bez právní kontroly⁴⁹. |

---

## Metodika a instrukce pro tvorbu anti-slop skillu (`SKILL.md`)

V ekosystému moderních AI agentů (jako jsou Claude Code, Cursor, OpenAI Codex, Gemini CLI či OpenClaw)²⁰ představuje soubor `SKILL.md` modulární instrukční sadu, kterou agent načítá při generování, editaci nebo auditu textu⁹. Aby byl takový skill v praxi účinný a nedegradoval osobitý autorský styl uživatele na sterilní korporátní prózu, kombinuje navržená architektura principy ze dvou hlavních open-source projektů:
1. **Editor-First přístup (`petergyang/no-ai-slop`):** Definuje dva striktně oddělené pracovní režimy: **Edit** (výchozí), provádějící minimální efektivní zásah (*minimum effective edit*) při zachování autentického hlasu autora včetně závěrečného přehledu *Co se změnilo* (*What changed*), a **Detect** (audit), který pouze vypíše nalezené vzorce, ocituje konkrétní větu a navrhne opravu bez přepisování celého textu⁹.
2. **Tiered Audit & Scoring přístup (`Azayzel/stop-slop`):** Zavádí čtyřúrovňovou hierarchii oprav (od mechanických škrtů přes přepis struktur a aktivaci podmětu až po vynucení konkrétnosti) a pětirámcový bodovací systém ($1\text{--}10$ bodů v každé dimenzi), kde jakékoli skóre pod $7$ bodů nebo celkový součet pod $35/50$ vrací text k přepracování před doručením uživateli¹¹.

### Postup implementace souboru `SKILL.md` do pracovního prostředí
Pro nasazení skillu v praxi postupujte podle následujících čtyř kroků:
1. **Uložení souboru `SKILL.md` do adresáře agenta:** V nástrojích podporujících standardizované agentní skilly (Claude Code, Codex, Cursor, Gemini CLI, OpenClaw) uložte níže uvedený kód do souboru `skills/no-slop-cz/SKILL.md`. Pokud pracujete ve webovém rozhraní ChatGPT, Claude nebo Gemini, vložte obsah souboru přímo do systémových instrukcí projektu (*Brand Voice / Project Instructions*)²⁷.
2. **Připojení ukázek vlastního stylu (`brand-voice.md`):** Samotný anti-slop skill odstraňuje negativní vzorce, ale jak zdůrazňují praktické metodiky (Skillminers, DetekceGPT), pro pozitivní zachování tónu značky potřebuje model referenční vzor²². Připojte ke skillu dokument s ukázkami vašich dřívějších lidských textů a instrukcí „Piš v tomto stylu“²².
3. **Připojení terminologického glosáře (`glossary.md`):** Při překladech a lokalizacích přiložte tabulku schválených oborových termínů, klíčových slov pro lokální SEO (která má model přirozeně skloňovat) a seznam názvů produktů či tarifů, které se nikdy nepřekládají⁷.
4. **Spárování s kontrolním souborem (`eval.md`):** Podle vzoru repozitáře `no-ai-slop` uložte vedle hlavního souboru také krátký verifikační checklist `eval.md` (uvedený v závěru této zprávy), podle něhož agent v kroku 4 svého pracovního postupu zkontroluje upravený návrh před vypsáním na obrazovku⁹.

---

## Kompletní šablona souboru `SKILL.md` (Připravená k nasazení)

Níže uvedený blok představuje kompletní, produkčně připravený soubor `SKILL.md`. Zkopírujte jej a uložte přímo do svého projektu. Struktura striktně odděluje **Sekci 1 (Obecná pravidla / Universal Anti-Slop)** a **Sekci 2 (Lokalizace a česká specifika)** a integruje dvourežimové řízení, čtyřúrovňový audit i bodovací matici.

```markdown
---
name: no-slop-cz
description: Odstraňuje AI klišé (AI slop) z českých i anglických textů, opravuje strojové překlady do přirozené češtiny (slovosled, aktuální členění větné, slovesný rod, zájmena) a vynucuje českou typografickou normu ČSN 01 6910. Použij vždy, když píšeš, edituješ, překládáš, lokalizuješ nebo audituješ jakýkoliv text určený lidskému čtenáři (články, blogy, e-maily, prodejní landing pages, UI texty, dokumentaci, příspěvky na sociální sítě). Aplikuj automaticky i tehdy, když uživatel výslovně neřekne „ať to nezní jako AI“.
---

# No Slop CZ: Lidský redaktor a lokalizační specialista

Jsi ostrý, zkušený lidský šéfredaktor a seniorní český lokalizátor. Tvým úkolem je chránit myšlenku, fakta a osobitý hlas autora a současně nemilosrdně vyřezávat prázdnou vatu, šablonovitá AI klišé (AI slop), anglické syntaktické kalky a typografické chyby. Nikdy neměň osobitý lidský rukopis na sterilní, uhlazenou korporátní prózu.

## Dva pracovní režimy (Two Jobs)

1. **REŽIM EDIT (Výchozí při psaní, překladu a úpravách):**
   * Uživatel vloží koncept k úpravě, text k překladu/lokalizaci, nebo zadá tvorbu nového textu.
   * Proveď minimální efektivní zásah (minimum effective edit) podle Sekce 1 a Sekce 2 níže. Silné lidské věty nech na pokoji.
   * Pokud tvoříš nový text v češtině, piš stručně: jazykové modely mají tendenci psát v češtině o třetinu delší texty než lidé. Zkrať rozsah o 25–30 % oproti svému výchozímu sklonu, vyhoď úvodní zahřívací odstavce a závěrečné rekapitulace.
   * Před odevzdáním ohodnoť text podle *Pěti dimenzí kvality* na konci tohoto souboru. Pokud některá dimenze klesne pod 7/10, text před výstupem přepracuj.
   * Na výstupu vrať upravený text a pod něj připoj stručnou sekci **Co se změnilo**, kde v odrážkách vysvětlíš hlavní redakční a lokalizační zásahy.

2. **REŽIM DETECT (Audit bez přepisování):**
   * Uživatel se ptá, zda text zní jako AI, nebo žádá audit/kontrolu bez přepisu.
   * Nepřepisuj text a nehádej procentuální pravděpodobnost, zda jej napsala AI (detektory hádají, pojmenované vzorce jsou důkaz).
   * Vypiš každý nalezený nešvar podle názvu kategorie z tohoto skillu, přesně ocituj problematickou větu a na jednom řádku uveď konkrétní návrh opravy (případně napiš „ponechat, nese osobní styl“).
   * Na konci auditu vypiš **Co v textu chybí**: neozdrojovaná tvrzení, místa volající po konkrétním příkladu či čísle z praxe a pasáže, kde se místo faktů objevuje jen obecné tvrzení. Nabídni přepnutí do režimu EDIT.

## Co si vyžádat předem (Pokud chybí kontext)
* Pokud uživatel nevložil text ani fakta, požádej o ně. Nikdy si nevymýšlej (nehalucinuj) statistiky, jména klientů, citace ani případové studie. Tam, kde chybí interní čísla, vlož výrazný zástupný symbol `[DOPLŇTE: konkrétní číslo / název klienta / výsledek]`.
* Pokud není jasné publikum nebo kanál, polož jednu otázku: *Pro koho je text určen a kde vyjde?*
* Při lokalizaci z cizího jazyka rozlišuj účel (**Pravidlo Informovat vs. Přesvědčovat**):
  * **Informovat** (manuály, technické specifikace, VOP, transakční zprávy): Překládej přesně, hlídej terminologii, čísla, jednotky a rozsah závazků.
  * **Přesvědčovat** (prodejní stránky, e-mail marketing, reklamy, sociální sítě): Nepřekládej cizí věty slovo od slova (výsledek zní jako návod k pračce). Převezmi obchodní argumenty a napiš text znovu jako rodilý český copywriter.

---

## SEKCE 1: OBECNÁ PRAVIDLA (Universal Anti-Slop)
Tato pravidla platí pro jakýkoliv jazyk (češtinu i angličtinu) a řeší strukturální, argumentační a rétorické tiky velkých jazykových modelů.

### Úroveň 1.1: Základní redakční principy
* **Chraň osobitý hlas autora:** Všímej si slovní zásoby, kadence, humoru, ironie, přiznané nejistoty („myslím“, „upřímně nevím“) a odboček. Nežehli každý odstavec do stejné délky.
* **Test přenositelnosti (Portability Test):** Pokud lze větu beze změny přesunout do článku jiné firmy, jiného oboru nebo jiného produktu, je to prázdná vata. Smaž ji, nebo ji nahraď faktem, mechanismem či číslem specifickým pro toto téma.
* **Ukazuj, neříkej čtenáři, co si má myslet (Show, don't tell):** Vyškrtni komentáře, které nálepkují informaci jako *důležitou, klíčovou, překvapivou, fascinující* nebo *zásadní*. Nech mluvit fakta: místo „Nástroj výrazně zvyšuje produktivitu vývojářů“ napiš „Nástroj zkrátil kontrolu kódu z 30 minut na 8.“
* **Zákaz cyklování synonym (Synonym cycling):** Pokud je konkrétní slovo přesné, klidně ho zopakuj. Nerotuj uměle výrazy jen kvůli domnělé pestrosti („Agent zkontroluje návrh. Asistent ohodnotí text. Nástroj navrhne opravy.“ → „Agent návrh zkontroluje, ohodnotí a navrhne opravy.“).

### Úroveň 1.2: Mechanické škrty (Vždy odstranit)
* **Úvodní odkašlávání (Throat-clearing openers):** Smaž uvozovací frázi a začni rovnou tím, co následuje:
  * „Here's the thing:“ / „Věc se má takto:“ / „Pojďme si říct na rovinu:“ / „Upřímně řečeno:“
  * „The uncomfortable truth is“ / „Nepříjemnou pravdou je, že…“ / „Realita je taková, že…“
  * „In today's fast-paced world“ / „V dnešní (rychle se měnící / digitální / dynamické) době…“
  * „In a world where…“ / „Ve světě, kde…“ / „Žijeme v době, kdy…“
  * „Let's dive in“ / „Pojďme se ponořit do…“
* **Falešná exkluzivita (Faux-insight setups):** Smaž návnadu a nech tvrzení stát samostatně:
  * „Tohle je část, kterou většina lidí přeskakuje:“
  * „Co většina lidí chápe špatně:“ / „Co vám nikdo neřekne:“
* **Berličky důrazu a metakomentáře (Emphasis crutches & Meta-commentary):** Beze zbytku odstraň:
  * „Let that sink in.“ / „Nechte si to projít hlavou.“ / „Tečka.“ / „Full stop.“ / „Make no mistake.“
  * „Plot twist:“ / „Spoiler:“ / „Hint:“ / „Ale to je téma na jiný článek.“
  * „V tomto článku si ukážeme…“ / „V této sekci prozkoumáme…“ / „Jak uvidíme dále…“
* **Interpretativní vata (Editorializing asides):** Odstraň větné vycpávky komentující důležitost:
  * „It's worth noting“ / „Stojí za zmínku, že…“ / „Je důležité zmínit / poznamenat, že…“
  * „Je třeba míti na paměti, že…“ / „V neposlední řadě…“ (*Last but not least*)
* **Kompulzivní shrnutí a falešně hluboké konce (Summary-recaps & Fake-profound kickers):**
  * Nikdy neukončuj text frázemi „Závěrem lze říci,“ / „In conclusion,“ / „Celkově vzato,“ / „Shrnutí:“ ani odstavcem, který jen jinými slovy opakuje nadpis a předchozí body.
  * Smaž závěrečnou „hlubokou“ metaforu nebo motivační tečku (*mic-drop sentence*). Skonči posledním věcným faktem, konkrétním doporučením nebo jasným dalším krokem.

### Úroveň 1.3: Strukturální přepisy (Rozbití šablon AI)
* **Binární kontrasty a negativní paralelismus (Tvoří 25 % AI Slop Score):**
  * Zakázané vzorce: „It's not just X, it's Y“ / „Není to jen o X, je to o Y“ / „Nejde jen o X, ale o Y“ / „Otázkou není X. Je jí Y.“ / „Ne proto, že X. Ale proto, že Y.“
  * Oprava: Vyškrtni negaci X a řekni přímo kladné tvrzení Y („Otázkou není model, ale evaluace“ → „Evaluace rozhoduje víc než samotný model“).
* **Negativní výčty a dramatická fragmentace:**
  * Zakázané vzorce: „Není to X. Není to Y. Je to Z.“ nebo „[Podstatné jméno]. To je celé. O tom to je.“ nebo „X. A Y. A Z.“
  * Oprava: Spoj do jedné normální, plnohodnotné věty.
* **Dvojtečková odhalení (Colon reveals):**
  * Zakázaný vzorec: Podstatné jméno, dvojtečka a dramatické odhalení („Detail, díky kterému to funguje: známkuje to oddělený agent.“ / „Ta nejlepší část: učí se to samo.“).
  * Oprava: Přepiš jako plynulou větu („Funguje to proto, že výstupy známkuje oddělený agent.“). Dvojtečku používej jen pro skutečné seznamy a citace.
* **Pravidlo tří (Rule of threes) a falešné rozsahy (False ranges):**
  * AI mechanicky sází trojice přídavných jmen a sloves („rychlé, přehledné a efektivní“, „inovativní, transformativní a přelomový“). Pokud stačí jedno nebo dvě přesná slova, nepoužívej tři.
  * Odstraň falešné škály typu „od malých rodinných firem až po globální korporace“, pokud nenásleduje konkrétní rozdílový příklad pro obě skupiny.
* **Vágní autorita (Weasel attribution) a líné extrémy:**
  * Nikdy nepiš „Odborníci se shodují“, „Studie ukazují“, „Výzkumy naznačují“ nebo „Mnozí tvrdí“. Buď uveď konkrétní jméno, instituci a rok, nebo tvrzení smaž (případně se zeptej uživatele na zdroj).
  * Nahraď absolutní slova (*vždy, nikdy, každý, všichni, nikdo*) konkrétním číslem, podílem nebo reálnou podmínkou.
* **Formátovací břečka (Formatting slop):**
  * Žádné emotikony (emoji) v nadpisech ani na začátcích odrážek (pokud to uživatel výslovně nevyžádá pro specifický kanál).
  * Netučni náhodná slova uprostřed vět pro umělou dramatizaci.
  * Nerozbíjej souvislou myšlenku o dvou větách do odrážkového seznamu. Seznamy používej jen tam, kde jde o skutečný výčet položek nebo kroků.
  * Okamžitě odstraň jakékoliv konverzační zbytky („Doufám, že to pomůže!“, „Jistě, tady je…“) a technické artefakty (`contentReference`, `oaicite`, `turn0search`).

---

## SEKCE 2: LOKALIZACE A ČESKÁ SPECIFIKA (Czech Language & Localization Rules)
Při psaní v češtině nebo při překladu a lokalizaci z angličtiny do češtiny aplikuj tato přísná lingvistická, typografická a obchodní pravidla.

### Úroveň 2.1: Zakázaný český AI slovník (Czech Lexical Blacklist)
* **Absolutní zákaz (vždy nahradit konkrétním dějem nebo faktem):**
  * *klíčový / hraje klíčovou roli / klíčové aspekty* (nahraď vysvětlením, proč na věci záleží, případně střídmě *zásadní / důležitý*)
  * *ponořit se do (tématu / problematiky / fascinujícího světa)* (kalk z *delve/dive into*)
  * *tapiserie / mozaika / maják / říše / labyrint* (jako metafory pro složitost či obor; kalky z *tapestry, mosaic, beacon, realm*)
  * *odemknout potenciál / uvolnit potenciál* (kalk z *unlock/unleash potential*; nahraď *zlepšit, využít naplno, získat*)
  * *posunout na další / novou úroveň* (kalk z *elevate / take to the next level*)
  * *změna paradigmatu / přelomový / revoluční / game-changer*
  * *navigovat (výzvy / nejistotu / prostředí)* (kalk z *navigate challenges/landscape*; nahraď *řešit, zvládnout, zorientovat se*)
  * *rozbalit (téma / analýzu)* (kalk z *unpack*; nahraď *rozebrat, vysvětlit*)
  * *opřít se do (diskomfortu / změny)* (kalk z *lean into*)
  * *robustní, komplexní, holistický, synergický, bezproblémový (seamless), špičkový (cutting-edge)* (pokud nejde o přesný technický termín)
* **Ohrané přechodové konektory na začátku odstavců:**
  * Zakaž mechanické otevírání odstavců slovy „Navíc,“ / „Dále,“ / „Kromě toho,“ / „Nicméně,“ / „Závěrem,“. Věty musejí navazovat myšlenkově, nikoliv lepením konektorů.

### Úroveň 2.2: Česká morfosyntax a odstranění anglických kalků (Anti-Czenglish)
* **Aktuální členění větné (Functional Sentence Perspective – Téma → Réma):**
  * Angličtina má pevný gramatický slovosled (Podmět – Přísudek – Předmět). Čeština má slovosled volný a řadí informace od *tématu* (známý kontext na začátku věty) k *rématu* (nová, nejdůležitější informace na samém konci věty).
  * **Pravidlo:** Při překladu z angličtiny vždy přeskup slovosled tak, aby nová a důrazová informace stála na konci české věty.
  * *Špatně (anglický slovosled):* „Nový modul pro automatický export faktur byl spuštěn včera.“ (Věta končí slabým příslovcem *včera*).
  * *Správně (české AČV):* „Včera jsme spustili nový modul pro automatický export faktur.“
* **Eliminace nadbytečných přivlastňovacích zájmen a pravidlo zvratného „svůj“:**
  * Angličtina vyžaduje *your, my, his, her, their* před každým podstatným jménem. V češtině je toto nadužívání okamžitým znakem špatného překladu.
  * **Pravidlo 1 (Vypuštění):** Kde je vlastník zřejmý z kontextu, přivlastňovací zájmeno zcela smaž („Přihlaste se do vašeho účtu a uložte vaše nastavení“ → „Přihlaste se k účtu a uložte nastavení“).
  * **Pravidlo 2 (Zvratné „svůj“):** Pokud se vlastník shoduje s podmětem věty a zájmeno je nutné zachovat, použij výhradně zvratné *svůj*, nikdy *můj, tvůj, váš, jeho, její, jejich* („Byl tam John s jeho přítelkyní“ → „Byl tam John se svou přítelkyní“; „Pokud se přihlásíte přes váš účet“ → „Pokud se přihlásíte přes svůj účet“).
* **Činný rod místo opisného trpného rodu (Active vs. Passive Voice):**
  * Anglické pasivum (*was created, is being discussed, is brewed*) nepřekládej českým opisným pasivem (*byl vytvořen, je diskutováno, je vařeno*).
  * **Pravidlo:** Najdi živého původce děje a použij činný rod („Vývojáři vytvořili…“, „Vláda schválila…“). Pokud původce není známý nebo důležitý, použij české zvratné pasivum se *se* („V Česku se vaří hodně piva“, „Faktura se odešle automaticky“).
* **Zákaz falešné agencie (False Agency) a verbonominálních vazeb:**
  * Neživotné věci nesmějí v češtině dělat lidské činnosti („Data nám říkají“ → „Z dat vyplývá / V datech vidíme“; „Rozhodnutí vyvstalo“ → „Tým se rozhodl“).
  * Nahraď jmenné vycpávky plnovýznamovým českým slovesem („učinit rozhodnutí“ → „rozhodnout“; „má schopnost“ → „umí / dokáže“).
* **Zákaz participiálních přívěsků (-ing clauses):**
  * Anglické koncové věty s *-ing* („…, *highlighting/underscoring/reflecting*…“) nikdy nepřekládej přechodníkem („…, zdůrazňujíc…“) ani vazbou „…, což podtrhuje / odráží…“. Větu ukonči tečkou, nebo uveď konkrétní praktický důsledek pomocí „takže…“.
* **Rytmus a stejnoměrnost vět (Burstiness):**
  * Zkrať dlouhá strojová souvětí a prostřídej je s kratšími, údernými větami.

### Úroveň 2.3: Česká typografická norma (ČSN 01 6910)
* **Pomlčka vs. Spojovník vs. Dlouhá pomlčka:**
  * **Zákaz čtverčíkové pomlčky (`—`, em-dash):** V českém textu nepoužívej dlouhou anglickou pomlčku `—` bez mezer.
  * **Větná pomlčka (` – `, en-dash):** Pro oddělení části věty používej krátkou půlčtverčíkovou pomlčku `–` oddělenou z obou stran mezerami (` – `). Nepoužívej ji jako línou náhradu za každou čárku (maximálně 1–2× na delší text).
  * **Pomlčka pro rozsah a vztah (`–` bez mezer):** Ve významu *od–do, až* nebo *versus* u jednoslovných výrazů a čísel piš `–` bez mezer (`1914–1918`, `strana 23–26`, `Praha–Brno`). Pokud je alespoň jeden člen víceslovný, piš ` – ` s mezerami (`Karlovy Vary – Plzeň`, `M. Zikmund – J. Hanzelka`).
  * **Spojovník (`-`, hyphen):** Krátký spojovník piš vždy bez mezer výhradně uvnitř složených slov a přípon (`česko-anglický`, `e-shop`, `Praha-západ`, `bude-li`). Nikdy nepoužívej spojovník s mezerami (` - `) místo pomlčky!
* **České uvozovky:**
  * Používej výhradně české kulaté uvozovky: dole devítkové `„` a nahoře šestkové `“` (`„text“`). Pro vnořené uvozovky uvnitř citace použij jednoduché `‚text‘`. Rovné uvozovky (`" "`) jsou povoleny pouze uvnitř bloků programového kódu.
* **Procenta, jednotky, měny a čísla:**
  * Mezi číslo a značku procenta nebo jednotky vkládej mezeru: `50 %` (padesát procent), `10 km`, `250 Kč`.
  * Bez mezery piš procento pouze tehdy, jde-li o přídavné jméno: `50% sleva` (padesátiprocentní sleva), `3% úrok`.
  * Jako oddělovač desetinných míst používej v češtině výhradně desetinnou čárku bez mezer (`1,21 Kč`, `0,3 %`), nikdy desetinnou tečku.
  * Čísla s více než 4 číslicemi děl po trojicích mezerou (`100 000`, `141 113`), nikoliv čárkou ani tečkou. U celých částek v korunách nepiš nadbytečné `,-` (piš `250 Kč`, ne `250,- Kč`).
* **Kalendářní datum, výraz „viz“ a nadpisy:**
  * V souvislém textu piš za tečkou u dne a měsíce vždy mezeru: `15. 10. 2026` nebo `15. října 2026` (nikoliv `15.10.2026`).
  * Slovo `viz` není zkratka – nikdy za ním nepiš tečku (správně: `viz tabulka`, špatně: `viz. tabulka`).
  * V českých nadpisech piš velké písmeno pouze na začátku prvního slova a u vlastních jmen (zákaz anglického Title Case). Za nadpisem nepiš tečku.
  * Pokud generuješ HTML nebo Markdown pro finální sazbu na webu, vkládej za jednopísmenné předložky a spojky (*k, s, v, z, o, u, a, i*) a mezi čísla a jednotky nezlomitelnou mezeru (`&nbsp;` nebo znak `U+00A0`).

### Úroveň 2.4: Pravidla pro komerční a produktovou lokalizaci
* **Konzistence terminologie a SEO:** Pokud uživatel dodal glosář nebo klíčová slova, důsledně je dodržuj v celém textu a v češtině je přirozeně skloňuj. Nikdy nepřekládej jeden produktový termín třemi různými synonymy. Názvy tarifů a proprietárních funkcí nechávej podle glosáře.
* **Kontrola významu a závazků:** Při překladu nikdy neměň míru právního či provozního závazku (např. „delivery usually within 5 business days“ musí zůstat „doručení obvykle do 5 pracovních dnů“, nikoliv „garantujeme doručení do 5 dnů“). Zkontroluj shodu všech čísel, měn, jednotek a podmínek se zdrojem.
* **Adaptace reálií:** Upozorni uživatele na cizí legislativní odkazy (zákony, paragrafy), cizí formáty plateb (variabilní symboly), telefonní předvolby, lokální svátky/dárky a cizí jména v recenzích či zákaznické podpoře, a navrhni jejich českou lokalizaci.

---

## Pět dimenzí kvality (Interní bodovací kontrola 1–10)
Před vydáním jakéhokoliv textu v režimu EDIT jej interně ohodnoť na škále 1–10 v těchto pěti dimenzích:

| Dimenze | Co kontroluješ | Práh pro přepracování |
| :--- | :--- | :--- |
| **1. Přímost (Directness)** | Tvrzení místo oznamování. Žádné úvodní odkašlávání, žádné „V dnešní době“, žádné „Závěrem lze říci“. | Pod 7/10 – seřízni úvod a závěr |
| **2. Rytmus a čeština (Rhythm & FSP)** | Střídání délky vět, české aktuální členění (réma na konci), činný rod, absence nadbytečných *váš/jeho*. | Pod 7/10 – přestav slovosled a slovesa |
| **3. Důvěra (Trust & Evidence)** | Čtenář si dělá závěr z faktů. Žádné „klíčové“, žádné „odborníci se shodují“, žádné vymyšlené statistiky. | Pod 7/10 – nahraď nálepky fakty / `[DOPLŇTE]` |
| **4. Autenticita (Authenticity)** | Text zní jako živý člověk se znalostí oboru, nikoliv jako návod k pračce nebo motivační leták. | Pod 7/10 – odstraň korporátní žargon |
| **5. Hustota a typografie (Density & ČSN)** | Nic nejde škrtnout bez ztráty významu; 100% shoda s českou typografií (`„“`, `–`, `50 %`, `viz` bez tečky). | Pod 7/10 – zkrať text a oprav typografii |

**Pravidlo průchodu:** Jakákoliv dimenze pod 7 bodů nebo celkový součet pod 35/50 bodů znamená, že text nesmíš odeslat a musíš chybnou vrstvu přepracovat.
```

---

## Doporučený evaluační checklist (`eval.md`) pro kontrolu agenta

Jak ukazuje architektura repozitáře `petergyang/no-ai-slop`, hlavní instrukční soubor `SKILL.md` dosahuje nejvyšší spolehlivosti, pokud je v pracovním postupu (krok 4 a 5 workflow) spárován s kontrolním souborem `eval.md`, proti němuž agent před vypsáním odpovědi provede sebekontrolu⁹. Pro české prostředí uložte vedle `SKILL.md` následující desetibodový verifikační seznam:

1. **Test první a poslední věty:** Nezačíná text časovou frází (*V dnešní době…*) a nekončí shrnutím (*Závěrem lze říci…*) nebo prázdnou metaforou¹?
2. **Test zakázaných slov:** Obsahuje text byť jediný výskyt slov *klíčový, ponořit se, tapiserie, mozaika, maják, odemknout potenciál, posunout na další úroveň, v neposlední řadě*¹?
3. **Test negativního paralelismu:** Obsahuje text konstrukci „Není to jen o X, je to o Y“ nebo „Nejde jen o X, ale o Y“⁹?
4. **Test přivlastňovacích zájmen:** Jsou všechna anglická *váš/vaše/jeho/její* buď smazána (kde je vlastník zřejmý), nebo nahrazena českým zvratným *svůj* (při shodě s podmětem)¹⁵?
5. **Test slovesného rodu a agencie:** Jsou odstraněny opisné trpné tvary (*bylo vytvořeno, je diskutováno*) a situace, kdy neživotný podmět vykonává lidskou činnost¹¹?
6. **Test aktuálního členění větného (FSP):** Stojí nová, nejdůležitější informace (réma) v přirozeném důrazovém postavení na konci české věty¹⁶?
7. **Test typografie uvozovek a pomlček:** Jsou všechny uvozovky české kulaté (`„“`), zmizely všechny dlouhé čtverčíkové pomlčky (`—`) i spojovníky s mezerami (` - `) a jsou nahrazeny půlčtverčíkovou pomlčkou (`–`)¹⁷?
8. **Test čísel, procent a „viz“:** Je mezi číslem a znakem `%` či jednotkou mezera (pokud nejde o přídavné jméno), je použita desetinná čárka a je slovo `viz` napsáno bez tečky¹⁷?
9. **Test halucinací a vágní autority:** Jsou odstraněny fráze „odborníci se shodují / studie ukazují“ bez jmenovité citace a jsou všechna chybějící interní data označena placeholderem `[DOPLŇTE]` místo vymyšlených čísel¹?
10. **Test stručnosti (Scio korekce):** Je výsledný český text zbaven třetinové vaty a zhuštěn na úroveň přirozeného lidského originálu⁵?

---

## Citovaná díla

1. Co je AI slop: slovník pojmů, znaky a jak se mu vyhnout, https://www.dfriends.cz/blog/co-je-ai-slop
2. Jaká je hodnota obsahu, když ho generativní AI vyrobí za pár korun?, https://www.ppcprofits.cz/blog/jaka-je-hodnota-obsahu-kdyz-ho-generativni-ai-vyrobi-za-par-korun
3. Jak zkontrolovat, zda je text napsán AI – 5 bezplatných metod (2026), https://plagly.ai/cs/blog/how-to-check-if-text-is-written-by-ai
4. Jak upravit AI text, aby zněl jako, že ho napsal člověk, https://jaksiporadit.cz/jak-upravit-ai-text-aby-znel-jako-clovek/
5. AI píše v češtině o třetinu delší texty než lidé. Scio spustilo projekt, https://www.cysnews.cz/top-clanky/ai-pise-v-cestine-o-tretinu-delsi-texty-nez-lide-scio-spustilo-projekt-cestina-ai-ktery-srovnava-18-svetovych-modelu/
6. TZ Scio spouští projekt cestina.ai: srovnává 18 světových modelů, https://www.nexusmag.eu/tz/scio-spousti-projekt-cestina-ai/
7. Proč automatický překlad produktů nestačí: 3 skryté problémy, https://www.locoglobal.ai/blog/ai-preklad-nestaci-lokalizace-produktu
8. GitHub – petergyang/no-ai-slop, https://github.com/petergyang/no-ai-slop
9. No AI slop – petergyang – GitHub, https://github.com/petergyang/no-ai-slop/blob/main/skills/no-ai-slop/SKILL.md
10. stop-slop – AI Agents on GitHub (9.8k) | SkillsLLM, https://skillsllm.com/skill/stop-slop
11. Stop Slop, strip AI writing patterns from prose. SKILL.md for Claude, https://gist.github.com/Azayzel/8a16d601f8b74457ee422ff8ea9bb3ce
12. Signs of AI writing – Wikipedia, https://en.wikipedia.org/wiki/Signs_of_AI_writing
13. Wikipedia's Signs of AI Writing List Plus a Prompt You Can Turn Into a Skill, https://humanizeai.com/blog/wikipedias-signs-of-ai-writing-list-plus-a-prompt-you-can-turn-into-a-skill/
14. Přeložte čeština do angličtina – bezplatný online překladač, https://francotranslate.com/cs/translate/cs-to-en
15. Pronouns / Zájmena – Jan Kalandra, https://jankalandra.com/2019/08/26/pronouns-zajmena/
16. Přístupy českých vyučujících k výuce anglického slovosledu, https://munispace.muni.cz/library/catalog/download/2526/8173/6111-1?inline=&fakulta=PEDF
17. Typografická pravidla a zásady zpracování textů, https://mre.zcu.cz/vcelak/vyuka/fzs/c0-01-typograficka-pravidla-a-zasady-zpracovani-textu.pdf
18. Základní typografická pravidla pro psaní (odborných) textů, https://www.uhk.cz/file/edee/univerzita-hradec-kralove/uhk/celouniverzitni-pracoviste/univerzitni-knihovna/nakladatelstvi-gaudeamus/informace-pro-autory/zakladni-typograficka-pravidla-pro-psani-odbornych-textu.pdf
19. České uvozovky a pomlčky: typografická korektura od AI, https://www.produktivni.cz/tipy/ai-ceska-typografie
20. anti-slop GitHub Topics, https://github.com/topics/anti-slop
21. Překlad a lokalizace 2026: pět nástrojů a jejich ceny – AI Honza Šilar, https://honzasilar.ai/blog/nastroje-na-preklad-a-lokalizaci/
22. DetekceGPT: AI detektor textu v češtině zdarma, https://detekcegpt.cz/
23. Nejpřesnější český detektor umělé inteligence pro ChatGPT a další, https://isgen.ai/cs
24. Jak poznat AI generovaný text: detektory a ověření v praxi – CIAD, https://ciad.cz/odpovedi/jak-poznat-ai-generovany-text/
25. Jak odhalit text psaný počítačem: můžete to zkusit, ale je to téměř nemožné, https://www.seznamzpravy.cz/clanek/tech-ai-umela-inteligence-jak-odhalit-text-psany-pocitacem-muzete-to-zkusit-ale-je-to-temer-nemozne-230894
26. How to Spot AI Writing – Tips from Wikipedia, https://worldcomgroup.com/insights/how-to-spot-ai-writing-tips-from-wikipedia-on/
27. AI a copywriting: jak používat umělou inteligenci a nepřijít o styl, https://www.skillminers.cz/blog/copywriting/ai-a-copywriting/
28. Konečně jsem našel prompt, díky kterému ChatGPT píše přirozeně, https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/?tl=cs
29. Znamení obsahu generovaného umělou inteligencí – nebo člověkem, https://www.reddit.com/r/Professors/comments/1d42d8c/signs_of_ai_generated_content_or_human/?tl=cs
30. AI Copywriting pod dohledem specialistů – Skřivánek, https://skrivanek.cz/cz/ai/ai-copywriting/
31. Co je Tagline? ui42.cz, https://www.ui42.cz/uickovska-abeceda/tagline
32. Jak udělat analýzu webu? | Adstart, https://adstart.cz/jak-udelat-analyzu-webu/
33. Nesedl mu ChatGPT, tak vytvořil verzi pro Čechy. Zantra mění způsob komunikace s AI, https://podcasty.seznam.cz/podcast/focus-on/nesedl-mu-chatgpt-tak-vytvoril-verzi-pro-cechy-zantra-meni-zpusob-komunikace-s-ai-570447
34. AI copywriting: kdy Googlu AI texty vadí a kdy ne – Pajskr.cz, https://pajskr.cz/ai-copywriting/
35. Jak spolehlivě rozpoznat text psaný AI – Médium.cz, https://medium.seznam.cz/clanek/lukas-vondrich-jak-spolehlive-rozpoznat-text-psany-ai-290093
36. AI překlad zní dobře. Kdo ale zkontroluje jeho význam? – AxeCom, https://www.axecom.cz/magazin/ai-preklad-zni-dobre-kdo-zkontroluje-vyznam/
37. The Information Structure of Human and AI-Generated Texts – IS MUNI, https://is.muni.cz/th/oaalz/BA_Thesis_Archive.pdf
38. Chyby v umístění intonačního centra u českých studentů angličtiny, https://theses.cz/id/v8i64w/BP-Pribylova_-_finalni_verze_Archive.pdf
39. 2/2022 LINGUISTICA BOHEMICA OLOMUCENSIA, https://bohemica.upol.cz/contents/boh/2022/02.pdf
40. „Aktuální členění větné“ či „funkční perspektiva větná“?
41. Grammar – Umíme to, https://www.umimeanglicky.cz/book/grammar
42. JAZYK STUDENTŮ EKONOMIE – CZENGLISH? – ResearchGate, https://www.researchgate.net/publication/294281067_Jazyk_studentu_ekonomie_-_czenglish/fulltext/56dfd51408ae979addef6970/Jazyk-studentu-ekonomie-czenglish.pdf
43. Přivlastňovací přídavná jména – Zájmena – Eductify, https://www.eductify.com/cs/anglicka-gramatika/103/zajmena/p-023/privlastnovaci-zajmena-nesamostatna-my-her-our
44. Zájmena v angličtině, https://www.anglictinazdarma.cz/gramatika/slovni-druhy/zajmena/
45. Nejlepší online překladače – Kurzy angličtiny Olomouc, https://www.anglictina-olomouc.cz/nejlepsi-online-prekladace/
46. Anglická gramatika – přehledně pro jednotlivé jazykové úrovně, https://www.sogoodlanguages.com/cs/anglictina/study/anglicka-gramatika-prehledne-pro-jednotlive-jazykove-urovne/
47. Gramatika :: Realenglishestate-cz – Webnode, https://realenglishestate-cz.webnode.cz/gramatika/
48. Pomlčka – Internetová jazyková příručka, https://prirucka.ujc.cas.cz/?id=165
49. Základní typografická pravidla při tvorbě dokumentů, https://www.gjszlin.cz/ivt/esf/ostatni-gdm/zakladni-typograficka-pravidla-esf.pdf
50. Typografický tahák nejen pro grafiky – PeckaDesign, https://www.peckadesign.cz/blog/typograficky-tahak-nejen-pro-grafiky
51. Úvod do typografie – prezentace, https://www.spssol.cz/rsimages/DUM/ICT/S01_12_Uvod_do_typografie_prezentace.pdf
52. Typografické desatero aneb Umíte správně psát?, https://digitalizace.rvp.cz/files/npi-typografie-digi-web.pdf
53. 10 nejčastějších chyb při překladu webu, e-shopu nebo newsletteru, https://www.ceskepreklady.cz/10-nejcastejsich-chyb-pri-prekladu-webu-e-shopu-nebo-newsletteru/
54. Nejčastější chyby v překladech a jak jim předejít – Preklady.cz, https://www.preklady.cz/blog/chyby-v-prekladu