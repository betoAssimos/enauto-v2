import requests
import urllib3
from rich import print
import time

urllib3.disable_warnings()

payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

base_url = "https://10.10.20.90"
auth_url = f"{base_url}/j_security_check"

session = requests.session()
session.post(url=auth_url, data=payload, verify=False)

token_url = f"{base_url}/dataservice/client/token"

token = session.get(url=token_url, verify=False).text
session.headers.update({"X-XSRF-TOKEN": token})

# ── Get device health summary ─────────────────────────────────
response = session.get(
    f"{base_url}/dataservice/device/monitor",
    verify=False
)
devices = response.json()["data"]
 
for device in devices:
    print(f"{device.get('host-name', 'N/A'):<25} "
          f"Status: {device.get('status', 'N/A'):<10} "
          f"Reach: {device.get('reachability', 'N/A'):<12} "
          f"CPU: {device.get('cpu-load', 'N/A')}%")
    
# ── Get BFD sessions (shows tunnel health between edges) ──────
system_ip = "10.10.1.1"
 
response = session.get(
    f"{base_url}/dataservice/device/bfd/sessions",
    params={"deviceId": system_ip},
    verify=False
)
bfd_sessions = response.json()["data"]
 
for bfd in bfd_sessions:
    print(f"Peer: {bfd.get('system-ip', 'N/A'):<16} "
          f"State: {bfd.get('state', 'N/A'):<8} "
          f"Color: {bfd.get('local-color', 'N/A'):<15} "
          f"Loss: {bfd.get('loss-percentage', 0)}%")
    
# ── Get OMP routes (SD-WAN overlay routing) ───────────────────
response = session.get(
    f"{base_url}/dataservice/device/omp/routes/received",
    params={"deviceId": system_ip},
    verify=False
)
omp_routes = response.json()["data"]
 
for route in omp_routes[:10]:
    print(f"Prefix: {route.get('prefix', 'N/A'):<20} "
          f"Origin: {route.get('from-peer', 'N/A'):<16} "
          f"Site: {route.get('site-id', 'N/A')}")
    
# ── Get app-route stats (SLA measurements per tunnel) ─────────
response = session.get(
    f"{base_url}/dataservice/device/app-route/statistics",
    params={"deviceId": system_ip},
    verify=False
)
app_stats = response.json()["data"]
 
for stat in app_stats:
    print(f"Remote: {stat.get('remote-system-ip', 'N/A'):<16} "
          f"Color: {stat.get('local-color', 'N/A'):<15} "
          f"Latency: {stat.get('latency', 'N/A'):<8} "
          f"Loss: {stat.get('loss', 'N/A'):<8} "
          f"Jitter: {stat.get('jitter', 'N/A')}")
    
# ── Get active alarms ─────────────────────────────────────────
r = session.get(f"{base_url}/dataservice/alarms/count", verify=False)
print(r.status_code, repr(r.text[:300]))
response = session.post(
    f"{base_url}/dataservice/alarms",
    json={
        "query": {
            "condition": "AND",
            "rules": [
                {
                    "field": "active",
                    "type": "boolean",
                    "value": ["true"],
                    "operator": "equal"
                }
            ]
        }
    },
    verify=False
)
print(response.status_code)
print(repr(response.text[:400]))
alarms = response.json()["data"]
 
for alarm in alarms[:5]:
    print(f"[{alarm.get('severity', 'N/A')}] "
          f"{alarm.get('type', 'N/A')}: "
          f"{alarm.get('message', 'N/A')[:60]} "
          f"— {alarm.get('host-name', 'N/A')}")
    
