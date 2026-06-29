import requests
import urllib3
from rich import print
import time

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

base_url = "https://10.10.20.90"
auth_url = f"{base_url}/j_security_check"

session = requests.session()
session.post(url=auth_url, data=payload, verify=False)

token_url = f"{base_url}/dataservice/client/token"

token_response = session.get(url=token_url, verify=False)
token = token_response.text

# ── Before attaching, get the variables the template needs ────
template_id = "<device-template-id>"
 
response = session.get(
    f"{base_url}/dataservice/template/device/config/input",
    params={"templateId": template_id},
    verify=False
)
input_schema = response.json()
 
# This tells you what variables need values per device
print("Required variables:")
for column in input_schema.get("header", {}).get("columns", []):
    print(f"  {column['property']}: {column.get('title', '')}")

# ── Attach template to one or more devices ────────────────────
attach_payload = {
    "deviceTemplateList": [
        {
            "templateId": template_id,
            "device": [
                {
                    "csv-status": "complete",
                    "csv-deviceId": "C8K-aaaa-bbbb-cccc-dddd",
                    "csv-deviceIP": "10.10.1.1",
                    "csv-host-name": "Branch-cEdge-01",
                    "//system/host-name": "Branch-cEdge-01",
                    "//system/system-ip": "10.10.1.1",
                    "//system/site-id": "100",
                    "/0/vpn0-interface/ip/address": "192.168.1.1/24",
                    "/0/vpn0-interface/tunnel-interface/color": "biz-internet"
                }
            ],
            "isEdited": False,
            "isMasterEdited": False
        }
    ]
}
 
response = session.post(
    f"{base_url}/dataservice/template/device/config/attachfeature",
    json=attach_payload,
    verify=False
)
response.raise_for_status()
action_id = response.json()["id"]
print(f"Template attach initiated: action ID = {action_id}")

def wait_for_action(session, base_url, action_id, timeout=300, interval=10):
    """Poll an SD-WAN action until completion."""
    elapsed = 0
 
    while elapsed < timeout:
        response = session.get(
            f"{base_url}/dataservice/device/action/status/{action_id}",
            verify=False
        )
        status_data = response.json()
 
        summary = status_data.get("summary", {})
        status = summary.get("status", "unknown")
 
        print(f"Status: {status} "
              f"(Success: {summary.get('count', {}).get('success', 0)}, "
              f"Failure: {summary.get('count', {}).get('failure', 0)})")
 
        if status in ("done", "Done - Scheduled"):
            return status_data
        if summary.get("count", {}).get("failure", 0) > 0:
            # Check detailed error
            for device in status_data.get("data", []):
                if device.get("statusId") == "failure":
                    print(f"  FAILED: {device.get('host-name')} "
                          f"— {device.get('activity', ['Unknown error'])}")
            return status_data
 
        time.sleep(interval)
        elapsed += interval
 
    raise TimeoutError(f"Action {action_id} did not complete within {timeout}s")
 
result = wait_for_action(session, base_url, action_id)

# ── Detach a device from its template ─────────────────────────
detach_payload = {
    "deviceType": "vedge",
    "devices": [
        {
            "deviceId": "C8K-aaaa-bbbb-cccc-dddd",
            "deviceIP": "10.10.1.1"
        }
    ]
}
 
response = session.post(
    f"{base_url}/dataservice/template/config/device/mode/cli",
    json=detach_payload,
    verify=False
)
action_id = response.json()["id"]
print(f"Detach action: {action_id}")