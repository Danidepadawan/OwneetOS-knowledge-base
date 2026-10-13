---
type: wave
legacy: "ROADMAP.md How we work; CONTRIBUTING.md Workflow"
tags: [workflow, process]
---
# How we work

Decision: [[step-workflow]] · Guard: [[collaboration]] · Plan: [[wave-1]]

1. **One step per prompt**, in the order of the wave notes. A step marked *(multi-prompt)* is
   expected to need more than one prompt; it is still reviewed as one unit.
2. At the end of every step the assistant reports what was done, how it was verified, and anything
   that deviated from the plan. The step is marked done only after the **owner approves it**.
3. Steps marked **Owner input** stop and ask before acting (installing software on the host,
   creating remote resources, choices with long-term impact).
4. Any change of plan is recorded in the [[decision-log]] (and its decision note) and reflected in
   the wave notes, so they always show the current plan.
5. Steps may be split, merged or reordered when reality requires it. That is expected and is
   always done openly, never silently.

## A step, from start to approval

1. Read the step note, its phase note, and the decisions and best practices it links.
2. Screens: interactive demo first, approved by the owner ([[demo-before-code]]).
3. Build and verify in the VMs ([[testing-and-verification]]); run the checks
   ([[checks-before-commit]]); commit locally ([[commits-and-branches]]).
4. Write the outcome in the step note (what, how verified, measurements, versions, open points)
   and set its status; record any new decision ([[kb-rules]]).
5. Report to the owner and wait for approval before the next step.
