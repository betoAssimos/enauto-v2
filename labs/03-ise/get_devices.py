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


 
# ── Test: Get all network devices ─────────────────────────────
response = requests.get(
    f"{BASE_URL}/ers/config/networkdevice",
    auth=AUTH,
    headers=HEADERS,
    verify=False
)
print(response.headers.get("Content-Type"))
print(response.text[:300])
response.raise_for_status()
 
result = response.json()["SearchResult"]
print(f"Total devices: {result['total']}")
for device in result["resources"]:
    print(f"  {device['name']} (ID: {device['id']})")