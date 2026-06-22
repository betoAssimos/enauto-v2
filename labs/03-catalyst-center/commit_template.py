import requests, urllib3, json, time
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://10.10.20.185"
auth_url = base_url + "/dna/system/api/v1/auth/token"
task_url = base_url + "/dna/intent/api/v1/task/"
version_url = base_url + "/dna/intent/api/v1/template-programmer/template/version"
username, password = "administrator", "Cisco1234!"

template_id = "d90a6f36-8753-41e8-b94c-6ca233009edb"   # from create_template.py

token = requests.post(url=auth_url, auth=(username, password), verify=False).json()["Token"]
headers = {"x-auth-token": token, "Accept": "application/json", "Content-Type": "application/json"}

# commit -> version (already committed once as v1; re-run makes v2, harmless)
commit = requests.post(url=version_url, headers=headers,
                       json={"templateId": template_id, "comments": "beto v1"},
                       verify=False).json()
print(commit)

# the version id is NOT in the commit response — fetch template details
details_url = base_url + f"/dna/intent/api/v1/template-programmer/template/{template_id}"
details = requests.get(url=details_url, headers=headers, verify=False).json()
print(details)