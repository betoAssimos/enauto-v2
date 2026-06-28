import requests
from rich import print

merakikey = "ADD_MERAKI_KEY_HERE"
base_url = "https://api.meraki.com/api/v1/"
org = "organizations"

headers = {
    "X-Cisco-Meraki-API-Key": merakikey
}

response = requests.get(url=base_url + org, headers=headers).json()
print(response)
