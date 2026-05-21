# Handover — Current State of the ENAUTO 300-435 Study

**Last updated:** 2026-05-21 (Week 1 Day 1 — bootstrap + pre-stage)
**Updated by:** Claude (Week 1 Day 1 session with Beto)
**Status:** ✅ Repo live. Lab 01 pre-staged. Beto now on theory input (CBT Nuggets + silvancodes). Next AI session = Day 4 pyang lab.

> **For any new AI session:** Read `master_context.md` first, then this file. Confirm understanding briefly, then wait for Beto's go-ahead before doing anything.

---

## 1. Where we are right now

| Field | Value |
|---|---|
| Current week | **1** |
| Current day in week | Day 1 complete; Days 2–3 = theory input (Beto solo); next AI touch = Day 4 |
| Current blueprint domain | 1.0 Foundation |
| Current sub-topic | About to cover 1.1–1.5 via theory (Days 1–3), then Lab 01 (Days 4–6) |
| Days until ceiling exam date (2026-08-17) | 88 |
| Active sandbox reservation | none (Meraki public key always available; first reservation ~Day 24) |
| Weeks completed | 0 / 13 |

---

## 2. Last session — summary

**Session date:** 2026-05-21
**Session type:** Week 1 Day 1 — repo bootstrap + Lab 01 pre-stage
**Outcome:** Repo is live on GitHub with foundation docs, project scaffold, and full directory skeleton. Week 1 theory map delivered. Lab 01 (Foundation) fully pre-staged with READMEs and exercise checklist. Beto handed off to solo theory input (Days 2–3).

**What was done this session:**
- Local cleanup done (`~/enauto-v2` → `~/enauto-v2-old-backup`, fresh dir created).
- Directory skeleton built (labs/, mocks/, notes/, tests/ per master_context §12).
- Project files generated and committed: `README.md`, `requirements.txt`, `pyproject.toml`, `secrets.example.env`, `.gitignore`.
- Initial push to `main` succeeded (commit `93f99c7`).
- **Cleanup:** WSL `:Zone.Identifier` files had been committed by accident; deleted, pattern added to `.gitignore`, committed (`0bad012`).
- **Week 1 theory map** delivered: blueprint 1.1–1.5 mapped to CBT Nuggets Data Modelling module + silvancodes 1.0 deep-dive, with proactive listen-for distinctions (OpenConfig/IETF/native naming, NETCONF datastore semantics, RESTCONF media types, RFC 8340 tree symbols).
- **Lab 01 pre-staged** (chosen over starting theory immediately — pure prep, no code): 5 READMEs + EXERCISES.md (17 blueprint-tagged tasks) covering pyang (Day 4), NETCONF get-config (Day 5), RESTCONF GET (Day 6). All read-only; writes deferred to Week 2.

**Key facts established this session:**
- `requirements.txt` is unpinned at first install; freeze to `requirements.lock` after first successful `pip install`.
- `catalystcentersdk` may not resolve in pip — fallback is legacy `dnacentersdk`.
- Catalyst SD-WAN has no official SDK — using `requests` directly.
- WSL environment: watch for `:Zone.Identifier` files on any Windows→Linux file copy. `.gitignore` now catches them, but eyeball `ls -la` after copying.

---

## 3. Next planned step

**Title:** Week 1 Day 1 — Repo bootstrap and Foundation kickoff

**Title:** Week 1 Day 4 — Lab 01 kickoff (pyang), once theory input is done

**Prerequisite before next AI session (Beto solo, Days 2–3):**
- Watch CBT Nuggets **Data Modelling** module. (Python Basics + Git Basics are AUTOCOR revisit — skim or skip.)
- Read silvancodes **1.0_Foundation_Deep_Dive**.
- Start `notes/01-foundation.md` in own words.
- `pip install -r requirements.txt` from repo root; freeze to `requirements.lock` once it succeeds.

**Next AI session sub-steps (Day 4 — pyang lab, theory-first, piece by piece):**

1. Brief confirm of theory absorption before any command runs — do NOT assume foundation is fresh just because AUTOCOR covered it; confirm with Beto.
2. Theory walk: where YANG models live, namespace conventions, container/list/leaf in tree form, RFC 8340 symbol set.
3. Acquire three "interfaces" YANG modules (OpenConfig, IETF, Cisco-native) → `labs/01-foundation/01-pyang/yang-models/`. Note source URLs.
4. `pyang -f tree` on each; read output together; identify symbols.
5. `pyang -f sample-json-skeleton` and `-f sample-xml-skeleton` on OpenConfig interfaces; trace each line back to the tree.
6. Note structural differences (JSON vs XML, flavor vs flavor) in `notes/01-foundation.md`.

Full plan + 17-task checklist already pre-staged in `labs/01-foundation/EXERCISES.md` and the per-exercise READMEs. Day 5 = NETCONF get-config; Day 6 = RESTCONF GET; Day 7 = 20Q mock on 1.0.

**Estimated time for Week 1:** ~22 hours over 7 days. Foundation is mostly revisit territory from AUTOCOR — if Beto absorbs fast, Week 1 may compress (needs Day 7 mock ≥85% + Beto shape certification per master_context §7).

---

## 4. Open questions / pending decisions

None blocking. Day 5–6 sandbox availability (DevNet Always-On IOS-XE) is the one thing to confirm before Day 5; fixture fallback exists if it's down.

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

- **Entry point is Day 4 (pyang lab), not Day 1.** Repo bootstrap and Lab 01 pre-stage are done. Beto is doing theory input (Days 2–3) between sessions. First thing next session: confirm theory absorption before launching into pyang — do NOT assume foundation is fresh just because AUTOCOR covered it.
- **Beto has passed AUTOCOR.** Skip basic Python, Git, NETCONF/RESTCONF, YANG concept introductions. He knows these. Week 1 is exam-aligned revisit, not first-time teaching.
- **Lab 01 is already pre-staged.** Plan + 17-task checklist live in `labs/01-foundation/EXERCISES.md` and per-exercise READMEs (`01-pyang`, `02-netconf-getconfig`, `03-restconf-get`). Read those first — don't re-plan what's already planned.
- **First lab approach:** theory first, piece by piece, dry-run by default. Do NOT drop completed code on him — it breaks his learning chain. Write each call together, run it, see output, then the next.
- **All Week 1 labs are read-only.** No `edit-config`, no PUT/PATCH/POST/DELETE. Writes start Week 2.
- **The 59-question dump is the shape reference** for the Day 7 mock. Open it and match texture before generating.
- **DevNet Always-On IOS-XE sandbox** needed for Day 5–6 (NETCONF 830 / RESTCONF 443). Beto verifies host + creds into `.env` by Day 4 evening. If offline → fixture mode (AI generates representative XML/JSON; exam-relevant skill preserved).
- **Local Containerlab is down.** Day 5–6 run against DevNet sandbox or fixtures. Rebuilding a local topology is a Week 2 decision — discuss before choosing.
- **WSL gotcha:** Windows→Linux file copies create `:Zone.Identifier` files. `.gitignore` now catches them, but eyeball `ls -la` / `git status` after copying files in.
- **Old `~/enauto-v2-old-backup`** holds earlier Lab 01/02 work. Do NOT import wholesale — fresh repo by design.

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
