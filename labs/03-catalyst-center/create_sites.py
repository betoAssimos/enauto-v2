import requests
import urllib3
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

authentication_url = "https://10.10.20.185/dna/system/api/v1/auth/token"
site_url = "https://10.10.20.185/dna/intent/api/v1/site"
username = 'administrator'
password = 'Cisco1234!'

authentication_request = requests.post(url=authentication_url, auth=(username, password), verify=False).json()
# authentication_response = authentication_request.json()
my_token = (authentication_request["Token"])

headers = { 
    "x-auth-token": my_token,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

payload = {
    "type": "area",
    "site": {
        "area": {
            "name": "Area 51",
            "parentName": "Global"
        }
    }
}

site_request = requests.post(url=site_url, headers=headers, json=payload, verify=False)
print(site_request.text)