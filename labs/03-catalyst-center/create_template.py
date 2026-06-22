import requests, urllib3
from rich import print
import json, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://10.10.20.185"
auth_url = base_url + "/dna/system/api/v1/auth/token"
project_id = "2c72f459-0ed3-4e55-8307-d181033e29e3"
task_url = base_url + "/dna/intent/api/v1/task/"
create_url = base_url + f"/dna/intent/api/v1/template-programmer/project/{project_id}/template"
version_url = base_url + f"/dna/intent/api/v1/template-programmer/template/version"
username, password = "administrator", "Cisco1234!"

token = requests.post(url=auth_url, auth=(username, password), verify=False).json()["Token"]
headers = {"x-auth-token": token, "Accept": "application/json", "Content-Type": "application/json"}

payload = {
    "name": "loopback-test-3",
    "projectId": project_id,
    "softwareType": "IOS-XE",
    "deviceTypes": [{"productFamily": "Switches and Hubs"}],
    "templateContent": "interface Loopback{{ loop_id }}\n ip address {{ ip }} 255.255.255.255",
    "language": "JINJA",
    "templateParams": [
        {"parameterName": "loop_id", "dataType": "STRING", "required": True, "order": 3},
        {"parameterName": "ip", "dataType": "STRING", "required": True, "order": 2},
    ],
}

resp = requests.post(url=create_url, headers=headers, json=payload, verify=False).json()
task_id = resp["response"]["taskId"]

deadline = time.time() + 60
template_id = None
while time.time() < deadline:
    tr = requests.get(url=task_url + task_id, headers=headers, verify=False).json()["response"]
    print(tr)                     # raw once — confirm where templateId lives
    if tr.get("isError"):
        raise RuntimeError(tr.get("failureReason") or tr.get("progress"))
    if tr.get("endTime"):         # task done
        raw = tr["data"]
        try:
            template_id = json.loads(raw)["templateId"]
        except (json.JSONDecodeError, TypeError):
            template_id = raw
        break
    time.sleep(2)
else:
    raise RuntimeError("create task timeout")

print(f"templateId: {template_id}")

commit = requests.post(url=version_url, headers=headers,
                       json={"templateId": template_id, "comments": "beto v1"},
                       verify=False).json()

commit_task = commit["response"]["taskId"]

details_url = base_url + f"/dna/intent/api/v1/template-programmer/template/{template_id}"
details = requests.get(url=details_url, headers=headers, verify=False).json()
print(details)

deadline = time.time() + 60
versioned_id = None
while time.time() < deadline:
    tr = requests.get(url=task_url + commit_task, headers=headers, verify=False).json()["response"]
    print(tr)
    if tr.get("isError"):
        raise RuntimeError(tr.get("failureReason") or tr.get("progress"))
    if tr.get("endTime"):
        raw = tr["data"]
        try:
            versioned_id = json.loads(raw)["templateVersion"]
        except (json.JSONDecodeError, TypeError):
            versioned_id = raw
        break
    time.sleep(2)
else:
    raise RuntimeError("commit task timeout")

print(f"versionedTemplateId: {versioned_id}")