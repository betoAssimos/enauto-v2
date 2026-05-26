# labs/02-device/01_netmiko_show.py
# This script uses Netmiko to connect to a Cisco IOS XE device and execute the "show ip interface brief" command.
import os
from netmiko import ConnectHandler
from dotenv import load_dotenv
import json
# --- Load credentials from environment variables ---
load_dotenv()
device = {
    "device_type": "cisco_xe",
    "host": os.getenv("IOS_XE_HOST"),
    "username": os.getenv("IOS_XE_USERNAME"),
    "password": os.getenv("IOS_XE_PASSWORD"),
    "port": int(os.getenv("IOS_XE_SSH_PORT", "22")),
}

conn = ConnectHandler(**device)
output = conn.send_command("show ip interface brief", use_textfsm=True)
print(json.dumps(output, indent=2))
conn.disconnect()