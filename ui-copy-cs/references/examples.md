# Příklady a hraniční případy

Copyright © 2026 Luděk Sušický

Příklady vyjadřují styl tohoto skillu. Nevypovídají o autorství původního textu.

| Kontext | Před | Po | Důvod |
|---|---|---|---|
| Nadpis | Nastavení účtu. | Nastavení účtu | Nadpis bez koncové tečky |
| Větný nadpis | Vyberte soubor. | Vyberte soubor | Větná podoba na pravidle nic nemění |
| Tlačítko | Klikněte zde pro uložení. | Uložit změny | Konkrétní akce |
| Popisek | E-mail: | E-mail | Bez koncové dvojtečky; spojovník uvnitř slova zůstává |
| Nadpis se sloganem | Vaše projekty — vše na jednom místě | Vaše projekty | Výplň se odstraní, pomlčka se nenahradí jiným znakem |
| Krátké oznámení | Vaše změny byly úspěšně uloženy! | Změny uloženy | Pouze po potvrzeném uložení |
| Chyba bez známé příčiny | Jejda! Něco se pokazilo. | Soubor se nepodařilo nahrát | Jen pokud skutečně selhalo nahrání; příčina se nevymýšlí |
| Destruktivní dialog | Opravdu pokračovat? | Smazat projekt? | Konkrétní následek |
| Prázdný seznam | Objevte svět možností svých projektů | Zatím nemáte žádné projekty | Pouze po úspěšném načtení prázdného seznamu |
| Nadpis funkce | Není jen prohlížeč souborů — vaše kreativní pracovní plocha | Soubory | Marketingový kontrast i výplň pryč; nadpis pojmenovává obsah |
| Tlačítko | Snadno a bez námahy synchronizujte data | Synchronizovat | Nafouknutá výplň nahrazena samotnou akcí |
| Popis funkce | Slouží jako centrální rozhraní pro správu konceptů | Spravuje koncepty na jednom místě | Přímé sloveso místo nafouknuté konstrukce |

## Texty, které ponechat

- „Smazat tento soubor?“: otázka potřebuje otazník.
- „Soubor se nepodařilo uložit. Zkuste to znovu.“: dvě vysvětlující věty potřebují interpunkci; opakování musí být dostupný a smysluplný krok.
- „Nahrávání…“: operace opravdu probíhá.
- „Věk 12–15 let“: rozsah není spojovací pomlčka.
- `config.json`, `https://example.com`, `v1.2.3`, `--dry-run`: chráněné technické řetězce.
- „PDF, CSV a JSON“: věcná trojice formátů není klišé.
- Nadpis „Práce se soubory PDF“: už funguje, není důvod ho měnit.

## Řetězce v kódu

```jsx
// Před
<h2>Nastavení účtu.</h2>
<button aria-label="Uložit změny.">Uložit změny.</button>
const message = `Soubor ${filename} byl úspěšně uložen!`;
const output = "config.json";

// Po
<h2>Nastavení účtu</h2>
<button aria-label="Uložit změny">Uložit změny</button>
const message = `Soubor ${filename} uložen`;
const output = "config.json";
```

Zpráva o uložení patří do větve potvrzeného úspěchu. Interpolace `${filename}` ani hodnota `config.json` se nemění. Stejně zachovej ICU pluralizaci a formátovací tokeny jako `%s` nebo `{count}`.

## Hranice bezpečného zkrácení

„Projekt byl archivován“ nepřepisuj na „Projekt smazán“. „Koncept uložen“ nepřepisuj na „Publikováno“. „Může trvat až 5 minut“ nepřepisuj na „Hotovo za 5 minut“. Informaci o nemožnosti vrátit smazání zachovej v textu dialogu.

Při revizi neověřeného chování navrhni text podmíněně a uveď, co je potřeba zjistit. Nedoplňuj do aplikace slib jen proto, že zní lépe.
