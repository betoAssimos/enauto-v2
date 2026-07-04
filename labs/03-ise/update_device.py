import requests
from requests.auth import HTTPBasicAuth
import urllib3
 
# ── Disable self-signed cert warnings (lab only!) ──────────────
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# ── Connection Details ─────────────────────────────────────────
BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"
device_id = "fa116130-77f2-11f1-a602-a22b81bf19b1"  # from your POST's Location header
 
# ── Reusable auth and headers ─────────────────────────────────
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
 
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"          # CRITICAL — ISE defaults to XML!
}

# ── Update an existing NAD — must send the FULL object ────────
update_payload = {
    "NetworkDevice": {
        "id": device_id,
        "name": "Branch-Switch-01-Updated-v4",
        "description": "Updated via automation",
        "authenticationSettings": {
            "radiusSharedSecret": "NewSecret456!",
            "enableKeyWrap": False,
            "dtlsRequired": False,
            "keyInputFormat": "ASCII"
        },
        "profileName": "Cisco",
        "coaPort": 1700,
        "NetworkDeviceIPList": [
            {"ipaddress": "10.10.26.66", "mask": 32}
        ],
        "NetworkDeviceGroupList": [
            "Location#All Locations",
            "Device Type#All Device Types"
        ]
    }
}
 
response = requests.put(
    f"{BASE_URL}/ers/config/networkdevice/{device_id}",
    auth=AUTH,
    headers=HEADERS,
    json=update_payload,
    verify=False
)
if response.status_code == 200:
    print("Device updated:")
    print(response.text)
else:
    print(f"Failed ({response.status_code}): {response.text}")