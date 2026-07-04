import requests
from requests.auth import HTTPBasicAuth
import urllib3

# ── Disable self-signed cert warnings (lab only!) ──────────────
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ── Connection Details ─────────────────────────────────────────
BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"

AUTH = HTTPBasicAuth(USERNAME, PASSWORD)

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ── Get one device by ID ───────────────────────────────────────
DEVICE_ID = "fa116130-77f2-11f1-a602-a22b81bf19b1"

response = requests.get(
    f"{BASE_URL}/ers/config/networkdevice/{DEVICE_ID}",
    auth=AUTH,
    headers=HEADERS,
    verify=False
)

if response.status_code == 200:
    device = response.json()["NetworkDevice"]
    print(f"Name: {device['name']}")
    print(f"Description: {device.get('description')}")
    print(f"IP: {device['NetworkDeviceIPList'][0]['ipaddress']}/{device['NetworkDeviceIPList'][0]['mask']}")
    print(f"Profile: {device.get('profileName')}")
    print(f"SNMP Settings: {device.get('snmpsettings')}")
else:
    print(f"Failed ({response.status_code}): {response.text}")