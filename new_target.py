#!/usr/bin/env python3

import subprocess
import pyfiglet
import os

banner = pyfiglet.figlet_format("NOW WE ARE HACKIN")
print(banner)
# Asks user to input the target IP and name
target_ip = input("What is the target's IP: ")
target_name = input("What is the target's name: ")

htb_dir = os.path.expanduser("~/htb")
if os.path.exists(htb_dir):
    print("Beep boop beep boop. ~/htb dir detected...")
else:
    print("Beep boop beep boop. Error. Error. No ~/htb dir detected. Creating directory...")
    subprocess.run(f"mkdir {htb_dir}", shell=True)

# Defines commands (variables)  for a new directory for the target and runs the nmap scan -- feel free to adjust nmap flags and location of directory 
make_dir = f"mkdir ~/htb/{target_name}"
ping_ip = f"ping -c 3 {target_ip}"
nmap_scan = f"nmap -sV -sC -p- {target_ip} -oN ~/htb/{target_name}/{target_name}_nmap.txt"

# pings target to ensure connection
print(f"Pinging {target_ip}")
run_ping_ip = subprocess.run(ping_ip, shell=True)

# If statement to ping the ip to ensure a connection
if run_ping_ip.returncode == 0:
    
    # If able to ping the ip
    print(f"Making a new directory in /htb called {target_name}...")
    run_make_dir = subprocess.run(make_dir, shell=True, capture_output=True, text=True)
    
    print(f"Scanning the {target_ip} IP Address...")
    run_nmap_scan = subprocess.run(nmap_scan, shell=True, capture_output=True, text=True)

    print("Adding target to the hosts file...")
    add_hosts = f"echo '{target_ip} {target_name}.htb' | sudo tee -a /etc/hosts" 
    run_add_hosts = subprocess.run(add_hosts, shell=True)
    
    print("Happy Hacking!")
else:
    # unable to ping ip
    print(f"Unable to ping {target_ip}, check your VPN connection...")




