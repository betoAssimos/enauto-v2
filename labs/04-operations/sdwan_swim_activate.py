# labs/04-operations/sdwan_swim_activate.py
"""Activate installed image (changes partition, reboots device).
POST /dataservice/device/action/changepartition — dry-run default, --apply to execute."""
import sys
from sdwan_auth import get_session, BASE

DEVICE_IP = "10.10.1.17"
DEVICE_UUID = "dac3e7f5-b48f-d29b-0685-d3bb4b2ea991"
VERSION = "20.9.2"

payload = {
    "action": "changepartition",
    "devices": [{"deviceIP": DEVICE_IP, "deviceId": DEVICE_UUID, "version": VERSION}],
    "deviceType": "vedge",
}

s = get_session()

if "--apply" not in sys.argv:
    print("DRY-RUN, would POST:")
    print(payload)
    sys.exit(0)

resp = s.post(f"{BASE}/dataservice/device/action/changepartition", json=payload)
print(resp.status_code, resp.text[:300])