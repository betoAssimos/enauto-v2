# Handover — Current State of the ENAUTO 300-435 Study

**Last updated:** 2026-05-19 (planning session)
**Updated by:** Claude (planning session with Beto)
**Status:** ✅ Planning complete. Ready to begin Week 1, Day 1.

> **For any new AI session:** Read `master_context.md` first, then this file. Confirm understanding briefly, then wait for Beto's go-ahead before doing anything.

---

## 1. Where we are right now

| Field | Value |
|---|---|
| Current week | **0 (pre-Week 1)** |
| Current day in week | n/a |
| Current blueprint domain | n/a — about to start 1.0 |
| Current sub-topic | n/a — about to start 1.1 (OpenConfig/IETF/native YANG) |
| Days until ceiling exam date (2026-08-17) | 90 |
| Active sandbox reservation | none |
| Weeks completed | 0 / 13 |

---

## 2. Last session — summary

**Session date:** 2026-05-19
**Session type:** Strategy + planning
**Outcome:** Both foundation documents drafted (`master_context.md` and this `handover.md`). Repo strategy decided: Option C — fresh, study-driven structure, no AUTOCOR-style platform overhead. Schedule confirmed. Mock-shape rules and readiness signals defined.

**Key decisions made this session:**
- Repo: `https://github.com/betoAssimos/enauto-v2` (public, empty on GitHub, fresh start)
- Old local `~/enauto-v2` directory: move to `~/enauto-v2-old-backup` before creating new structure
- Schedule: 13 weeks default, compression allowed if mock evidence supports it
- Resources: CBT Nuggets for video theory, silvancodes for written reinforcement, AI for labs + mocks
- Mocks: per-section (20Q), per-controller in Section 3 (4 × 20Q), full-length ×2 in Week 13
- Mock-shape calibration against the 59-question dump; Beto holds permanent veto
- Readiness: composite signals (silvancodes is the independent calibration), not single AI-mock score
- Sandbox booking: just-in-time, ~4 days before each controller week
- Old `enterprise-netauto-platform` MCP server (in connector list): stale, ignore

---

## 3. Next planned step

**Title:** Week 1 Day 1 — Repo bootstrap and Foundation kickoff

**Sub-steps in order:**

1. **Local cleanup.**
   ```bash
   mv ~/enauto-v2 ~/enauto-v2-old-backup
   mkdir ~/enauto-v2 && cd ~/enauto-v2
   ```
2. **Commit the two foundation documents.** Place `master_context.md` and `handover.md` in the repo root.
3. **Create the directory skeleton** (per repo conventions in master_context.md §12):
   ```
   labs/{01-foundation,02-device,03-catalyst-center,03-meraki,03-sdwan,03-ise,04-operations,05-ai}/
   mocks/{section-1,section-2,section-3-catc,section-3-meraki,section-3-sdwan,section-3-ise,section-4,section-5,full-length}/
   notes/
   tests/
   ```
4. **Add Python project files:** `requirements.txt`, `pyproject.toml`, `secrets.example.env`, `.gitignore`. AI will draft these in the first Week 1 working session.
5. **Initial push to GitHub.** `git init`, first commit, push to `main`.
6. **Start Week 1 theory:** Beto watches CBT Nuggets Python Basics + Git Basics + Data Modelling modules. AI does not touch this — it's pure input on Beto's side.
7. **Read silvancodes `1.0_Foundation_Deep_Dive`** in parallel with the videos.
8. **Lab 01 kickoff** once videos + reading are complete: AI walks Beto through a small pyang + ncclient lab, theory first, piece by piece.

**Estimated time for Week 1:** ~22 hours over 7 days. Foundation is mostly revisit territory from AUTOCOR — if Beto absorbs fast, Week 1 may compress.

---

## 4. Open questions / pending decisions

None at this moment. All blocking decisions resolved in the planning session.

*Add new entries here as they come up during sessions. Each entry: `[DATE] question / decision needed.`*

---

## 5. Sandbox reservations — active and upcoming

