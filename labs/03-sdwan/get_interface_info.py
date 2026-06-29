import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

base_url = "https://10.10.20.90"
auth_url = f"{base_url}/j_security_check"

session = requests.session()
session.post(url=auth_url, data=payload, verify=False)

interface_url = f"{base_url}/dataservice/device/interface?deviceId=10.10.1.3"
interface_response = session.get(url=interface_url, verify=False).json()
print(interface_response)