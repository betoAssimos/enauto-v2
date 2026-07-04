import requests
from rich import print

merakikey = "a65c3c192dc8b8443a872f52cfe4d3dcb858cd9d"
org_url = "https://api.meraki.com/api/v1/organizations"

headers = {
    "Authorization": f"Bearer {merakikey}",
    "Content-Type": "application/json"
}

orgs_response = requests.get(url=org_url, headers=headers).json()
org_id = None
for org in orgs_response:
    if org["name"] == "DevNet-rU90PkMW1mpL":
        org_id = org["id"]
        break
if org_id is None:
    raise SystemExit("org not found")

networks_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"

payload = {
    "name": "Test Network",
    "productTypes": ["appliance", "switch", "wireless"],
    "timeZone": "America/Los_Angeles",
    "notes": "This is my test network"
}

network_response = requests.post(url=networks_url, headers=headers, json=payload)
print(network_response)