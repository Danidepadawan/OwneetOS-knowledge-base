---
type: best-practice
description: "What lives in the vault and what stays in the code repository's READMEs."
scope: project
tags: [best-practice, docs]
---
# Documentation: vault and repository

- **Knowledge** (rules, decisions, plans, designs) lives in this vault ([[kb-rules]]).
- **The code repository keeps what ships or what outside contributors need:** `README.md`,
  `CONTRIBUTING.md`, `docs/setup.md` (requirements and workspace setup, including copies of the
  workspace's `CLAUDE.md` and `.claude/settings.json`: update it when those change), `CREDITS.md`
  (shipped in the image), `LICENSE`, one `README.md` per top-level
  folder (purpose, build and test commands, layout), `docs/translating.md` (translators),
  `frontend/sounds/SOURCES.md` (attribution), and later the user guide.
- Every top-level folder has a short README stating its purpose.
- **Files that ship to users never contain vault links** (`[[note]]`): `CREDITS.md` (installed as
  `/usr/share/doc/owneetos/CREDITS.md`), `frontend/sounds/SOURCES.md` and anything else a package
  installs. Users do not have the vault: write plain words ("Settings → System → Credits and
  licences") instead.
- Component READMEs describe the current state; history and reasons go to the vault (step notes,
  decision notes).
- Markdown style: [[markdown]].
