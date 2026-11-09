# Použití a údržba / Usage and maintenance

Copyright © 2026 Luděk Sušický

## Česky

### Výběr varianty

Použij `cliche` pro obecné texty pro lidi (články, dokumentaci, e-maily, marketing, webové texty) v angličtině i češtině; české vrstvy si skill dotahuje z `cliche/references/` sám podle jazyka a úkolu. Pro řetězce rozhraní přímo v kódu při programování použij `ui-copy-cs` pro české UI a `ui-copy-en` pro anglické UI. Jazyk pokynů i příkladů odpovídá cílovému UI. U dvojjazyčné aplikace aplikuj varianty na příslušné řetězce; nenech jednu variantu přepsat druhý jazyk. Nenačítej víc skillů k jednomu úkolu, než úkol potřebuje.

### Připojení k práci

V chatu přilož `SKILL.md` nebo vlož celý jeho obsah. Agentovi s přístupem k souborům zadej skutečnou cestu a požádej ho o načtení. V prostředí s podporou skillů použij kompletní složku podle pravidel daného prostředí. Univerzální instalační cesta neexistuje; tento repozitář nemění konfiguraci žádného asistenta.

Samotný `SKILL.md` obsahuje všechna závazná pravidla. `references/examples.md` je doplňkový materiál pro nejasné případy, dostupný vedle skillu nebo jako další příloha. README a tato dokumentace nejsou nutnou součástí kontextu při každém použití.

### Kontrola a úprava

Rozlišuj požadavek na revizi od požadavku na změnu. Revize vypisuje problémy bez změny souborů; úprava mění pouze dotčené texty. Skill sám nepovoluje publikaci, deployment ani změnu licencí. Nevyžaduje síťové připojení.

Při úpravě zachovej funkční význam, technické tokeny, přístupnost a rozsah práce. Výrazy s tečkami či spojovníky nejsou automaticky chyby. Automatický linter může označit kandidáty, ale rozhodnutí potřebuje kontext prvku. Nepoužívej globální nahrazování v celém zdrojovém kódu.

### Aktualizace obou jazyků

Změnu společného pravidla proveď v obou `SKILL.md` a v odpovídajících příkladech. Jazykové rozdíly udržuj záměrně: české vykání a infinitiv, anglický přímý slovesný tvar a místní pravopis. Aktualizuj verzi, historii a ověř stejné hraniční případy v obou variantách. Zaznamenej konkrétní testovaný model jen při skutečném testování.

## English

### Choose a variant

Use `cliche` for general human-facing text (articles, documentation, e-mail, marketing, web copy) in English or Czech; the skill pulls its Czech layers from `cliche/references/` on demand according to language and task. For interface strings inside code while programming, use `ui-copy-cs` for Czech UI and `ui-copy-en` for English UI. Instructions and examples match the target language. In a bilingual application, apply each variant to its corresponding strings; do not let one overwrite the other language. Do not load more skills for one task than the task needs.

### Supply the skill

In chat, attach `SKILL.md` or paste its complete contents. Give a file-capable agent the actual path and ask it to read the file. In an environment with skill support, use the complete folder according to that environment's rules. There is no universal installation path; this repository changes no assistant configuration.

`SKILL.md` contains every binding rule. `references/examples.md` supplies optional context for ambiguous cases, alongside the skill or as another attachment. The README and this documentation need not be loaded for every task.

### Review and editing

Distinguish review requests from editing requests. A review reports problems without changing files; editing changes only the affected copy. The skill itself authorizes no publication, deployment or licensing changes. It requires no network connection.

Preserve functional meaning, technical tokens, accessibility and task scope. Periods and hyphens are not automatically mistakes. A linter can identify candidates, but deciding requires element context. Do not perform global replacements throughout source code.

### Maintain both languages

Change shared rules in both `SKILL.md` files and corresponding examples. Preserve intentional language differences: Czech polite address and infinitives, English direct action verbs and local spelling. Update the version and changelog, and review equivalent edge cases in both variants. Record a model as tested only after an actual test.

## Napojení na web / Website integration

Česky: Kanonický zdroj českého skillu je `ui-copy-cs/SKILL.md`. Ve webovém projektu vytvoří `testing/sync_ui_copy_skill.py` obě dosavadní stažitelné kopie pod názvem `psani-bez-ai-otisku.md`; připojí příklady do jednoho souboru a připojí licenci MIT. Poté se spouští `testing/build_articles.py` a `testing/build_seo.py`. Deployment je samostatný krok. Kompatibilní soubor ve vlastní bance md-skills se při změně zdroje obnovuje také; starý obsah se nevrací.

English: The canonical Czech source is `ui-copy-cs/SKILL.md`. In the website project, `testing/sync_ui_copy_skill.py` generates the two existing downloads named `psani-bez-ai-otisku.md`, embeds the examples in the same file and includes the MIT license. Next run `testing/build_articles.py` and `testing/build_seo.py`. Deployment is separate. Refresh the compatibility file in the local skill bank when changing the source too; do not restore the old content.
