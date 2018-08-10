from scapy.all import *

pcap = rdpcap("arquivo.pcap")
#pcap[3]
pcap.summary()
pcap[3].summary()
#pcap.show()
pcap[3].show()
#pcap.hexdump()
