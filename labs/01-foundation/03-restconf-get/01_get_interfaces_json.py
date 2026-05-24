import os
import requests
import urllib3
from dotenv import load_dotenv
import json

load_dotenv()
HOST = os.getenv("IOS_XE_HOST")
USERNAME = os.getenv("IOS_XE_USERNAME")
PASSWORD = os.getenv("IOS_XE_PASSWORD")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"
    headers = {"Accept": "application/yang-data+json"}
    response = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD), verify=False)
    print(f"HTTP status code: {response.status_code}")
    data = response.json()
    with open("labs/01-foundation/03-restconf-get/output/interfaces.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()