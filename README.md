# READ ME
This script is for learning purposes only and to be used on the HackTheBox platform. 

This script will add the ~/htb dir if you do not already have the dir. It will not check for dups at this time. Please adjust if you would like.

This script will add your new target to from htb to the /etc/hosts, add a new folder to the ~/htb dir, and run an nmap scan. The namp scan will be outputted in the new directory.

Usage: 
./new_target.py 
When prompted to add IP, add the IP of the HTB target.
When prompted to add the name of the box, do so. You may have to adjust the /etc/hosts file with the proper name.htb if it changes. I.e. if you are doing the TwoMillion box, and enter TwoMillion as the name, then the /etc/hosts file will have TwoMillion.htb but it is supposed to be 2million.htb to navigate to the site. 

The nmap scan that is being ran is: nmap -sV -sC -p- and you can adjust it if you would like. It is on line 23.

Make sure you are connected to your openvpn or else the script will fail. 
