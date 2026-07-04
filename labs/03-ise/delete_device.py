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

response = requests.delete(
    f"{BASE_URL}/ers/config/networkdevice/{device_id}",
    auth=AUTH,
    headers=HEADERS,
    verify=False
)
if response.status_code == 204:
    print("Device deleted successfully.")
else:
    print(f"Failed ({response.status_code}): {response.text}")