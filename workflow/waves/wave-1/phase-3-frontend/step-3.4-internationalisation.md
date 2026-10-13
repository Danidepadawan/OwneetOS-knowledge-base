---
type: step
description: "JSON message files, loader, **English as the default language** and fallback, `en` + `it` complete, `docs/translating.md` for contributors."
phase: "[[phase-3-frontend]]"
step: "3.4"
status: done
legacy: "ROADMAP.md 3.4"
tags: [step, phase-3]
---
# 3.4 Internationalisation

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** JSON message files, loader, **English as the default language** and fallback,
  `en` + `it` complete,
  `docs/translating.md` for contributors.
- **Done when:** a new language works by adding one JSON file, with no code change.
- **Outcome:** `owneet::I18n` in the frontend (C++, unit test `test_I18n`): one JSON file per
  language (`frontend/i18n/`, installed in `/usr/share/owneet-frontend/i18n/`; a file in
  `~/.config/owneet-frontend/i18n/` overrides it), `{placeholders}`, plural forms with six rule
  families (one-other, french, none, east-slavic, polish, czech), numbers in the language's style.
  English on first boot and for missing messages; the choice is saved in the frontend's settings.
  The theme uses the `Tr` singleton; all its text is in `en.json` and `it.json` (46 messages,
  palette names included). Language picker as in demo 3.3 (Appearance → Language, A applies at
  once). `tools/i18n-check`, part of `tools/lint`, checks the files. Checked in the builder VM
  (switch to Italian, kept after a restart). Limits: no right-to-left; non-Latin scripts need
  extra fonts, added with the first such language.
