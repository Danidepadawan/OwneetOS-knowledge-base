---
type: guard
tags: [guard, product]
---
# Guard: product invariants

- **Never require a mouse or a keyboard**, anywhere: installer, first setup, apps, settings, and
  anything the console opens (Steam included). They may only work as an optional fallback.
  ([[hard-constraints]] C2)
- **Never bind the Guide button** outside the system daemon `owneetd` (apps and themes never see
  it). ([[guide-button]])
- **Never give a button two meanings on the same screen**, and never use LB / RB for anything but
  switching top-level sections. ([[controller-input-map]])
- **Never intercept any input but Guide** while a game or app is running. ([[controller-input-map]])
- **Never add bloat**: no desktop environment, no display manager, no dependency that is not
  justified by what it saves; idle target with Steam and Brave closed is under 500 MB RAM.
  ([[hard-constraints]] C1, C4)
- **Never add an own server** or anything that needs one; never collect telemetry. Crash reports
  only with explicit opt-in consent. ([[online-and-chat]], [[legal-compliance]])
- **Never require internet** for local or DRM-free content. The only exception is Proton's one-time
  download for Windows games. ([[hard-constraints]] C9, [[games-on-disk]])
- **Never hard-code UI text or colours**: text through the i18n message files, colours through the
  palette tokens. ([[ui-text-and-i18n]], [[design-tokens]])
- **Never support ARM or legacy BIOS boot**: x86_64 and UEFI only. ([[hard-constraints]] C3,
  [[system-requirements]])
- **Never make a Wave 1 feature depend on dual boot.** ([[installer-and-firmware]])
- **Never show technical names to the user** where the user does not need them (e.g. Proton is never
  named). ([[games-on-disk]], [[writing-for-users]])
