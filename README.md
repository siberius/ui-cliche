# UI Klišé (Text without AI Clichés)

[Česky](README.cs.md)
[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/ui-cliche)

> 📖 **Article and context on Vibemaker:** [Texty rozhraní bez AI klišé](https://vibemaker.cz/clanek/psani-bez-ai-otisku/)

Provider-independent Markdown skills for text without AI clichés. The flagship **cliche** skill edits or audits any human-facing text (articles, documentation, e-mail, marketing, web copy) with a lean English core and a Czech localization layer loaded only when needed. The specialized **ui-copy** skills (`ui-copy-cs`, `ui-copy-en`) cover interface strings inside code while programming, with protected technical tokens and accessibility rules.

| Skill | Scope | Detail loaded on demand |
|---|---|---|
| [cliche/SKILL.md](cliche/SKILL.md) | Any human-facing text, edit or detect | [Universal patterns](cliche/references/patterns.md) · [Czech lexicon](cliche/references/czech-lexicon.md) · [Czech syntax](cliche/references/czech-syntax.md) · [Czech typography](cliche/references/czech-typography.md) · [Czech examples](cliche/references/examples-cz.md) |
| [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | Czech interface strings in code | [Czech examples](ui-copy-cs/references/examples.md) |
| [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | English interface strings in code | [English examples](ui-copy-en/references/examples.md) |

The cliche skill uses progressive disclosure: its SKILL.md holds only the identity, the two jobs, the core principles and the quality gate. Pattern catalogs, the Czech lexicon, Czech syntax and typography live in `references/` and are read only for the language and task at hand; an English edit never loads the Czech layer.

## Installation and Quick Start

Install with the [Skills CLI](https://github.com/vercel-labs/skills) from [skills.sh](https://skills.sh). Use `-g` for user-level installation, or choose a specific agent with `-a` (`-a codex`, `-a claude-code`, etc.):

```bash
# Install all skills in this repository (cliche, ui-copy-cs, ui-copy-en)
npx skills add siberius/ui-cliche --full-depth -g -a codex

# Or install only the general human-facing text editing skill
npx skills add siberius/ui-cliche --skill cliche --full-depth -g -a codex

# Or install UI interface copy skills for code
npx skills add siberius/ui-cliche --skill ui-copy-cs --full-depth -g -a codex
npx skills add siberius/ui-cliche --skill ui-copy-en --full-depth -g -a codex

# List available skills in this repository
npx skills add siberius/ui-cliche --full-depth --list
```

Without `--agent`, `skills use` prints a prepared prompt. To launch a supported agent with a skill temporarily:

```bash
npx skills use siberius/ui-cliche --skill cliche --full-depth --agent codex
```

## For all AI assistants

These skills are provider-independent text instructions. Use them with any AI assistant that accepts text context: attach the Markdown, paste its contents, or ask a coding agent with file access to read it. No API key, dependency, script, account or proprietary tool is required by the skill.

If your environment supports folder-based skills, provide the complete language folder, including its `references` directory, according to that environment's documentation. A filename or link alone does not guarantee automatic discovery. In a plain chat, attach the examples as well when needed; the assistant may not be able to follow local links.

This is a portability statement, not a claim that every model has been tested or will follow every instruction reliably. See [validation](docs/VALIDATION.md).

## Quick start

Attach the English `SKILL.md` and ask:

> Apply this skill to the interface copy in the settings dialog. Preserve application behaviour, technical strings and interpolation. Edit the affected UI text and report what you verified.

For a review without edits:

> Review the interface copy using this skill. Identify specific issues and suggest replacements. Do not change files.

For prose and general text, attach the cliche `SKILL.md` and ask:

> Edit this article draft with this skill. Preserve my voice and factual claims. Return the edited draft and a short What changed list.

For a Czech text, the skill itself reads its Czech references (lexicon, syntax, typography) when needed.

## What it changes

cliche (any human-facing text):

- Named cliché patterns (throat-clearing, binary contrasts, colon reveals, rule of threes, weasel attribution and more) detected and cut
- The author's voice, qualifiers and factual claims preserved; missing data becomes a visible placeholder, never an invention
- For Czech: calques and marketing filler replaced, theme-to-rheme word order, "svůj" and active voice, ČSN 01 6910 typography
- Five-dimension quality gate (any dimension under 7/10 goes back) and a minimum-length discipline for new Czech text

ui-copy (interface strings in code):

- No terminal periods in headings, buttons and short labels
- No decorative clause-connecting dashes or generic AI slogans
- Concrete action labels, consistent terminology, preserved consequences
- Marketing contrasts and inflated filler vocabulary replaced by concrete wording
- Protected code identifiers, URLs, filenames, placeholders and pluralization

The skills define an editorial style. They do not identify AI authorship or optimize for detector scores. Explicit user requirements and binding project rules take precedence.

## What it is not

- Not an AI detector: the skills name patterns a reader can check; they do not score text or guess who wrote it. AI detectors are unreliable on Czech; see [sources](docs/SOURCES.md).
- Not a proof of human authorship: an edited text passes the style rules, nothing more.
- Not a general article or code editor: cliche does not rewrite opinions into house style, and ui-copy never touches technical strings, identifiers or interpolated values.
- No runtime: the skills are plain Markdown. No network calls, no accounts, no data collection, nothing installed by the skill itself.

## Documentation

- [Usage and maintenance](docs/USAGE.md)
- [Validation scenarios and status](docs/VALIDATION.md)
- [Sources and design decisions](docs/SOURCES.md)
- [Version history](CHANGELOG.md)

Version: cliche 1.0.0 · ui-copy 1.1.0 · 2026-11-10

### Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

## Lineage

The cliche skill continues the article-oriented work of the original Psaní bez AI otisků skill and supersedes the short-lived prose-cs/prose-en editions. Its methodology is informed by petergyang/no-ai-slop, Azayzel/stop-slop and the Czech AI-slop analysis stored in [docs/analyza-ceskeho-ai-slopu.md](docs/analyza-ceskeho-ai-slopu.md); see [sources](docs/SOURCES.md).

The ui-copy skills replace the general Psaní bez AI otisků skill as the source for the Czech attachment on Vibemaker; existing website addresses are retained.

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
