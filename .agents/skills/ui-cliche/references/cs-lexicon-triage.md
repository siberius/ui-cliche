# Třístupňová terminologická triáž (cs-lexicon-triage)

Tato reference slouží LLM v roli adjudikátora pro posouzení kandidátů z linteru (`soft_candidate`) a eliminaci planých poplachů na platném českém jazyce.

## Zlaté pravidlo adjudikace
> **Regex nesmí mít monopol nad sémantikou.**  
> Pokud se podezřelé slovo nachází v přirozeném lidském textu, je přesné a doložené fakty, **nepřepisujte ho**. Ponechte jej a zařaďte do sekce `Zachováno (ověřeno)`.

---

## 1. Třístupňový rozhodovací katalog

### Kategorie 1: Doménově vázané termíny
Termíny, které mají v konkrétním oboru přesný a nezastupitelný význam, ale mimo něj působí cize či úřednicky.

| Výraz | Odborná doména | Kdy ZACHOVAT | Kdy NAHRADIT | Zavedená náhrada mimo doménu |
|---|---|---|---|---|
| **prerekvizity** | Vysoké školství, studijní plány, formální logika | V univerzitních informačních systémech (SIS, IS MUNI), sylabech předmětů a akreditačních spisech. | V SaaS aplikacích, komerčních e-shopech, webových průvodcích a obchodních slidech. | *co potřebujete předem*, *vstupní požadavky*, *nutné podmínky* |
| **robustní** | IT architektura, kryptografie, statistika | Je-li doložen konkrétní mechanismus (např. *robustní šifrování AES-256*, *robustní odhad rozptylu*). | Jako prázdné marketingové adjektivum (*robustní nástroj pro každého*). | *spolehlivý*, *stabilní*, nebo konkrétní popis mechanismu |
| **komplexní** | Medicína, věda, stavební řízení | Jde-li o vyšetření všech složek systému (např. *komplexní onkologické vyšetření*). | Jako vycpávkové synonymum pro „velký“ či „úplný“ (*komplexní platforma*). | *ucelený*, *kompletní*, *přehledný*, nebo škrtnout |
| **klíčový** | Analýza rizik, metriky | Jde-li o definovanou metriku (*klíčový ukazatel výkonnosti – KPI*). | Jako automatické zdůrazňovadlo (*klíčová výhoda našeho řešení*). | *hlavní*, *důležitý*, nebo uvést přímo fakt |

### Kategorie 2: Posunuté kalky a falešní přátelé
Výrazy, kde doslovný překlad z angličtiny posunul význam slova v češtině do nepřirozené nebo matoucí polohy.

| Výraz | Původ a diagnóza | Kdy ZACHOVAT | Kdy NAHRADIT | Přirozená česká náhrada |
|---|---|---|---|---|
| **hygienický standard** | Vychází z anglického *hygiene factors* (Herzbergova dvoufaktorová teorie). V češtině vázáno na fyzickou čistotu a sanitaci. | V medicíně, stravování, provozních předpisech a BOZP pro čistotu. | V produktovém marketingu, IT zabezpečení a obchodních textech. V HR teorii upřesnit na *hygienické faktory*. | *samozřejmý základ*, *nezbytné minimum*, *základní standard* |
| **dedikovaný** | Z anglického *dedicated*. V češtině tradičně znamená „věnovaný s věnováním“ (např. kniha). | U technických entit v IT žargonu (*dedikovaný server*). | V obecných rozhraních a popisech lidí či týmů (*dedikovaný specialista*). | *vyhrazený*, *samostatný*, *osobní poradce* |
| **adresovat** | Z anglického *to address an issue*. V češtině znamená psát adresu na obálku. | Výhradně při práci s poštovními/IP adresami. | Všude ve významu řešit problém či reagovat na podnět. | *řešit*, *vypořádat*, *reagovat na*, *odstranit problém* |

### Kategorie 3: Neusazené překladové kalky a pseudotermíny
Doslovné překlady anglických frází, které v češtině netvoří ustálený pojem a zastírají podstatu věci.

| Výraz | Původní anglický výraz | Diagnóza | Rozhodovací pravidlo | Doporučená česká náhrada |
|---|---|---|---|---|
| **mrtvé adresy / mrtvé odkazy** | *dead addresses / dead URLs* | Žargon, který běžnému uživateli neříká, co se stalo. | **Vždy nahradit** konkrétním popisem technického stavu. | *neexistující stránky (chyba 404)*, *nefunkční odkazy*, *nedoručitelné adresy* (u e-mailu) |
| **zkušenost** (vázaná na produkt) | *user experience / customer experience* | Nekritické vkládání slova *zkušenost* do každé věty (*„vaše nákupní zkušenost“*). | Nahradit přirozeným popisem nákupu, používání či prostředí. | *nákup*, *používání aplikace*, *objednávka* |
| **bezproblémový** | *seamless* | Oblíbené AI klišé pro jakékoli propojení systémů. | Nahradit konkrétním faktem (např. automatické párování). | *plynulý*, *automatický*, *přímý* |

---

## 2. Absolutní pojistka proti tvorbě novotvarů (Zákaz neologismů)

> **ZÁKAZ NEOLOGISMŮ:**  
> Pokud model narazí na pseudoodborný výraz a v češtině pro něj neexistuje jednoslovný zavedený ekvivalent, **nesmí model vymýšlet nový český patvar**.  
> **Správný postup:** Rozložte pojem na analytickou konstrukci: **konkrétní činné sloveso + přesný předmět**.
> 
> *Příklad:* Místo neologismu typu *„předpožadavkovost“* či *„vícekrokovost“* napište: *„Co musíte splnit před zápisem“* nebo *„Postup má 3 kroky“*.
