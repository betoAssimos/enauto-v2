# Handover — Current State of the ENAUTO 300-435 Study

**Last updated:** 2026-05-23 (Week 1 Day 7 — Lab 01 complete, 1.0 closed, Day 7 mock shape-vetoed)
**Updated by:** Beto + AI session
**Status:** ✅ Lab 01 fully done (pyang + NETCONF get-config + RESTCONF GET). 1.0 Foundation at 100%. Day 7 mock attempted, verdict **Off** — score not counted, recalibration guidance recorded below. Ready for Week 2 (Device-Level) on Beto's go-ahead.

> **For any new AI session:** Read `master_context.md` first, then this file. Confirm understanding briefly, then wait for Beto's go-ahead before doing anything.

---

## 1. Where we are right now

| Field | Value |
|---|---|
| Current week | **1 (complete)** |
| Current day in week | Day 7 done (mock attempted, shape-vetoed Off). Week 1 labs all complete. |
| Current blueprint domain | 1.0 Foundation — **100% covered and labbed** |
| Current sub-topic | 1.1–1.5 all labbed. Next domain: 2.0 Device-Level (Week 2). |
| Days until ceiling exam date (2026-08-17) | ~86 (note: calendar/day-count offset exists — see §4) |
| Active sandbox reservation | none (Meraki public key always available; first reservation ~Day 24 for Catalyst Center) |
| Weeks completed | 1 / 13 |

---

## 2. Last session — summary

**Session date:** 2026-05-23 (Days 5–7, single sitting)
**Session type:** Week 1 Days 5–6 labs + Day 7 mock
**Outcome:** Lab 01 completed end to end. 1.0 Foundation closed to 100%. Day 7 mock generated and sat; Beto vetoed shape (**Off**), so score does not count. Recalibration notes captured for next mock build.

**What was done:**
- **Day 5 — NETCONF get-config (E1.2.a–d).** `01_hello.py`: ncclient `manager.connect`, logged advertised capabilities, clean close. Read off real datastore support — box advertises `writable-running`, `rollback-on-error`, `validate`, `xpath`, `with-defaults`; **no `:candidate`, no `:startup`.** `02_get_interfaces.py`: `get_config(source="running")` with subtree filters for both IETF (`urn:ietf:params:xml:ns:yang:ietf-interfaces`) and OpenConfig (`http://openconfig.net/yang/interfaces`). Pretty-printed to disk via `xml.dom.minidom.toprettyxml`. Output: `running-interfaces-ietf.xml`, `running-interfaces-openconfig.xml`.
- **Day 6 — RESTCONF GET (E1.3).** `01_get_interfaces_json.py`: `requests.get` to `/restconf/data/ietf-interfaces:interfaces`, `Accept: application/yang-data+json`, HTTP Basic auth, `verify=False`. 200 OK. Parsed with `resp.json()`, saved pretty to `output/interfaces.json`.
- **1.2 note** written by Beto into `notes/01-foundation.md` (datastores, get vs get-config, subtree filter, IETF vs OC structure). Foundation notes now complete.
- **Day 7 mock** — 20Q on 1.0, five-mode rotation attempted. Sat under exam conditions. Score 18/20 raw, **but Beto vetoed shape → Off → score not counted.** See §6 and §11.

**Key technical facts established (real device output, devnetsandboxiosxec9k.cisco.com):**
- Same 12 interfaces pulled three ways (NETCONF/XML IETF, NETCONF/XML OC, RESTCONF/JSON) — model is transport- and encoding-independent. This is the core 1.2–1.4 demonstration.
- **YANG `list` → repeated sibling elements in XML, JSON array of objects in JSON.** Same list, two serializations.
- **OpenConfig** wraps writable leaves in a `<config>` container (config/state twin; `get-config` returns `<config>` only, no `<state>`), adds a `subinterfaces` layer, encodes IPv4 mask as `prefix-length`. **IETF** places leaves bare under `<interface>`, encodes mask as dotted `netmask`. Same fact, different model.
- `Accept` header selects RESTCONF payload format (`+json` / `+xml`); same URL, different encoding.
- RESTCONF JSON top key is module-qualified: `"ietf-interfaces:interfaces"`, then `"interface": [...]` inside.
- `~` is NOT expanded by Python `open()` — use relative paths from repo root or `os.path.expanduser`.
- `.env` needs `load_dotenv()` (python-dotenv is in the locked deps) — `os.getenv` does not read the file by itself.

---

## 3. Next planned step

