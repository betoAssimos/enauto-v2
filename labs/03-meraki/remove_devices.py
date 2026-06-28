# remove_device.py — UNTESTED reference (no live/reserved Meraki sandbox available)
# Endpoint: POST /networks/{networkId}/devices/remove  → unclaims device from network
# Verify against a reserved sandbox before trusting.

import requests
from rich import print

merakikey = "ADD_YOUR_KEY_HERE"
org_url = "https://api.meraki.com/api/v1/organizations"

headers = {
    "Authorization": f"Bearer {merakikey}",
    "Content-Type": "application/json"
}

orgs_response = requests.get(url=org_url, headers=headers).json()
org_id = None
for org in orgs_response:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]
        break
if org_id is None:
    raise SystemExit("org not found")

network_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"

network_response = requests.get(url=network_url, headers=headers).json()
network_id = None
for network in network_response:
    if network["name"] == "DevNet Sandbox ALWAYS ON":
        network_id = network["id"]
        break
if network_id is None:
    raise SystemExit("network not found")


remove_url = f"https://api.meraki.com/api/v1/networks/{network_id}/devices/remove"

payload = {"serial": "Q2MD-BHHS-5FDL"}

remove_response = requests.post(url=remove_url, headers=headers, json=payload)
print(remove_response)