#!/usr/bin/env python3
'''
ICMP packets sniffer (needs root privs).
run the script.
open another terminal and ping a host to recevice icmp packet.

when you send udp packet to closed port on server, he will respond with icmp.
It means the host is alive and the port is closed.
If no response , the port is either open or the packet is filtred by firewall.
'''

import socket

if __name__ == '__main__':
	
	sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

	#include ip header
	sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

	# recev buffer of 4096 bytes
	data, addr = sniffer.recvfrom(4096)

	print("recv from : [{}]".format(addr))
	print("data : [{}]".format(data))

	# close socket 
	sniffer.close()