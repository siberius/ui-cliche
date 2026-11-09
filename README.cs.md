# UI klišé — texty rozhraní bez AI stop

[English](README.md)

Dva obsahově odpovídající Markdown skilly pro psaní textů rozhraní při tvorbě webů a aplikací. Řeší nadpisy, tlačítka, formuláře, dialogy, stavy, chyby a přístupné popisky, včetně řetězců uvnitř kódu.

| Jazyk rozhraní | Skill | Příklady |
|---|---|---|
| Čeština | [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | [České příklady](ui-copy-cs/references/examples.md) |
| Angličtina | [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | [Anglické příklady](ui-copy-en/references/examples.md) |

Varianty mají stejný rozsah, pravidla interpunkce, postup a ochranu významu. Gramatika a příklady odpovídají jazyku. Vybírej podle jazyka rozhraní, který se může lišit od jazyka rozhovoru s asistentem.

## Pro všechny AI asistenty

Skilly jsou textové instrukce nezávislé na poskytovateli. Použij je s kterýmkoli AI asistentem, který přijímá textový kontext: přilož Markdown, vlož obsah nebo požádej programujícího agenta s přístupem k souborům o načtení. Skill nevyžaduje API klíč, závislosti, skript, účet ani proprietární nástroj.

Pokud prostředí podporuje skilly ve složkách, poskytni celou jazykovou složku včetně `references` podle dokumentace daného prostředí. Název souboru nebo odkaz sám nezaručuje automatické načtení. V obyčejném chatu podle potřeby přilož i příklady; asistent nemusí umět otevřít místní odkazy.

Jde o přenositelnost, nikoli o tvrzení, že byly otestovány všechny modely nebo že každý dodrží všechny pokyny. Viz [ověření](docs/VALIDATION.md).

## Rychlé použití

Přilož český `SKILL.md` a zadej:

> Použij tento skill na texty dialogu nastavení. Zachovej chování aplikace, technické řetězce a interpolace. Uprav dotčené texty rozhraní a uveď, co jsi ověřil.

Pro kontrolu bez úprav:

> Zkontroluj texty rozhraní podle tohoto skillu. Vypiš konkrétní problémy a navrhni opravy. Soubory neměň.

## Co řeší

- Nadpisy, tlačítka a krátké popisky bez koncových teček
- Odstranění dekorativních spojovacích pomlček a generických sloganů
- Konkrétní názvy akcí a jednotnou terminologii
- Pravdivé chyby a oznámení úspěchu se zachováním následků
- Běžnou interpunkci ve vysvětlení a skutečných otázkách
- Ochranu identifikátorů, URL, názvů souborů, proměnných a pluralizace

Skill stanovuje redakční styl. Neurčuje autorství a neoptimalizuje skóre detektorů AI. Není editorem článků, nevyžaduje nepravidelné délky vět a nezakazuje věcné seznamy tří položek. Výslovné zadání uživatele a závazná pravidla projektu mají přednost.

## Dokumentace

- [Použití a údržba](docs/USAGE.md)
- [Kontrolní scénáře a stav ověření](docs/VALIDATION.md)
- [Zdroje a rozhodnutí](docs/SOURCES.md)
- [Historie verzí](CHANGELOG.md)

Verze 1.0.0 · 2026-10-30

## Autor

**Luděk Sušický** — biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — další vzdělávací projekty a otevřené aplikace

## Nahrazení původního skillu

Česká varianta nahrazuje obecný skill Psaní bez AI otisků. Je zdrojem české přílohy na webu Vibemaker; původní webové adresy zůstávají zachované. Webová příloha obsahuje příklady přímo v jednom Markdown souboru. Starý skill pro články se samostatně neudržuje.

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
