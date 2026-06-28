import requests
from rich import print

merakikey = "ADD_YOUR_KEY_HERE"
base = "https://api.meraki.com/api/v1"

headers = {"Authorization": f"Bearer {merakikey}"}

orgs = requests.get(f"{base}/organizations", headers=headers).json()

org_id = None
for org in orgs:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]
        break
if org_id is None:
    raise SystemExit("org not found")

resp = requests.get(f"{base}/organizations/{org_id}/networks", headers=headers)
print(resp.status_code)
print(resp.json())