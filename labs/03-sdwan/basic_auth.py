import requests
import urllib3

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

auth_url = "https://10.10.20.90/j_security_check"

session = requests.session()


auth_request = session.post(url=auth_url, data=payload, verify=False)
print(auth_request)