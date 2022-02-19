from netmiko import ConnectHandler
from dotenv import load_dotenv
import re
import os
import sys

### Load .env file to get password ###
load_dotenv()

### Cisco params used for netmiko package ###
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '',
    'username': 'tsmtbs07',
    'password': os.getenv('PASSWORD')
}

### Load hostlist.csv file to get ip address of switches ###
all_devices = []
csvfile = open('hostlist.csv','r')
csvlines = csvfile.readlines()
csvfile.close()
for line in csvlines:
    line = line.strip()
    line = line.split(',')
    all_devices.append(line[0])

### Iterate through ip addresses and login to each switch.  Append to csvfile is found
csvoutfile = 'bridge-tables.csv'
csvfh = open(csvoutfile,'w')
csvfh.write("Host,MacAddress,Port\n")
for a_device in all_devices:
    cisco_device['host'] = a_device
    net_connect = ConnectHandler(**cisco_device)

    ### Send command to switch for bridge tables
    output = net_connect.send_command("show mac address-table")

    ### Match mac addresses using regex
    mac_match = r"(\w{4}\.\w{4}\.\w{4})\s+\w+\s+(\S+)"
    mac_search = re.compile(mac_match,re.I)
    mac_addresses = mac_search.findall(output)

    ### If macs are found, write them to csvfile
    if mac_addresses:
        for mac in mac_addresses:
            csvfh.write("%s,%s,%s\n" % (cisco_device['host'],mac[0],mac[1]))

csvfh.close()