#!/usr/bin/env python3
# updated : 01-15-2019

import zipfile
import os
import argparse

does_file_exists = lambda file_path: True if os.path.isfile(file_path) else False

if __name__ == "__main__":

    zip_file = None
    wordlist = None
    passwords = list()

    # get command line arguement
    parser = argparse.ArgumentParser(description="zip file cracker")
    parser.add_argument("-z", "--zip", nargs=1, required=True, help="zip file")
    parser.add_argument(
        "-w", "--wordlist", nargs=1, required=True, help="wordlist file"
    )

    args = parser.parse_args()
    zip_file = args.zip[0]
    wordlist = args.wordlist[0]

    # check args validity
    if does_file_exists(zip_file):
        head, tail = os.path.splitext(zip_file)
        if tail != ".zip":
            print("not a zip file : {}".format(zip_file))
            exit()
    else:
        print("zip file not found: {}".format(zip_file))
        exit()

    if does_file_exists(wordlist):
        with open(wordlist, "r") as file:
            for line in file:
                passwords.append(line.rstrip("\n"))
    else:
        print("wordlist not found : {}".format(wordlist))
        exit()

    # crack the password with passwords list
    zipObj = zipfile.ZipFile(zip_file)

    for password in passwords:
        try:
            print("trying password : {}".format(password))
            zipObj.extractall(pwd=password.encode(), path=os.path.split(zip_file)[0])
            print("N PASSWORD FOUND : {}".format(password))
            zipObj.close()
            exit()
        except RuntimeError:
            pass
        except Exception as e:
            raise e

    else:
        # this block execute when not password can unlock the zip file
        print("\nprocess finished.")
        print("zip file : {} is still locked !!".format(zip_file))
        print("all passwords on : {} are invalid !!!".format(wordlist))
        exit()
