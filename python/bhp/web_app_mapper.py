#!/usr/bin/env python3

import queue
import threading
import urllib.request
import os
import time

target_url = 'http://localhost/dvwa' # dont add backslash at the end of url
local_directory = '/var/www/html/dvwa/'
filters = ['.jpg', '.html', '.gif', '.css', '.png']
threads = 10

web_paths = queue.Queue()

os.chdir(local_directory)
for r, d, f in os.walk('.'):
	for file in f:
		# constructe remote path
		remote_path = os.path.join(r, file)
		if remote_path.startswith('.'):
			remote_path = remote_path[1:]

		# add only remote path not existing in filters
		if os.path.splitext(file)[1] not in filters:
			web_paths.put(remote_path)

def test_remote():
	time.sleep(1)
	while not web_paths.empty():
		path = web_paths.get()

		url = target_url + path
		print(url)
		continue
		try :

			req = urllib.request.Request(url)

			response  = urllib.request.urlopen(req)

			print('[+] OK [{}] -> {}'.format(response.code, url))
			response.close()
		except urllib.error.URLError as error :
			print('[-] Failed [{}] -> {}'.format(error.code, url))
			pass

def main():

	for i in range(threads):
		print('[*] Spawning thread {}'.format(i))
		t = threading.Thread(target=test_remote)
		t.start()
if __name__ == '__main__':
	main()