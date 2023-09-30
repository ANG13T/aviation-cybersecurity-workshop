class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.CYAN}{bcolors.BOLD}\n     Simulated Avionics CAN Bus Environment{bcolors.ENDC}{bcolors.ENDC}")
print(f"{bcolors.CYAN}Created by Angelina Tsuboi (angelinatsuboi.com){bcolors.ENDC}")
print(f"\n{bcolors.BLUE}ENTER COMMAND > {bcolors.ENDC}", end='')

prefix = "ENTER COMMAND"

command = input()
while command != "shutdown now":
    if command == "nmap 192.168.1.1":
        print(f"\n{bcolors.CYAN}Nmap scan report for {command[5:]}\nHost is up (0.043s latency).\nNot shown: 65532 closed ports\nPORT      STATE    SERVICE\n21/tcp    OPEN       ftp\n23/tcp    OPEN       telnet\n5555/tcp    OPEN       freeciv\n\nNmap done: 1 IP address (1 host up scanned){bcolors.ENDC}")
        prefix = "ENTER COMMAND"

print(f"{bcolors.GREEN}Congratulations! You've successfully downed the drone and completed the challenge.{bcolors.ENDC}")
print(f"{bcolors.CYAN}Flag: DRONE{{XyZ34!@67Ab}}{bcolors.ENDC}")