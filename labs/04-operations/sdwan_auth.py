# labs/04-operations/sdwan_auth.py
"""Login to vManage: JSESSIONID + XSRF token. Imported by the other scripts."""
import os
import urllib3
import requests
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

BASE = f"https://{os.environ['SDWAN_HOST']}"


def get_session():
    s = requests.Session()
    s.verify = False
    resp = s.post(
        f"{BASE}/j_security_check",
        data={"j_username": os.environ["SDWAN_USER"], "j_password": os.environ["SDWAN_PASS"]},
    )
    if "<html" in resp.text.lower():          # vManage returns 200 even on bad creds
        raise SystemExit("Auth failed")
    token = s.get(f"{BASE}/dataservice/client/token").text
    s.headers["X-XSRF-TOKEN"] = token         # required on writes
    return s