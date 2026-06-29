import requests
import urllib3
from rich import print
import time

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

base_url = "https://10.10.20.90"
auth_url = f"{base_url}/j_security_check"

session = requests.session()
session.post(url=auth_url, data=payload, verify=False)

token_url = f"{base_url}/dataservice/client/token"

token_response = session.get(url=token_url, verify=False)
token = token_response.text
session.headers.update({"X-XSRF-TOKEN": token})

# ── List all centralized policies ─────────────────────────────
response = session.get(
    f"{base_url}/dataservice/template/policy/vsmart",
    verify=False
)
print(response.status_code)
print(repr(response.text[:300]))
policies = response.json()["data"]
 
for policy in policies:
    print(f"{policy['policyName']:<30} "
          f"Active: {policy.get('isPolicyActivated', False):<6} "
          f"ID: {policy['policyId']}")