**Title:** Week 2 — Device-Level Automation (blueprint 2.1, 2.2, 2.3).

Per master_context §7 schedule:
- CBT Nuggets modules: Netmiko · Modern Automation Protocols · NETCONF · RESTCONF.
- silvancodes: 2.0_Device_Level_Deep_Dive.
- No end-of-week mock for Week 2 (next mock is Week 3, 20Q on 2.0).

**Writes begin in Week 2.** Week 1 was read-only by design. Week 2 introduces `edit-config` / RESTCONF PUT/PATCH/POST — dry-run by default per master_context §4, explicit `--apply` to touch the device. **Note for write labs:** this sandbox box has no candidate datastore, so `edit-config` targets `running` directly — no candidate→commit cycle available on this device (the general candidate/commit model is still exam material regardless).

**Compression decision: MERGED.** Beto called the Week 1→2 merge (2026-05-23). Rationale: Lab 01 and `notes/01-foundation.md` are complete — the substantive work — and the only missing compression signal was the Week 1 mock, which was deliberately voided on a shape veto, not failed. No real coverage is skipped. Week 1 is closed; work proceeds directly into Week 2 Device-Level. Note: the standard §7 trigger (mock ≥85% + shape certification) was not formally met; this merge is a deliberate judgment call by Beto, recorded as such.

**Theory input status (Beto, before Week 2 labs):**
- ⏳ CBT Nuggets Netmiko / Modern Automation Protocols / NETCONF / RESTCONF modules — watch.
- ⏳ silvancodes 2.0_Device_Level_Deep_Dive — read.
- ⏳ `notes/02-device.md` — start.

---

## 4. Open questions / pending decisions

- **Calendar vs day-count offset (non-blocking).** Real calendar date is ~1 day ahead of the schedule's "Day N" count (Beto confirmed: "today is day 6 since the start, keep as day 5"). Day numbers in this study are schedule-relative, not literal elapsed days. Days-to-ceiling math should be reconciled against the real calendar if it ever matters for booking. Parked for now.
- ~~**Week 1→2 compression**~~ — DECIDED 2026-05-23: **merged.** See §3.

*Add new entries here as they come up. Each entry: `[DATE] question / decision needed.`*

---

## 5. Sandbox reservations — active and upcoming

| Sandbox | Status | Booked | Expires | Purpose |
|---|---|---|---|---|
| DevNet Always-On IOS-XE | ✅ Verified reachable (NETCONF 830, RESTCONF 443) | n/a | n/a | Used Week 1 Days 5–6; available for Week 2 device labs |
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
| 1 | 1.0 Foundation (20Q) | 18/20 raw — **NOT COUNTED** | **Off** | Shape vetoed. See §11 for full critique. Score void per master_context §8. Rebuild guidance carried to §11 for next mock. |

*Each row added after a mock. Shape verdict = "Right" / "Off" / "Mixed" per master_context §8.*

---

## 7. Weak areas queue (for spaced review)

| Blueprint sub-topic | Why flagged | Last revisited |
|---|---|---|
| 1.3 / 1.4 — JSON/XML namespace→key mapping | Two mock slips (Q11: `xmlns` binds namespace, not datastore; Q14: RESTCONF JSON top key is module-qualified `ietf-interfaces:interfaces` then `interface`). Conceptual understanding sound; mechanical recall of key structure to firm up. | 2026-05-23 |

*Format: `[Blueprint sub-topic] — [why flagged] — [last revisited date]`. Reviewed end of each week and end of each month.*

---

## 8. Blueprint coverage tracker

| Domain | Sub-topics covered | Sub-topics remaining | Coverage % |
|---|---|---|---|
| 1.0 Foundation | 5 / 5 | 0 | **100%** |
| 2.0 Device-Level | 0 / 7 | 7 | 0% |
| 3.0 Controller-Based | 0 / 6 | 6 | 0% |
| 4.0 Operations | 0 / 6 | 6 | 0% |
| 5.0 AI in Automation | 0 / 4 | 4 | 0% |
| **Overall** | **5 / 28** | **23** | **18%** |

*Updated end of each week as sub-topics get touched and labbed.*

---

## 9. Notes for the next AI session

