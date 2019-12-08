#!/usr/bin/env python3

'''
simple ssh client script, mimiking ssh on Unix env.
'''
import paramiko
import argparse
import os

key_exists = lambda key_path: True if os.path.isfile(key_path) else False

def command(ssh_obj):
    while True:
        cmd = str(input('$ '))
        if cmd == 'exit':
            break
            # ssh_obj will be closed in main function
        stdin, stdout, stderr, = ssh_obj.exec_command(cmd)
        # print error if there is any
        error = stderr.read()
        if len(error):
            print(error)
            continue # continue because there is not output, the command have failed
        for line in stdout.read().decode().split('\n'):
            print(line)

def connect_password(ssh_obj, server, user, port_numer):
    '''
    connect to ssh object using password
    '''
    # you have three times to type valid password, otherwise the connection is close
    essay = 0
    while essay < 3 :
        try:
            passwd = input('[*] Type password for {} : '.format(user))
            ssh_obj.connect(server, port=port_numer, username=user, password=passwd)
            print('[+] Connection established')
            break
        except paramiko.ssh_exception.AuthenticationException:
            print('[-] Wrong password. Try Again.')
            essay += 1
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("[-] Connect to port 22 : connection refused")
            ssh_obj.close()
            exit()
        except Exception as e:
            raise e
    else:
        print('\n[?] You typed wrong password 3 times')
        print('[*] Closing connection ...')
        ssh_obj.close()
        exit()

    command(ssh_obj)
    ssh_obj.close()
    print('[+] Connection closed')

def connect_key(ssh_obj, server, user, port_numer, pkey_filename):
    '''
    connect to ssh object using private key
    '''

    # get the private key
    pssphrase = None
    essay = 0
    while essay < 3:
        try:
            pssphrase = str(input('[*] Type passphrase for private key : '))
            if not len(pssphrase) :
                pssphrase = None

            privatekey = paramiko.RSAKey.from_private_key_file(PRIVATEKEY, password=pssphrase)
            break
        except Exception as e:
            raise e

    # connect to ssh object
    try:
        ssh_obj.connect(server, port=port_number, username=user, pkey=privatekey, passphrase=pssphrase)
        print('[+] Connection established .')
    except :
        print('[-] Failed to connect ')
        exit()
    finally:
        ssh_obj.close()


if __name__=='__main__':
    whoami = os.environ.get('USER')
    USER = ''
    SERVER = 'localhost'
    PORT = 22
    PRIVATEKEY = None

    # get args from command line
    parser = argparse.ArgumentParser(description='ssh client for Unix')
    parser.add_argument('user', nargs=1, help='username for login', metavar='user')
    parser.add_argument('server', nargs=1, help="server to connect with", metavar='server')
    parser.add_argument('-p', '--port', type=int, nargs=1, help='port', metavar='port', default=[22])
    parser.add_argument('-i',nargs=1, help="private key filename", metavar='pkey')
    args = parser.parse_args()

    # check valid args
    USER = args.user[0]
    SERVER = args.server[0]
    PORT = args.port[0]
    if args.i :
        if not key_exists(args.i[0]):
            print("[-] Private key Not Found")
            exit()

        PRIVATEKEY = args.i[0]


    # create ssh object
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    # automatically add unknown hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    # try connecting with default private key .ssh/id_rsa if available
    if key_exists('/home/' + str(whoami) + '/.ssh/id_rsa'):
        print('[+] Connecting with availabe private key at ~/.ssh/id_rsa')
        print('[*] Type Enter to skip')
        pssphrase = str(input('[*] Type passphrase (~/.ssh/id_rsa) :'))
        if len(pssphrase):
            try:
                privatekey = paramiko.RSAKey.from_private_key_file('/home/' + str(whoami) + '/.ssh/id_rsa' , password=pssphrase)
                client.connect(SERVER, port=PORT, username=USER, pkey=privatekey, passphrase=pssphrase)
                print('[+] Connection established ')
                command(client)
                client.close()
                print('[+] Connection closed')
                exit()
            except paramiko.ssh_exception.SSHException :
                print('[-] Wrong passphrase')
                print('[*] Failed to read private key\n')
            except Exception as e:
                raise e

    # connect using provided private key
    if PRIVATEKEY != None :
        connect_key(client, SERVER, USER, PORT, PRIVATEKEY)
        exit()

    # connect using provided password
    connect_password(client, SERVER, USER, PORT)
    exit()
