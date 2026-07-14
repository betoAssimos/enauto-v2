# labs/04-operations/sdwan_swim_repo.py
"""Software repository images. GET /dataservice/device/action/software/images"""
from sdwan_auth import get_session, BASE

s = get_session()
repo = s.get(f"{BASE}/dataservice/device/action/software/images?imageType=software").json()["data"]
for img in repo:
    print(img["availableFiles"], "-", img["versionName"])