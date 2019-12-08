#!/usr/bin/env python3
###############################################################################
# Script Name   : url_inspector.py
# Description   : Check Status of URL, UP/DOWN
# Arguments     : wordlist of URLs, line by line.
# Date(modifed) : 2019-11-12
# Author        : _ablil
# Email         : ablil@protonmail.com
##############################################################################
import sys
import urllib.request
import time
import os

# check if file exists
file_exists = lambda file: True if os.path.isfile(file) else False

def url_inspector(url):
	'''
	check if url is active or not.
	return http code or False
	'''

	try:
		req = urllib.request.Request(url)

		response = urllib.request.urlopen(req)

		return response.code
	except:
		return False


def get_urls(files):
	'''
	read urls from all files and return a list of URLs
	'''
	existing_files = len(files) # number of existing file
	urls_list = list()

	for file in files:
		if not file_exists(file):
			print('[-] File Not Found : {}'.format(file))
			existing_files -= 1
		else :
			print("[*] Reading {}...".format(file))
			with open(file, 'r') as f:
				urls = f.read().split('\n')
				urls = urls[:len(urls) -1 ]

				# add urls to list
				for url in urls :
					urls_list.append(url)

	if not existing_files:
		exit()
	return urls_list


def usage():
	print('''
 URLs Inspector
 Usage : python3 url_inspector.py <urls file>

 Example : python3 url_inspector.py urlslist.lst
		''')
	exit()

def main(url_list):

	active_urls = 0		# number of active url

	print('checking {} URLs ...'.format(len(url_list)))
	time.sleep(1)

	for url in url_list:
		status = url_inspector(url)

		if status == 200 :
			print('[+] ACTIVE ({}) : {}'.format(status, url))
			active_urls += 1
		elif status is False:
			print('[?] Unknown state : {}'.format(url))
		else:
			print('[-] INACTIVE ({}) : {}'.format(status, url))

	print('[+] Found {} Active URL'.format(active_urls))


if __name__ == '__main__':

	if len(sys.argv) < 2:
		usage()

	urls = get_urls(sys.argv[1:])
	time.sleep(1)
	main(urls)
