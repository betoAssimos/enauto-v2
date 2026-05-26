# labs/02-device/02_netconf_show.py
# This script uses ncclient to connect to a Cisco IOS XE device and execute the "show version" command using NETCONF.
import os
from ncclient import manager
from xml.dom import minidom
import argparse
from dotenv import load_dotenv
# --- Load credentials from environment variables ---
load_dotenv()
m = manager.connect(
    host=os.getenv("IOS_XE_HOST"),
    port=int(os.getenv("IOS_XE_NETCONF_PORT", 830)),
    username=os.getenv("IOS_XE_USERNAME"),
    password=os.getenv("IOS_XE_PASSWORD"),
    hostkey_verify=False,
    device_params={"name": "iosxe"},
    timeout=30,
)
print(f"NETCONF session ID {m.session_id}.")
print(f"Connected: {m.connected}")

#full_config = m.get_config(source="running")
#print(full_config.xml[:500])
print("####################################")

filter_xml = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""
interfaces = m.get_config(source="running", filter=filter_xml)
print(minidom.parseString(interfaces.xml).toprettyxml(indent="  ")[:1000])

print(" ── Verify 1──────────────────────────────────────────────────────")
verify = m.get_config(source="running", filter="""
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback200</name>
    </interface>
  </interfaces>
</filter>
""")
print(minidom.parseString(verify.xml).toprettyxml(indent="  "))

#for capability in m.server_capabilities:
#    if "ietf-interfaces" in capability:
#        print(capability)


parser = argparse.ArgumentParser()
parser.add_argument("--apply", action="store_true",
                    help="actually send edit-config; default is dry-run")
args = parser.parse_args()
# ── Create Loopback200 via edit_config ──────────────────────────
new_loopback = """
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface nc:operation="delete">
      <name>Loopback200</name>
      <description>NETCONF Automated</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
        ianaift:softwareLoopback
      </type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>20.200.200.2</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""
if args.apply:
    edit_result = m.edit_config(target="running", config=new_loopback)
    print(f"Config applied: {edit_result.ok}")
else:
    print("DRY-RUN — would send this edit-config payload to target=running:")
    print(new_loopback)
    print("Re-run with --apply to send.")

print("── Verify 2──────────────────────────────────────────────────────")
verify = m.get_config(source="running", filter="""
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback200</name>
    </interface>
  </interfaces>
</filter>
""")
print(minidom.parseString(verify.xml).toprettyxml(indent="  "))
 
# ── Close session ───────────────────────────────────────────────
m.close_session()