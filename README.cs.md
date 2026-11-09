# UI klišé — texty bez AI stop

[English](README.md)

Markdown skilly nezávislé na poskytovateli pro texty bez AI klišé. Vlajkový skill **cliche** upravuje nebo audituje jakýkoliv text pro lidi (články, dokumentaci, e-maily, marketing, webové texty): anglické jádro je úsporné a česká lokalizační vrstva se dotahuje jen podle potřeby. Specializované skilly **ui-copy** (`ui-copy-cs`, `ui-copy-en`) řeší řetězce rozhraní přímo v kódu při programování, s ochranou technických tokenů a pravidly přístupnosti.

| Skill | Rozsah | Detail dotahovaný dle potřeby |
|---|---|---|
| [cliche/SKILL.md](cliche/SKILL.md) | Jakýkoliv text pro lidi, úprava i detekce | [Univerzální vzory](cliche/references/patterns.md) · [Český lexikon](cliche/references/czech-lexicon.md) · [Česká syntax](cliche/references/czech-syntax.md) · [Česká typografie](cliche/references/czech-typography.md) · [České příklady](cliche/references/examples-cz.md) |
| [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | České řetězce rozhraní v kódu | [České příklady](ui-copy-cs/references/examples.md) |
| [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | Anglické řetězce rozhraní v kódu | [Anglické příklady](ui-copy-en/references/examples.md) |

Skill cliche používá progresivní odkrývání: SKILL.md nese jen identitu, dva typy zadání, základní principy a kvalitativní bránu. Katalogy vzorů, český lexikon, českou syntax a typografii najdeš v `references/` a čti jen pro daný jazyk a úkol; úprava anglického textu českou vrstvu nenačítá.

## Pro všechny AI asistenty

Skilly jsou textové instrukce nezávislé na poskytovateli. Použij je s kterýmkoli AI asistentem, který přijímá textový kontext: přilož Markdown, vlož obsah nebo požádej programujícího agenta s přístupem k souborům o načtení. Skill nevyžaduje API klíč, závislosti, skript, účet ani proprietární nástroj.

Pokud prostředí podporuje skilly ve složkách, poskytni celou jazykovou složku včetně `references` podle dokumentace daného prostředí. Název souboru nebo odkaz sám nezaručuje automatické načtení. V obyčejném chatu podle potřeby přilož i příklady; asistent nemusí umět otevřít místní odkazy.

Jde o přenositelnost, nikoli o tvrzení, že byly otestovány všechny modely nebo že každý dodrží všechny pokyny. Viz [ověření](docs/VALIDATION.md).

## Rychlé použití

Přilož český `SKILL.md` a zadej:

> Použij tento skill na texty dialogu nastavení. Zachovej chování aplikace, technické řetězce a interpolace. Uprav dotčené texty rozhraní a uveď, co jsi ověřil.

Pro kontrolu bez úprav:

> Zkontroluj texty rozhraní podle tohoto skillu. Vypiš konkrétní problémy a navrhni opravy. Soubory neměň.

Pro obecné texty přilož `cliche/SKILL.md` a zadej:

> Uprav tímto skillem tento koncept článku. Zachovej můj hlas a skutková tvrzení. Vrať upravený text a stručný seznam „Co se změnilo“.

U českého textu si skill sám dotáhne české reference (lexikon, syntax, typografii), jakmile je potřebuje.

## Co řeší

cliche (jakýkoliv text pro lidi):

- Pojmenované klišé vzory (odkašlávání, binární kontrasty, odhalení dvojtečkou, pravidlo tří, vykroutená atribuce a další) rozpoznávané a škrtané
- Zachovaný autorův hlas, výhrady a skutková tvrzení; chybějící data jako viditelný zástupný symbol, nikdy vymyšlená hodnota
- Pro češtinu: kalky a marketingová vata nahrazené, aktuální členění větné (téma → réma), „svůj“ a činný rod, typografie ČSN 01 6910
- Kvalitativní brána pěti dimenzí (dimenze pod 7/10 jde zpět) a disciplína stručnosti u nových českých textů

ui-copy (řetězce rozhraní v kódu):

- Nadpisy, tlačítka a krátké popisky bez koncových teček
- Odstranění dekorativních spojovacích pomlček a generických sloganů
- Konkrétní názvy akcí a jednotnou terminologii
- Marketingové kontrasty a nafouknutou slovní zásobu nahrazené konkrétním pojmenováním
- Ochranu identifikátorů, URL, názvů souborů, proměnných a pluralizace

Skilly stanovují redakční styl. Neurčují autorství a neoptimalizují skóre detektorů AI. Výslovné zadání uživatele a závazná pravidla projektu mají přednost.

## Dokumentace

- [Použití a údržba](docs/USAGE.md)
- [Kontrolní scénáře a stav ověření](docs/VALIDATION.md)
- [Zdroje a rozhodnutí](docs/SOURCES.md)
- [Historie verzí](CHANGELOG.md)

Verze 2.0.0 (cliche) a 1.1.0 (ui-copy) · 2026-11-10

## Autor

**Luděk Sušický** — biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — další vzdělávací projekty a otevřené aplikace

## Rodokmen

Skill cliche navazuje na článkovou práci původního skillu Psaní bez AI otisků a nahrazuje krátce existující edice prose-cs/prose-en. Jeho metodika vychází z petergyang/no-ai-slop, Azayzel/stop-slop a analýzy českého AI slopu uložené v [docs/analyza-ceskeho-ai-slopu.md](docs/analyza-ceskeho-ai-slopu.md); viz [zdroje](docs/SOURCES.md).

Skilly ui-copy nahrazují obecný skill Psaní bez AI otisků jako zdroj české přílohy na webu Vibemaker; původní webové adresy zůstávají zachované.

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
