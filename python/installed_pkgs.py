#!/usr/bin/env python3

import re
import time

msg = " Unpacking nmap (7.60-1ubuntu5) ... "

def main():

	installed_pkgs = list()
	log_file = '/var/log/apt/term.log'

	print(" Get installed packages on Linux machine from".format(log_file))

	# find pattern
	pattern = re.compile(r'Unpacking (\S+) (\S+)')

	with open(log_file, 'r') as f:

		# read lines from log file
		print("[*] Reading {} ...".format(log_file))
		data = f.read()
		lines = data.split('\n')

		time.sleep(1)

		# parse file
		print("[*] Parsing {} ...".format(log_file))
		for line in lines:
			match = re.findall(pattern, line)

			if len(match):
				installed_pkgs.append(match[0])

	time.sleep(1)
	
	print("[+] Operation Finished.")

	time.sleep(1)

	# display installed packages
	for pkg in installed_pkgs:
		package, version = pkg[0], pkg[1].strip('()')
		print("[+] Package : {} ({})".format(package, version))

	print("[+] total number of packages : {}".format(len(installed_pkgs)).title())

if __name__ == '__main__':
	main()