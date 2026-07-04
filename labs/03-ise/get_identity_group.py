import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"

AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
HEADERS = {"Accept": "application/json"}

# ── Paginate identity groups, 5 per page ───────────────────────
url = f"{BASE_URL}/ers/config/identitygroup?size=5&page=1"
page_num = 1
all_groups = []

while url:
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=False)
    if response.status_code != 200:
        print(f"Failed ({response.status_code}): {response.text}")
        break

    result = response.json()["SearchResult"]
    print(f"— Page {page_num}: {len(result['resources'])} of {result['total']} total —")
    for group in result["resources"]:
        print(f"  {group['name']}")
        all_groups.append(group)

    next_page = result.get("nextPage")
    url = next_page["href"] if next_page else None
    page_num += 1

print(f"\nCollected {len(all_groups)} groups across {page_num - 1} page(s)")