- **Week 1 is fully done.** Lab 01 (pyang, NETCONF get-config, RESTCONF GET) complete and committed. 1.0 at 100%. `notes/01-foundation.md` complete.
- **Entry point is Week 2 — Device-Level (2.1/2.2/2.3).** Theory-first as always; confirm Beto's CBT Nuggets + silvancodes input before labbing.
- **Writes start Week 2.** Dry-run by default, explicit `--apply` for device-touching calls (master_context §4). This sandbox has **no candidate datastore** — `edit-config` targets running directly.
- **Beto has passed AUTOCOR.** Skip basics. He labs by recognition fast; theory walks should be tight, not padded.
- **VERBOSITY: keep it short in labs.** Beto explicitly flagged over-long responses mid-session — "this should be a lab, I'm reading more than building." More code, less prose. Walk one call at a time, run, read output, next. Do not over-explain.
- **Anti-hallucination held to account this session.** Beto correctly flagged one unsupported claim (that the exam probes per-device capability advertisement — it does not; only the general datastore model is exam material). When stating what the exam tests, only assert what's grounded. Flag uncertainty plainly.
- **Mock shape was vetoed Off** — full rebuild guidance in §11. Read it before generating the Week 3 mock.
- **DevNet IOS-XE sandbox** verified reachable both ports. `.env` working (`IOS_XE_HOST`, `IOS_XE_NETCONF_PORT`, `IOS_XE_USERNAME`, `IOS_XE_PASSWORD`), loaded via `load_dotenv()`.
- **WSL gotcha:** Windows→Linux copies create `:Zone.Identifier` files. `.gitignore` catches them; still eyeball `git status` after copying.
- **59-question dump** confirmed as shape reference (multiple choice, frequent choose-two, "refer to the exhibit" + snippet, A–E). Content stale (Meraki v0 etc.) — texture only, never a learning source.
- **Local Containerlab still down.** Week 2 device labs run against DevNet sandbox or fixtures. Rebuild is a separate decision — discuss before choosing.

---

## 10. Session sign-off protocol

At the end of every session, AI updates this file with:

1. New "Last updated" date at top.
2. New entry in "Last session — summary."
3. Updated "Where we are right now" if position changed.
4. Updated "Next planned step."
5. New entries in mock log, weak areas, blueprint tracker as applicable.
6. Bookings updated if a sandbox was reserved or released.
7. Notes for the next AI updated.

Beto reviews the updated handover before closing. If he disagrees, fix it before he leaves. The handover must reflect reality, not aspiration.

---

## 11. Mock recalibration guidance — READ BEFORE BUILDING THE NEXT MOCK

Day 7 mock (1.0, 20Q) was vetoed **Off**. Beto's critique was correct and actionable. The next mock (Week 3, 20Q on 2.0) must fix all of the following. This section exists so calibration time is spent once, here, not re-litigated each mock.

**What went wrong:**

1. **Source material was described in prose, not shown.** Many questions said "the data appeared as..." instead of pasting the actual snippet. master_context §8 point 1 requires real source material *visible in the question* — a YANG tree, JSON/XML fragment, curl/requests snippet, or playbook. This is the exact AUTOCOR failure mode. **Fix: every question shows real code/payload/tree in the body.** We have real device payloads from Lab 01 — use that texture (real interface names, real structure).

2. **Mode labels didn't match mechanics.** A "Code Fill" question offered four pre-written header strings as A–D — that's a quiz, not a fill. **Fix: a real code-fill shows a snippet with an actual blank to complete.** Beto raised building a **lablet mode** — a small real code block with parts to type in — which is closest to the real exam. Add lablet as a rotation mode.

3. **No "choose two" questions.** The 59Q dump is ~1/3 choose-two. Running zero made the texture wrong. **Fix: include a realistic share of choose-two (roughly 1 in 4).**

4. **Answer-letter clustering.** Key was A×4, B×12, C×3, D×1 — 12 B's out of 20 is a tell. **Fix: flatten the answer distribution to roughly uniform across A/B/C/D (and check it before presenting).**

5. **Overall "didn't feel like the real exam."** The combination of the above. The standard is the 59Q dump's texture: scenario + visible artifact + plausible technical distractors.

**Direction (Beto's framing):** calibration should serve what Beto needs to learn, not endless shape-tuning. Bank these five fixes and apply them directly to the next mock build rather than running throwaway calibration rounds. The next mock should both *count* (correct shape) and *target real 2.0 content*.

**Grading note from this session (for the record, score void):** raw 18/20. Two misses (Q11, Q14) were JSON/XML namespace→key mechanics, not conceptual gaps — logged in §7 weak queue.

---

*End of handover. Week 1 complete. Ready for Week 2 (Device-Level) on Beto's signal.*