---
type: best-practice
description: "Conventional Commits, branch names, scopes, one change per commit."
scope: project
tags: [best-practice, git]
---
# Commits and branches

Comes from: [[repository]] (Conventional Commits confirmed by the owner, 2026-10-04).

- `main` must always build. Work happens on short-lived branches named
  `<area>/<short-description>`, e.g. `daemon/bluetooth-autopair`, `iso/plymouth-theme`.
- Since 2026-10-14 each developer works on a **phase branch** ([[repository]]), in the code
  repository and in this vault alike (phase 4 was `feature/step4_games`, now in `main`). The
  assistant commits a phase's work there; other work goes on the branch the owner names, `main`
  or another, and the assistant asks when it was not said (owner, 2026-10-20). At the end of a
  phase the owner pushes it into `main`; the other phase arrives through a reviewed pull request.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/):
  `type(scope): summary`, e.g. `feat(daemon): auto-pair gamepads over Bluetooth`.
  - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`. In practice the
    history also uses `design:` for demos and mockups.
  - Scopes match the top-level folders: `iso`, `packages`, `daemon`, `frontend`, `extension`,
    `installer`, `tools`, `vm`, `docs`, `design`. In practice the history also uses component
    scopes (`owneetd`, `display`) and no scope for changes across several folders.
  - The summary is plain English describing the effect, often with the roadmap step:
    `feat(frontend): notifications (step 3.11)`.
- **One logical change per commit.** A plan change goes into the vault in the same change as the
  code it affects.
- The assistant commits locally; the owner pushes ([[collaboration]]).

> [!question] Open
> `design:` and component scopes are used but not listed in `CONTRIBUTING.md`. Ask the owner
> whether to add them to the list or stop using them.
