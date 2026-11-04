"""
18:02 | 3 Nov - 2026 \ raheb

"""


import streamlit as st
import psutil
import socket
import subprocess
import ipaddress
from datetime import datetime
import pandas as pd

st.header("NEtwork scan")
st.title("Linux Network analyzer")
st.caption(f"Last scan: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"This program is open-source and licensed under the **MIT**  License")


if st.button("🔄 Refresh Network"):
    st.rerun()



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
    elif interface.startswith(("tun","tap")):
        interface_type = "VPN / Tunnel"
    else:
        interface_type = "Unknown"






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



total_interfaces = len(interfaces)

active_interfaces = sum(1 for stats in interface_stats.values() if stats.isup)
inactive_interfaces = total_interfaces - active_interfaces

col1, col2, col3 = st.columns(3)

col1.metric("Total Interfaces", total_interfaces)
col2.metric("Active Interfaces", active_interfaces)
col3.metric("Inactive Interfaces", inactive_interfaces)
    


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



#add Export

st.subheader("Export Network Information")

network_data = []

for interface, addresses in interfaces.items():
    for address in addresses:
        network_data.append({
            "Interface": interface,
            "Address": address.address,
            "Netmask": address.netmask,
            "Broadcast": address.broadcast    
                             
        })

df = pd.DataFrame(network_data)

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label = "📥 Download CSV",
    data = csv_data,
    file_name = "Network_reqort.csv",
    mime = "Text / csv")



# add Export "Text"

text_data = []

text_data.append("LINUX NETWORK ANALYZER REPORT")
text_data.append(f"Scan Time: {datetime.now()}")
text_data.append("=" * 40)


for interface, addresses in interfaces.items():
    stats = interface_stats.get(interface)
    status = "UP" if stats and stats.isup else "DOWN"

    text_data.append(f"\nInterface: {interface}")
    text_data.append(f"status: {status}")

    for address in addresses:
        text_data.append(f"Address: {address.address}")
        text_data.append(f"Netmask: {address.netmask}")
        text_data.append(f"Broadcast: {address.broadcast}")

txt_countent = "\n".join(text_data)

st.download_button(
    label="📄 Download TXT",
    data=txt_countent,
    file_name="Network_report.txt",
    mime = "text / plain"
)




st.write("creat by 'raheb' :) ")
