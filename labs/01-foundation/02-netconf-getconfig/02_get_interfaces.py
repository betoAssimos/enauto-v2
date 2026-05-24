import os
from ncclient import manager
from dotenv import load_dotenv
import xml.dom.minidom
# --- Load credentials from environment variables ---
load_dotenv()
HOST = os.getenv("IOS_XE_HOST")
PORT = int(os.getenv("IOS_XE_NETCONF_PORT", 830)) 
USERNAME = os.getenv("IOS_XE_USERNAME")
PASSWORD = os.getenv("IOS_XE_PASSWORD")

def pretty(xml_str):
    return xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")

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
        IETF_FILTER = """
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        """
        OC_FILTER = """
        <interfaces xmlns="http://openconfig.net/yang/interfaces"/>
        """
        ietf = m.get_config(source="running", filter=("subtree", IETF_FILTER))
        with open("labs/01-foundation/02-netconf-getconfig/output/running-interfaces-ietf.xml", "w") as f:
            f.write(pretty(ietf.data_xml))
        oc = m.get_config(source="running", filter=("subtree", OC_FILTER))
        with open("labs/01-foundation/02-netconf-getconfig/output/running-interfaces-openconfig.xml", "w") as f:
            f.write(pretty(oc.data_xml))

if __name__ == "__main__":    main()