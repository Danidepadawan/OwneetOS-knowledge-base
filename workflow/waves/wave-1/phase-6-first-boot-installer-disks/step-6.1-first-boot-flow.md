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
- **Built (2026-10-29):** owneetd 0.17.0 (`/v1/time`, `/v1/time/zone`, `/v1/time/zones`,
  `/v1/xone`, [[owneetd-api-time]]); `owneet-xone` 0.5.8-4 (the install unit and its polkit rule,
  the helper's progress file); `owneet-base` 0.0.52 (systemd-timesyncd on); `owneet-frontend`
  0.24.0 (`FirstStart.qml`, `Tr.trIn` for the title shown in each language, the messages in the
  five languages, the cities' names as messages). The first start counts as done with the
  interface's memory `firstStartDone`, which an installed console keeps and the USB stick never
  does. The picker lists the languages as Settings does (English first, then by their own name).
  Seen in the interface preview (`tools/preview-steps/first-start.txt`, `@firststart`): language,
  Wi-Fi with the keyboard, the suggested zone and the list of every city, the adapter's firmware,
  ready, no first start after a restart.
- **Open (2026-10-29):** "Read the terms" of the adapter's firmware: the demo opened Microsoft's
  terms in the web apps' window, but Brave is installed only with a web app
  ([[step-5.0.0-optional-web-apps]]), so it is not there at the first start: the owner chooses
  how. The time zone in Settings (this step's deliverable) needs its demo first
  ([[demo-before-code]]).
- **Decided (owner, 2026-10-29):** "Read the terms" shows a QR code with the address of
  Microsoft's terms, read on a phone (option a); if it turns out too awkward, the button goes and
  the consent sentence stays (option b). Settings → Language gets a "Time zone" row that opens the
  same list of cities, and the date and time can be set by hand when the console has not had them
  from the internet (a console with no internet and a wrong clock): demo first. The picker: English
  first, then alphabetical by the languages' own names. German, French and Spanish are translated
  for the whole console now ([[step-7.9-console-more-languages]]).
- **Tested in the test VM (2026-10-29)** with the ISO of the branch, live, no controller: the
  pairing screen with its title in each language; a keyboard goes on; Italian; the cable;
  Rome suggested and set by owneetd through polkit (`timedatectl`: Europe/Rome, synchronised); no
  adapter, so no firmware screen; the summary.
- **Done 2026-10-29:** the whole console in German, French and Spanish (664 messages each,
  drafted, `tools/i18n-check` wants the five complete), with their keyboard layouts in owneetd and
  on the on-screen keyboard (German QWERTZ, French AZERTY, Spanish), following the language.
- **Second round of the demos, for approval (2026-10-29):** `6.1-first-start.html` ("Read the
  terms" as a QR code with the address under it; without the internet "Set the time" on the time
  screen) and the new `6.1-settings-time.html` (Settings → Language: "Time zone", the list of
  cities; "Date and time", from the internet, or by hand without it).
- **Second round approved by the owner (2026-10-29)**, with the guarantee that without the internet the first start sets the date and time too, not only the time zone.
- **Built, second round (2026-10-29):** owneetd 0.18.0 (`PUT /v1/time/now`, the date and time in
  the zone given or the console's; polkit's set-time, [[owneetd-api-time]]); `owneet-frontend`
  0.25.0: the "Date and time" window (`ClockSheet.qml`: day, month, year, hours, minutes, as in the
  demo; at the first start in the time of the city shown, since the console's zone is not set
  yet), the list of
  every city (`TimeZoneSheet.qml`, the current one ticked and in the middle), the cities shared by
  the first start and Settings (`TimeZones.qml`), Settings → Language "Time zone" and "Date and
  time" (from the internet: it says so; without it: the window), the top bar clock following the
  zone chosen, and "Read the terms" as a QR code with the address. Seen in the interface preview
  (`tools/preview-steps/first-start-time.txt`).
- **Tested in the test VM (2026-10-29)** with the ISO of the branch, live, network off: the first
  start in Italian, "Not now", Rome suggested; "Set the time" opened on Rome's time (not the
  system's UTC) and saved two hours later: the system clock moved by two hours, the internet's time
  on again (`timedatectl`); "Continue" set Europe/Rome; the top bar clock showed the new time;
  Settings → Language: "Time zone" Rome · UTC+1, "Date and time" from the PC's clock, set again by
  hand; the toasts "Time set" and "Time zone: Rome". Microsoft's terms as a QR code seen in the
  interface preview (no Xbox adapter in the VM). Fixed on the way: the first start's time now
  follows a change at once, and the Settings row follows the top bar clock's minute.
- **Aligned with the approved demos (2026-10-29):** the code had added things the demos do not
  have (the city and UTC over the time fields, a D-pad prompt, a "Set the time" button under the
  list of cities, a short year, other prompts on the terms): removed at the owner's request, the
  screens are exactly as approved. Without the internet, a language with several cities (English,
  French, Spanish) had "Set the time" only in Settings, as in the demo.
- **Decided (owner, 2026-10-29):** the languages must not make a difference ([[first-boot-setup]]).
  First "Set the time" under the list of cities, in the time of the city last selected (demo
  approved); the interface preview showed that reaching the button passes over every city, so the
  window opened on the last one's time (Singapore for English). The owner chose instead: a city
  picked in a list gets the suggested city's screen (Continue, Choose another city, Set the time),
  with the text "Once online the clock sets itself; the time zone stays the one you choose." (not
  "Suggested from your language"). Demo `6.1-first-start.html` updated; the code waits for its
  approval ([[demo-before-code]]).
- **Built and tested (2026-10-29):** the demo approved by the owner; `FirstStart.qml`: a city
  picked in a list gets the suggested city's screen (new message `first.time.chosen` in the five
  languages); preview `tools/preview-steps/first-start-time-list.txt`. In the test VM, live,
  network off, in English: New York picked, its own screen with "Set the time", the window opened
  on New York's time and saved one hour later (the system clock moved by one hour), "Continue" set
  America/New_York, the summary and the top bar clock right. Italian (one city) unchanged.

