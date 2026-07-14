import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()
load_dotenv()

BASE_URL = f"https://{os.environ['IOS_XE_HOST']}/restconf/data"
HEADERS = {"Accept": "application/yang-data+json"}
AUTH = HTTPBasicAuth(os.environ["IOS_XE_USERNAME"], os.environ["IOS_XE_PASSWORD"])


def restconf_get(resource: str) -> dict:
    url = f"{BASE_URL}/{resource}"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    response.raise_for_status()
    return response.json()
