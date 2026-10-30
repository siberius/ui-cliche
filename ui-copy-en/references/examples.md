# Examples and edge cases

Copyright © 2026 Luděk Sušický

These examples express this skill's style. They do not identify the authorship of the original copy.

| Context | Before | After | Reason |
|---|---|---|---|
| Heading | Account settings. | Account settings | No terminal period in a heading |
| Sentence heading | Select a file. | Select a file | A complete sentence still follows the heading rule |
| Button | Click here to save. | Save changes | Specific action |
| Label | Email: | Email | No trailing colon |
| Heading with slogan | Your projects — all in one place | Your projects | Remove filler instead of substituting a different dash |
| Short notification | Your changes have been successfully saved! | Changes saved | Only after confirmed success |
| Error with unknown cause | Oops! Something went wrong. | Could not upload the file | Only if the upload actually failed; do not invent a cause |
| Destructive dialog | Are you sure you want to continue? | Delete project? | Specific consequence |
| Empty list | Discover a world of possibilities for your projects | No projects yet | Only after successfully loading an empty list |

## Copy to keep

- “Delete this file?”: a genuine question needs its question mark.
- “Could not save the file. Try again.”: two explanatory sentences need punctuation; retry must be available and appropriate.
- “Uploading…”: the operation is actually running.
- “Ages 12–15”: a range is not a clause-connecting dash.
- `config.json`, `https://example.com`, `v1.2.3`, `--dry-run`: protected technical strings.
- “PDF, CSV and JSON”: a factual list of three formats is not a cliché.
- The heading “Working with PDF files”: it already works and needs no change.

## Strings inside code

```jsx
// Before
<h2>Account settings.</h2>
<button aria-label="Save changes.">Save changes.</button>
const message = `File ${filename} has been successfully saved!`;
const output = "config.json";

// After
<h2>Account settings</h2>
<button aria-label="Save changes">Save changes</button>
const message = `File ${filename} saved`;
const output = "config.json";
```

The save message belongs in the confirmed-success branch. Neither `${filename}` nor the value `config.json` changes. Also preserve ICU plurals and formatting tokens such as `%s` or `{count}`.

## Limits of safe shortening

Do not change “Project archived” into “Project deleted”, “Draft saved” into “Published”, or “May take up to 5 minutes” into “Ready in 5 minutes”. Keep information about irreversible deletion in the dialog body.

When reviewing unverified behaviour, make the proposed copy conditional and state what needs checking. Do not introduce a promise merely because it reads better.
