import os
import subprocess

# Function to check if the user has sudo privileges
def sudo_check():
    try:
        subprocess.check_call(['sudo', '-v'], stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("\n[!] Root privileges required. Please provide the password.\n")
        password = input("sudo password: ")
        subprocess.check_call(['sudo', '-v'], input=password.encode(), stderr=subprocess.DEVNULL)

# Main menu with updated ASCII logo and color gradient
def main_menu():
    os.system("clear")
    print("\033[1;35m")
    print(" ________                                __    __            __  __ ")
    print("/        |                              /  |  /  |          /  |/  |")
    print("$$$$$$$$/   ______    _______  __    __ $$ | /$$/   ______  $$ |$$/ ")
    print("$$ |__     /      \\  /       |/  |  /  |$$ |/$$/   /      \\ $$ |/  |")
    print("$$    |    $$$$$$  |/$$$$$$$/ $$ |  $$ |$$  $$<    $$$$$$  |$$ |$$ |")
    print("$$$$$/     /    $$ |$$      \\ $$ |  $$ |$$$$$  \\   /    $$ |$$ |$$ |")
    print("$$ |_____ /$$$$$$$ | $$$$$$  |$$ \\__$$ |$$ |$$  \\ /$$$$$$$ |$$ |$$ |")
    print("$$       |$$    $$ |/     $$/ $$    $$ |$$ | $$  |$$    $$ |$$ |$$ |")
    print("$$$$$$$$/  $$$$$$$/ $$$$$$$/   $$$$$$$ |$$/   $$/  $$$$$$$/ $$/ $$/ ")
    print("                              /  \\__$$ |")
    print("                              $$    $$/")
    print("                               $$$$$$/ \033[0m")
    print("="*50)
    print("\033[1;37m Easy Kali Linux \nBy CoreHub.lol\033[0m")
    print("="*50)

    print("\033[1;32m[1] Hydra Brute Force Tool")
    print("[2] Nmap Network Scanning Tool")
    print("[3] John the Ripper Password Cracking")
    print("[4] SQLmap SQL Injection Tool")
    print("[5] Netcat Tool")
    print("[6] Nikto Web Scanner")
    print("[7] Aircrack-ng Tool")
    print("[8] Wireshark Tool\033[0m")
    print("[0] Exit")
    print("="*50)

    choice = input("Choose an option: ").strip()
    
    if choice == '1':
        hydra_tool()
    elif choice == '2':
        nmap_tool()
    elif choice == '3':
        john_the_ripper_tool()
    elif choice == '4':
        sqlmap_tool()
    elif choice == '5':
        netcat_tool()
    elif choice == '6':
        nikto_tool()
    elif choice == '7':
        aircrack_tool()
    elif choice == '8':
        wireshark_tool()
    elif choice == '0':
        print("\033[1;31mExiting... Goodbye!\033[0m")
        exit()
    else:
        print("\033[1;31mInvalid choice, please try again.\033[0m")
        main_menu()

# Hydra Tool
def hydra_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Hydra Brute Force Tool]\033[0m")
    print("="*50)

    target = input("Enter target (IP/Domain) (e.g. 1.1.1.1 or example.com): ").strip()
    module = input("Enter module (http-get/http-post-form/ssh/ftp/other) (e.g. http-get): ").strip()

    print(f"\nRunning Hydra with the following parameters:\nTarget: {target}\nModule: {module}")
    os.system(f"sudo hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt {module}://{target}")

    input("Press Enter to return to the main menu...")

# Nmap Tool
def nmap_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Nmap Network Scanning Tool]\033[0m")
    print("="*50)

    target = input("Enter target (IP/Domain) (e.g. 192.168.1.1 or example.com): ").strip()
    print("\nStarting Nmap scan...\n")
    os.system(f"sudo nmap -sS -O {target}")

    input("Press Enter to return to the main menu...")

# John the Ripper Tool
def john_the_ripper_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[John the Ripper Password Cracking Tool]\033[0m")
    print("="*50)

    password_file = input("Enter the path to the password file (e.g. /path/to/passwords.txt): ").strip()
    if not os.path.isfile(password_file):
        print(f"\033[1;31m[Error] The file {password_file} does not exist.\033[0m")
        return
    print(f"\nStarting password cracking on {password_file}...\n")
    os.system(f"sudo john {password_file}")

    input("Press Enter to return to the main menu...")

# SQLmap Tool
def sqlmap_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[SQLmap SQL Injection Tool]\033[0m")
    print("="*50)

    url = input("Enter URL (e.g. http://example.com/vulnerable.php?id=1): ").strip()
    if not url:
        print("\033[1;31m[Error] URL cannot be empty.\033[0m")
        return
    print(f"\nStarting SQLmap on {url}...\n")
    os.system(f"sudo sqlmap -u {url} --batch")

    input("Press Enter to return to the main menu...")

# Netcat Tool
def netcat_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Netcat Tool]\033[0m")
    print("="*50)

    ip = input("Enter target IP (e.g. 192.168.1.1): ").strip()
    port = input("Enter target port (e.g. 8080): ").strip()
    print(f"\nStarting Netcat connection to {ip} on port {port}...\n")
    os.system(f"nc {ip} {port}")

    input("Press Enter to return to the main menu...")

# Nikto Tool
def nikto_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Nikto Web Scanner]\033[0m")
    print("="*50)

    target = input("Enter target URL (e.g. http://example.com): ").strip()
    if not target:
        print("\033[1;31m[Error] URL cannot be empty.\033[0m")
        return
    print(f"\nStarting Nikto scan on {target}...\n")
    os.system(f"sudo nikto -h {target}")

    input("Press Enter to return to the main menu...")

# Aircrack-ng Tool
def aircrack_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Aircrack-ng Tool]\033[0m")
    print("="*50)

    print("Example usage: '/home/user/captures/capturefile.cap'\n")
    file = input("Enter path to the capture file (e.g. /path/to/capturefile.cap): ").strip()
    if not os.path.isfile(file):
        print(f"\033[1;31m[Error] The file {file} does not exist.\033[0m")
        return
    print(f"\nStarting Aircrack-ng on {file}...\n")
    os.system(f"sudo aircrack-ng {file}")

    input("Press Enter to return to the main menu...")

# Wireshark Tool
def wireshark_tool():
    os.system("clear")
    print("="*50)
    print("\033[1;35m[Wireshark Tool]\033[0m")
    print("="*50)

    print("Example usage: 'eth0', 'wlan0' (for Ethernet or Wireless)\n")
    interface = input("Enter network interface (e.g. eth0, wlan0): ").strip()
    if not interface:
        print("\033[1;31m[Error] Interface cannot be empty.\033[0m")
        return
    print(f"\nStarting Wireshark capture on {interface}...\n")
    os.system(f"sudo wireshark -i {interface}")

    input("Press Enter to return to the main menu...")

# Main function to start the program
if __name__ == "__main__":
    sudo_check()
    main_menu()
