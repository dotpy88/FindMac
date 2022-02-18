from netmiko import ConnectHandler
from dotenv import load_dotenv
import re
import os

load_dotenv()

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.165',
    'username': 'tsmtbs07',
    'password': os.getenv('PASSWORD')
}

cisco_device_2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.187',
    'username': 'tsmtbs07',
    'password': os.getenv('PASSWORD')
}

all_devices = [cisco_device,cisco_device_2]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show mac address-table")
    print(f"\n\n--------- Device {a_device['host']} ---------")
    mac_match = r"(\w{4}\.\w{4}\.\w{4})\s+\w+\s+(\S+)"
    mac_search = re.compile(mac_match,re.I)
    mac_addresses = mac_search.findall(output)
    if mac_addresses:
        print(mac_addresses)
    print("--------- End ---------") 
