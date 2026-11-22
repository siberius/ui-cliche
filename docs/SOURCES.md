# Zdroje a rozhodnutí / Sources and decisions

Copyright © 2026 Luděk Sušický

## Česky

Vlastní formulace pravidel, algoritmů a evaluačních scénářů vznikly pro tento projekt. Externí zdroje, normy a akademické práce slouží jako odborný podklad a inspirace.

### 1. Jazykovědné normy a odborné autority
- **Ústav pro jazyk český AV ČR (ÚJČ AV ČR):**
  - [Psaní výčtů a seznamů](https://prirucka.ujc.cas.cz/?id=870): definice heslovitých, syntakticky navázaných a větných výčtů (Profily A–D v ui-cliche).
  - [Tečka v samostatných titolcích a nápisech](https://prirucka.ujc.cas.cz/?id=160): pravidlo pro vynechávání koncové tečky u nadpisů, tlačítek a jednořádkových popisků.
  - [Interpunkce a uvozovky](https://prirucka.ujc.cas.cz/?id=162): česká sazba uvozovek 99–66 („…“).
- **ČSN 01 6910 (Úprava dokumentů zpracovaných textovými procesory):**
  - Pravidla pro členění čísel mezerami (10 000), mezery před značkou procent (15 % podstatné jméno vs. 15% přídavné jméno) a sazbu české pomlčky (–) s mezerami.
- **Akademický úzus a doménová terminologie:**
  - Informační systém Univerzity Karlovy (SIS UK) a Masarykovy univerzity (IS MUNI): standardní definice pojmu *prerekvizity* ve studijních plánech.
  - Herzbergova dvoufaktorová teorie pracovní motivace: ustálený odborný český termín *hygienické faktory* (proti marketingovému kalku *hygienický standard*).

### 2. Standardy pro české UX psaní a lokalizaci
- **Mozilla L10n CS (Czech Style Guide):**
  - [General Style Guide · Czech (cs)](https://mozilla-l10n.github.io/styleguides/cs/general.html): pravidla pro tlačítka v dokonavém infinitivu (*Nainstalovat*, *Uložit*), činný rod v tooltipech a eliminaci rozkazovacího způsobu v UI.
- **Česká UX a obsahová praxe:**
  - Zásady srozumitelnosti CTA prvků, pravdivosti závazků (Commitment Guard), zákazu anglického *Title Case* v českých nadpisech a oddělení labelu, nápovědy a placeholderu.

### 3. Agentní standardy a inženýrství promptů
- **Agentic AI Foundation (AAIF):**
  - Otevřený standard formátu Agent Skills (`SKILL.md`), progressive disclosure princip a token economy.
- **Anthropic Skill-Creator & Best Practices:**
  - Metodika vývoje evaly řízených skillů (*Evals First*), oddělení triggerovacích evalů (přesnost aktivace) od behaviorálních evalů.
- **Zdeněk Dvořák – repozitář kalky:**
  - Standard bezdependenčního deterministického linteru a regresního testování (každé pravidlo povinně s pozitivním vzorem a protipříkladem).
- **David Fogl (Continero) – Korektor:**
  - Zásada, že nálezy linteru jsou návrhy a nikoli rozsudky; důraz na titulky slidů nesoucí zjištění.
- **kubicek.ai – Humanizátor:**
  - Oddělení jazykových referencí a vkládání zástupných značek `[doplnit: ...]` při chybějících datech.

---

## English

The rules, algorithms, and evaluation scenarios in `ui-cliche v2.0` were originally created for this project, informed by Czech academic linguistics, international UX style guides, and agent engineering standards.

### Key References:
- **Institute of the Czech Language of the Czech Academy of Sciences (ÚJČ AV ČR):** Bullet list punctuation guidelines, heading/button period omission rules, and typographic standards.
- **Czech National Standard ČSN 01 6910:** Punctuation, dashes, spacing for percentages, currencies, and multi-digit numbers.
- **Mozilla Czech Localization Style Guide:** Perfective infinitives on UI actions, active-voice tooltips, and anti-imperative conventions.
- **Agentic AI Foundation (AAIF):** Open Agent Skills specification (`SKILL.md`), progressive disclosure directory structure, and multi-client interoperability (Claude Code, OpenAI Codex, Gemini CLI, Cursor, VS Code).
- **Anthropic Skill Authoring Best Practices:** Evals-first development loop, trigger precision benchmarks, and multi-judge validation principles.
