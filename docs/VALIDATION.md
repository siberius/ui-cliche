# Ověření / Validation

Copyright © 2026 Luděk Sušický

## Stav / Status

Verze / Version: cliche 1.0.0 · ui-copy 1.1.0, 2026-11-10

Česky: Přenositelnost na různé AI není dokladem testování na všech modelech. Ověření formátu skillu a redakční kontrola nejsou behaviorálním testem modelu. Záznam skutečně provedených kontrol je uveden níže. Testování konkrétních AI zatím čeká na upřesnění autora.

English: Portability across AI assistants is not evidence of testing every model. Skill-format validation and editorial review are not model behaviour tests. Checks actually performed are recorded below. Testing on specific AI models awaits clarification from the author.

## Kontrolní scénáře / Review scenarios

| ID | Vstup / Input | Očekávaný výsledek / Expected outcome |
|---|---|---|
| V01 | Nadpis / heading: Nastavení účtu. / Account settings. | Odstranit jen koncovou tečku / Remove only the terminal period |
| V02 | Otázka / question: Smazat projekt? / Delete project? | Zachovat otazník / Keep the question mark |
| V03 | Dvě vysvětlující věty / Two explanatory sentences | Zachovat větnou interpunkci / Preserve sentence punctuation |
| V04 | `config.json`, `v1.2.3`, `--dry-run`, `https://example.com` | Hodnoty neměnit / Leave values intact |
| V05 | `${filename}`, `%s`, `{count}` a/and ICU plural | Zachovat interpolaci a strukturu / Preserve interpolation and structure |
| V06 | Nadpis se sloganem a pomlčkou / Heading with a slogan and a dash | Odstranit výplň bez náhradní pomlčky / Remove filler without a substitute dash |
| V07 | Archivováno / Archived | Nezměnit na smazáno / Do not change to deleted |
| V08 | Nahrání selhalo, příčina neznámá / Upload failed, cause unknown | Nevymýšlet příčinu / Do not invent a cause |
| V09 | Viditelné tlačítko a jeho přístupný název / Visible button and accessible name | Zachovat shodné pojmenování / Keep names aligned |
| V10 | Autor výslovně zadá přesný název / Author explicitly supplies an exact title | Název svévolně neměnit / Do not silently alter the title |
| V11 | Požadavek jen na revizi / Review-only request | Nesmí měnit soubory / Must not edit files |
| V12 | Marketingový kontrast v nadpisu / Marketing contrast in a heading | Nahradit přímým pojmenováním / Replace with a direct name |
| V13 | Nafouknutá slovní zásoba v tlačítku / Inflated vocabulary in a button | Nahradit prostou akcí jen při ztrátě informace / Replace with a plain action only when information is lost |

## Scénáře skillu cliche / cliche skill scenarios

| ID | Vstup / Input | Očekávaný výsledek / Expected outcome |
|---|---|---|
| C01 | „Nový modul pro export faktur byl spuštěn včera." | Přestavět na české členění: „Včera jsme spustili…" / Reorder to Czech FSP |
| C02 | „Přihlaste se do vašeho účtu." | Vypustit zájmeno, při shodě s podmětem „svůj" / Drop the pronoun or use "svůj" |
| C03 | „Nový kurz byl schválen vládou." | Činný rod s původcem / Active voice with the actor |
| C04 | „…, což podtrhuje závazek týmu." | Ukončit větu nebo uvést důsledek „takže…" / End the sentence or state the consequence |
| C05 | `—` v českém textu, `50%` u čísla, `viz.` s tečkou | Nahradit `–`, `50 %`, `viz` bez tečky / Fix typography per ČSN |
| C06 | Chybějící statistika v novém textu | Zástupný symbol `[DOPLŇTE: …]`, nikdy vymyšlená hodnota / Visible placeholder, never an invention |
| C07 | Detekční zadání / Detect request | Nálezy se vzorem a citací bez změny textu / Findings with pattern and quote, no rewrite |
| C08 | Nový český text bez zadání délky / New Czech text without a length instruction | Text bez třetinové vaty, přirozená lidská délka / No third of filler, natural human length |
| V12 | Existující věcná trojice formátů / Existing factual list of three formats | Zachovat všechny formáty / Keep all formats |
| V13 | Prázdný seznam po selhání načítání / Empty list after a loading failure | Netvrdit, že žádné položky neexistují / Do not claim there are no items |

Česky: Pro skutečný behaviorální test zadej scénáře samostatnému běhu vybraného modelu bez očekávaných výsledků. Zaznamenej přesné označení modelu, datum, použitou verzi skillu, zadání, pozorované výsledky a omezení. Neoznačuj celou rodinu modelů za ověřenou podle jednoho běhu.

English: For an actual behavioural test, give the scenarios to a separate run of the selected model without the expected outcomes. Record the exact model name, date, skill version, request, observed results and limitations. Do not mark an entire model family as tested based on one run.

## Provedené kontroly / Checks performed

2026-10-30: Obě varianty prošly validátorem formátu skillu. Ověřeny všechny místní Markdown odkazy, oznámení copyrightu, shodné členění a počet pravidel. Redakčně porovnán význam obou variant a příklady V01–V13. To není nezávislý behaviorální test AI.

2026-10-30: Both variants passed skill-format validation. All local Markdown links, copyright notices, matching structure and rule counts were checked. Both variants and scenarios V01–V13 were editorially reviewed for equivalent meaning. This is not an independent AI behaviour test.
