#!/usr/bin/python3

import requests
import sys
import json
from time import sleep

def usage():
    print("Find MAC Address Vendors")
    print("")
    print("usage: ")
    print(f"\tpython3 {sys.argv[0]} FC:FB:FB:01:FA:24 ...")

def main():
    
    if len(sys.argv) < 2:
        usage()
    else:
        macs = sys.argv[1:]
        for mac in macs:
            sleep(0.5)
            r = requests.get(f"https://api.macvendors.com/{mac}")
            
            try:
                data = r.json()
                if 'errors' in data.keys():
                    print(f"{mac} Not Found")
            except json.decoder.JSONDecodeError:
                # success
                print(f"{mac} {r.text}")
            except Exception as e:
                print(e)


if __name__=='__main__':
    main()
