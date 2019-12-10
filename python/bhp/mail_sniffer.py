#!/usr/bin/env python3

from scapy.all import *



### email protocols ###
# These protocol belongs to Application Layer in OSI model

# POP3 : Post Office Protocol (version 3)
pop3 = {
	110: 'default non-encrypted port',
	995: 'encrypted port'
}
# IMAP : Internet Message Access Protocol
imap = {
	143: 'default non-encrypted port',
	993: 'encrypted port'
}
# SMTP : Simple Mail Transfer Protocol
smtp = {
	25: 'default non-encrypted port',
	2525: 'port opened on all SiteGround servers in case port 25 is filtred by ISP',
	465: 'encrypted port'
}
#####################

# packet callback function
def packet_callback(packet):
	print(packet.show())
	
	if packet[TCP].payload:
		mail_packet = str(packet[TCP].payload)
		print(mail_packet)

def main():

	# sniff packt and call callback function
	try:
		sniff(filter='tcp port 110 or tcp port 143 or tcp port 25',
			iface='wlo1',
			count=5,
			prn=packet_callback)
	except KeyboardInterrupt:
		pass

if __name__ == '__main__':
	main()