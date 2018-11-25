import ipaddresses
import nmaptocsv
import os
from datetime import datetime
import subprocess

os.mkdir('Nmap_output')
#print(datetime.now())
os.chdir('nmap_output')
#subprocess.call('dir', shell=True)

print('+ Starting Nmap on ' + str(ipaddresses.totalips) + ' IPs')
for ips in ipaddresses.allips:
    nmapcmd = 'nmap -oX ' +"tcp_" + str(ips) + ".xml" +" " + str(ips)
    output=subprocess.check_output(nmapcmd, shell=True)

print('++ Nmap scan completed')
print('+ Creating CSVs')
for root, dirs, filenames in os.walk("."):
    for name in filenames:
        filenameraw, fileext = os.path.splitext(name)
        #print(filenameraw)
        targets = nmaptocsv.parse_nmap_xml(name,filenameraw+".csv")
        print(targets)


