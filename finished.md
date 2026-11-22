# Záznam dokončených změn (finished.md)

## 2026-11-22 | v2.0.0

- Výsledek: Kompletní přestavba repozitáře `ui-cliche` na nativní češtinu pro aplikace, weby a prezentace (Surface-Aware Microcopy & Slide Editing) podle standardu Agent Skills (AAIF).
- Rozsah změn:
  - Odpojení od anglického základu, vytvořen nový řídicí manifest `.agents/skills/ui-cliche/SKILL.md` (<250 řádků).
  - Vytvořeny specializované moduly progresivního odkrývání v `references/`: `surface-app.md`, `surface-web.md`, `surface-slides.md`, `cs-lexicon-triage.md` a `cs-typography-lists.md`.
  - Vyvinut deterministický bezdependenční Python 3.9+ linter `scripts/ui_lint.py` s rozdělením na `hard_lint` a `soft_candidate`, maskováním i18n proměnných a podporou `keep-terms.yaml`.
  - Vytvořena deterministická testovací sada `tests/test_ui_lint.py` s 19 testy s povinnými protipříklady.
  - Založen 4vrstvý evaluační rámec: `evals/trigger_evals.json` (24 dotazů), `evals/evals.json` (15 scénářů) a testovací korpus `evals/corpus/`.
  - Vytvořen evaluační runner `scripts/run_evals.py` a naměřen benchmark v `evals/benchmark.json`.
  - Aktualizována dokumentace `README.md`, `README.cs.md`, `CHANGELOG.md` a doplněn povinný autorský blok.
- Ověření a metriky:
  - 19/19 unit testů linteru úspěšných.
  - Přesnost spuštění: 100 % (24/24 trigger dotazů).
  - Záchyt vad (Koš A): 100,0 %.
  - Plané nálezy na lidském textu (Koš B FPR): 0,0 % (cíl byl < 5 %).
  - Ochrana i18n ICU a HTML syntaxe (Koš C): 100,0 %.

## 2026-11-14 | v1.2.0

- Výsledek: Integrace balíčku ui-cliche do ekosystému skills.sh.
- Rozsah:
  - Repozitář hostuje 3 specializované skilly: cliche (vlajkový univerzální skill pro texty s českou lokalizační vrstvou), ui-copy-cs (české řetězce rozhraní v kódu) a ui-copy-en (anglické řetězce rozhraní v kódu).
  - Přidány odznaky skills.sh a sekce rychlé instalace do README.md, README.cs.md a docs/USAGE.md.
  - Sjednocen autorský blok podle kanonického standardu.
  - Nastaveny GitHub topics (agent-skills, skills, claude-skills, copywriting, localization) a domovská stránka pro automatickou indexaci katalogů.
- Ověření: Všechny 3 skilly i repozitář na skills.sh vracejí kód HTTP 200.
