import requests
import urllib3
from rich import print
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://10.10.20.185"
authentication_url = base_url + "/dna/system/api/v1/auth/token"
devices_url = base_url + "/dna/intent/api/v1/network-device"
command_runner_url = base_url + "/dna/intent/api/v1/network-device-poller/cli/read-request"
task_url = base_url + "/dna/intent/api/v1/task/"
file_url = base_url + "/dna/intent/api/v1/file/"

username = 'administrator'
password = 'Cisco1234!'

authentication_request = requests.post(url=authentication_url, auth=(username, password), verify=False).json()
my_token = (authentication_request["Token"])

headers = { 
    "x-auth-token": my_token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

devices_response = requests.get(url=devices_url, headers=headers, verify=False).json()
devices_list = devices_response["response"]

device_ids = []
for device in devices_list:
    device_ids.append(device["id"])

payload = {
    "commands": [
        "show ip interface brief", "show version"],
    "deviceUuids": device_ids
}

cli_response = requests.post(url=command_runner_url, headers=headers, json=payload, verify=False).json()
task_id = cli_response["response"]["taskId"]

file_id = None
deadline = time.time() + 60
while time.time() < deadline:
    task_request = requests.get(url=task_url + task_id, headers=headers, verify=False).json()["response"]
    if task_request.get("isError"):
        raise RuntimeError(f"Task {task_id} failed: "f"{task_request.get('failureReason') or task_request.get('progress')}" )
    try:
        file_id = json.loads(task_request["progress"])["fileId"]
        break
    except (KeyError, TypeError, json.JSONDecodeError):
        time.sleep(2)
else:
    raise RuntimeError(f"Task {task_id} did not complete within 60 seconds")

file_request = requests.get(url=file_url + file_id, headers=headers, verify=False).json()
print(file_request)

for output in file_request:
    cmd_success = output["commandResponses"]["SUCCESS"]
    for cmd in cmd_success:
        print("\n")
        print(cmd_success[cmd])