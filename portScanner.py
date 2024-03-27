import socket
import sys

import termcolor
from termcolor import colored, cprint

def scan(target, ports):
    print(termcolor.colored('\n' + ' Starting Scan For ' + str(target),'red'))
    for port in range(1,ports):
        scan_port(target,port)
def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print(termcolor.colored('[+] Port Opened '+ str(port),'green'))
        sock.close()
    except:
        print(termcolor.colored('[-] Port Closed ' + str(port), 'red'))
        sock.close()

targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))


if',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets",'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(''),ports)
else:
    scan(targets,ports)
