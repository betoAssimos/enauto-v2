import requests
from rich import print

API_TOKEN = "02ac-e6b706a5-89ad-4fbc-9b34-741f01e5a100"
AGENTS_URL = "https://api.thousandeyes.com/v7/agents"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}

agent_request = requests.get(url=AGENTS_URL, headers=headers).json()
agents = agent_request["agents"]
for agent in agents:
    agent_name = agent["agentName"]
    agent_id = agent["agentId"]
    print(f"{agent_name}: {agent_id}")