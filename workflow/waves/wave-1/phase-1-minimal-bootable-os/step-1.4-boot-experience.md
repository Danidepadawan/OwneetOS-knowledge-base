---
type: step
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.4"
status: done
legacy: "ROADMAP.md 1.4"
tags: [step, phase-1]
---
# 1.4 Boot experience

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** systemd-boot config, Plymouth theme with the OwneetOS mark, quiet kernel
  parameters, no text on screen in normal boots.
- **Done when:** power-on to placeholder shows only the logo.
- **Outcome:** `owneet-branding` package (wordmark generated from Bricolage Grotesque by
  `tools/branding/make-wordmark`; Plymouth theme `owneet`: wordmark + coral spinner on deep navy),
  silent kernel/systemd parameters, hidden boot menu, silent autologin. Recorded the boot in the test
  VM (screenshot every 0.4 s): after the VM firmware, only the splash (2.4–9.3 s), then a dark
  screen without text (about 4 s in the VM, software rendering), then the console session.
  Problems found and fixed: Plymouth fell back to its text splash (serial console; theme images
  linked instead of copied); keeping the splash on screen until the UI (`--retain-splash`) delayed
  autologin by 30 s, so it was removed. **Left for step 3.2:** a seamless splash-to-UI handover
  (no dark gap). The owner approved the splash with the wordmark changed to "Owneet" + coral "OS".
