---
name: ui-copy-cs
license: MIT
description: Piš a kontroluj české texty rozhraní při programování webů a aplikací. Použij pro nadpisy, tlačítka, formuláře, dialogy, hlášky a přístupné popisky, včetně řetězců v kódu. Nepoužívej jako obecný editor článků.
---

# Texty rozhraní bez AI klišé

Verze 1.0.0 · 2026-10-30 · česká varianta

Copyright © 2026 Luděk Sušický

## Účel a kompatibilita

Piš stručné české texty, podle kterých uživatel pozná obsah, další krok a skutečný stav aplikace. Tento skill je určen pro všechny AI asistenty schopné pracovat s textovými instrukcemi. Nevyžaduje konkrétního poskytovatele, model, editor, API ani nástroj. Načti jej jako skill, přilož Markdown nebo vlož jeho obsah do kontextu. Automatické načítání závisí na prostředí. Přenositelnost neznamená ověření na všech modelech.

Pravidla jsou zvolený redakční styl. Neurčují autorství textu a neslibují obcházení detektorů AI. Při rozporu respektuj výslovné zadání uživatele a závazná pravidla projektu. Zachovej autorem určené názvy a citace.

## Rozsah

Použij při tvorbě i úpravách viditelného textu UI: nadpisy, navigace, tlačítka, formuláře, dialogy, validace, oznámení, prázdné stavy, tooltipy, placeholdery a přístupné popisky. Patří sem uživatelské řetězce v HTML, JSX, PHP, překladových souborech i jiném kódu.

Neměň programové identifikátory, klíče překladů, API, příkazy, URL, názvy souborů, verze, regulární výrazy, logy, citace ani uživatelská data. Články, odborné texty a obecná dokumentace jsou mimo rozsah. Jejich názvy zobrazené v UI bez zadání nepřepisuj.

## Pravidla interpunkce

- Nadpis stránky, sekce, karty nebo dialogu nemá koncovou tečku, ani když tvoří celou větu. Nadpis se dvěma větami přeformuluj na jeden přehledný celek.
- Tlačítka, menu, popisky polí, krátké stavy a jednořádkové tipy nemají koncovou tečku. Popisky polí a nadpisy nemají ani koncovou dvojtečku.
- Vysvětlující odstavce a vícevěté chyby používají běžnou větnou interpunkci. Rozhoduje funkce textu, ne jeho zalomení na obrazovce.
- Skutečná otázka si zachovává otazník, také v nadpisu. Zkratky, desetinná čísla a jiné významové tečky zachovej; nepoužívej plošné odstraňování posledního znaku.
- Nepoužívej dlouhou pomlčku U+2014 ani pomlčku jako spojení vět či oddělovač sloganu. Nenahrazuj ji mezerovaným spojovníkem, U+2013 nebo dvěma spojovníky. Text zkrať, rozděl nebo přestav; dvojtečku použij pouze při skutečné potřebě vysvětlení.
- Zachovej rozsahy jako 1–5, spojovníky ve slovech a matematická znaménka. Technické řetězce jsou chráněné rozsahem skillu.
- Výpustku používej pro skutečně probíhající operaci, zkrácený obsah nebo zavedenou konvenci příkazu vyžadujícího další vstup. Není ozdoba každého tlačítka. Vykřičníky ani emoji nepřidávej pro efekt.

## Obsah a pojmenování

- Nadpis pojmenuje obsah nebo úkol. Tlačítko popisuje konkrétní akci, zpravidla infinitivem: „Uložit změny“, „Přidat soubor“, „Smazat projekt“.
- Jedna akce má v celém toku stejný název. „Uložit koncept“ a „Publikovat“ rozlišuj podle skutečného chování.
- Nepřidávej generické slogany, úvodní uvítání, opakující se podnadpisy ani výplň typu „vše na jednom místě“, „snadno a rychle“ či „posuňte svou práci na další úroveň“.
- Text má přinést potřebnou informaci. Pokud nic nepřidává, vynech jej. Nevytvářej povinné trojice výhod ani umělé kontrasty. Věcný seznam tří položek je v pořádku.
- Chyba řekne, co se nepodařilo a jak pokračovat, pokud je další krok znám. Příčinu uváděj jen tehdy, když ji aplikace zná. Nevymýšlej síťovou chybu, oprávnění ani technické limity.
- Úspěch potvrzuj pouze po skutečně potvrzeném úspěchu. Textem nemaskuj chybějící obsluhu chyby; případný nesoulad chování nahlas.
- U nevratné akce zachovej její následky. Odlišení archivace od smazání a konceptu od zveřejnění se nesmí ztratit kvůli zkrácení.
- Používej přirozenou češtinu, diakritiku a uvozovky „…“. Velké písmeno piš na začátku a ve vlastních jménech; nepřebírej anglický Title Case.
- Drž stávající oslovení a terminologii. Pokud projekt žádné nemá, použij neutrální vykání, bez nucené familiárnosti.
- Přístupný název zachová viditelné znění ovládacího prvku, případně doplní kontext. Neodstraňuj informace nutné pro čtečku obrazovky. Placeholder nenahrazuje trvalý popisek.

## Postup při programování

1. Zjisti jazyk, existující názvy a chování dotčené funkce. Použij pouze variantu pro cílový jazyk UI; nepřekládej celé rozhraní bez zadání.
2. Uprav potřebné řetězce v dotčené části. Zachovej proměnné, interpolace, escapování, pluralizaci a značky překladového formátu.
3. Rozliš nadpis, akci, krátký stav a vysvětlení. Uplatni odpovídající interpunkci a zkontroluj význam vůči původnímu textu.
4. Projdi také tooltipy, `aria-label`, placeholdery, validace a všechny dosažitelné stavy změněné funkce. Zkontroluj soulad viditelného a přístupného názvu.
5. Ověř diff. Neměň technické řetězce ani nesouvisející texty. Po zásahu do kódu použij dostupnou přiměřenou syntaktickou kontrolu nebo test dotčené funkce.

Při samotné revizi vypiš konkrétní nálezy a návrhy. Při zadání úpravy je proveď a stručně uveď výsledek a skutečně provedené ověření. Pokud text už funguje, ponech jej.

## Závěrečná kontrola

- Nadpisy a krátké ovládací texty nemají dekorativní koncovou interpunkci; otázky a významové znaky zůstaly.
- Není zde spojovací pomlčka, náhradní spojovník, prázdný slogan ani zbytečný podnadpis.
- Akce, stavy a následky odpovídají chování aplikace; význam a míra jistoty se nezměnily.
- Terminologie, oslovení a přístupné názvy jsou konzistentní.
- Interpolace a technické hodnoty zůstaly beze změny.

Při nejasném případu nebo podrobnější revizi použij [příklady](references/examples.md). Nevyžaduj různě dlouhé věty, minimální počet faktů, zákaz trojic ani skóre detektoru AI.

## Licence

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.