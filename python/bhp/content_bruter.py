#!/usr/bin/env python3

import urllib.request
import queue
import time
import threading

target_url = 'http://example.com'
wordlist_file = 'all.txt'
threads = 50
user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
resume = None # resume wordlist bruteforcing from this word

def build_wordlist(wordlist_file):
	'''
	build queue object lis from wordlis file
	'''

	words = queue.Queue()
	found_resume = False

	print("[*] Reading {} ...".format(wordlist_file))
	with open(wordlist_file, 'rb') as f:
		raw_words = f.readlines()

		for word in raw_words :
			
			word = word.rstrip()

			# check if we gonna resume from  a word build the entire list
			if resume is not None:
				
				if found_resume:
					words.put(word.decode())
				else:
					if word == resume:
						print('[+] Resuming wordlist from {}'.format(word.decode()))
			else :
				words.put(word.decode())

	return words


def dir_brute(words_queue, extensions=None):

	time.sleep(1)

	while not words_queue.empty():

		attempt = words_queue.get()
		

		url = '{}/{}'.format(target_url, attempt)
		try:
			header = dict()
			header['User-Agent'] = user_agent
			req = urllib.request.Request(url, headers=header)
			response = urllib.request.urlopen(req)
			
			if len(response.read()):
				print("[+] [{}] => {}".format(response.code, url))
		except urllib.error.URLError as e:
		
			if hasattr(e, 'code') and e.code != 404:
				print('[?] [{}] => {}'.format(e.code, url))
			pass

def main():

	words = build_wordlist(wordlist_file)

	for i in range(threads):
		print('[*] Spawning Thread {} ...'.format(i))
		t = threading.Thread(target=dir_brute, args=(words, ))
		t.start()

if __name__ == '__main__':
	main()


