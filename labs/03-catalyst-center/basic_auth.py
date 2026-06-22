import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

authentication_url = "https://10.10.20.185/dna/system/api/v1/auth/token"
username = 'administrator'
password = 'Cisco1234!'

authentication_request = requests.post(url=authentication_url, auth=(username, password), verify=False).json()
# authentication_response = authentication_request.json()
print(authentication_request["Token"])