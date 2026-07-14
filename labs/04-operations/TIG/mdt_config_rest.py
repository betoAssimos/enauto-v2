import requests
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print

urllib3.disable_warnings()
URL = "https://172.30.30.11/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data/mdt-subscription=1"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.get(url=URL, headers=headers, auth=HTTPBasicAuth("admin", "admin"), verify=False)
print(response.text)

PAYLOAD = {
  "Cisco-IOS-XE-mdt-cfg:mdt-subscription": {
    "subscription-id": 1,
    "base": {
      "stream": "yang-push",
      "encoding": "encode-kvgpb",
      "period": 500,
      "xpath": "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds"
    },
    "mdt-receivers": [
      {
        "address": "172.30.30.1",
        "port": 57000,
        "protocol": "grpc-tcp"
      }
    ]
  }
}


response = requests.put(url=URL, headers=headers, json=PAYLOAD,auth=HTTPBasicAuth("admin", "admin"), verify=False)
print(response.status_code)