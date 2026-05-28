#!/usr/bin/env python3
import requests, urllib3
import argparse, json, os, sys
from dotenv import load_dotenv
# --- Load credentials from environment variables ---
load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.getenv("IOS_XE_HOST")
PORT = os.getenv("IOS_XE_RESTCONF_PORT", "443")
USER = os.getenv("IOS_XE_USERNAME")
PASS = os.getenv("IOS_XE_PASSWORD")

IFACE = "Loopback200"
BASE_URL = f"https://{HOST}:{PORT}/restconf/data"
AUTH = (USER, PASS)
HEADERS = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

IFACE_URL = f"{BASE_URL}/ietf-interfaces:interfaces/interface={IFACE}"

PAYLOAD = {"ietf-interfaces:interface": {
    "name": IFACE,
    "description": "ENAUTO 2.3 RESTCONF lab",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {"address": [{"ip": "20.201.201.1",
                                  "netmask": "255.255.255.0"}]}}}

def session():
    s = requests.Session()
    s.auth = (USER, PASS); s.headers.update(HEADERS); s.verify = False
    return s

def create(s, apply):
    print(f"[create] PUT {IFACE_URL}")
    print(json.dumps(PAYLOAD, indent=2))
    if not apply:
        print("[dry-run] not sent. re-run with --apply.\n"); return
    r = s.put(IFACE_URL, data=json.dumps(PAYLOAD))
    print(f"[create] -> {r.status_code}  (201=created, 204=replaced)")
    if r.text: print(r.text)

def verify(s):
    print(f"[verify] GET {IFACE_URL}")
    r = s.get(IFACE_URL)
    print(f"[verify] -> {r.status_code}  (200=present, 404=absent)")
    if r.text: print(r.text)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="send to device (default: dry-run)")
    args = p.parse_args()
    if not all([HOST, USER, PASS]):
        sys.exit("missing env: IOS_XE_HOST / IOS_XE_USERNAME / IOS_XE_PASSWORD")
    s = session()
    create(s, args.apply)
    if args.apply:
        verify(s)

if __name__ == "__main__":
    main()