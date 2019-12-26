#!/usr/bin/env python3
# created : 01-16-2019

import os
import sys

does_path_exists = lambda pathname: True if os.path.exists(pathname) else False
rename2mp3 = lambda src, dest: os.rename(src, dest)

if __name__ == "__main__":
    usage = "usage : python3 mp4tomp3.py /root/Music/"

    if len(sys.argv) != 2:
        print(usage)
        exit()

    if sys.argv[1] in ("-h", "--help"):
        print(usage)
        exit()

    if not does_path_exists(sys.argv[1]):
        print("path not found : {}".format(sys.argv))
        exit()

    for file in os.listdir(sys.argv[1]):

        src = os.path.join(sys.argv[1], file)
        head, tail = os.path.splitext(file)
        dst = os.path.join(sys.argv[1], head + ".mp3")

        if tail == ".mp4":
            print("{} >>> {}".format(file, dst))
            rename2mp3(src, dst)
    exit()
