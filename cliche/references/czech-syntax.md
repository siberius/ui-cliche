# Česká morfosyntax: slovosled, zájmena, rod, agencie

Copyright © 2026 Luděk Sušický

Anglický model promítá do češtiny anglickou syntax. Pět rovin, na kterých to
opravovat, s příklady. Detekční zpráva cituje chybnou větu a navrhne opravu.

## 1. Aktuální členění větné (téma → réma)

Čeština má volný slovosled; informace řadí od tématu (známý kontext) na
začátku k rématu (nová, nejdůležitější informace) na konci věty. Angličtina
má pořadí pevné a při překladu ho model otrocky opisuje.

- Špatně (anglické pořadí, slabé réma): „Nový modul pro automatický export
  faktur byl spuštěn včera."
- Správně (české členění): „Včera jsme spustili nový modul pro automatický
  export faktur."

**Pravidlo:** nová a důrazová informace patří na konec české věty.
Existenční anglické vazby („There came a moment…") se v češtině řeší prostou
inverzí („Nastal okamžik…").

## 2. Přivlastňovací zájmena a zvratné „svůj“

Angličtina vyžaduje *your, his, their* před podstatným jménem; čeština je
většinou nepotřebuje.

- **Pravidlo 1 (vypuštění):** je-li vlastník zřejmý z kontextu, zájmeno
  úplně vynechej. „Přihlaste se do vašeho účtu a uložte vaše nastavení"
  → „Přihlaste se k účtu a uložte nastavení".
- **Pravidlo 2 („svůj"):** shoduje-li se vlastník s podmětem věty, patří
  tam výhradně zvratné *svůj*, nikdy *můj, tvůj, váš, jeho, její, jejich*.
  „Byl tam John s jeho přítelkyní" → „…se svou přítelkyní";
  „přihlásíte se přes váš účet" → „přes svůj účet".

## 3. Trpný rod nahraď činným, nebo zvratným

Anglické pasivum (*was approved, is being discussed*) nepřekládej českým
opisným pasivem (*byl schválen, je diskutováno*).

- **Činný rod s původcem:** najdi aktéra a udělej z něj podmět.
  „Nový kurz byl schválen vládou" → „Vláda schválila nový kurz."
- **Zvratné pasivum:** není-li původce důležitý, použij *se*.
  „V Česku se vaří hodně piva", „Faktura se odešle automaticky."
- Opisné pasivum zůstává jen tam, kde je skutečně zdůrazněn děj nad
  původcem (úřední a odborné texty), ne jako výchozí volba.

## 4. Falešná agencie a verbonominální vazby

- Neživotné věci nedělají lidské činnosti: „rozhodnutí vyvstalo"
  → „tým se rozhodl"; „data nám říkají" → „z dat vyplývá"; „stížnost se
  stala opravou" → „ze stížnosti vznikla oprava" (a ideálně: kdo ji
  opravil).
- Plnovýznamová slovesa místo vazeb: „učinit rozhodnutí" → „rozhodnout";
  „má schopnost" → „umí, dokáže"; „provést analýzu" → „analyzovat";
  „slouží jako centrální uzel pro správu konceptů" → „spravuje koncepty
  na jednom místě".

## 5. Přechodníky a přívěsky s -ing

Anglická zakončení „…, *highlighting/underscoring*…" nepřekládej
přechodníkem („…, zdůrazňujíc…") ani mechanickou vazbou „…, což
podtrhuje / odráží…".

- Větu ukonči tečkou, nebo
  uveď praktický důsledek spojkou: „…, takže reporty stahujete jako PDF."

## 6. Rytmus (střídání délky vět)

Strojový text má stejnoměrné věty. Prostřídej dlouhá souvětí s krátkými
údernými větami podle emocionální váhy sdělení; krátká věta za dlouhým
souvětím nese důraz.

## Pravidla pro lokalizaci a překlad (čtěte jen u překladu)

- **Informovat vs. přesvědčovat:** technické a právní texty (manuály,
  obchodní podmínky, parametry) překládej přesně, hlídej terminologii, čísla
  a jednotky. Prodejní texty (landing pages, e-maily, reklamy) slovo od
  slova nepřekládej, výsledkem je „návod k pračce": převezmi obchodní
  argumenty a napiš text znovu jako rodilý český copywriter.
- **Závazky se nemění:** „doručení obvykle do 5 pracovních dnů" nesmí
  být „doručujeme garantovaně do 5 dnů". Rozsah závazku, dávkování i kroky
  postupu zůstávají přesně podle zdroje; plynulý překlad snadno posune
  význam, kontroluj větu po větě proti originálu.
- **Glosář a terminologie:** dodá-li uživatel glosář nebo klíčová slova,
  drž je v celém textu a přirozeně je skloňuj. Jeden pojem, jeden překlad;
  žádné rotování synonymy. Názvy tarifů a produktů překládej jen podle
  glosáře.
- **Reálie:** cizí legislativní odkazy (paragrafy, zákony jiných států),
  telefonní předvolby, formáty plateb, lokální dárky a cizí jména v podpoře
  nebo recenzích nelze převzít bez kontroly. Navrhni českou náhradu
  a neviditelné nech k rozhodnutí uživatele s poznámkou v Co se změnilo.
- **Chybějící data se nevymýšlejí:** místo vymyšleného čísla vlož
  zástupný symbol `[DOPLŇTE: …]`.
