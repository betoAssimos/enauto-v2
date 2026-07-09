import requests
from rich import print

API_TOKEN = "02ac-e6b706a5-89ad-4fbc-9b34-741f01e5a100"
TESTS_URL = "https://api.thousandeyes.com/v7/tests/http-server"
MY_URL = "https://www.cisco.com"
AGENT_ID = 4589

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "testName": "Florida_Cisco_Test",
    "url": MY_URL,
    "interval": "60",
    "agents": [
        {"agentId": AGENT_ID}
    ]

}

test_request = requests.post(url=TESTS_URL, headers=headers, json=payload)
print(test_request)