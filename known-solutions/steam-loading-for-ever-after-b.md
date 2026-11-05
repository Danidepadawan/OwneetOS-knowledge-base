---
type: known-solution
description: "B on Steam's home page leaves Steam on an endless loading screen; Guide still comes back, closing Steam clears it. Seen since 2026-10-13; no sign of it in Steam's logs; the cause is not proved."
status: open
seen: 2026-10-13
updated: 2026-11-05
tags: [known-solution, steam, gamescope]
---
# Steam loads for ever after B

## Symptom

Steam's Big Picture opened from the console: B on Steam's home page shows Steam's loading screen, which never ends (owner, FrankenPC, 2026-11-05,
reported as serious). Holding Guide still comes back to the console; closing Steam from its tile clears it.

## What is known

- **2026-10-13:** Steam started on a `steam://` address: Back from that first page loaded for ever. Fixed for that case: Steam starts on its own
  home page and gets the address afterwards (commit 231d919).
- **2026-10-15:** reported again, "endless loading after B or after cancelling in Steam" ([[decision-log]]). Judged impossible to detect; the answer was the
  window "How to come back from Steam" ([[steam-integration]]), and the owner confirmed the bugs of that round as solved.
- **2026-11-05:** the address reached Steam 2 s after its interface was up, as in the test before; the same again. So the new wait did not visibly bring it,
  but that is not proved: the earlier test of the same day has no report on B.
- **Logs:** nothing in `console_log.txt` or `webhelper.txt` at the moment of the press: still nothing to detect it with.

## Solution

None yet. The likely cause (not proved): the first entry of Steam's own page history is its loading screen, and B goes back to it.
**Next, the deciding test:** Steam started with no address at all, B on its home: if it loads for ever too, it is Steam's own behaviour and not ours.

## The owner's idea (2026-11-05)

Read the page Steam is on: if B on its home leads to a page that does not exist, that is the culprit, and the console can come back to its own home. Checked in FrankenPC's
test: no log says the page, and the window's title stays "Big Picture" on every snapshot. The only way known is Steam's debugging port, which [[legal]] covers: not used unless the owner decides.

## What must not be tried

Steam's debugging port, to read or rewrite its pages, without the owner's decision on [[legal]]: it would also leave a port through which any program on the console could drive the signed-in Steam; catching B while Steam is on screen ([[product-invariants]]: only Guide).

## Watch out

Steam's window in the test VM runs in cage, not gamescope: this test is about Steam's pages, so it should hold there too, but check it on FrankenPC before concluding.
