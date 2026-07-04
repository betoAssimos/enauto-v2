import requests
from rich import print

merakikey = "ADD_YOUR_KEY_HERE"
base = "https://api.meraki.com/api/v1"
headers = {"Authorization": f"Bearer {merakikey}"}

# --- resolve org_id (guard included) ---
orgs = requests.get(f"{base}/organizations", headers=headers).json()
org_id = None
for org in orgs:
    if org["name"] == "DevNet-rU90PkMW1mpL":
        org_id = org["id"]
        break
if org_id is None:
    raise SystemExit("org not found")

# --- paginated fetch ---
url = f"{base}/organizations/{org_id}/networks"
params = { "perPage": 10 }   # perPage; pick a small value to force multiple pages
all_networks = []

while url:
    resp = requests.get(url=url, headers=headers, params=params)
    all_networks.extend(resp.json())

    # requests parses the Link header for you:
    next_link = resp.links.get("next")     # → {'url': '...', 'rel': 'next'} or None
    url = next_link["url"] if next_link else None
    params = {}   # think: is perPage still needed in the next URL?

print(len(all_networks))
print(all_networks)