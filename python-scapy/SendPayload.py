from scapy.all import *

ip = IP(dst="192.168.53.1")
tcp = TCP(dport=80, flags="S")
raw = Raw(b"Hacking!")
pkt = ip/tcp/raw
sr(pkt)
pkt.show()
