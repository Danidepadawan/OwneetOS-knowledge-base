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
  adapter and the internet: Download, Read the terms, Not now), ready with a summary. Branch
  `feature/step6_installer`.
- **Demo approved by the owner (2026-10-26)** after two changes: the Wi-Fi signal drawn as the
  settings' icon, and the five languages of Wave 1 in the picker ([[languages]]) with their time
  zones (Berlin; Paris, Bruxelles, Genève, Montréal; Madrid, Ciudad de México, Bogotá, Lima, Buenos
  Aires, Santiago). The screens' code comes after Danidepadawan's merge.
- **Code started (owner, 2026-10-29)** on the branch `feature/phase6`, one branch for the whole
  phase 6. Agreed at the start: the first start is shown once on an installed console, until
  "Ready" (turned off half way it starts again, keeping the choices already made), and at every
  start from the USB stick ([[step-6.2-live-vs-installed-mode]]); the picker lists the five
  languages from the start, the first start's own messages in all five and the rest of the console
  in English for German, French and Spanish until [[step-7.9-console-more-languages]]
  ([[first-boot-setup]], [[languages]]). Plan: owneetd (the time zone through systemd-timedated,
  the Xbox adapter's firmware through a root unit, both allowed by polkit to the console user
  only; the first start's state), then the screens as in the approved demo, then the test VM.
