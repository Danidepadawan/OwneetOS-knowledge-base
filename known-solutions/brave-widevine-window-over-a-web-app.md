---
type: known-solution
description: "Brave shows its own window 'Restart browser to enable Google Widevine' (Block / Allow) over a web app; the controller cannot close it. Comes after every Widevine download."
status: solved
seen: 2026-10-19
updated: 2026-10-19
tags: [known-solution, brave, widevine, web-apps]
---
# Brave's Widevine window over a web app

## Symptom

- Over a playing video (YouTube's TV interface, a new profile) Brave shows **"www.youtube.com is
  asking you to: Restart browser to enable Google Widevine"**, with "Don't ask again", Block /
  Allow, "By installing, you'll agree to Google's terms of use" and a link to
  `brave://settings/extensions`.
- The controller cannot close it, with or without the extension's navigation: it is **Brave's own
  window**, outside the page, which no content script can reach. Only the mouse can.
- Another web app (Netflix, an older profile) never shows it.

## Cause

- Widevine **is** turned on (`"widevine_opted_in": true` in the profile's `Local State` and
  `Default/Preferences`, owneetd's seed of [[step-5.1-brave-in-the-os]]), and Brave downloads it
  per profile (`WidevineCdm/4.10.3112.0` in each profile folder).
- On Linux a freshly downloaded Widevine works **only after Brave restarts**, so Brave asks for the
  restart in that window. A profile that downloaded it in an earlier session (Netflix's) never
  asks; **every Widevine update asks again**, in old profiles too.
- The "Don't ask again" box is the setting `brave.ask_widevine_install` (the name is in Brave's
  program: `grep -a -o "brave\.[a-z_.]*widevine[a-z_.]*" /opt/brave-bin/brave`).

## Solution

owneetd 0.12.7 (`daemon/internal/catalog/open.go`, [[step-5.3-youtube]]): before every opening
of a web app (Brave closed for it), owneetd sets `brave.ask_widevine_install` = false (and the
sidebar setting) in both settings files of the profile, keeping everything else Brave wrote.
Verified in the test VM (2026-10-19): a new profile downloaded Widevine without the window, and an
older profile got the settings at its next opening. The user's consent to Google's terms is asked by the
console instead, from [[step-5.4-netflix]] ([[legal-compliance]]). Still open there: the first
protected video of a new profile may fail until Brave restarts.

## How we found it

1. The owner's screenshot (test VM, cage): the window over YouTube's video.
2. In the VM, for each profile: `ls PROFILE/WidevineCdm` (both had 4.10.3112.0) and
   `grep -o '"widevine[^,}]*' "PROFILE/Local State" PROFILE/Default/Preferences` (opted in, both):
   the opt-in worked, so the window was the restart question, not the install one.
3. The setting behind "Don't ask again": Brave's own program, as above.

## Watch out

- Any window of Brave's own (permission bubbles, info bars, the sidebar) is out of the
  extension's reach: turn it off with a policy or a profile setting, never leave it to the user.
- A profile setting written only into new profiles misses the old ones: set it before every
  opening.
