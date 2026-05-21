# 02-netconf-getconfig — NETCONF read-only operations

**Day:** 5 of Week 1
**Scope:** Blueprint 1.2 (NETCONF half)
**Dependencies:** `ncclient` from `requirements.txt`. DevNet Always-On IOS-XE sandbox or local fixtures.

## NETCONF concept layer (reminder)

NETCONF runs over SSH (port 830 by default). The protocol exchanges XML-encoded RPCs against named datastores (`running`, `candidate`, `startup`). Operations relevant to this lab:

| Operation | What it does | Touches device? |
|---|---|---|
| `<hello>` | Capability advertisement on session open. | No (handshake) |
| `<get>` | Returns running config + operational state. | Read-only |
| `<get-config>` | Returns config from a named datastore. | Read-only |
| `<edit-config>` | Modifies a datastore (merge/replace/create/delete). | **WRITE — not used in Week 1** |
| `<commit>` | Commits candidate → running. | **WRITE — not used in Week 1** |
| `<lock>` / `<unlock>` | Prevents concurrent modification. | State change — not used in Week 1 |

This lab uses **only `<hello>` and `<get-config>`**.

## What `ncclient` is

A Python client library that wraps NETCONF mechanics: SSH transport, capability negotiation, RPC framing, XML parsing. The two objects you'll touch:

- `ncclient.manager.connect(...)` — opens a session, returns a `Manager`.
- `Manager.get_config(source='running', filter=...)` — issues the RPC, returns the response.

## What we'll do on Day 5

**Theory walk first:**
1. NETCONF session lifecycle (TCP → SSH → hello exchange → RPC loop → close).
2. Capability strings — how they encode supported features and YANG models.
3. The structure of an `ncclient` filter (subtree vs xpath, when to use each).
4. Datastore semantics: why `running` for read on IOS-XE (no candidate by default on RESTCONF/NETCONF unless configured).

**Then we build:**
1. `01_hello.py` — connect, dump capabilities to stdout, close. Confirms the connection works.
2. `02_get_interfaces.py` — connect, `get_config` with a subtree filter scoped to interfaces, save XML, close.

**Piece by piece.** No completed script lands first. We write `connect(...)` together, run it, see what it returns, then write the next call.

## Target device

DevNet **Always-On IOS-XE sandbox** (CSR1000v or Catalyst 8000v). To verify before Day 5:

1. Visit https://developer.cisco.com/site/sandbox/ → find "IOS XE on Cat 8kv" or "IOS XE on CSR Latest Code" Always-On entry.
2. Note hostname, NETCONF port (830), credentials.
3. Populate `IOS_XE_HOST`, `IOS_XE_USERNAME`, `IOS_XE_PASSWORD` in `.env`.
4. Sanity-check reachability: `ssh -p 830 <user>@<host>` should connect, then immediately exchange NETCONF hello XML (looks like garbled XML — that's normal, it's the server hello).

If the always-on sandbox is offline: switch to fixture mode. AI generates a representative `running-interfaces.xml` from documentation; the lab parses the fixture instead of live data. The exam-relevant skill (reading and constructing NETCONF payloads) is preserved.

## Output layout

```
02-netconf-getconfig/
├── README.md                          # this file
├── 01_hello.py                        # Day 5: write together
├── 02_get_interfaces.py               # Day 5: write together
├── fixtures/
│   └── (running-interfaces.xml)       # only if sandbox unavailable
└── output/                            # created Day 5
    ├── capabilities.txt
    └── running-interfaces.xml
```

## Read-only enforcement

This lab will not call `edit_config`, `lock`, `unlock`, `commit`, or `discard_changes`. The Manager session is used for reads only. If we later add write paths in Week 2 labs, they will require an explicit `--apply` flag that defaults off.

## Exam payoff

- "Which NETCONF operation retrieves only configuration data?" → `<get-config>`.
- "Which datastore is queried by default on Cisco IOS-XE?" → `running` (no candidate enabled by default).
- "Given this `ncclient` snippet, what does the response contain?" — you'll have read several responses by end of day.
