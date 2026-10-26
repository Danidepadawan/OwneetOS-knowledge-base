---
type: step
description: "Controller (auto-pairing, as in the mockup) → language → network → ready. The keyboard layout follows the chosen language (console and…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.1"
status: in-progress
legacy: "ROADMAP.md 6.1"
tags: [step, phase-6]
---
# 6.1 First-boot flow

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** controller (auto-pairing, as in the mockup) → language → network → ready.
  The keyboard layout follows the chosen language (console and on-screen keyboard), and can be
  changed in Settings.
  Includes the notice that the first setup needs a Bluetooth or cable controller, and the consent
  dialog for the Xbox dongle firmware (`owneet-xone-firmware install --accept-microsoft-terms`
  when `/run/owneet/xone-firmware-needed` exists).
- **Time zone (added 2026-10-11):** the system runs on UTC until a time zone is chosen, so the
  clock is behind in Italy (2 hours in summer; owner's NiPoGi test). The first-boot flow asks for
  the time zone (suggested from the language, e.g. Italian → Europe/Rome) and Settings gets a
  way to change it. Details agreed with the owner at the start of this step.
- **Demo (2026-10-26):** `design/demos/6.1-first-start.html`: the approved mockup's pairing screen
  (nothing to press; the note that the first set-up needs a Bluetooth or cable controller, the Xbox
  adapter working after its firmware), the language (English, Italiano; the keyboard follows), the
  network (cable, Wi-Fi with the console's keyboard, or "Not now": games on disks work offline),
  the time zone (suggested from the language with its time; a scrolling list of cities for a
  language with several zones; "Choose another city"), the Xbox adapter's firmware (only with an
  adapter and the internet: Download, Read the terms, Not now), ready with a summary. Waiting for
  the owner's approval. Branch `feature/step6_installer`.
