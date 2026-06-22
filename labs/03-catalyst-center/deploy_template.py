import requests, urllib3, json, time, sys
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://10.10.20.185"
auth_url = base_url + "/dna/system/api/v1/auth/token"
task_url = base_url + "/dna/intent/api/v1/task/"
deploy_url = base_url + "/dna/intent/api/v1/template-programmer/template/deploy"
status_url = base_url + "/dna/intent/api/v1/template-programmer/template/deploy/status/"
username, password = "administrator", "Cisco1234!"

template_id = "d90a6f36-8753-41e8-b94c-6ca233009edb"          # the template
versioned_id = "4c162df2-ada4-47ae-b588-89f2fe4efe83"         # v2, the deployable version
device_id = "0a84b333-fedc-4097-9100-ec806f8e1d11"            # sw1

token = requests.post(url=auth_url, auth=(username, password), verify=False).json()["Token"]
headers = {"x-auth-token": token, "Accept": "application/json", "Content-Type": "application/json"}

payload = {
    "templateId": template_id,
    "targetInfo": [
        {
            "type": "MANAGED_DEVICE_UUID",
            "id": device_id,
            "versionedTemplateId": versioned_id,
            "params": {"loop_id": "200", "ip": "10.99.99.99"},
        }
    ],
}

# dry-run by default — write to a shared sandbox switch only on explicit --apply
apply = "--apply" in sys.argv
if not apply:
    print("[DRY-RUN] payload that WOULD be sent (pass --apply to deploy):")
    print(payload)
    sys.exit(0)

deploy = requests.post(url=deploy_url, headers=headers, json=payload, verify=False).json()
print(deploy)

# deploy returns a deploymentId (often wrapped in a message string) — extract it,
# then poll the dedicated deploy-status endpoint (NOT /task/)
raw = deploy.get("deploymentId") or deploy.get("response", "")
deployment_id = raw.split(":")[-1].strip() if ":" in str(raw) else raw

deadline = time.time() + 60
while time.time() < deadline:
    st = requests.get(url=status_url + deployment_id, headers=headers, verify=False).json()
    print(st)
    status = st.get("status") or st.get("devices", [{}])[0].get("status")
    if status in ("SUCCESS", "FAILURE"):
        break
    time.sleep(2)
else:
    raise RuntimeError("deploy status timeout")