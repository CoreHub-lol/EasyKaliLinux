# Easy Kali Linux by CoreHub.lol

![License Badge](https://img.shields.io/badge/License-MIT-green)
![Python Version Badge](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform Badge](https://img.shields.io/badge/Platform-Linux-purple)
![Version Badge](https://img.shields.io/badge/Version-1.0%20Stable-red)

**Easy Kali Linux** is a user-friendly terminal-based tool designed to simplify the use of popular penetration testing tools available in Kali Linux. With an easy-to-navigate interface and a set of pre-configured commands, this tool allows both beginners and experienced users to quickly run security audits on networks and websites.

The main goal of this project is to provide simplified access to powerful hacking tools such as Hydra, Nmap, SQLmap, Aircrack-ng, and more.

## Features

- **Hydra Brute Force Tool**: A fast network login cracker.
- **Nmap Network Scanning Tool**: A powerful network discovery and security auditing tool.
- **John the Ripper Password Cracking**: A tool for cracking password hashes.
- **SQLmap SQL Injection Tool**: An automated tool for SQL injection testing.
- **Netcat**: A networking utility used for reading or writing data across network connections.
- **Nikto Web Scanner**: A web server scanner that detects security vulnerabilities.
- **Aircrack-ng**: A suite of tools for WiFi network security testing.
- **Wireshark**: A network protocol analyzer for network troubleshooting and analysis.

## Installation

### Requirements:
- Python 3.8 or later
- Kali Linux or a compatible environment with the tools installed

Clone this repository:

```bash
git clone https://github.com/corehub/easykalilinux.git
cd easykalilinux
```

Install dependencies:

```bash
pip install colorama
pip install termcolor

```

## Usage

1. **Ensure you have root privileges**: The tool requires `sudo` to run certain tools. When you run the tool, you will be asked to enter your sudo password.
   
2. **Run the tool**:

```bash
python3 main.py
```

3. **Choose an option**: You will be presented with a menu where you can choose from various tools (e.g., Hydra, Nmap, SQLmap, etc.).

## Tool Breakdown

### Hydra Brute Force Tool
Hydra is a fast and flexible tool for brute-force password cracking. You can choose from several modules (http-get, ssh, ftp, etc.) and specify the target.

### Nmap Network Scanning Tool
Nmap is a popular tool for network discovery and vulnerability scanning. It can be used to find open ports and discover hosts in a network.

### John the Ripper Password Cracking
John the Ripper is used to crack password hashes. It supports many different hash algorithms and wordlist-based attacks.

### SQLmap SQL Injection Tool
SQLmap automates the process of detecting and exploiting SQL injection vulnerabilities.

### Netcat
Netcat is a versatile networking tool that allows you to read and write data across network connections. It can be used for port scanning, transferring files, and more.

### Nikto Web Scanner
Nikto is a web server scanner that detects various vulnerabilities such as outdated software and security misconfigurations.

### Aircrack-ng
Aircrack-ng is a suite of tools for Wi-Fi network security testing. It supports packet capture, network cracking, and encryption analysis.

### Wireshark
Wireshark is a network protocol analyzer used to capture and analyze the data traveling through your network interfaces.

## Contribution

If you'd like to contribute, please fork the repository and submit a pull request. Ensure that your contributions follow the existing code style and are properly tested.

### Steps to contribute:
1. Fork the repo.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and ethical penetration testing purposes only. The use of this tool for unauthorized access to systems is illegal. Always have explicit permission before testing any network or website.

---

For more information, check out the official website: [CoreHub.lol](https://corehub.lol)
```

