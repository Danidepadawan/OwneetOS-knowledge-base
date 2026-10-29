---
type: decision
description: "GitHub repository, main ruleset and owner bypass, the owner pushes, GPL-3.0-or-later, Conventional Commits."
area: process
status: active
decided: 2026-10-03
updated: 2026-10-20
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
  - **Phase branches** (owner and Danidepadawan, 2026-10-14), in the code repository **and in
    the knowledge base**: the owner finishes phase 4 on `feature/step4_games`, Danidepadawan works
    on phase 5 on a branch of his own. Phase 4 was finished and fast-forwarded into `main` on
    2026-10-19.
  - **Which branch the assistant commits on** (owner, 2026-10-20): a phase's work on its phase
    branch; any other work on the branch the owner names (`main` or another), case by case. When
    the owner has not said, the assistant asks before committing.
  - **End of a phase:** the owner pushes phase 4 into `main`; then Danidepadawan opens a pull
    request for his phase, which is reviewed before it is merged.
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
| 2026-10-14 | Phase branches, in the code repository and in the knowledge base: phase 4 is finished on `feature/step4_games` (owner), phase 5 on Danidepadawan's own branch; the assistant never commits on `main`. At the end of the phase the owner pushes phase 4 into `main`, then Danidepadawan opens a pull request, which is reviewed. |
| 2026-10-20 | Phase 4 closed and fast-forwarded into `main` (2026-10-19). Outside a phase, the owner names the branch case by case (`main` or another); the assistant asks when it was not said. Replaces "never on `main`" of 2026-10-14. |
