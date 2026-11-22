# Changelog

Copyright © 2026 Luděk Sušický

Versioning is per skill; the repository hosts more than one.

## Release 2.0.0 (2026-11-22)

- **Architektonický a lingvistický přelom na nativní češtinu (Surface-Aware Microcopy & Slide Editing):**
  - Odpojení od univerzálního anglického klišé-jádra. Nové nativně české jádro zaměřené výhradně na App UI, konverzní web a prezentační slidy.
  - Tvrdé vymezení záběru: odmítnutí plného přepisu dlouhé prózy, článků, LinkedIn příspěvků a smluv (ochrana proti nesprávnému použití mikrotextových pravidel).
- **Dvoustupňový hybridní model (Linter + LLM adjudikátor):**
  - Vytvořen bezdependenční Python 3.9+ linter `scripts/ui_lint.py` s oddělením deterministických vad (`hard_lint`) a měkkých kandidátů k sémantickému posouzení (`soft_candidate`).
  - Zaveden princip „Zachovat jako výchozí stav“ s verdiktem `BEZ ÚPRAV`.
- **Třístupňová terminologická triáž (`references/cs-lexicon-triage.md`):**
  - Doménově vázané termíny (*prerekvizity* na VŠ zachovány, v SaaS nahrazeny), posunuté kalky (*hygienický standard* v medicíně zachován, na webu *samozřejmý základ*), neusazené kalky (*mrtvé adresy* -> *nefunkční odkazy / chyba 404*).
  - Absolutní lingvistická pojistka: přísný zákaz tvorby neologismů a pseudoodborných složenin.
- **Interpunkční profily výčtů podle ÚJČ AV ČR a ČSN 01 6910 (`references/cs-typography-lists.md`):**
  - Profily A (heslovitý v UI bez teček), B (syntakticky navázaný s dvojtečkou a čárkami/středníky), C (větný) a D (normalizace smíšených výčtů).
  - Typografická pravidla: zákaz teček za tlačítky a nadpisy, zákaz anglického Title Case v češtině, náhrada em-dash (—) za krátkou pomlčku (–) s mezerami.
- **Pravidla českého UX psaní (`references/surface-app.md`, `references/surface-web.md`, `references/surface-slides.md`):**
  - Tlačítka v dokonavém infinitivu, tooltipech v činném rodě, pokrytí 6 stavů rozhraní, jednotnost tykání/vykání, UX Commitment Guard pro CTA závazky.
- **Čtyřvrstvý evaluační rámec a benchmark (`evals/`):**
  - 24 trigger testů v `evals/trigger_evals.json` (100% přesnost aktivace).
  - 15 zlatých behaviorálních scénářů v `evals/evals.json` a testovací korpus v `evals/corpus/`.
  - Naměřené výsledky: 100 % záchyt vad (Koš A), 0,0 % planých nálezů na čistém textu (Koš B FPR), 100 % ochrana i18n ICU syntaxe (Koš C).
  - 19 deterministických jednotkových testů v `tests/test_ui_lint.py`.
- **Multi-agentní kompatibilita (AAIF):**
  - Řídicí manifest v `.agents/skills/ui-cliche/SKILL.md` (<250 řádků), podpora pro OpenAI Codex, Gemini CLI, Cursor, VS Code, symlink pro Claude Code a `prompts/chat-compact.md` pro webové chaty.

## Release 1.2.0 (2026-11-14)

- Add skills.sh ecosystem support: installation guides via Skills CLI, catalog badges and discovery sections.
- Configure repository topics (agent-skills, skills, claude-skills, copywriting, localization) for automated directory crawling.
- Align author block with canonical portfolio standard across README editions.

## Unreleased: documentation and version alignment (2026-11-11)

- Add the `cliche` skill to the `md-skills` bank README so the flagship text skill is discoverable next to `ui-copy-cs` and `ui-copy-en`.
- Relabel the historical 1.1.0 entry as `prose 1.1.0` and the 2026-10-30 entry as `ui-copy 1.0.0`, so the per-skill version history no longer shows cliche 1.1.0 before cliche 1.0.0.
- Align the Czech length claim with the benchmark recorded in docs/SOURCES.md
  ("models tend to write Czech texts about a third longer"), without dropping
  the number.
- Fix the dimension/layer inconsistency in the edit workflow and quality gate.
- Repair the Czech typography introduction and clarify the lexicon wording.
- Replace "burstiness" with a Czech description in the Czech syntax reference.
- Replace vague detector claims in both READMEs with a sourced statement.
- No rule, example or Czech layer was cut; the edits remove vague wording and
  keep the existing methodology.

## cliche 1.0.0 (2026-11-10)

- New flagship skill `cliche`: one lean English SKILL.md (identity, two jobs,
  core principles, five-dimension quality gate) with progressive disclosure
- Language layers in references, loaded only as needed: universal pattern
  catalog, Czech lexicon (calques, filler, marketing vocabulary), Czech
  syntax (functional sentence perspective, "svůj", passive voice, false
  agency, localization meaning-preservation), Czech typography (ČSN 01 6910)
  and Czech worked examples
- Detect mode reports named patterns, quoted lines, fixes and what is
  missing; Edit mode returns a What changed list
- Missing internal data becomes a visible placeholder, never an invention
- Supersedes the prose-cs and prose-en editions released with ui-copy 1.1.0
  (absorbed into the two-part architecture)
- Source analysis stored as docs/analyza-ceskeho-ai-slopu.md; methodology
  recorded in docs/SOURCES.md

## prose 1.1.0 (2026-11-09), superseded by cliche 1.0.0

- Formalized the two job types: review findings as one row per finding (pattern, quoted string, suggested fix) and a "What changed" list after edits
- Added the portability test for filler detection and a contextual ban on inflated marketing vocabulary
- Added marketing contrasts and inflated verb constructions to the cut patterns
- Extended both example tables and validation scenarios (V12, V13)
- Source: patterns adapted from petergyang/no-ai-slop (MIT); see docs/SOURCES.md

## ui-copy 1.0.0 (2026-10-30)

- Added equivalent Czech and English skills for UI copy during programming
- Defined punctuation by element type, with protected technical strings and interpolation
- Added localized examples, usage documentation, source attribution and validation scenarios
- Documented provider-independent use without claiming universal model testing
- Licensed both skills and accompanying documentation under MIT by author decision
