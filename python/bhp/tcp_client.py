#!/usr/bin/env python

# import modules
import socket
import argparse

# define functions
def client_handler(client, host, port):
    # connect to socket
    client.connect((host, port))

    while True :
        # send data
        c_data = str(raw_input(" type : "))
        if c_data == 'quit':
            client.close()
            print 'connection closed successfully'
            break
        else :
            client.send(c_data)

        # recv data
        data = client.recv(1024)
        if len(data) == 0:
            print 'connection closed by peer'
            client.close()
            break
        else :
            print ' --> %s' %(data)



def main(host='127.0.0.1', port=444) :
    # create socket
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # send and recv
    client_handler(client_socket, host, port)

if __name__ == '__main__' :
    # parse args from command line
    parser = argparse.ArgumentParser(description='tcp client script with python')
    parser.add_argument('-p', '--port', type=int, nargs=1, required=True, help='port number')
    parser.add_argument('-s', '--server', nargs='?', required=True, help='server ip , defautl : 127.0.0.1 (localhost)', const='127.0.0.1')
    args = parser.parse_args()

    # call main function
    main(args.server, int(args.port[0]))

