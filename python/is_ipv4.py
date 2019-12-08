#!/usr/bin/env python
# updated : 01-14-2019

import re
import sys
 
def is_ipv4(ip_address):
    '''
    check if given ip_address is valid or not by comparing it user-defined regexp
    '''

    if not re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_address) :
        return False


    # split ip by dots (.) into parts & check if every part in range from 0 to 255 inclusive
    splited_ip = ip_address.split(".")
    for ip_part in splited_ip:
        if not (int(ip_part) in range(256)):
            return False

    return True


if __name__ == '__main__':
    usage = "usage : python3 is_ipv4.py 192.170.40.93"

    # add help menu
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        print(usage)
        exit()

    if not (len(sys.argv) == 2 ):
        print(usage)
    else :
        print(is_ipv4(sys.argv[1]))