| Sandbox | Status | Booked | Expires | Purpose |
|---|---|---|---|---|
| Meraki (public always-on key) | ✅ Available | n/a | n/a | Use any time for Week 5 |
| Catalyst Center | Not booked yet | — | — | Book ~Day 24 (4 days before Week 4) |
| SD-WAN | Not booked yet | — | — | Book ~Day 38 (4 days before Week 6) |
| ISE | Not booked yet | — | — | Book ~Day 45 (4 days before Week 7) |

**AI reminder schedule (AI must surface these proactively):**
- 📅 ~Day 24 (around 2026-06-12): "Book Catalyst Center sandbox for Week 4."
- 📅 ~Day 38 (around 2026-06-26): "Book SD-WAN sandbox for Week 6."
- 📅 ~Day 45 (around 2026-07-03): "Book ISE sandbox for Week 7 (or confirm Catalyst Center bundle includes it)."

---

## 6. Mock log

| Week | Section | Score | Shape verdict | Notes |
|---|---|---|---|---|
| — | — | — | — | No mocks taken yet. |

*Each row added after a mock. Shape verdict = "Right" / "Off" / "Mixed" per master_context §8.*

---

## 7. Weak areas queue (for spaced review)

Empty — no mocks taken yet.

*Format for entries: `[Blueprint sub-topic] — [why flagged] — [last revisited date]`. Reviewed at end of each week and end of each month.*

---

## 8. Blueprint coverage tracker

| Domain | Sub-topics covered | Sub-topics remaining | Coverage % |
|---|---|---|---|
| 1.0 Foundation | 0 / 5 | 5 | 0% |
| 2.0 Device-Level | 0 / 7 | 7 | 0% |
| 3.0 Controller-Based | 0 / 6 | 6 | 0% |
| 4.0 Operations | 0 / 6 | 6 | 0% |
| 5.0 AI in Automation | 0 / 4 | 4 | 0% |
| **Overall** | **0 / 28** | **28** | **0%** |

*Updated end of each week as sub-topics get touched and labbed.*

---

## 9. Notes for the next AI session

- **First-time session for Week 1.** Beto has not yet started any CBT Nuggets videos for this course. Do not assume foundation knowledge is fresh — confirm with him before launching into ncclient code.
- **Beto has passed AUTOCOR.** Skip basic Python, Git, NETCONF/RESTCONF, YANG concept introductions. He knows these. The Week 1 work is exam-aligned revisit, not first-time teaching.
- **The 59-question dump is the shape reference for mocks.** When generating the Week 1 mock (end of Week 1), open the dump and match the texture.
- **First lab approach:** theory first, piece by piece, dry-run by default. Do not drop completed code on him. He explicitly stated in past sessions that this breaks his learning chain.
- **Old `~/enauto-v2` directory exists locally** with some Lab 01/02 work from earlier sessions. The plan is to back it up (`mv` to `~/enauto-v2-old-backup`) and start the public repo fresh. Do not try to import the old code wholesale.
- **The local lab is down.** No Containerlab topology running. Any device-level lab in Weeks 1–3 needs to either (a) run against a DevNet sandbox device, (b) be theoretical/dry-run only, or (c) rebuild a small Containerlab topology in Week 2 if Beto wants live targets. Discuss with him before choosing.

---

## 10. Session sign-off protocol

At the end of every session, AI updates this file with:

1. **New "Last updated" date** at the top.
2. **New entry in "Last session — summary"** describing what was done.
3. **Updated "Where we are right now"** if position changed.
4. **Updated "Next planned step"** with concrete next sub-steps.
5. **New entries** in mock log, weak areas, blueprint tracker as applicable.
6. **Bookings updated** if a sandbox was reserved or released.
7. **Notes for the next AI** updated with anything important to carry forward.

Beto reviews the updated handover before closing the session. If he disagrees with anything, fix it before he leaves. The handover must reflect reality, not aspiration.

---

*End of handover. Ready for Week 1, Day 1 on Beto's signal.*
