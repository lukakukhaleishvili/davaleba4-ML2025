from scapy.all import *
import re

def is_tor_over_vpn(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        if packet.haslyer(TCP) or packet.haslayer(UDP):
            dst_port = packet[IP].dport
            src_port = packet[IP].sport


            tor_ports = [9001,9050,9051,443]

            if dst_port in tor_ports or src_port in tor_ports:
                 print(f"[!] Suspicious TOR traffic on port {dst_port} or {src_port}")
                 return True
    return False

def sniff_packets(interface):
    print(f"[+] Starting packet capture on {interface}...")
    sniff(iface=interface, prn=is_tor_over_vpn, store=0)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="TOR over VPN Traffic Detector")
    parser.add_argument("-i", "--interface", default="Wi-Fi", help="Network interface to sniff on (e.g., Wi-Fi)")
    args = parser.parse_args()

    sniff_packets(args.interface)