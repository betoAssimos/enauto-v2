"""
import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

auth_url = "https://10.10.20.90/j_security_check"

session = requests.session()


session.post(url=auth_url, data=payload, verify=False)

device_url = "https://10.10.20.90/dataservice/device?site-id=101"

list_of_devices = session.get(url=device_url, verify=False).json()
print(list_of_devices["data"])
"""

"""
import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

auth_url = "https://10.10.20.90/j_security_check"

session = requests.session()


session.post(url=auth_url, data=payload, verify=False)

device_url = "https://10.10.20.90/dataservice/device"

list_of_devices = session.get(url=device_url, verify=False).json()
print(list_of_devices["data"])
"""

import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

auth_url = "https://10.10.20.90/j_security_check"

session = requests.session()


session.post(url=auth_url, data=payload, verify=False)

device_url = "https://10.10.20.90/dataservice/system/device/controllers"

list_of_devices = session.get(url=device_url, verify=False).json()
print(list_of_devices["data"])