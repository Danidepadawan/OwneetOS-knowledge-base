---
type: meta
tags: [meta]
---
# Legacy references

Commit messages and old branches refer to the files this vault replaced. Those files
were deleted from the code repository on 2026-10-13 (still in its git history). This table
says where each reference points now ([[knowledge-base]]).

## `PROJECT_RULES.md` sections

| Old reference | Note(s) now |
|---|---|
| header ("source of truth", "ask, do not assume") | [[step-workflow]], [[collaboration]], [[kb-rules]] |
| §1 Vision | [[vision]] |
| §2 Hard constraints (C1–C9) | [[hard-constraints]] |
| §3 Target hardware | [[system-requirements]], [[console-session]] (cage fallback) |
| §4 Architecture | [[architecture-stack]], [[owneetd]], [[frontend-fork]] |
| §5 Distribution, build and updates | [[distribution-and-updates]], [[package-signing]] |
| §6 Installation, boot and disks | [[installer-and-firmware]], [[disks]], [[games-on-disk]] |
| §7 Controllers | [[controllers-and-pairing]], [[xbox-wireless-dongle]] |
| §8 Features | [[game-library]], [[steam-integration]], [[online-and-chat]] |
| §9 UI / UX | [[design-direction]], [[demo-before-code]], [[languages]], [[home-and-library]], [[ui-patterns]], [[design-tokens]] |
| §9.1 Controller input map | [[controller-input-map]], [[guide-button]] |
| §10 Roadmap, Wave 1, later waves, nice-to-have | [[wave-1-scope]], [[wave-1]], [[wave-2]], [[backlog]] |
| §11 Development environment | [[development-environment]], [[repository]] |
| §12 Legal compliance | [[legal-compliance]], [[frontend-fork]] |
| §13 Decision log | [[decision-log]] |

## Other files

| Old reference | Note(s) now |
|---|---|
| `ROADMAP.md`, "roadmap step N.M" | [[wave-1]] → `step-N.M-…` notes (e.g. "step 3.9" → [[step-3.9-settings]]) |
| `ROADMAP.md` "How we work" | [[how-we-work]] |
| `docs/daemon-design.md` | [[owneetd-design]] and the `owneetd-api-*` notes |
| `docs/frontend-architecture.md` | [[frontend-architecture]], [[frontend-pegasus-internals]], [[frontend-steam-local-files]], [[frontend-input]], [[frontend-changes]] |
| `design/sounds.md` | [[interface-sounds-spec]] |
| `design/README.md` (demos list) | [[mockups-and-demos]] |
| `CONTRIBUTING.md` (rules for every component, commits) | [[commits-and-branches]], [[license-headers]], [[checks-before-commit]], [[product-invariants]] |

On 2026-10-13 every such reference in the code repository (comments, scripts, CI, READMEs,
demo headers) was rewritten as a link to its note, e.g. `[[controller-input-map]]`
([[code-comments]]); this table remains for commit messages and old branches.
