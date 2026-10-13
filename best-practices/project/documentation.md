---
type: best-practice
scope: project
tags: [best-practice, docs]
---
# Documentation: vault and repository

- **Knowledge** (rules, decisions, plans, designs) lives in this vault ([[kb-rules]]).
- **The code repository keeps what ships or what outside contributors need:** `README.md`,
  `CONTRIBUTING.md`, `CREDITS.md` (shipped in the image), `LICENSE`, one `README.md` per top-level
  folder (purpose, build and test commands, layout), `docs/translating.md` (translators),
  `frontend/sounds/SOURCES.md` (attribution), and later the user guide.
- Every top-level folder has a short README stating its purpose.
- Component READMEs describe the current state; history and reasons go to the vault (step notes,
  decision notes).
- Markdown style: [[markdown]].
