---
type: step
description: "Going back to any published version of OwneetOS from Settings: the list of versions, the download in reverse, the warning; split from 7.1."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.1b"
status: todo
tags: [step, phase-7]
---
# 7.1b Going back to any version *(split from 7.1 on 2026-10-25)*

Up: [[phase-7-updates-and-first-release]] · Status: **todo** · Follows [[step-7.1-updates]]

- **Deliverables:** in Settings → System, the published versions of OwneetOS with their dates; the
  user picks one, reads the warning (personal data do not go back; an old version has old
  security problems and may not know newer hardware) and confirms; the console downloads that
  version's OwneetOS packages (kept published for every release) and Arch's packages of its
  Arch Linux Archive date, installs them as an update in reverse (spare copy, 3 tries, the same
  rollback of [[step-6.3-installer-backend]]) and restarts ([[distribution-and-updates]]).
- **Done when:** in the test VM, going from a newer version to an older one works, and a broken
  older version goes back by itself to the one the user came from.
