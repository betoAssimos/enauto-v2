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
list_of_users = session.get(url=user_url, verify=False).json()
print(list_of_users["data"])