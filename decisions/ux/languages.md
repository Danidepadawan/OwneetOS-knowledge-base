---
type: decision
description: "JSON message files, English default and fallback; Wave 1 in English, Italian, German, French and Spanish; keyboard layout chosen separately."
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-29
legacy: "PROJECT_RULES.md §9 (i18n)"
tags: [decision, ux, i18n]
---
# Interface languages

- **i18n via JSON message files** with interchangeable labels; as many languages as possible.
  Wave 1 ships **English, Italian, German, French and Spanish** (owner, 2026-10-26; the three new
  ones checked by people the authors know, [[step-7.9-console-more-languages]], after
  Danidepadawan's merge); adding a language must require no code changes.
- **English is the default language** (first boot, and fallback for any missing label); Italian is
  one of the additional languages.
- The language is chosen from a list (a picker). The **keyboard layout** is chosen separately from
  the language (default "same as the language").
- **The picker lists the five languages of Wave 1 from the start** (owner, 2026-10-29), before
  German, French and Spanish are complete or checked: missing messages show in English. The
  reviews may come after the first release; they are also a way to ask the community to help
  improve OwneetOS. Every screen added from step 6.1 on comes in the five languages.

Practice: [[ui-text-and-i18n]]. Translator guide: `docs/translating.md` (code repository).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-08 | Demo 3.3 feedback: wordmark/logo provisional (final logo before the launch, roadmap 7.6); about twenty palettes (Tide in vivid "minty" cyan; new Ember, Espresso, Harbor and more) in a picker with live preview; language chosen from a list; the Guide prompt reads "Home" ([[design-direction]]). |
| 2026-10-08 | English is the default UI language and the fallback for missing labels; Italian is one of the additional languages ([[design-direction]]). |
| 2026-10-26 | Wave 1 adds German, French and Spanish to English and Italian (step 7.9, after Danidepadawan's merge; checked by people the authors know). |
| 2026-10-29 | The language picker lists the five languages of Wave 1 from the start, before German, French and Spanish are complete or checked (missing messages in English; the reviews may come later and invite the community to help); new screens come in the five languages. |
| 2026-10-29 | German, French and Spanish translated for the whole console now, with step 6.1 (step 7.9 moved earlier); the picker alphabetical after English. |
