from scapy.all import *

def arp_display(pkt):
    if pkt[ARP].op == 1:
        return "[*] Requisição: " + pkt[ARP].psrc + " esta perguntando por " + pkt[ARP].pdst
    if pkt[ARP].op == 2:
        return "Resposta: " + pkt[ARP].hwsrc + " Tem o endereço " + pkt[ARP].psrc

print(sniff(prn=arp_display, filter="arp", store=0))
