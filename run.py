#!/usr/bin/env python3
import datetime
from scapy.all import sendp, sniff, UDP

inbound = "wlan0"
outbound = "eth0"

def is_wol(p):
    # Check for WoL packet type
    try:
        ethernet_wol = p.type == 0x0842
    except AttributeError:
        ethernet_wol = False

    # Check UDP packet for WoL ports
    udp_wol = UDP in p and p.dport in [9, 7]

    # Could also check for specific ('ff'*6+MAC*6) in p
    return ethernet_wol or udp_wol

def forward(p):
    p.show()
    sendp(p, iface=outbound)

if __name__ == "__main__":
    print("Starting WoL forwarding")
    sniff(iface=inbound, lfilter=is_wol, prn=forward, store=0)
