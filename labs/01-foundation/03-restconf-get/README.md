# 03-restconf-get — RESTCONF read-only operations

**Day:** 6 of Week 1
**Scope:** Blueprint 1.2 (RESTCONF half)
**Dependencies:** `requests` from `requirements.txt`. Same sandbox as Lab 02.

## RESTCONF concept layer (reminder)

RESTCONF is a RESTful HTTP/HTTPS interface (port 443 typically) that exposes the same YANG-modeled data NETCONF serves, using HTTP methods instead of XML RPCs. Method mapping:

| RESTCONF method | NETCONF equivalent | Touches device? |
|---|---|---|
| `GET` | `get` / `get-config` | Read-only |
| `POST` | `edit-config (create)` | **WRITE — not used in Week 1** |
| `PUT` | `edit-config (replace)` | **WRITE — not used in Week 1** |
| `PATCH` | `edit-config (merge)` | **WRITE — not used in Week 1** |
| `DELETE` | `edit-config (delete)` | **WRITE — not used in Week 1** |

This lab uses **only `GET`**.

## Headers that matter

| Header | Purpose | Values you'll use |
|---|---|---|
| `Accept` | Tell server what to return. | `application/yang-data+json` or `application/yang-data+xml` |
| `Content-Type` | Tell server what you're sending (writes only). | n/a this lab |
| `Authorization` | HTTP Basic on IOS-XE RESTCONF. | `Basic <base64(user:pass)>` |

The `+yang-data` suffix is the marker that distinguishes RESTCONF media types from generic JSON/XML. The exam tests this directly.

## URL structure

```
https://<host>/restconf/data/<module>:<container>/<list>=<key>
```

For interfaces:

```
https://<host>/restconf/data/ietf-interfaces:interfaces
```

The module prefix (`ietf-interfaces:`) is **mandatory** when the data node is at a module boundary. Forgetting it returns 400.

## What we'll do on Day 6

**Theory walk first:**
1. Why RESTCONF exists alongside NETCONF (HTTP toolchain compatibility, easier curl/Postman testing).
2. The exact URL grammar — `/restconf/data/...` vs `/restconf/operations/...`.
3. How HTTP status codes map to NETCONF errors (200, 204, 400, 404, 409).
4. JSON vs XML response shape for the same data.

**Then we build:**
1. `01_get_interfaces_json.py` — `requests.get` with `Accept: application/yang-data+json`. Pretty-print, save.
2. `02_get_interfaces_xml.py` — same URL, `Accept: application/yang-data+xml`. Save.
3. **Compare** the JSON and XML outputs side-by-side, and compare both against the NETCONF XML from Lab 02. Three different views of the same underlying YANG data.

**Piece by piece.** We write the headers dict, run a request, see the 200, then add the JSON parse, etc.

## Target device

Same as Lab 02 — DevNet Always-On IOS-XE sandbox. Same credentials. Different port (443 instead of 830).

Sanity check on Day 6: `curl -k -u <user>:<pass> -H 'Accept: application/yang-data+json' https://<host>/restconf/data/ietf-interfaces:interfaces` should return 200 with a JSON body.

If sandbox is unavailable: switch to fixture mode. Same approach as Lab 02.

## Output layout

```
03-restconf-get/
├── README.md                          # this file
├── 01_get_interfaces_json.py          # Day 6: write together
├── 02_get_interfaces_xml.py           # Day 6: write together
├── fixtures/
│   ├── (interfaces.json)              # only if sandbox unavailable
│   └── (interfaces.xml)
└── output/                            # created Day 6
    ├── interfaces.json
    └── interfaces.xml
```

## Read-only enforcement

This lab only issues `GET` requests. No `POST`, `PUT`, `PATCH`, or `DELETE`. If we later add write paths in Week 2, they will require an explicit `--apply` flag that defaults off.

## Exam payoff

- "What media type does RESTCONF use for JSON?" → `application/yang-data+json`.
- "Which HTTP method maps to `edit-config (merge)`?" → `PATCH`.
- "Given this RESTCONF URL, identify the YANG module." → straightforward parse.
- "RESTCONF returns 409. What does this mean?" → conflict, typically data-resource-already-exists or operation-not-supported in current state.
