---
type: decision
area: process
status: active
decided: 2026-10-03
updated: 2026-10-04
legacy: "PROJECT_RULES.md §11 (repository), §13 (2026-10-03, 2026-10-04)"
tags: [decision, process, git]
---
# Repository, licence and commits

- Repository: **[github.com/fancy-dino/OwneetOS](https://github.com/fancy-dino/OwneetOS)**
  (public), shared with another developer.
  - `main` is protected by a ruleset: no deletion, no force push, pull request with an approval and
    passing CI checks (`Lint`, `ISO`) required. **The owner (repository admin) is on the bypass
    list** and may push directly ("option A"); every other contributor goes through pull
    requests. CI runs on every push anyway.
  - There is no GitHub CLI (`gh`) on the host and the assistant's shell has no GitHub credentials:
    the assistant commits locally, the **owner pushes** ("Sync Changes" in VS Code). Other GitHub
    actions are done by the owner through VS Code or the website, until `gh` is installed (with
    the owner's approval).
- Licence **GPL-3.0-or-later** for OwneetOS's own code ([[license-headers]]).
- Commit messages follow **Conventional Commits** ([[commits-and-branches]]).
- English for all project text ([[hard-constraints]] C6).

Guard: [[collaboration]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Public repo; English mandatory for all project text. |
| 2026-10-04 | License GPL-3.0-or-later and Conventional Commits confirmed by the owner; step 0.4 approved. |
| 2026-10-04 | Repository published at github.com/fancy-dino/OwneetOS; `main` ruleset active (step 0.5). |
| 2026-10-04 | `main` ruleset: PR + approval + green CI for contributors; owner bypasses and pushes directly (option A). |
