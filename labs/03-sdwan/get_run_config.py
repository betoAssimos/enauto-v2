import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

base_url = "https://10.10.20.90"
auth_url = f"{base_url}/j_security_check"

session = requests.session()
session.post(url=auth_url, data=payload, verify=False)

# ── Get running config of a device ────────────────────────────
device_id = "C8K-aaaa-bbbb-cccc-dddd"    # UUID, not system-ip
 
response = session.get(
    f"{base_url}/dataservice/device/config",
    params={"deviceId": device_id},
    verify=False
)
 
running_config = response.json()
print(running_config)