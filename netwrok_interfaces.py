##Fetch information about the system's architecture (32-bit or 64-bit).
##List Network Interfaces:
import platform
import psutil
import socket

def get_system_architecture():
    return platform.architecture()[0]

def list_network_interfaces():
    print("Network Interfaces:")
    for interface, addrs in psutil.net_if_addrs().items():
        ipv4_addr = "N/A"
        ipv6_addr = "N/A"
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ipv4_addr = addr.address
            elif addr.family == socket.AF_INET6:
                ipv6_addr = addr.address
        print(f"Interface: {interface}, IPv4 Address: {ipv4_addr}, IPv6 Address: {ipv6_addr}")

if __name__ == "__main__":
    architecture = get_system_architecture()
    print("System Architecture:", architecture)
    list_network_interfaces()
