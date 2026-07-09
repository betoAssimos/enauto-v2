import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()  # lab sandboxes use self-signed certs

DNAC = "https://sandboxdnac.cisco.com"

def get_token():
    url = f"{DNAC}/dna/system/api/v1/auth/token"
    resp = requests.post(url,
                         auth=HTTPBasicAuth("devnetuser", "Cisco123!"),
                         verify=False)
    resp.raise_for_status()
    return resp.json()["Token"]

token = get_token()
headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

def get_images():
    url = f"{DNAC}/dna/intent/api/v1/image/importation"
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()["response"]

for img in get_images():
    print(img["name"], img["version"], img["imageUuid"], img.get("isGoldenTagged"))

def tag_golden(image_uuid, family, role="ALL", site="-1"):
    url = f"{DNAC}/dna/intent/api/v1/image/importation/golden"
    payload = {
        "imageId": image_uuid,
        "deviceFamilyIdentifier": family,   # from the device family API
        "deviceRole": role,                 # ALL, ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN
        "siteId": site,                     # "-1" = global
        "taggedGolden": True
    }
    resp = requests.post(url, headers=headers, json=payload, verify=False)
    resp.raise_for_status()
    return resp.json()

# To untag, you'd DELETE the same resource path with the identifiers as query params.

def distribute(device_uuid, image_uuid):
    url = f"{DNAC}/dna/intent/api/v1/image/distribution"
    payload = [{
        "deviceUuid": device_uuid,
        "imageUuid": image_uuid
    }]
    resp = requests.post(url, headers=headers, json=payload, verify=False)
    resp.raise_for_status()
    return resp.json()["response"]["taskId"]   # <-- async: returns a taskId

task_id = distribute("<device-uuid>", "<image-uuid>")

import time

def wait_for_task(task_id, timeout=600):
    url = f"{DNAC}/dna/intent/api/v1/task/{task_id}"
    start = time.time()
    while time.time() - start < timeout:
        resp = requests.get(url, headers=headers, verify=False)
        result = resp.json()["response"]
        if result.get("isError"):
            raise Exception(f"Task failed: {result.get('failureReason')}")
        if result.get("endTime"):           # endTime present => finished
            return result
        time.sleep(5)
    raise TimeoutError("Task did not complete in time")

wait_for_task(task_id)

def activate(device_uuid, image_uuid):
    url = f"{DNAC}/dna/intent/api/v1/image/activation/device"
    payload = [{
        "deviceUuid": device_uuid,
        "imageUuidList": [image_uuid],
        "activateLowerImageVersion": False,
        "distributeIfNeeded": True   # will distribute first if not already staged
    }]
    resp = requests.post(url, headers=headers, json=payload, verify=False)
    resp.raise_for_status()
    return resp.json()["response"]["taskId"]

task_id = activate("<device-uuid>", "<image-uuid>")
wait_for_task(task_id)