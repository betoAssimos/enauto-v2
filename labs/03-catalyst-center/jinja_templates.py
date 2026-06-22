import requests
import urllib3
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://10.10.20.185"
authentication_url = base_url + "/dna/system/api/v1/auth/token"
client_health_url = base_url + "/dna/intent/api/v1/template-programmer/template"
username = 'administrator'
password = 'Cisco1234!'

authentication_request = requests.post(url=authentication_url, auth=(username, password), verify=False).json()
# authentication_response = authentication_request.json()
my_token = (authentication_request["Token"])

headers = { 
    "x-auth-token": my_token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

template_request = requests.get(url=client_health_url, headers=headers, verify=False).json()
print(template_request)