import re
import os
import sys

### Load maclist.csv file to get macs to find ###
all_macs = []
csvfile = open('maclist.csv','r')
csvlines = csvfile.readlines()
csvfile.close()
for line in csvlines:
    line = line.strip()
    line = line.split(',')
    all_macs.append(line[0])

### Load bridge-tables.csv file to get mac to port mappings
bridge_tables = {}
csvfile = open('bridge-tables.csv','r')
csvlines = csvfile.readlines()
csvfile.close()
for line in csvlines[1:]:
    line = line.strip()
    line = line.split(',')
    host = line[0]
    mac = line[1]
    port = line[2]
    if not bridge_tables.get(mac):
        bridge_tables[mac] = []
    if [host,mac,port] not in bridge_tables[mac]:
        bridge_tables[mac].append([host,mac,port])


### Create csv file of matches ###
csvoutfile = 'found-mac-addresses.csv'
csvfh = open(csvoutfile,'w')
csvfh.write("Host,MacAddress,Port\n")
for mac in all_macs:
    if bridge_tables.get(mac):
        for record in bridge_tables[mac]:
            csvfh.write("%s,%s,%s\n" % (record[0],record[1],record[2]))
csvfh.close()

