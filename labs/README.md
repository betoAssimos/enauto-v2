# Lab 01 — Foundation (Blueprint 1.0)

**Status:** Pre-staged. Walked together Days 4–6 of Week 1.
**Read-only:** No `edit-config`, no PUT/PATCH/POST. Writes are a Week 2 concern.

## Blueprint coverage

| Sub-topic | Where it's exercised |
|---|---|
| 1.1 OpenConfig / IETF / native YANG | `01-pyang/` — same domain across all three flavors |
| 1.2 NETCONF / RESTCONF | `02-netconf-getconfig/` + `03-restconf-get/` |
| 1.3 JSON payload from YANG | `01-pyang/` (`pyang -f sample-json-skeleton`) + `03-restconf-get/` (live JSON) |
| 1.4 XML payload from YANG | `01-pyang/` (`pyang -f sample-xml-skeleton`) + `02-netconf-getconfig/` (live XML) |
| 1.5 RFC 8340 tree interpretation | `01-pyang/` (`pyang -f tree`) — every model reviewed in tree form |

## Why this order

1. **pyang first.** Pure local work. No network, no credentials, no surprises. Builds the muscle memory of reading YANG → predicting the payload → verifying with `pyang`.
2. **NETCONF second.** Once you can predict an XML payload from a YANG tree, NETCONF `get-config` becomes "the protocol that retrieves what you predicted." `ncclient` mechanics layer cleanly on top of foundation.
3. **RESTCONF last.** Same data, different transport. The compare-and-contrast against NETCONF cements the operation/method mapping (`get` → GET, `edit-config merge` → PATCH, etc.) that the exam tests directly.

## Structure

```
labs/01-foundation/
├── README.md                      # this file
├── EXERCISES.md                   # checklist of what you produce
├── 01-pyang/
│   ├── README.md                  # Day 4 plan
│   └── yang-models/               # populated Day 4
├── 02-netconf-getconfig/
│   ├── README.md                  # Day 5 plan
│   └── fixtures/                  # populated if/when offline mode needed
└── 03-restconf-get/
    ├── README.md                  # Day 6 plan
    └── fixtures/
```

## Prerequisites before Day 4

- [ ] CBT Nuggets **Data Modelling** module watched.
- [ ] silvancodes **1.0_Foundation_Deep_Dive** read.
- [ ] `notes/01-foundation.md` started — your own words, not transcripts.
- [ ] `pip install -r requirements.txt` succeeded from the repo root.
- [ ] DevNet Always-On IOS-XE sandbox host + credentials verified and in `.env` (Day 5 prerequisite — can wait until Day 4 evening).

## What "done" looks like at end of Week 1

1. Three runnable scripts — one per sub-exercise — that you can rerun cleanly.
2. `notes/01-foundation.md` covering all five sub-topics in your own words.
3. `mocks/section-1/week-01-mock.md` — 20Q mock, score logged, shape verdict declared.
4. `handover.md` blueprint tracker updated: 1.0 → 5/5 sub-topics covered.
