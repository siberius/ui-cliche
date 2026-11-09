---
name: prose-cs
license: MIT
description: Upravuj české texty do srozumitelné lidské prózy bez AI klišé a zachovej autorův hlas. Použij pro články, eseje, příspěvky a texty dokumentace, nebo jen pro detekci klišé bez přepisu. Ne pro texty rozhraní; při programování použij ui-copy-cs.
---

# Próza bez AI klišé

Verze 1.0.0 · 2026-11-09 · česká varianta

Copyright © 2026 Luděk Sušický

Metodika adaptována z [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT); toto vydání je samostatný text. Viz docs/SOURCES.md v repozitáři.

## Účel a kompatibilita

Přeměň koncept na srozumitelnější a živější prózu se zachováním osobního hlasu autora. Skill je určen všem AI asistentům schopným pracovat s textovými instrukcemi; nevyžaduje poskytovatele, model ani nástroj. Načti jej jako skill, přilož Markdown nebo vlož jeho obsah do kontextu. Přenositelnost neznamená ověření na všech modelech.

Pravidla jsou zvolený redakční styl. Neurčují autorství, neskórují text a neslibují obcházení detektorů AI. Výslovné zadání uživatele a závazná pravidla projektu mají přednost.

## Rozsah

Články, eseje, příspěvky na blog, newslettery a texty dokumentace. Texty rozhraní při programování patří skillu `ui-copy-cs`. Neměň citace, parafráze cizích textů, kód, technické identifikátory, URL ani autorova skutková tvrzení a výhrady.

## Dva typy zadání

**Úprava (výchozí).** Oprav koncept podle pravidel níže a vrať celý upravený text plus stručný seznam „Co se změnilo".

**Detekce.** Na dotaz, jestli text vypadá jako od AI, nebo na revizi bez přepisu: pojmenuj každý vzor, který se v textu objeví, cituj řádek a navrhni opravu v několika slovech. Text nepřepisuj, neskóruj ani neodhaduj, kdo ho napsal. Pojmenované vzory jsou důkaz, který si čtenář může ověřit; detektory jen hádají.

## Zásady úpravy

- Zachovej autorův skutečný hlas: slovní zásobu, rytmus, útočnost, humor, nejistotu a odbočky. Nestruď osobitý text do jednotného leštu.
- Proveď minimální účinný zásah. Silné věty nech být. Hrubý koncept s opravdovým hlasem musí i po úpravě znít jako týž člověk.
- Začni pointou, když úvod nic nepřidává. Osobní vsuvku nech, když nese charakter nebo kontext.
- Zachovej autorův význam. Nikdy nevymýšlej tvrzení, příklady, statistiky ani názory. Něco-li nejasné, zeptej se.
- Buď konkrétní. Jména, čísla, data, mechanismy a důsledky porážejí abstrakce.
- Uplatni test přenositelnosti: věta, kterou byste beze změny přesunuli do cizího článku, je výplň. Vyškrtni ji, nebo ji nahraď něčím specifickým pro toto téma.
- Piš v činném rodu. Lidé jednají; věci nedělají lidské činy.
- Nech slovesa dělat práci: „učinil rozhodnutí“ je „rozhodl“; „má schopnost“ je „umí“.
- Zachovej výhrady a dovětky. „Myslím“, „možná“ a „upřímně“ zůstávají, když vyjadřují skutečnou nejistotu nebo mluvený rytmus.
- Zachovej užitečnou ostrost: vyhraněné názory, humor a poctivá přiznání patří autorovi. Nenahrazuj je bezpečnějším zněním.

## Slova k vyštěknutí

Nafouknutá slovní zásoba: „prozkoumat hloubky“ (delve), „podpořit rozvoj“ (foster), „využít potenciál“ (leverage), „usnadnit cestu“, „posílit“ (empower), „zefektivnit“, „robustní“, „špičkové“, „revoluční“, „bezkompromisní“, „paradigma“, „game changer“, „mozaika možností“, „pokladnice znalostí“, „pohltit vás“, „zcela nová úroveň“, „vyrazit na cestu“ (embark), „nastartovat“, „neustále se vyvíjející“.

