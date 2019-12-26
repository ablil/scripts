#!/usr/bin/env python3
#####################################################################
# Script Name   : content_bruteforcer.py
# Description   : Check wordlist of names against a domain name
# Arguments     : Domain Name (URL), wordlist
# Date(modifed) : 2019-11-12
# Author        : _ablil
# Email         : ablil@protonmail.com
######################################################################
import urllib.request
import queue
import time
import threading
import sys

################################## Global Variables ####################################
wordlist_file = "/tmp/mytemporary/all.txt"
threads = 50
user_agent = (
    "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"
)
resume = None  # resume wordlist bruteforcing from this word
#######################################################################################


def build_wordlist(wordlist_file):
    """
        Transform Wordlist into Queue Data Object.
	"""

    words = queue.Queue()
    found_resume = False

    print("[*] Reading {} ...".format(wordlist_file))
    with open(wordlist_file, "r") as f:
        raw_words = f.readlines()

        for word in raw_words:

            word = word.rstrip()

            #### change the following code based on your wordlist layout
            foo = word.split(".")
            if len(foo) > 2:
                word = "/".join(foo[: len(foo) - 1])
                word = word + "." + foo[len(foo) - 1]
            ###########################################################

            # Resume building wordlist or Not
            if resume is not None:

                if found_resume:
                    words.put(word)
                else:
                    if word == resume:
                        print("[+] Resuming wordlist from {}".format(word))
            else:
                words.put(word)

    return words


def dir_brute(words_queue, target_url, extensions=None):

    time.sleep(1)

    while not words_queue.empty():

        attempt = words_queue.get()

        url = "{}/{}".format(target_url, attempt)
        try:
            # Send HTTP Request
            header = dict()
            header["User-Agent"] = user_agent
            req = urllib.request.Request(url, headers=header)
            response = urllib.request.urlopen(req)

            if len(response.read()):
                print("[+] [{}] => {}".format(response.code, url))
        except urllib.error.URLError as e:

            if hasattr(e, "code") and e.code != 404:
                print("[?] [{}] => {}".format(e.code, url))
            pass
            print(url)


def usage():
    print(
        """
 Content Brute Forcer
 Usage :python3 content_bruteforcer.py <url> <worldlist>

 Example : python3 content_bruteforcer.py http://example.com wordlist.txt
		"""
    )
    exit()


def main():

    # get args
    if len(sys.argv) != 3:
        usage()
    else:
        target_url = sys.argv[1]
        wordlist_file = sys.argv[2]

    words = build_wordlist(wordlist_file)

    for i in range(threads):
        print("[*] Spawning Thread {} ...".format(i))
        t = threading.Thread(target=dir_brute, args=(words, target_url,))
        t.start()


if __name__ == "__main__":
    main()
