# Changelog

Copyright © 2026 Luděk Sušický

Versioning is per skill; the repository hosts more than one.

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
