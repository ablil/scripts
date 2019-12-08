#!/usr/bin/env python3
import sys
import time
import os

dir_exists = lambda directory : True if os.path.exists(directory) else False

def harvester(directory):
	'''
	return all logs file on directory
	'''
	logs = list()
	try:
		for item in os.walk(directory):
			dirpath, dirnames, filenames = item

			# check every filenames in dirpath
			for file in filenames :
				root, ext = os.path.splitext(file)

				if ext == '.log':
					logs.append(os.path.join(dirpath, file))
	except KeyboardInterrupt :
		print("[*] Aborting ...")
		time.sleep(1)
		return logs
	return logs
	
def usage():
	print(" Logs files Harvester : logs_harvester.py")

	print("\n usage : sudo python3 logs_harvester.py dir1 dir2 dir3 ...\n")
	exit()

def main(dirs):

	directories = list()
	logs = list()

	# check if all directories exists
	for directory in dirs:
		if not dir_exists(directory):
			print("[-] {} Not Found.(Exluded)".format(directory))
		else :
			directories.append(directory)

	if not len(directories):
		print("[-] No directory Exists. Aborting ...")
		exit()

	# walk through directories
	for directory in directories :
		print("[*] Processing {} ...".format(directory))
		logs += harvester(directory)
		time.sleep(1)

	# display logs
	print("[+] Found {} log file".format(len(logs)))
	time.sleep(1)
	for log in logs:
		print("[+] {}".format(log))

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		usage()

	main(sys.argv[1:])
