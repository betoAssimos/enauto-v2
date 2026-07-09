### Code for SDWAN Reservable Sandbox
import requests, json, urllib3
urllib3.disable_warnings()

base_url = "https://10.10.20.90"

### Getting our JSESSIONID Cookie from the header and parsing the string so we only have the cookie left.
auth_url = "/j_security_check"
auth_payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"}
session = requests.Session()
auth_response = session.post(url=f"{base_url}{auth_url}", data=auth_payload, verify=False)
print(auth_response.headers)
jsessionid = (auth_response.headers["Set-Cookie"].split(";")[0])
# ── Filter by device type ─────────────────────────────────────
# Device types: "vedge", "vsmart", "vbond", "vmanage"
response = session.get(
    f"{base_url}/dataservice/device",
    params={"device-type": "vedge"},    # WAN edge routers
    verify=False
)
vedges = response.json()["data"]
 
# ── Get controllers only ──────────────────────────────────────
response = session.get(
    f"{base_url}/dataservice/system/device/controllers",
    verify=False
)
controllers = response.json()["data"]
 
for ctrl in controllers:
    print(f"{ctrl.get('deviceType'):<12} "
          f"{ctrl.get('host-name', 'N/A'):<20} "
          f"{ctrl.get('system-ip', 'N/A'):<20}"
          f"{ctrl.get('deviceId', 'N/A'):<10} ")