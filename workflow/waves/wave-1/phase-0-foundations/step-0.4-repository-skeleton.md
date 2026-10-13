---
type: step
description: "`git init`; directory layout (`iso/`, `packages/`, `daemon/`, `frontend/`, `extension/`, `installer/`, `tools/`, `vm/`, `docs/`,…"
phase: "[[phase-0-foundations]]"
step: "0.4"
status: done
legacy: "ROADMAP.md 0.4"
tags: [step, phase-0]
---
# 0.4 Repository skeleton

Up: [[phase-0-foundations]] · Status: **done**

- **Goal:** a clean, documented repository that another developer can join.
- **Deliverables:** `git init`; directory layout (`iso/`, `packages/`, `daemon/`, `frontend/`,
  `extension/`, `installer/`, `tools/`, `vm/`, `docs/`, `design/`); `README.md`, `LICENSE`
  (GPLv3), `CONTRIBUTING.md` (English only, commit style, one-step workflow), `.gitignore`
  (VM images, caches, build output), `.editorconfig`.
- **Done when:** the tree is committed locally and every folder has a short README stating its purpose.
