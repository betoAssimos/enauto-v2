# labs/04-operations/sdwan_swim_status.py
"""Poll a device action. GET /dataservice/device/action/status/{id}"""
import sys
import time
from sdwan_auth import get_session, BASE

ACTION_ID = sys.argv[1]

s = get_session()
while True:
    task = s.get(f"{BASE}/dataservice/device/action/status/{ACTION_ID}").json()
    status = task["summary"]["status"]
    print(status, "-", [d.get("currentActivity") for d in task["data"]])
    if status != "in_progress":
        break
    time.sleep(10)