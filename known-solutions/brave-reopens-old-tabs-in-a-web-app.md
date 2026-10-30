---
type: known-solution
description: "Brave's window \"Fix the tabs slowing your browser\" lists other tabs of the web app, Spotify asks \"Listen on this phone\" or plays \"on Web Player\": Brave reopened the previous session's tabs, hidden behind the kiosk window."
status: solved
seen: 2026-10-26
updated: 2026-10-31
tags: [known-solution, brave, web-apps]
---
# Brave reopens old tabs behind a web app

## Symptom

- Over a web app, Brave's own window **"Fix the tabs slowing your browser — These tabs are using
  extra resources"** with *Dismiss* / *Fix these tabs*, listing **other tabs of the same web app**
  (two Spotify tabs, 2026-10-26). It needs a mouse.
- On Spotify: its window **"… playing on Web Player — Listen on this phone"**, a green bar
  **"Playing on Web Player (Chrome)"** at the bottom, the song playing "elsewhere"; on the desktop
  player Play seemed to reload or do nothing.
- Only one page is ever visible (kiosk mode): the other tabs are hidden behind it.

## Cause

Brave's startup setting reopened the **previous session's tabs** every time owneetd started the web
app, and owneetd's address opened one more tab on top. Each opening left another hidden player of
the same account, so Spotify saw several "devices" and Brave several heavy tabs. Nothing on screen
showed the tabs, so it looked like Spotify misbehaving.

## Solution

- Managed policy **`RestoreOnStartup` = 5** (open only the address given):
  `packages/owneet-base/brave-policies.json`, owneet-base 0.0.52 ([[step-5.5-spotify]]).
- Brave's performance alert turned off as well: `--disable-features=PerformanceInterventionUI` in
  owneetd's command (owneetd 0.16.3), in the **same** `--disable-features` as the extension's
  feature, since Brave reads only the last one.

## How we found it

1. The alert's list named two Spotify tabs, and on 2026-10-24 the green "Playing on Web Player"
   bar had already shown another player of the same account.
2. In the test VM, with Spotify open:
   `ls -la /home/owneet/.local/share/owneet/webapps/spotify/Default/Sessions` showed two saved
   sessions (2.3–2.7 MB each).
3. The policy added by hand to `/etc/brave/policies/managed/owneet.json`, Spotify closed (Brave
   exits with every tab) and opened again: no alert, no "Listen on this phone".

## Watch out

- Any web app can show it (each has its own profile). If hidden tabs seem back, check that the
  installed policy file still has `RestoreOnStartup`, and look at the profile's `Sessions` folder.
- `brave://policy` cannot be opened (internal pages are blocked): read the policy file instead.
