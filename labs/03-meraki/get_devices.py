import requests
from rich import print

merakikey = "a65c3c192dc8b8443a872f52cfe4d3dcb858cd9d"
org_url = "https://api.meraki.com/api/v1/organizations"

headers = {
    "Authorization": f"Bearer {merakikey}"
}

orgs_response = requests.get(url=org_url, headers=headers).json()
org_id = None
for org in orgs_response:
    if org["name"] == "DevNet-rU90PkMW1mpL":
        org_id = org["id"]
        break
if org_id is None:
    raise SystemExit("org not found")

devices_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/devices"

devices_response = requests.get(url=devices_url, headers=headers).json()
for device in devices_response:
    mac_addr = device["mac"]
    serial_number = device["serial"]
    product_type = device["productType"]
    print(f"MAC ADDRESS: {mac_addr}")
    print(f"SERIAL NUMBER: {serial_number}")
    print(f"PRODUCT TYPE: {product_type}")
    print("=================\n")