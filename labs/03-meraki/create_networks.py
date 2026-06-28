import requests
from rich import print

merakikey = "ADD_YOUR_KEY_HERE"
org_url = "https://api.meraki.com/api/v1/organizations"

headers = {
    "Authorization": f"Bearer {merakikey}",
    "Content-Type": "application/json"
}

orgs_response = requests.get(url=org_url, headers=headers).json()
for org in orgs_response:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]

networks_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"

payload = {
    "name": "Test Network",
    "productTypes": ["appliance", "switch", "wireless"],
    "timeZone": "America/Los_Angeles",
    "notes": "This is my test network"
}

network_response = requests.post(url=networks_url, headers=headers, json=payload)
print(network_response)