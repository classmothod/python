from scapy.all import *

pkts = sniff(iface="wlan0",count=30)
wrpcap("log.pcap", pkts)
