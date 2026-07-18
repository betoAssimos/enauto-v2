import requests
from requests.auth import HTTPBasicAuth
import urllib3
 
# ── Disable self-signed cert warnings (lab only!) ──────────────
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# ── Connection Details ─────────────────────────────────────────
BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"

MAC_ADD = "AA:BB:CC:11:22:33"
POLICY_NAME = "NuggetPolicy"
 
# ── Reusable auth and headers ─────────────────────────────────
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
 
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"          # CRITICAL — ISE defaults to XML!
}

# ── Add a new payload to ISE ─────────────
payload = {
    "OperationAdditionalData": {
        "additionalData": [
            {"name": "macAddress", "value": MAC_ADD},
            {"name": "policyName", "value": POLICY_NAME}
        ]
    }
}
 
response = requests.put(
    f"{BASE_URL}/ers/config/ancendpoint/apply",
    auth=AUTH,
    headers=HEADERS,
    json=payload,
    verify=False
)
print(response.text)
response.raise_for_status()    # 201 Created
# The Location header contains the new resource URL
new_device_url = response.headers.get("Location")
if response.status_code == 204:
    print(f"Policy associated: {response.headers.get('Location')}")
else:
    print(f"Failed ({response.status_code}): {response.text}")