import argparse
import sys
from datetime import datetime
from libnmap.parser import NmapParser

targets = []

def parse_nmap_xml(nmap_xml_file, output_file):
    oufile = ""
    f = None
    if len(output_file)>0:
        f = open (output_file, "w")
    nmap_parse = NmapParser.parse_fromfile(nmap_xml_file)
    for host in nmap_parse.hosts:
        for service in host.services:
            targets.append(host.address+","+str(service.port)+","+str(service.state)+","+service.service+","+service.banner)
    data = "IP,Port,State,Service Name,Service Info"
    #print(data)
    if f != None:
        f.write(data+"\n")
    for target in targets:
        #print (target)
        if f != None:
            f.write(target+"\n")
    return targets
