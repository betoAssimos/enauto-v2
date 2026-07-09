# labs/04-operations/sdwan_inventory.py
"""Devices and running versions. GET /dataservice/device"""
from sdwan_auth import get_session, BASE

s = get_session()
devices = s.get(f"{BASE}/dataservice/device").json()["data"]
for d in devices:
    print(d["host-name"], d["device-type"], d["deviceId"], d["uuid"])

ved = s.get(f"{BASE}/dataservice/system/device/vedges?deviceIP=10.10.1.17").json()["data"][0]
for k in ved:
    if "ersion" in k:
        print(k, "=", ved[k])