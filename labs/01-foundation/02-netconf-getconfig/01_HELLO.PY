import os
from ncclient import manager
from dotenv import load_dotenv
# --- Load credentials from environment variables ---
load_dotenv()
HOST = os.getenv("IOS_XE_HOST")
PORT = int(os.getenv("IOS_XE_NETCONF_PORT", 830)) 
USERNAME = os.getenv("IOS_XE_USERNAME")
PASSWORD = os.getenv("IOS_XE_PASSWORD")

print(f"HOST={HOST!r} PORT={PORT!r} USER={USERNAME!r} PASS_set={PASSWORD is not None}")

def main():
    # --- Establish NETCONF session ---
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False,
        look_for_keys=False,
        allow_agent=False,
        device_params={"name": "iosxe"},
    ) as m:
        print(f"NETCONF session established with {HOST}.")
        # --- Send <hello> message and print server capabilities ---
        print("Server capabilities:")
        for cap in m.server_capabilities:
            print(cap)

if __name__ == "__main__":    main()