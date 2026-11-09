# UI Klišé (UI Copy without AI Clichés)

[Česky](README.cs.md)

Two equivalent Markdown skills for writing interface copy without AI clichés while building websites and applications. They cover headings, buttons, forms, dialogs, statuses, errors and accessible labels, including strings inside code.

| UI language | Skill | Examples |
|---|---|---|
| Czech | [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | [Czech examples](ui-copy-cs/references/examples.md) |
| English | [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | [English examples](ui-copy-en/references/examples.md) |

The versions share scope, punctuation policy, workflow and safeguards. Grammar and examples are localized. Choose the language of the interface, which may differ from the language of your conversation with the assistant.

## For all AI assistants

These skills are provider-independent text instructions. Use them with any AI assistant that accepts text context: attach the Markdown, paste its contents, or ask a coding agent with file access to read it. No API key, dependency, script, account or proprietary tool is required by the skill.

If your environment supports folder-based skills, provide the complete language folder, including its `references` directory, according to that environment's documentation. A filename or link alone does not guarantee automatic discovery. In a plain chat, attach the examples as well when needed; the assistant may not be able to follow local links.

This is a portability statement, not a claim that every model has been tested or will follow every instruction reliably. See [validation](docs/VALIDATION.md).

## Quick start

Attach the English `SKILL.md` and ask:

> Apply this skill to the interface copy in the settings dialog. Preserve application behaviour, technical strings and interpolation. Edit the affected UI text and report what you verified.

For a review without edits:

> Review the interface copy using this skill. Identify specific issues and suggest replacements. Do not change files.

## What it changes

- No terminal periods in headings, buttons and short labels
- No decorative clause-connecting dashes or generic AI slogans
- Concrete action labels and consistent terminology
- Accurate error and success messages, with preserved consequences
- Normal punctuation in explanations and genuine questions
- Protected code identifiers, URLs, filenames, placeholders and pluralization

The skill defines an editorial style. It does not identify AI authorship or optimize for detector scores. It is not an article editor and does not require irregular sentence lengths or ban factual lists of three items. Explicit user requirements and binding project rules take precedence.

## Documentation

- [Usage and maintenance](docs/USAGE.md)
- [Validation scenarios and status](docs/VALIDATION.md)
- [Sources and design decisions](docs/SOURCES.md)
- [Version history](CHANGELOG.md)

Version 1.0.0 · 2026-10-30

## Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

## Replacement of the original skill

The Czech variant replaces the general Psaní bez AI otisků skill. It is the source for the Czech attachment on Vibemaker; existing website addresses are retained. The web attachment includes the examples in one Markdown file. The old article-oriented skill is no longer maintained separately.

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
