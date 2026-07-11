from ncclient import manager
from rich import print
from xml.dom import minidom

DEVICE = {
    "host": "172.30.30.11",
    "port": 830, 
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
}

NC_FILTER = """
<mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
 <mdt-subscription>
  <subscription-id>1</subscription-id>
 </mdt-subscription>
</mdt-config-data>
"""

with manager.connect(**DEVICE) as m:
    response = m.get_config("running", filter=("subtree", NC_FILTER))
    xml = minidom.parseString(response.data_xml)
    pretty_result = xml.toprettyxml()
    print(pretty_result)

MY_CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
    <mdt-subscription>
      <subscription-id>1</subscription-id>
      <base>
        <stream>yang-push</stream>
        <encoding>encode-kvgpb</encoding>
        <source-vrf>clab-mgmt</source-vrf>
        <period>500</period>
        <xpath>/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds</xpath>
      </base>
      <mdt-receivers>
        <address>172.30.30.1</address>
        <port>57000</port>
        <protocol>grpc-tcp</protocol>
      </mdt-receivers>
    </mdt-subscription>
  </mdt-config-data>
</config>
"""

with manager.connect(**DEVICE) as m:
    response = m.edit_config(target="running", config=MY_CONFIG, default_operation="merge")
    print(response.xml)