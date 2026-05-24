# Lab 01 — Exercises Checklist

Tick each box as the task is completed during Days 4–6. Each task maps to a blueprint sub-topic. Tasks marked **(produce)** result in a committed artifact (script, output, or note section).

## 01-pyang — Day 4

- [X] **E1.1.a** [1.1] Acquire three "interfaces" YANG modules — one OpenConfig, one IETF, one Cisco-native — and place them in `01-pyang/yang-models/`. Note the source URL of each.
- [ ] **E1.1.b** [1.1] In `notes/01-foundation.md`, write a 3-row table comparing the three modules: filename, namespace URI, root container path, one structural difference you observed.
- [X] **E1.5.a** [1.5] Run `pyang -f tree` on each of the three modules. **(produce)** Save the tree output to `01-pyang/output/<flavor>-tree.txt`.
- [ ] **E1.5.b** [1.5] In `notes/01-foundation.md`, list every RFC 8340 tree symbol you encountered (`+--rw`, `+--ro`, `?`, `*`, `[key]`, `+---x`, etc.) and what each means in one line.
- [X] **E1.3.a** [1.3] Run `pyang -f sample-json-skeleton` on the OpenConfig interfaces module. **(produce)** Save to `01-pyang/output/openconfig-interfaces-skeleton.json`. there is no sample-json-skeleton, jtox is used instead.
- [X] **E1.4.a** [1.4] Run `pyang -f sample-xml-skeleton` on the same module. **(produce)** Save to `01-pyang/output/openconfig-interfaces-skeleton.xml`.
- [X] **E1.3.b + E1.4.b** [1.3, 1.4] In `notes/01-foundation.md`, compare the JSON and XML skeletons of the same model side-by-side. Identify three structural differences (namespaces, array vs list syntax, key positioning, etc.).

## 02-netconf-getconfig — Day 5

- [ ] **E1.2.a** [1.2] Verify the DevNet Always-On IOS-XE sandbox is reachable (`ssh` or `nc -zv host 830`). If unavailable, switch to offline-fixture mode.
- [ ] **E1.2.b** [1.2] **(produce)** `02-netconf-getconfig/01_hello.py` — open an `ncclient` Manager session, log the server's advertised capabilities, close cleanly. Read-only by definition.
- [ ] **E1.2.c** [1.2] **(produce)** `02-netconf-getconfig/02_get_interfaces.py` — issue `get_config` against the `running` datastore, filtered to interfaces. Save the returned XML to `02-netconf-getconfig/output/running-interfaces.xml`.
- [ ] **E1.2.d** [1.2] In `notes/01-foundation.md`, write 4 lines on: what `get` vs `get-config` returns, why we used `get-config` here, and what a candidate datastore would change.

## 03-restconf-get — Day 6

- [ ] **E1.2.e** [1.2] **(produce)** `03-restconf-get/01_get_interfaces_json.py` — `requests.get` against the IOS-XE RESTCONF endpoint for interfaces, `Accept: application/yang-data+json`. Save to `03-restconf-get/output/interfaces.json`.
- [ ] **E1.2.f** [1.2] **(produce)** `03-restconf-get/02_get_interfaces_xml.py` — same request, `Accept: application/yang-data+xml`. Save to `03-restconf-get/output/interfaces.xml`.
- [ ] **E1.2.g** [1.2] In `notes/01-foundation.md`, write the operation/method mapping table from memory: NETCONF `get`, `get-config`, `edit-config (merge/replace/create/delete)`, `commit` → RESTCONF HTTP method. Verify against the silvancodes deep-dive.
- [ ] **E1.2.h** [1.2] Compare `02-netconf-getconfig/output/running-interfaces.xml` against `03-restconf-get/output/interfaces.xml`. Note three structural differences (envelope, namespaces, root element).

## End-of-week mock — Day 7

- [ ] **E1.M** 20-question mock on blueprint 1.0. Save to `mocks/section-1/week-01-mock.md`. Score logged. Shape verdict declared (Right / Off / Mixed) per master_context §8.
