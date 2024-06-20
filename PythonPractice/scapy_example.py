from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from scapy.packet import Raw


def packet_callback(packet):
    # Check if the packet has an IP layer
    print(packet)
    if IP in packet:
        ip_layer = packet[IP]
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        # Check for TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Segment: {tcp_layer.sport} -> {tcp_layer.dport}")
            print(f"Flags: {tcp_layer.flags}")

        # Check for UDP layer
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Datagram: {udp_layer.sport} -> {udp_layer.dport}")

        # Check for ICMP layer
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"ICMP Packet: Type={icmp_layer.type} Code={icmp_layer.code}")

        # Print the raw payload if any
        if packet.haslayer(Raw):
            raw_data = packet[Raw].load
            print(f"Raw Payload: {raw_data}")

    print("\nffffffffffffffffffff")  # Add a newline for better readability


# Sniff packets on the network interface (e.g., "eth0")
# Use the appropriate interface for your system, like "eth0" for Ethernet or "wlan0" for Wi-Fi.
sniff(iface="WiFi", prn=packet_callback, count=10)
