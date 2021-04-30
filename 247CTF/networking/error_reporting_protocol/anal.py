from scapy.all import *

cap = rdpcap('./error_reporting.pcap')

f = open("aaa.jpg", 'wb')
for i, pkt in enumerate(cap[1:]):
    f.write(bytes(pkt[ICMP].payload))
