---
type: step
description: "Workflow for linting (shell, Markdown, later Go/Rust and QML), placeholder ISO job; extend the `main` ruleset to require pull requests…"
phase: "[[phase-0-foundations]]"
step: "0.9"
status: done
legacy: "ROADMAP.md 0.9"
tags: [step, phase-0]
---
# 0.9 CI skeleton

Up: [[phase-0-foundations]] · Status: **done**

- **Goal:** GitHub Actions that lint and build what exists.
- **Deliverables:** workflow for linting (shell, Markdown, later Go/Rust and QML), placeholder ISO job;
  extend the `main` ruleset to require pull requests and passing checks (done by the owner on the website).
- **Progress:** `tools/lint` (shellcheck, SPDX headers, markdownlint 0.23.3) passes in the builder VM;
  `.github/workflows/ci.yml` runs it on every push and pull request, plus a placeholder ISO job.
  Actions pinned to commit SHAs. Builder provisioning now also installs `shellcheck`, `nodejs`, `npm`.
- **Done when:** CI is green on `main`.
