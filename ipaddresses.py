# Fetch, store, and count IP addresses
import ipaddress

set1 = set() #set to store subnets or ips from the file
totalips = 0 #initial value for total ips
allips = set() #set to store all ip addresses (extracted from subnets)

fileread = open("ips.txt","r") #read file named ips.txt

#read line by line and append to the list set1
#Since the data type is set, all the duplicate values will automatically be removed
for ips in fileread:
    set1.add(ips.strip())   #strip the \n from each line end
    
for ip in set1: #take subnets and extract them and append them to allips and count total number of ips
    net4 = ipaddress.ip_network(ip)
    #totalips = totalips + net4.num_addresses
    for ip in net4:
        allips.add(ip)
        
totalips = allips.__len__()
    
print("total number of IP addresses:" + str(totalips))

