# UI Klišé v2.0: Native Czech Microcopy & Slide Editor
*(Surface-Aware Microcopy & Slide Editing for AI Agents)*

[English](README.md) · [Česky](README.cs.md)  
[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/ui-cliche)
[![Agent Skills AAIF](https://img.shields.io/badge/Agent%20Skills-AAIF%20Standard-success)](https://agentskills.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 📖 **Context on Vibemaker:** [Texty rozhraní bez AI klišé](https://vibemaker.cz/clanek/psani-bez-ai-otisku/)

`ui-cliche v2.0` is a specialized agent skill and hybrid linter for **native Czech interface copy in apps, websites, and presentation decks**. Unlike generic English-derived slop reducers, it replaces blanket word bans with surface-aware microcopy editing: checking Czech action infinitives, active-voice tooltips, truthfulness of CTA commitments, strict bullet punctuation per ÚJČ AV ČR and ČSN 01 6910, 3-tier triage of technical calques, and safe masking of i18n placeholders.

Built to comply with the **Agent Skills Open Standard (AAIF)**, supported natively by **Claude Code, OpenAI Codex, Gemini CLI, Cursor, and VS Code**.

---

## Benchmark Evaluation Results (v2.0)

Evaluated across a golden suite of 15 behavioral scenarios and 24 activation triggers (`evals/benchmark.json`):

| Metric & Evaluation Basket | Baseline (v1.x) | ui-cliche v2.0 | Target Goal | Status |
|---|---|---|---|---|
| **Flaw & AI Cliché Recall (Basket A)** | ~70 % | **100.0 %** | $\ge 90\,\%$ | ✅ Met |
| **False Positive Rate on Clean Text (Basket B)** | 25–35 % *(rewrote valid domain terms)* | **0.0 %** | $< 5\,\%$ | ✅ Elite specificity |
| **i18n ICU & HTML Preservation (Basket C)** | Fragile (risk of mangled syntax) | **100.0 %** | $100\,\%$ | ✅ Rock solid |
| **Trigger Precision (Trigger Evals)** | Untested | **100.0 %** *(24/24 queries)* | $\ge 90\,\%$ | ✅ Sharp boundaries |
| **Linter Average Latency** | — | **~50 ms** *(Python 3.9+)* | $< 200\text{ ms}$ | ✅ Instantaneous |

---

## Scope: What It Solves and What It Rejects

| Surface | In-Scope Elements | Core Quality Objective |
|---|---|---|
| **App UI** | Buttons, form fields, helper text, tooltips, empty states, error/success messages, i18n (`.json`, `.po`, `.tsx`). | Perfective infinitives (*Uložit*), active-voice tooltips, consistent addressing (tykání/vykání), coverage of 6 UI states, ban on cringe humor (*Upsík*) in payment flows. |
| **Web Surfaces** | Hero headlines, feature cards, pricing tables, CTA blocks, trust bars, FAQ. | Cutting unsubstantiated superlatives, eliminating English Title Case, commitment verification (*ihned*, *zdarma*). |
| **Presentation Slides** | Slide titles, bullet lists, callout boxes, KPI/chart labels. | Finding-driven slide titles, syntactic list parallelism, strictly unified Czech bullet punctuation. |
| **OUT OF SCOPE** | **Long articles, blog posts, LinkedIn personal stories, contracts, emails over 300 words.** | **Hard refusal of full rewrites.** Alerts the user to the microcopy scope and offers selective inspection of headlines and CTA buttons only. |

---

## 6 Key Architectural Innovations

1. **Two-Stage Hybrid Engine (Linter + LLM Adjudicator):** A zero-dependency Python script (`scripts/ui_lint.py`) identifies mechanical defects (`hard_lint`) and flags candidate terms (`soft_candidate`). The LLM adjudicates domain context. When clean, it returns the explicit verdict `BEZ ÚPRAV` (No changes needed).
2. **Three-Tier Terminology Triage:**
   - *Domain-bound terms:* Terms like *prerekvizity* are kept in university systems; in SaaS apps they are replaced by natural phrases (*co potřebujete předem*).
   - *Shifted calques:* E.g. *hygienický standard* is kept in sanitation; in product marketing it becomes *samozřejmý základ*.
   - *Unsettled calques:* E.g. *mrtvé adresy* is always replaced by *nefunkční odkazy / neexistující stránky (chyba 404)*.
   - *Strict ban on neologisms:* Unknown terms are expanded into a plain verb + noun structure.
3. **Four List Punctuation Profiles (ÚJČ AV ČR / ČSN 01 6910):**
   - *Profile A (Itemized):* No colon, capitalized UI entries, **no terminal periods or commas** (default for UI and slides).
   - *Profile B (Syntactically linked):* Introductory colon, lowercase items, commas/semicolons, terminal period on the last item.
   - *Profile C (Sentential):* Complete sentences, initial capital, terminal periods on every item.
   - *Profile D (Normalization):* Automatic syntax unification.
4. **UX Commitment & Factuality Guard:** Prevents unfounded promises like *ihned zdarma* when card info is required. Inserts the tag `[ověřit obchodní podmínku]`.
5. **Protected Project Dictionary (`keep-terms.yaml`):** Teams specify proprietary and domain terminology that the linter and LLM are forbidden from altering.
6. **Progressive Disclosure (Token Economy):** Loading only the active surface reference (`surface-app.md`, `surface-web.md`, or `surface-slides.md`) saves context window tokens.

---

## Installation and Quick Start

### 1. Via Skills CLI (skills.sh)
```bash
# Install to any supported agent (e.g. codex, claude-code, gemini-cli)
npx skills add siberius/ui-cliche --full-depth -g -a codex
```

### 2. Standard Agent Paths (AAIF / Claude Code / Cursor)
- **Codex, Gemini CLI, Cursor, VS Code:** The skill manifest resides at `.agents/skills/ui-cliche/SKILL.md`.
- **Claude Code:** Automatically reads the prepared symlink at `.claude/skills/ui-cliche/SKILL.md`.

### 3. Running the Standalone Linter
```bash
# Lint an application i18n file
python3 scripts/ui_lint.py --surface app src/locales/cs.json

# Lint a landing page with JSON output
python3 scripts/ui_lint.py --surface web index.html --json

# Lint with project-specific protected terms
python3 scripts/ui_lint.py --surface app strings.json --keep-terms keep-terms.yaml
```

---

## Repository Structure

```
ui-cliche/
├── .agents/skills/ui-cliche/
│   └── SKILL.md                          # Primary AAIF manifest (<250 lines)
├── references/
│   ├── surface-app.md                    # App UI rules, 6 states, action verbs
│   ├── surface-web.md                    # Conversion copy, CTA, proof rules
│   ├── surface-slides.md                 # Slide titles, bullet list density
│   ├── cs-lexicon-triage.md              # 3-tier triage of technical calques
│   └── cs-typography-lists.md            # ÚJČ / ČSN 01 6910 list profiles A–D
├── scripts/
│   ├── ui_lint.py                        # Zero-dependency Python 3.9+ linter
│   └── run_evals.py                      # Evaluation and benchmark runner
├── assets/
│   └── keep-terms.example.yaml           # Protected terms template
├── evals/
│   ├── trigger_evals.json                # 24 trigger queries (in-scope / out-of-scope)
│   ├── evals.json                        # 15 golden behavioral scenarios
│   ├── benchmark.json                    # Benchmark test results and metrics
│   └── corpus/                           # Test fixtures for Baskets A, B, and C
├── tests/
│   └── test_ui_lint.py                   # 19 unit tests with counter-examples
└── prompts/
    └── chat-compact.md                   # Compact prompt for web-based chats
```

---

### Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

---

## License

MIT License · Copyright © 2026 Luděk Sušický. See [LICENSE](LICENSE).
