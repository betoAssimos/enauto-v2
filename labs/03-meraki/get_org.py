import requests
from rich import print

merakikey = "a65c3c192dc8b8443a872f52cfe4d3dcb858cd9d"
base_url = "https://api.meraki.com/api/v1/"
org = "organizations"

headers = {
    "X-Cisco-Meraki-API-Key": merakikey
    # headers = {"Authorization": f"Bearer {merakikey}"}
}

response = requests.get(url=base_url + org, headers=headers).json()
print(response)
