---
name: ui-copy-en
license: MIT
description: Write and review English interface copy while building websites and applications. Use for headings, buttons, forms, dialogs, messages and accessible labels, including strings inside code. Do not use as a general article editor.
---

# UI copy without AI clichés

Version 1.1.0 · 2026-11-09 · English variant

Copyright © 2026 Luděk Sušický

## Purpose and compatibility

Write concise English copy that helps users identify content, take the next step and understand the application's actual state. This skill is intended for all AI assistants capable of following text instructions. It requires no particular provider, model, editor, API or tool. Load it as a skill, attach the Markdown file or paste its contents into context. Automatic discovery depends on the environment. Portability does not mean testing on every model.

These rules define an editorial style. They do not identify authorship or promise to bypass AI detectors. Resolve conflicts in favour of explicit user requests and binding project rules. Preserve author-approved names and quotations.

## Scope

Apply when creating or editing UI copy: headings, navigation, buttons, forms, dialogs, validation, notifications, empty states, tooltips, placeholders and accessible labels. This includes user-facing strings in HTML, JSX, PHP, translation files and other code.

Do not change program identifiers, translation keys, APIs, commands, URLs, filenames, versions, regular expressions, logs, quotations or user data. Articles, academic prose and general documentation are outside scope. Do not rewrite their titles displayed in the UI without a request.

## Punctuation rules

- Page, section, card and dialog headings have no terminal period, even when they form complete sentences. Rephrase a two-sentence heading as one clear unit.
- Buttons, menu items, field labels, short statuses and brief tips have no terminal period. Field labels and headings also have no trailing colon.
- Explanatory paragraphs and multi-sentence errors use normal sentence punctuation. Classify text by its function, not its visual line wrapping.
- Genuine questions keep their question mark, including in headings. Preserve abbreviations, decimal numbers and other meaningful periods; never remove the last character indiscriminately.
- Do not use an em dash U+2014 or a dash to connect clauses or attach a slogan. Do not substitute a spaced hyphen, U+2013 or double hyphen. Shorten, split or restructure the wording; use a colon only when clarification needs it.
- Preserve ranges such as 1–5, lexical hyphens and mathematical signs. Technical strings are protected by the scope of this skill.
- Use an ellipsis for an operation actually in progress, truncated content or an established command convention requiring further input. It is not decoration for every button. Do not add exclamation marks or emojis for effect.

## Content and naming

- A heading names the content or task. A button names the specific action with a direct verb: “Save changes”, “Add file”, “Delete project”.
- Give the same action the same name throughout a flow. Distinguish “Save draft” from “Publish” according to actual behaviour.
- Do not add generic slogans, introductory welcomes, redundant subheadings or filler such as “all in one place”, “quick and easy” or “take your work to the next level”.
- Apply the portability test: if a string could appear unchanged in any other application, it is filler. Replace it with the concrete purpose of this feature, or remove it.
- Do not write marketing contrasts such as “not just a file browser, but a workspace”. Name the feature directly. A factual comparison of two real options is not affected.
- Replace inflated vocabulary with plain wording only when it stands in place of concrete information: utilize → use, leverage → use, “seamlessly”, “effortlessly”, “powerful”, “intuitive”, “cutting-edge”, “streamlined”. Do not alter quoted product names or established terms.
- Prefer “is” and direct verbs over inflated constructions. “Serves as a centralized hub for draft management” becomes “Manages drafts in one place”.
- Copy must supply needed information. Omit it when it adds nothing. Do not manufacture benefit triads or rhetorical contrasts. A factual list of three items is fine.
- An error explains what failed and how to continue when a next step is known. State a cause only when the application knows it. Do not invent network failures, permissions or technical limits.
- Confirm success only after actual success has been confirmed. Do not hide missing error handling with copy; report any mismatch in behaviour.
- Preserve the consequences of irreversible actions. Shortening must not erase the distinction between archiving and deletion, or drafts and publication.
- Use natural English and sentence case; preserve proper names. Follow the project's British or American spelling. If none is established, use American English consistently. Prefer common verbs such as “use” over “utilize”.
- Keep existing address and terminology. If none exists, use a neutral, direct tone. Use contractions where they fit the product voice without forced familiarity.
- An accessible name retains the visible control wording and may add context. Do not remove information needed by screen-reader users. A placeholder does not replace a persistent label.

## Programming workflow

1. Identify the language, existing terms and behaviour of the affected feature. Use only the variant for the target UI language; do not translate the entire interface without a request.
2. Edit the necessary strings in the affected area. Preserve variables, interpolation, escaping, plural forms and translation-format markup.
3. Distinguish headings, actions, short statuses and explanations. Apply the appropriate punctuation and compare meaning against the original copy.
4. Also review tooltips, `aria-label`, placeholders, validation and all reachable states of the changed feature. Check agreement between visible and accessible names.
5. Review the diff. Do not change technical strings or unrelated copy. After editing code, use an available, proportionate syntax check or test of the affected feature.

A request has one of two job types. For a review, report findings without changing files: one finding per row with the pattern, the quoted string and a suggested fix. Do not rewrite the text, score it or guess whether AI wrote it. For an edit, change the affected strings, then report a short “What changed” list: each change with its reason, plus the verification actually performed. Leave working copy alone.

## Final check

- Headings and short control text have no decorative ending punctuation; questions and meaningful characters remain.
- There are no clause-connecting dashes, substitute hyphens, empty slogans, marketing contrasts, inflated filler vocabulary or redundant subheadings.
- Actions, states and consequences match application behaviour; meaning and certainty have not changed.
- Terminology, tone and accessible names are consistent.
- Interpolation and technical values remain intact.

For ambiguous cases or a detailed review, consult the [examples](references/examples.md). Do not impose varied sentence lengths, minimum fact counts, a ban on triads or AI-detector scores.

## License

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.