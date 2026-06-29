import requests
import urllib3
 
# ── Disable self-signed cert warnings (lab only!) ──────────────
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# ── Connection Details ─────────────────────────────────────────
BASE_URL = "https://10.10.20.90"
USERNAME = "admin"
PASSWORD = "C1sco12345"
 
# ── Step 1: Authenticate (get JSESSIONID cookie) ──────────────
session = requests.Session()
 
login_response = session.post(
    f"{BASE_URL}/j_security_check",
    data={                              # form-encoded, NOT json=
        "j_username": USERNAME,
        "j_password": PASSWORD
    },
    verify=False
)
 
# Check for successful login
# vManage returns 200 even on failure — check for redirect or body
if b"<html>" in login_response.content:
    raise Exception("Login failed — check credentials")
 
print(f"Session cookie: {session.cookies.get('JSESSIONID')[:20]}...")
 
# ── Step 2: Get XSRF Token (required for write operations) ────
token_response = session.get(
    f"{BASE_URL}/dataservice/client/token",
    verify=False
)
xsrf_token = token_response.text
 
# Add XSRF token to session headers for all future requests
session.headers.update({
    "X-XSRF-TOKEN": xsrf_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
})
 
print(f"XSRF Token: {xsrf_token[:20]}...")
print("Authenticated successfully — session ready for API calls")