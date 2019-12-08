#!/usr/bin/env python3

'''
simple ARP packet sniffer.
Should run as Root
'''

from scapy.all import *


def callback(packet):
	print(packet.summary())
	
def sniffer():

	try:
		sniff(filter='arp', prn=callback)
	except KeyboardInterrupt:
		pass

def main():
	sniffer()

if __name__ == '__main__':
	print("arp sniffer")
	main()