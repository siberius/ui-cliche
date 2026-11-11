# Česká typografie (ČSN 01 6910)

Copyright © 2026 Luděk Sušický

Pomocný detektor neupraveného AI textu. Tabulka ukazuje chybnou a správnou
sazbu; platí pro český text, ne pro bloky kódu a ne pro citace cizího
originálu.

## Uvozovky

- Používej výhradně české kulaté uvozovky: spodní „devítkové" na začátku,
  horní „šestkové" na konci (`„text“`). Vnořené citace uvnitř citace: `‚text‘`.
- Rovné (`"`) i anglické (`“”`) uvozovky v českém textu jsou chyba. Rovné
  uvozovky zůstávají jen v programovém kódu.

## Pomlčky a spojovník

Vsuvka s ` – ` je podle ČSN legitimní česká sazba. V autorském textu ji
zachovej (maximálně 1–2× na text); škrtni ji tehdy, když je tikem: nahrazuje
čárky, objevuje se v kupách nebo nese umělé drama.

| Znak | Kdy | Příklad |
|---|---|---|
| `–` (půlčtverčíková) s mezerami | vsuvka ve větě, jen 1–2× na text | „Vše funguje – až na export." |
| `–` bez mezer | rozsah a vztah jednoslovných výrazů | `1914–1918`, `strana 23–26`, `Praha–Brno` |
| `–` s mezerami i u rozsahu | je-li některý člen víceslovný | `Karlovy Vary – Plzeň`, `M. Zikmund – J. Hanzelka` |
| `-` (spojovník) vždy bez mezer | uvnitř složených slov | `česko-anglický`, `e-shop`, `bude-li` |

- Dlouhá čtverčíková pomlčka `—` (em-dash) v českém textu nepatří; stejně tak
  spojovník s mezerami ` - ` místo pomlčky.
- Pomlčka nesmí stát na začátku řádku.

## Procenta, jednotky, čísla

- Mezera mezi číslem a značkou: `50 %`, `10 km`, `250 Kč`.
- Bez mezery jen jako přídavné jméno: `50% sleva` (padesátiprocentní),
  `3% úrok`.
- Desetinná čárka, nikdy tečka: `1,21 Kč`, `0,3 %`.
- Čísla nad čtyři číslice děl pevnou mezerou po trojicích: `100 000`,
  `141 113` (nikoli čárkou ani tečkou).
- U celých částek v korunách nepiš `,-`: `250 Kč`, ne `250,- Kč`.

## Datum, předložky, nadpisy

- Datum v souvislém textu: `15. 10. 2026` nebo `15. října 2026`
  (s mezerami za tečkami); `15.10.2026` jen ve strojovém dvoumístném zápisu.
- `viz` není zkratka: píše se bez tečky (`viz tabulka`, ne `viz. tabulka`).
- `§` s mezerou před číslem: `§ 64`.
- České nadpisy: velké písmeno jen na začátku prvního slova a u vlastních
  jmen; anglický Title Case neplatí. Za nadpisem není tečka.
- Za jednopísmenné předložky a spojky (*k, s, v, z, o, u, a, i*) a mezi
  číslo a jednotku patří ve finální sazbě (HTML/Markdown) nezlomitelná
  mezera (`&nbsp;`, `U+00A0`), aby nepřecházely na konec řádku.
