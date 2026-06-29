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

# ── Create a VPN feature template ────────────────────────────
vpn_template = {
    "templateName": "Branch-VPN10-Service",
    "templateDescription": "Service VPN 10 for branch LAN",
    "templateType": "vpn-vedge",
    "deviceType": ["vedge-C8000V"],
    "templateMinVersion": "15.0.0",
    "templateDefinition": {
        "vpn-id": {
            "vipObjectType": "object",
            "vipType": "constant",
            "vipValue": 10
        },
        "name": {
            "vipObjectType": "object",
            "vipType": "constant",
            "vipValue": "Branch-LAN"
        },
        "dns": [{
            "dns-addr": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "8.8.8.8"
            },
            "role": {
                "vipObjectType": "object",
                "vipType": "constant",
                "vipValue": "primary"
            }
        }]
    },
    "factoryDefault": False
}
 
response = session.post(
    f"{base_url}/dataservice/template/feature",
    json=vpn_template,
    verify=False
)
response.raise_for_status()
template_id = response.json()["templateId"]
print(f"Feature template created: {template_id}")

# ── Create a device template combining feature templates ──────
device_template = {
    "templateName": "Branch-cEdge-Full",
    "templateDescription": "Complete branch cEdge configuration",
    "deviceType": "vedge-C8000V",
    "configType": "template",         # "template" = feature-based
    "generalTemplates": [
        {
            "templateId": "<system-feature-template-id>",
            "templateType": "cisco_system"
        },
        {
            "templateId": "<vpn0-feature-template-id>",
            "templateType": "cisco_vpn",
            "subTemplates": [
                {
                    "templateId": "<wan-interface-template-id>",
                    "templateType": "cisco_vpn_interface"
                }
            ]
        },
        {
            "templateId": "<vpn10-feature-template-id>",
            "templateType": "cisco_vpn",
            "subTemplates": [
                {
                    "templateId": "<lan-interface-template-id>",
                    "templateType": "cisco_vpn_interface"
                }
            ]
        },
        {
            "templateId": "<vpn512-feature-template-id>",
            "templateType": "cisco_vpn"
        }
    ],
    "policyId": "",
    "featureTemplateUidRange": []
}
 
response = session.post(
    f"{base_url}/dataservice/template/device/feature",
    json=device_template,
    verify=False
)
response.raise_for_status()
device_template_id = response.json()["templateId"]
print(f"Device template created: {device_template_id}")