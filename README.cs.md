# UI klišé — texty a próza bez AI stop

[English](README.md)

Markdown skilly nezávislé na poskytovateli, ve dvou produktových řadách. **Texty rozhraní** (`ui-copy-cs`, `ui-copy-en`) řeší nadpisy, tlačítka, formuláře, dialogy, stavy, chyby a přístupné popisky, včetně řetězců uvnitř kódu. **Próza** (`prose-cs`, `prose-en`) upravuje články, eseje, příspěvky a texty dokumentace do srozumitelné lidské prózy se zachováním autorova hlasu, nebo jen detekuje klišé vzory bez přepisu.

| Řada | Jazyk | Skill | Příklady |
|---|---|---|---|
| Texty rozhraní | Čeština | [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | [České příklady](ui-copy-cs/references/examples.md) |
| Texty rozhraní | Angličtina | [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | [Anglické příklady](ui-copy-en/references/examples.md) |
| Próza | Čeština | [prose-cs/SKILL.md](prose-cs/SKILL.md) | [České příklady](prose-cs/references/examples.md) |
| Próza | Angličtina | [prose-en/SKILL.md](prose-en/SKILL.md) | [Anglické příklady](prose-en/references/examples.md) |

V rámci řady mají jazykové varianty stejný rozsah, pravidla, postup a ochranu významu. Gramatika a příklady odpovídají jazyku. Vybírej podle jazyka cílového textu, který se může lišit od jazyka rozhovoru s asistentem. Nenačítej skill pro rozhraní a skill pro prózu k témuž úkolu; každý má svůj rozsah.

## Instalace a rychlé spuštění

Nainstaluj skilly přímo do svého AI asistenta (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline a dalších) přes CLI standard [skills.sh](https://skills.sh):

```bash
# Instalace všech 4 skillů do aktuálního projektu
npx skills add siberius/ui-cliche

# Globální instalace pro všechny projekty
npx skills add siberius/ui-cliche -g

# Instalace jen konkrétního skillu (např. české UI texty nebo česká próza)
npx skills add siberius/ui-cliche --skill ui-copy-cs
npx skills add siberius/ui-cliche --skill prose-cs
```

Jednorázové vyzkoušení bez trvalé instalace:

```bash
npx skills use siberius/ui-cliche@ui-copy-cs
```

## Pro všechny AI asistenty

Skilly jsou textové instrukce nezávislé na poskytovateli. Použij je s kterýmkoli AI asistentem, který přijímá textový kontext: přilož Markdown, vlož obsah nebo požádej programujícího agenta s přístupem k souborům o načtení. Skill nevyžaduje API klíč, závislosti, skript, účet ani proprietární nástroj.

Pokud prostředí podporuje skilly ve složkách, poskytni celou jazykovou složku včetně `references` podle dokumentace daného prostředí. Název souboru nebo odkaz sám nezaručuje automatické načtení. V obyčejném chatu podle potřeby přilož i příklady; asistent nemusí umět otevřít místní odkazy.

Jde o přenositelnost, nikoli o tvrzení, že byly otestovány všechny modely nebo že každý dodrží všechny pokyny. Viz [ověření](docs/VALIDATION.md).

## Rychlé použití

Přilož český `SKILL.md` a zadej:

> Použij tento skill na texty dialogu nastavení. Zachovej chování aplikace, technické řetězce a interpolace. Uprav dotčené texty rozhraní a uveď, co jsi ověřil.

Pro kontrolu bez úprav:

> Zkontroluj texty rozhraní podle tohoto skillu. Vypiš konkrétní problémy a navrhni opravy. Soubory neměň.

Pro prózu přilož český `prose-cs/SKILL.md` a zadej:

> Uprav tímto skillem tento koncept článku. Zachovej můj hlas a skutková tvrzení. Vrať upravený text a stručný seznam „Co se změnilo“.

## Co řeší

Texty rozhraní:

- Nadpisy, tlačítka a krátké popisky bez koncových teček
- Odstranění dekorativních spojovacích pomlček a generických sloganů
- Konkrétní názvy akcí a jednotnou terminologii
- Marketingové kontrasty a nafouknutou slovní zásobu nahrazené konkrétním pojmenováním
- Pravdivé chyby a oznámení úspěchu se zachováním následků
- Běžnou interpunkci ve vysvětlení a skutečných otázkách
- Ochranu identifikátorů, URL, názvů souborů, proměnných a pluralizace

Próza:

- Pojmenované klišé vzory (binární kontrasty, protahovací úvody, odhalení dvojtečkou, nafouknutá významnost, vykroutená atribuce a další) rozpoznávané a škrtané
- Zachovaný autorův hlas, výhrady a skutková tvrzení; nic se nevymýšlí
- Minimální účinný zásah se zprávou „Co se změnilo“; detekce bez přepisu

Skilly stanovují redakční styl. Neurčují autorství a neoptimalizují skóre detektorů AI. Výslovné zadání uživatele a závazná pravidla projektu mají přednost.

## Dokumentace

- [Použití a údržba](docs/USAGE.md)
- [Kontrolní scénáře a stav ověření](docs/VALIDATION.md)
- [Zdroje a rozhodnutí](docs/SOURCES.md)
- [Historie verzí](CHANGELOG.md)

Verze 1.1.0 (texty rozhraní) a 1.0.0 (próza) · 2026-11-09

## Autor

**Luděk Sušický** — biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — další vzdělávací projekty a otevřené aplikace

## Rodokmen

Česká varianta `ui-copy-cs` nahrazuje obecný skill Psaní bez AI otisků jako zdroj české přílohy na webu Vibemaker; původní webové adresy zůstávají zachované. Webová příloha obsahuje příklady přímo v jednom Markdown souboru.

Edice pro prózu (`prose-cs`, `prose-en`) navazují na článkovou práci původního skillu s výslovným rozsahem. Jejich metodika je adaptována z [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT); texty tohoto repozitáře jsou samostatné. Viz [zdroje](docs/SOURCES.md).

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
