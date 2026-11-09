---
name: prose-en
license: MIT
description: Edit English prose into clear, human writing without AI clichés while preserving the author's voice. Use for articles, essays, posts and documentation prose, or to detect the cliché patterns without rewriting. Not for interface copy; use ui-copy-en while programming.
---

# Prose without AI clichés

Version 1.0.0 · 2026-11-09 · English variant

Copyright © 2026 Luděk Sušický

Methodology adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT); this edition is an independent text. See the repository's docs/SOURCES.md.

## Purpose and compatibility

Turn a draft into clearer, more alive prose while keeping the writer's personal voice. The skill targets all AI assistants capable of following text instructions; no provider, model or tool is required. Load it as a skill, attach the Markdown file or paste its contents. Portability does not mean testing on every model.

These rules define an editorial style. They do not identify authorship, score text or promise to bypass AI detectors. Explicit user requests and binding project rules take precedence.

## Scope

Articles, essays, blog posts, newsletters and documentation prose. Interface copy while programming belongs to `ui-copy-en`. Do not alter quotations, cited text, code, technical identifiers, URLs or the author's factual claims and uncertainty markers.

## Two jobs

**Edit (default).** Fix the draft with the rules below and return the full edited text plus a short "What changed" list.

**Detect.** When asked whether a text reads as AI-generated, or to audit without rewriting: name each pattern that appears, quote the line and give the fix in a few words. Do not rewrite, score the text or guess who wrote it. Named patterns are evidence the reader can check; detectors guess.

## Editing principles

- Preserve the writer's real voice: vocabulary, cadence, bluntness, humor, uncertainty and digressions. Do not flatten distinctive writing into uniform polish.
- Make the minimum effective edit. Leave strong sentences alone. A rough draft with a real voice must still sound like the same person.
- Lead with the point when the setup adds nothing. Keep a personal aside or admission when it carries character or context.
- Keep the author's meaning. Never invent claims, examples, statistics or opinions. If something is unclear, ask.
- Be concrete. Names, numbers, dates, mechanisms and consequences beat abstractions.
- Apply the portability test: a sentence that could move unchanged into anyone else's essay is filler. Cut it or replace it with something specific to this subject.
- Use active voice. People do things; things do not do human verbs.
- Make verbs do the work: "made a decision" becomes "decided"; "has the ability to" becomes "can".
- Keep qualifiers and caveats. "I think", "maybe" and "to be honest" stay when they express real uncertainty or spoken rhythm.
- Keep useful edge: strong opinions, humor and honest admissions belong to the writer. Do not replace them with safer wording.

## Words to cut

Inflated vocabulary: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving.

Empty adverbs when they add nothing: just, literally, simply, actually, truly, fundamentally, importantly, crucially, inevitably.

Empty phrases: it is worth noting, it is important to note, at the end of the day, when it comes to, at its core, in today's world, the reality is, in terms of, in order to, going forward, let's dive in.

Cut them when they delay or dilute the point. Keep an occasional phrase when it is part of the writer's recognizable voice and the sentence still earns its place.

## Patterns to cut

- **Binary contrasts.** "Not X, but Y." State Y directly.
- **Throat-clearing openers.** "Here's the thing", "Let me be clear", "The uncomfortable truth is". State the point.
- **Faux-insight setups.** "What most people get wrong", "The part everyone misses". Make the claim stand alone.
- **Colon reveals.** A noun phrase, a colon, a dramatic fragment. Write a plain sentence; use colons for lists, labels and quotes.
- **Superficial analysis.** Trailing "-ing" clauses that pretend to explain: "highlighting", "underscoring", "showcasing". State the consequence or cut it.
- **Importance puffery.** "Stands as a testament", "marks a pivotal moment". State the fact and let the reader judge.
- **Interpretive metadiscourse.** "The key point is", "That last part matters", redundant "in other words". Delete the aside or replace it with support.
- **Weasel attribution.** "Experts agree", "studies show". Name the source or cut the claim.
- **Fake-strong verbs.** "Serves as a hub for" becomes "tracks drafts and approvals in one place".
- **Synonym cycling.** If the clear word is right, repeat it. The agent, the assistant and the tool are one thing.
- **Dramatic fragmentation.** "X. And Y. And Z." Use complete sentences; keep an intentional fragment when it is the writer's rhythm.
- **Rhetorical setups.** "What if I told you", "Plot twist", self-answered question pairs. Make the point.
- **Fake-profound kickers.** Delete the cute final aphorism; end on the clearest concrete sentence already in the draft.
- **Summary-recap endings.** "In conclusion", "Ultimately", a final paragraph restating the piece. End on the last concrete point or a next action.
- **Formatting slop.** Emoji in headings, bold sprinkled mid-sentence, bullet lists replacing two sentences of prose, headers over two-sentence sections.
- **Em dashes.** Never use U+2014 and never join clauses with a spaced dash. Use a colon, a comma, parentheses or a new sentence. The en dash stays only inside ranges (22–23, 2020–2026).

## Workflow

1. Read the full draft before editing. Identify the core point and the voice traits worth preserving. If the core point is unclear, ask.
2. For a detect request, return the findings report and stop.
3. For an edit, make the minimum effective changes and run the final check.
4. Return the full edited draft and a short "What changed" list with a reason per change.

For ambiguous cases, consult the [examples](references/examples.md).

## Final check

- Each named pattern was checked; none remains in the edited draft.
- The writer's voice, qualifiers and factual claims survived; nothing was invented.
- No em dashes; ranges keep their en dash.
- The ending is a concrete point or next action, not a recap or aphorism.

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
