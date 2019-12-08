#!/usr/bin/env python
# updated : 01-14-2019

import re
import sys

def is_mac(mac_address):
	'''
	check if given mac_address is valid by comparing it to user-defined regexp
	'''
	return True if re.fullmatch(r'[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}', mac_address.upper()) else False

if __name__ == '__main__':
	usage = "usage : python3 is_mac.py a4:4e:31:51:8c:dd"

	# add help menu
	if len(sys.argv) == 2 and sys.argv in ('-h', '--help'):
		print(usage)
		exit()
		
	if not ( len(sys.argv) == 2 ):
		print(usage)
	else :
		print(is_mac(sys.argv[1]))
