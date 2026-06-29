import requests, json, urllib3
from rich import print
urllib3.disable_warnings()

base_url = "https://10.10.20.90"

### Getting our JSESSIONID Cookie from the header and parsing the string so we only have the cookie left.
auth_url = "/j_security_check"
auth_payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"}

session = requests.Session()
session.post(url=f"{base_url}{auth_url}", data=auth_payload, verify=False)

user_url = f"{base_url}/dataservice/admin/user"
token_url = f"{base_url}/dataservice/client/token"

token_response = session.get(url=token_url, verify=False)
token = token_response.text

user_payload = {
    "group": ["netadmin"],
    "description": "This is an another example",
    "userName": "john",
    "password": "password1234567!"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-XSRF-TOKEN": token
}

create_user = session.post(url=user_url, json=user_payload, headers=headers, verify=False)
print(create_user.status_code)