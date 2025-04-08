<div align="center">
  <img src="https://www.corehub.lol/logo.png" alt="CoreHub.lol Logo" width="150" />
  <h1>Easy Kali Linux</h1>
  <p>A user-friendly terminal-based tool for penetration testing</p>
  
  <p>
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge" />
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version Badge" />
    <img src="https://img.shields.io/badge/Platform-Linux-purple" alt="Platform Badge" />
    <img src="https://img.shields.io/badge/Version-1.0%20Stable-red" alt="Version Badge" />
  </p>
</div>

## Overview

**Easy Kali Linux** is a user-friendly terminal-based tool designed to simplify the use of popular penetration testing tools available in Kali Linux. With an easy-to-navigate interface and a set of pre-configured commands, this tool allows both beginners and experienced users to quickly run security audits on networks and websites.

The main goal of this project is to provide simplified access to powerful security tools such as Hydra, Nmap, SQLmap, Aircrack-ng, and more.

<div align="center">
  <img src="https://cdn.discordapp.com/attachments/1349801104589852674/1359248735682433225/image.png?ex=67f6ca88&is=67f57908&hm=3a9a5bb37e2912cd9d44fd2f8094b767ebba5bc50d52ae9c1e5befa0af0b8649&?height=300&width=600" alt="Easy Kali Linux Screenshot" />
</div>

## Features

<table>
  <tr>
    <td width="50%">
      <h3>Hydra Brute Force Tool</h3>
      <p>A fast network login cracker for testing password security.</p>
    </td>
    <td width="50%">
      <h3>Nmap Network Scanning</h3>
      <p>Powerful network discovery and security auditing tool.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>John the Ripper</h3>
      <p>Advanced tool for cracking password hashes.</p>
    </td>
    <td width="50%">
      <h3>SQLmap SQL Injection</h3>
      <p>Automated tool for SQL injection vulnerability testing.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>Netcat</h3>
      <p>Versatile networking utility for reading/writing network data.</p>
    </td>
    <td width="50%">
      <h3>Nikto Web Scanner</h3>
      <p>Web server scanner that detects security vulnerabilities.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>Aircrack-ng</h3>
      <p>Suite of tools for WiFi network security assessment.</p>
    </td>
    <td width="50%">
      <h3>Wireshark</h3>
      <p>Network protocol analyzer for troubleshooting and analysis.</p>
    </td>
  </tr>
</table>

## Installation

### Requirements:
- Python 3.8 or later
- Kali Linux or a compatible environment with the tools installed

### Quick Start

1. Clone this repository:

```bash
git clone https://github.com/corehub/easykalilinux.git
cd easykalilinux
markdown project="Easy Kali Linux" file="README.md"
```

2. Install required Python packages:


```shellscript
pip install colorama
pip install termcolor
pip install requests
pip install pyfiglet
pip install tqdm
```

## Usage

1. **Ensure you have root privileges**: The tool requires `sudo` to run certain tools. When you run the tool, you will be asked to enter your sudo password.
2. **Run the tool**:


```shellscript
python3 main.py
```

3. **Choose an option**: You will be presented with a menu where you can choose from various tools.

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
