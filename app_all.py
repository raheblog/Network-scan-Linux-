"""
18:02 | 3 Nov - 2026 \ raheb

"""


import streamlit as st
import psutil
import socket
import subprocess
import ipaddress

st.header("NEtwork scan")
st.title("Network scan - Linux")
st.write(f"This program is open-source and licensed under the **MIT**  License")


interfaces = psutil.net_if_addrs()
interface_stats = psutil.net_if_stats()

result = subprocess.run(
    ["ip", "route"],
    capture_output=True,
    text=True
)
route_lines = result.stdout.splitlines()
for line in route_lines:
    parts = line.split()
    if parts[0] == "default":
        gateway = parts[2]
        device = parts[4]

        st.write("Default Gateway:", gateway)
        st.write("Connected Interface:", device)



st.subheader("Network Routing")
st.code(result.stdout)


st.subheader("Network **Interfaces** ")



for interface, addresses in interfaces.items():
    stats = interface_stats.get(interface)
    status = "🟢 UP" if stats and stats.isup else "🔴 DOWN"

    if interface == "lo":
        interface_type = "Loopback"
    elif interface.startswith(("wl",)):
        interface_type = "Wi-Fi"
    elif interface.startswith(("en","eth")):
        interface_type = "Ethernet"
    elif interface.startswith(("tun","tup")):
        interface_type = "VPN / Tunnel"
    else:
        interface_type = "Unknow"






    with st.expander(f"🌐 {interface} | {interface_type} | {status}"):

        for address in addresses:

            if address.family == socket.AF_INET:
                st.write("IPv4:", address.address)
                st.write("Subnet Mask:", address.netmask)
                st.write("Broadcast:", address.broadcast)

                network = ipaddress.IPv4Interface(
                f"{address.address}/{address.netmask}"
                    )

                st.write("CIDR:", f"/{network.network.prefixlen}") 
                st.write("Network address:", network.network.network_address)
                st.write("Broadcast Address:", network.network.broadcast_address)
    

            elif address.family == socket.AF_INET6:
                st.write("IPv6:", address.address)

            elif address.family == psutil.AF_LINK:
                st.write("MAC Address:", address.address)


        


#DNS server

st.subheader("DNS server")

dns_server = []

with open("/etc/resolv.conf", "r") as file:
    for line in file:
        if line.startswith("nameserver"):
            dns = line.split()[1]
            dns_server.append(dns)

for dns in dns_server:
    st.write("DNS:", dns)



