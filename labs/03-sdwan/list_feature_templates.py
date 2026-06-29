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

# ── Get all feature templates ─────────────────────────────────
response = session.get(
    f"{base_url}/dataservice/template/feature",
    verify=False
)
feature_templates = response.json()["data"]
 
for ft in feature_templates:
    print(f"{ft['templateName']:<35} "
          f"Type: {ft['templateType']:<20} "
          f"Attached: {ft.get('devicesAttached', 0)}")
    
# ── Get all device templates ──────────────────────────────────
response = session.get(
    f"{base_url}/dataservice/template/device",
    verify=False
)
device_templates = response.json()["data"]
 
for dt in device_templates:
    print(f"{dt['templateName']:<35} "
          f"Model: {dt['deviceType']:<20} "
          f"Attached: {dt.get('devicesAttached', 0)}")