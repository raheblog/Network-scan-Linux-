<div align="center">

# 🐧 Linux Network Analyzer

### A Simple & Interactive Network Information Dashboard for Linux

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Platform](https://img.shields.io/badge/Platform-Linux-yellow?logo=linux&logoColor=white)](https://www.kernel.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Understand your Linux network configuration without digging through complicated terminal outputs.**

</div>

---

## 📌 About The Project

**Linux Network Analyzer** is a Python-based application designed to collect, analyze, and display network configuration information on Linux systems through a clean and interactive web dashboard.

Instead of manually checking multiple terminal commands, users can access important network information in one place.

The project focuses on making Linux network configuration easier to understand, inspect, and export.

## ✨ Features

- **Network Interface Detection** – Identify available network interfaces.
- **Interface Status** – Display whether interfaces are UP or DOWN.
- **Interface Classification** – Identify Wi-Fi, Ethernet, Loopback, and VPN/Tunnel interfaces.
- **IP Information** – Display IPv4 and IPv6 addresses.
- **MAC Address** – Retrieve hardware addresses.
- **Subnet Analysis** – Calculate CIDR, Network Address, and Broadcast Address.
- **Default Gateway** – Detect the system's default gateway and connected interface.
- **DNS Information** – Display configured DNS server addresses.
- **Network Dashboard** – Show total, active, and inactive interfaces.
- **Refresh** – Update network information on demand.
- **Export Reports** – Download network interface information in CSV and TXT formats.

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| Psutil | Network interface information |
| Pandas | CSV data processing |
| Socket | Network address information |
| IPaddress | IP and subnet calculations |
| Subprocess | Linux network command execution |

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd linux-network-analyzer
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
python -m pip install streamlit psutil pandas
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 📊 Project Structure

```text
Linux-Network-Analyzer/
│
├── app.py
├── README.md
├── LICENSE
└── .venv/
```

## 🎯 Project Goals

This project was created to:

- Improve practical Python programming skills.
- Explore Linux networking and system information.
- Build a useful tool with a graphical interface.
- Practice working with Python libraries and Linux commands.
- Make network configuration information more accessible.

## 🔮 Future Development

Potential improvements for future versions:

- More advanced network interface classification.
- Improved network configuration reporting.
- Better dashboard design and user experience.
- Additional export formats.
- Improved error handling and compatibility.

## 🤖 Development Note

This project was developed by **Raheb**, with assistance from AI tools during the development process.

AI was used as a supporting tool for learning, problem-solving, debugging, and code improvement. The project itself is a human-led programming effort, with its development direction, decisions, implementation, and testing guided by the developer.

**AI-assisted development does not mean an AI-generated project.**

## 👨‍💻 Author

**Raheb**

Linux Enthusiast | Python Developer | Technology Explorer

- Website: https://raheblog.ir
- GitHub: https://github.com/YOUR_USERNAME

---

<div align="center">

**Built with Python & curiosity.**

⭐ If you find this project useful, consider giving it a star!

</div>
