# UI Klišé (Copy and Prose without AI Clichés)

[Česky](README.cs.md)

Provider-independent Markdown skills for text without AI clichés in two product lines. **UI copy** (`ui-copy-cs`, `ui-copy-en`) covers headings, buttons, forms, dialogs, statuses, errors and accessible labels, including strings inside code. **Prose** (`prose-cs`, `prose-en`) edits articles, essays, posts and documentation prose into clear, human writing while preserving the author's voice, or detects the cliché patterns without rewriting.

| Line | Language | Skill | Examples |
|---|---|---|---|
| UI copy | Czech | [ui-copy-cs/SKILL.md](ui-copy-cs/SKILL.md) | [Czech examples](ui-copy-cs/references/examples.md) |
| UI copy | English | [ui-copy-en/SKILL.md](ui-copy-en/SKILL.md) | [English examples](ui-copy-en/references/examples.md) |
| Prose | Czech | [prose-cs/SKILL.md](prose-cs/SKILL.md) | [Czech examples](prose-cs/references/examples.md) |
| Prose | English | [prose-en/SKILL.md](prose-en/SKILL.md) | [English examples](prose-en/references/examples.md) |

Within a line, the language versions share scope, policy, workflow and safeguards. Grammar and examples are localized. Choose the language of the target text, which may differ from the language of your conversation with the assistant. Do not load a UI-copy skill and a prose skill for the same task; each has its scope.

## For all AI assistants

These skills are provider-independent text instructions. Use them with any AI assistant that accepts text context: attach the Markdown, paste its contents, or ask a coding agent with file access to read it. No API key, dependency, script, account or proprietary tool is required by the skill.

If your environment supports folder-based skills, provide the complete language folder, including its `references` directory, according to that environment's documentation. A filename or link alone does not guarantee automatic discovery. In a plain chat, attach the examples as well when needed; the assistant may not be able to follow local links.

This is a portability statement, not a claim that every model has been tested or will follow every instruction reliably. See [validation](docs/VALIDATION.md).

## Quick start

Attach the English `SKILL.md` and ask:

> Apply this skill to the interface copy in the settings dialog. Preserve application behaviour, technical strings and interpolation. Edit the affected UI text and report what you verified.

For a review without edits:

> Review the interface copy using this skill. Identify specific issues and suggest replacements. Do not change files.

For prose, attach the English prose `SKILL.md` and ask:

> Edit this article draft with this skill. Preserve my voice and factual claims. Return the edited draft and a short What changed list.

## What it changes

UI copy:

- No terminal periods in headings, buttons and short labels
- No decorative clause-connecting dashes or generic AI slogans
- Concrete action labels and consistent terminology
- Marketing contrasts and inflated filler vocabulary replaced by concrete wording
- Accurate error and success messages, with preserved consequences
- Normal punctuation in explanations and genuine questions
- Protected code identifiers, URLs, filenames, placeholders and pluralization

Prose:

- Named cliché patterns (binary contrasts, throat-clearing, colon reveals, importance puffery, weasel attribution and more) detected and cut
- The author's voice, qualifiers and factual claims preserved; nothing invented
- Minimum effective edit with a What changed report; detection without rewriting

The skills define an editorial style. They do not identify AI authorship or optimize for detector scores. Explicit user requirements and binding project rules take precedence.

## Documentation

- [Usage and maintenance](docs/USAGE.md)
- [Validation scenarios and status](docs/VALIDATION.md)
- [Sources and design decisions](docs/SOURCES.md)
- [Version history](CHANGELOG.md)

Version 1.1.0 (ui-copy) and 1.0.0 (prose) · 2026-11-09

## Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

## Lineage

The Czech `ui-copy-cs` variant replaces the general Psaní bez AI otisků skill as the source for the Czech attachment on Vibemaker; existing website addresses are retained. The web attachment includes the examples in one Markdown file.

The prose editions (`prose-cs`, `prose-en`) continue the article-oriented work of the original skill with an explicit scope. Their methodology is adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT); this repository's texts are independent. See [sources](docs/SOURCES.md).

## License / Licence

MIT · Copyright © 2026 Luděk Sušický. [LICENSE](LICENSE).
