# labs/04-operations/sdwan_swim_install.py
"""Install an image on a device partition (no activate, no reboot).
POST /dataservice/device/action/install — dry-run default, --apply to execute."""
import sys
from sdwan_auth import get_session, BASE

DEVICE_IP = "10.10.1.17"    # deviceId field from sdwan_inventory.py (system IP)
DEVICE_UUID = "dac3e7f5-b48f-d29b-0685-d3bb4b2ea991"  # uuid field from sdwan_inventory.py
VERSION = "20.9.2"

payload = {
    "action": "install",
    "input": {"version": VERSION, "versionType": "vmanage", "reboot": False, "vEdgeVPN": 0, "vSmartVPN": 0, "sync": True},
    "devices": [{"deviceIP": DEVICE_IP, "deviceId": DEVICE_UUID}],
    "deviceType": "vedge",
}

s = get_session()

if "--apply" not in sys.argv:
    print("DRY-RUN, would POST:")
    print(payload)
    sys.exit(0)

resp = s.post(f"{BASE}/dataservice/device/action/install", json=payload)
print(resp.status_code, resp.text[:300])