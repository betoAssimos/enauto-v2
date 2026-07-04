import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://10.10.20.77"
USERNAME = "admin"
PASSWORD = "C1sco12345!"

AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ── 1. Get the Employee identity group ID ─────────────────────
# Expects: 200 + SearchResult (summaries: id, name, description)
response = requests.get(
    f"{BASE_URL}/ers/config/identitygroup",
    auth=AUTH, headers=HEADERS, verify=False
)
groups = response.json()["SearchResult"]["resources"]
employee_group = next((g for g in groups if g["name"] == "Employee"), None)

# ── 2. Create the user ────────────────────────────────────────
# Expects: 201 + Location header with new resource URL; body is EMPTY
user_payload = {
    "InternalUser": {
        "name": "jsmith",
        "description": "John Smith - Engineering",
        "enabled": True,
        "email": "jsmith@example.com",
        "password": "TempP@ss123!",
        "firstName": "John",
        "lastName": "Smith",
        "changePassword": True,
        "identityGroups": employee_group["id"] if employee_group else "",
        "passwordIDStore": "Internal Users"
    }
}

response = requests.post(
    f"{BASE_URL}/ers/config/internaluser",
    auth=AUTH, headers=HEADERS, json=user_payload, verify=False
)
if response.status_code != 201:
    print(f"Create failed ({response.status_code}): {response.text}")
    raise SystemExit(1)

location = response.headers.get("Location")
user_id = location.rstrip("/").split("/")[-1]   # extract real ID from Location
print(f"User created: {location}")

# ── 3. Get ALL users (list endpoint) ─────────────────────────────
# Expects: 200 + SearchResult.resources (summaries only — no email/groups)
# Paginated: size/page params, follow SearchResult.nextPage.href if present
response = requests.get(
    f"{BASE_URL}/ers/config/internaluser",
    auth=AUTH, headers=HEADERS, verify=False
)
if response.status_code == 200:
    users = response.json()["SearchResult"]["resources"]
    print(f"Total users: {response.json()['SearchResult']['total']}")
    for u in users:
        print(f"  {u['name']} — ID: {u['id']}")
else:
    print(f"Get-all failed ({response.status_code}): {response.text}")

# ── 4. Get ONE user by ID (detail endpoint) ──────────────────────
# Expects: 200 + full object wrapped in "InternalUser" key
# On missing ID: 404 with EMPTY body
# user_id comes from the POST's Location header — never hardcode it
response = requests.get(
    f"{BASE_URL}/ers/config/internaluser/{user_id}",
    auth=AUTH, headers=HEADERS, verify=False
)
if response.status_code == 200:
    user = response.json()["InternalUser"]
    print(f"Username: {user['name']}, Enabled: {user['enabled']}, Email: {user.get('email', 'N/A')}")
else:
    print(f"Get-by-id failed ({response.status_code}): {response.text}")

# ── 5. Get the user by its REAL ID ────────────────────────────
response = requests.get(
    f"{BASE_URL}/ers/config/internaluser/{user_id}",
    auth=AUTH, headers=HEADERS, verify=False
)
if response.status_code == 200:
    user = response.json()["InternalUser"]
    print(f"Username: {user['name']}, Enabled: {user['enabled']}, Email: {user.get('email', 'N/A')}")
else:
    print(f"Get failed ({response.status_code}): {response.text}")

# ── 6. Update (PUT — full object, real ID) ────────────────────
# Expects: 200 + UpdatedFieldsList body; NO Location header
# WARNING: full-replace — omitted fields are silently DELETED
# (proven on networkdevice: snmpsettings wiped, UpdatedFieldsList never mentioned it)
user_payload["InternalUser"]["id"] = user_id
user_payload["InternalUser"]["description"] = "Updated role"

response = requests.put(
    f"{BASE_URL}/ers/config/internaluser/{user_id}",
    auth=AUTH, headers=HEADERS, json=user_payload, verify=False
)
if response.status_code == 200:
    print(f"User updated: {response.text}")
else:
    print(f"Update failed ({response.status_code}): {response.text}")

# ── 7. Delete ─────────────────────────────────────────────────
# Expects: 204 + EMPTY body
response = requests.delete(
    f"{BASE_URL}/ers/config/internaluser/{user_id}",
    auth=AUTH, headers=HEADERS, verify=False
)
if response.status_code == 204:
    print("User deleted.")
else:
    print(f"Delete failed ({response.status_code}): {response.text}")