---
type: decision
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-08
legacy: "PROJECT_RULES.md §9 (i18n)"
tags: [decision, ux, i18n]
---
# Interface languages

- **i18n via JSON message files** with interchangeable labels; as many languages as possible.
  Wave 1 ships Italian + English; adding a language must require no code changes.
- **English is the default language** (first boot, and fallback for any missing label); Italian is
  one of the additional languages.
- The language is chosen from a list (a picker). The **keyboard layout** is chosen separately from
  the language (default "same as the language").

Practice: [[ui-text-and-i18n]]. Translator guide: `docs/translating.md` (code repository).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-08 | Demo 3.3 feedback: wordmark/logo provisional (final logo before the launch, roadmap 7.6); about twenty palettes (Tide in vivid "minty" cyan; new Ember, Espresso, Harbor and more) in a picker with live preview; language chosen from a list; the Guide prompt reads "Home" ([[design-direction]]). |
| 2026-10-08 | English is the default UI language and the fallback for missing labels; Italian is one of the additional languages ([[design-direction]]). |
