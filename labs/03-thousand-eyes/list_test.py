import requests
from rich import print

API_TOKEN = "02ac-e6b706a5-89ad-4fbc-9b34-741f01e5a100"
TESTS_URL = "https://api.thousandeyes.com/v7/tests"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}

test_request = requests.get(url=TESTS_URL, headers=headers).json()
print(test_request)