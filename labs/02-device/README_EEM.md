## EEM applet — on-box automation (blueprint 2.7)

**File:** `eem_cfg_watch.cfg`
**Demonstrates:** Embedded Event Manager applet — event detection (syslog ED) + action, configured and verified live on the local Containerlab IOS-XE box.

### What it does

`CFG-WATCH` triggers on the `%SYS-5-CONFIG_I` syslog (emitted whenever a config session ends) and responds by writing its own syslog marker via `action 1.0 syslog msg`.

### Key mechanics verified live

- **Policy types:** *applet* (config-mode, line-by-line — used here) vs *script policy* (Tcl file, or Python running inside guestshell). Applet chosen: guestshell-inside-vrnetlab nesting support is unverified, and applet covers the blueprint mechanics.
- **Event detectors seen so far:** `syslog` (this lab), `timer` (scheduled tasks, e.g. config backup), `cli`, `none` (manual-only — runs via `event manager run <name>` from exec mode).
- **Action ordering:** action labels (`1.0`, `2.0`, ...) execute in string-sorted order.
- **Loop safety:** the action emits `%HA_EM-6-LOG`, which does not match the `%SYS-5-CONFIG_I` pattern — no self-trigger. A broad pattern (e.g. `"CONFIG"`) would loop. Pattern discipline, not luck.
- **Creation fires it once:** the config session that creates the applet triggers it on exit — registration completes before that session's own CONFIG_I is emitted (confirmed by timestamps, 14 ms apart).
- **Persistent:** re-fires on every subsequent config session, not one-shot.

### Verification commands

```
show event manager policy registered
show logging | include CFG-WATCH|CONFIG_I
```