import requests
from requests.auth import HTTPBasicAuth
import urllib3
 
# ── Disable self-signed cert warnings (lab only!) ──────────────
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# ── Connection Details ─────────────────────────────────────────
BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"
 
# ── Reusable auth and headers ─────────────────────────────────
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
 
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"          # CRITICAL — ISE defaults to XML!
}

# ── Add a new NAD (Network Access Device) to ISE ─────────────
nad_payload = {
    "NetworkDevice": {
        "name": "Branch-Switch-01",
        "description": "Branch office access switch",
        "authenticationSettings": {
            "radiusSharedSecret": "MyR@diusSecret123",
            "enableKeyWrap": False,
            "dtlsRequired": False,
            "keyInputFormat": "ASCII"
        },
        "snmpsettings": {
            "version": "TWO_C",
            "roCommunity": "public",
            "pollingInterval": 3600,
            "linkTrapQuery": True,
            "macTrapQuery": True
        },
        "profileName": "Cisco",
        "coaPort": 1700,
        "NetworkDeviceIPList": [
            {
                "ipaddress": "10.10.22.66",
                "mask": 32
            }
        ],
        "NetworkDeviceGroupList": [
            "Location#All Locations",
            "Device Type#All Device Types"
        ]
    }
}
 
response = requests.post(
    f"{BASE_URL}/ers/config/networkdevice",
    auth=AUTH,
    headers=HEADERS,
    json=nad_payload,
    verify=False
)
print(response.text)
response.raise_for_status()    # 201 Created
# The Location header contains the new resource URL
new_device_url = response.headers.get("Location")
if response.status_code == 201:
    print(f"Device created: {response.headers.get('Location')}")
else:
    print(f"Failed ({response.status_code}): {response.text}")