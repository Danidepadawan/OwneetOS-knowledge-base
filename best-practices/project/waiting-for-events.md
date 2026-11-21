---
type: best-practice
description: "No hard-coded waits: wait for the event that says something happened, never a fixed time that stands for it; fixed times only as safety limits, repeat intervals or chosen durations, said so in the code."
tags: [best-practice, timing]
---
# Waiting for events, not for fixed times

**The rule (owner, 2026-11-09: "hard-coding is never a good solution"):** computers are slower or faster, and so are monitors,
disks, networks and the programs we run (Steam above all). A wait that stands for "the thing has happened" is never a fixed time:
the code waits for the event that says it (a process ended, a window appeared, a file changed, a log line, a D-Bus signal, a
reply), and goes on at once when it comes.

A fixed time is acceptable only as one of these, and the code says which in a comment:

- **A safety limit:** how long to wait at most for an event that may never come (a frozen app, a dead disk), so that the player is
  never left waiting for ever. What happens when the limit is reached is handled too.
- **A repeat interval:** how often something is checked or retried when nothing can tell when it changes (a ticker that reads a
  file). Prefer a notification (inotify, D-Bus, a log stream) when one exists.
- **A chosen duration:** what the player sees or feels, decided with the owner (how long a notice stays, a key's repeat, the
  time to hold a button, how long without progress counts as stuck).

Anything else is a bug to fix: replace it with the event, and when Steam or another program gives no signal at all, say so in
the comment, keep the time as a limit, and tell the owner.

Decision: [[decision-log]] (2026-11-09). The audit of the waits found then: [[step-4.2c-steam-without-its-interface]].
