---
type: technical-analysis
description: "API for daemon and OwneetOS version and session mode."
component: owneetd
legacy: "docs/daemon-design.md §4 Status"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Status

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/status` | **Implemented (2.2).** Daemon version, OwneetOS version, session mode (gamescope/cage) |
