---
type: best-practice
description: "No literal UI text: Tr singleton, en.json + it.json in the same change, key naming, placeholders, error codes."
scope: project
tags: [best-practice, i18n, ui]
---
# UI text and translations

Comes from: [[languages]], guard [[product-invariants]] (no hard-coded text).

- **No literal visible text in QML**: always the `Tr` singleton
  (`src/themes/owneet/foundation/Tr.qml`):

  ```qml
  Text { text: Tr.tr("games.empty") }
  Text { text: Tr.trn("games.count", games.count) }        // plural forms, {n}
  Text { text: Tr.tr("games.launching", { title: name }) } // {title} placeholder
  ```

- Add every new message to **`en.json` and `it.json` in the same change** (`frontend/i18n/`).
  English is the reference: every message exists there first.
- **Keys** are dotted, lower case, grouped by area: `prompt.back`, `games.count`,
  `appearance.palette`, `error.*` for owneetd's error codes. Keys are never translated.
- Keep `{placeholders}` exactly as in English; numbers are written in the language's own style.
- Button names in prompts ("A", "LB") and brand names (Xbox, PlayStation, Nintendo, Steam) are not
  translated.
- owneetd never sends UI text: its errors carry a stable `code` that the UI translates
  (`error.<code>`).
- `tools/i18n-check` (part of `tools/lint`) validates the files.
- Wording: [[writing-for-users]]. Translator guide: `docs/translating.md` (code repository).
