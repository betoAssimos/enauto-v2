import os

from dotenv import load_dotenv
from ncclient import manager
from xml.dom import minidom

load_dotenv()

HOST = os.environ["IOS_XE_HOST"]
PORT = int(os.environ["IOS_XE_NETCONF_PORT"])
USERNAME = os.environ["IOS_XE_USERNAME"]
PASSWORD = os.environ["IOS_XE_PASSWORD"]

NC_FILTER = """
<mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
 <mdt-subscription>
  <subscription-id>1</subscription-id>
 </mdt-subscription>
</mdt-config-data>
"""


def get_mdt_subscription() -> str:
    with manager.connect_ssh(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, hostkey_verify=False) as m:
        response = m.get_config("running", filter=("subtree", NC_FILTER))
        return minidom.parseString(response.data_xml).toprettyxml()


EDIT_TEMPLATE = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
  <mdt-subscription>
   <subscription-id>1</subscription-id>
   <base>
    <period>{period_cs}</period>
   </base>
  </mdt-subscription>
 </mdt-config-data>
</config>"""


def set_mdt_subscription_period(period_cs: int, apply: bool = False) -> str:
    edit_xml = EDIT_TEMPLATE.format(period_cs=period_cs)
    if not apply:
        return f"[dry-run] would send edit-config:\n{edit_xml}"

    with manager.connect_ssh(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, hostkey_verify=False) as m:
        response = m.edit_config(target="running", config=edit_xml)
        return response.xml
