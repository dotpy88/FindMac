Getting started -

1. pip install -r requirements.txt

2. Rename .env_example to .env and update network device credentials in this file

3. Populate hostlist.csv with ip of switch in first column

4. Run getMacAddresses.py to generate bridge-tables.csv file

5. Populate maclist.csv with mac of hosts to find in first column 

6. Run findMacs.py to generate found-mac-addresses.csv file

7. Results could contain duplicates if a mac address is seen on uplink ports