Prázdná příslovce, když nic nepřidávají: „prostě“, „doslova“, „vlastně“, „opravdu“, „právě“, „v zásadě“, „především“, „zásadně“, „nevyhnutelně“.

Prázdné obraty: „stojí za zmínku“, „je důležité si uvědomit“, „na konci dne“, „v dnešní době“, „v dnešním rychle se měnícím světě“, „skutečnost je taková“, „v neposlední řadě“, „nedá se popřít“, „faktem zůstává, že“, „pojďme se ponořit“.

Škrtni je, když zdržují nebo ředí pointu. Občasný obrat nech, když je součástí poznatelného hlasu autora a věta si místo stojí.

## Vzory k vyštěknutí

- **Binární kontrasty.** „Není to X, ale Y.“ Řekni přímo Y. Varianta „nejen… ale i“ patří sem.
- **Protahovací úvody.** „Věc je taková“, „buďme upřímní“, „nepříjemná pravda je“. Řekni pointu.
- **Předstírané postřehy.** „Co většina lidí přehlíží“, „to, co vám nikdo neřekne“. Nech tvrzení stát samotné.
- **Odhalení dvojtečkou.** Sousloví, dvojtečka, dramatický zbytek. Napiš obyčejnou větu; dvojtečku použij pro seznamy, popisky a citace.
- **Povrchní analýza.** Konstrukce „což poukazuje na“, „což podtrhuje“, „což ukazuje“ na konci věty. Řekni důsledek, nebo to škrtni.
- **Nafouknutá významnost.** „Stojí jako svědectví“, „znamená zlomový okamžik“. Uveď fakt a nech čtenáře posoudit.
- **Výkladové metakomentáře.** „Klíčové je“, „tohle je důležité“, zbytečné „jinými slovy“. Škrtni vsuvku, nebo ji nahraď podkladem.
- **Vykroutená atribuce.** „Odborníci se shodují“, „studie ukazují“. Pojmenuj zdroj, nebo tvrzení škrtni.
- **Předstíraně silná slovesa.** „Slouží jako centrální rozhraní pro“ je „spravuje koncepty na jednom místě“.
- **Střídání synonym.** Když je jasné slovo správné, opakuj ho. Agent, asistent a nástroj je jedna věc.
- **Dramatické útržky.** „X. A Y. A Z.“ Používej celé věty; záměrný útržek nech, když je to autorův rytmus.
- **Rétorické navedení.** „Co kdybych vám řekl“, „dějství se obrací“, samosplněné otázky a odpovědi. Řekni pointu.
- **Předstíraně hluboké pointy.** Závěrečný aforismus vymaž; skonči nejjasnější konkrétní větou, která už v textu je.
- **Shrňující konce.** „Závěrem“, „nakonec“, závěrečný odstavec opakující úvod. Skonči posledním konkrétním faktem nebo dalším krokem.
- **Formátovací výplň.** Emoji v nadpisech, tučně uprostřed věty, odrážky místo dvou vět prózy, nadpisy nad dvouřádkovými sekcemi.
- **Dlouhé pomlčky.** Nikdy nepoužívej U+2014 ani pomlčku jako spojku vět. Použij dvojtečku, čárku, závorku nebo novou větu. Krátká pomlčka U+2013 zůstává jen v rozsazích (22–23, 2020–2026). České uvozovky jsou „…“.

## Postup

1. Přečti celý koncept před úpravou. Urči hlavní pointu a rysy hlasu, které stojí za zachování. Není-li pointa jasná, zeptej se.
2. U detekčního zadání vrať jen zprávu s nálezy a skonči.
3. U úpravy proveď minimální účinné změny a spusť závěrečnou kontrolu.
4. Vrať celý upravený text a stručný seznam „Co se změnilo“ s důvodem u každé změny.

Při nejasných případech použij [příklady](references/examples.md).

## Závěrečná kontrola

- Každý pojmenovaný vzor byl zkontrolován; v upraveném textu nezůstal žádný.
- Autorův hlas, výhrady a skutková tvrzení přežily; nic nebylo vymyšleno.
- Žádná dlouhá pomlčka; rozsahy si drží krátkou pomlčku.
- Konec je konkrétní fakt nebo další krok, ne shrnutí ani aforismus.

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
