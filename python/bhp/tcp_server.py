#!/usr/bin/env python

# include moduels 
import socket
import argparse

# define functions

def handle_client(client_socket):

    while True :
        # recv data from user
        data = client_socket.recv(1024)
        if len(data) == 0 :
            client_socket.close()
            print'connection closed by peer'
            break
        else :
            print ' --> %s' %(data)

        # send data
        s_data = str(raw_input(' type : '))
        if s_data == 'quit' :
            client_socket.close()
            print 'connection closed successfully'
            break
        else:
            client_socket.send(s_data)

def main(host='0.0.0.0', port=444):
    # create socket then listen for incoming connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    # incomming connection
    client, port = server_socket.accept()
    print 'Connected To HOST : %s ON %s' %(port[0], port[1])

    # send & recv
    handle_client(client)

if __name__ == '__main__':
    # parse args from command line
    parser = argparse.ArgumentParser(description='tcp server script with python')
    parser.add_argument('-p','--port', type=int, help='type tcp port number', required=True, nargs=1)
    parser.add_argument('-l', '--listen', metavar='host', required=True, const='0.0.0.0', nargs='?', help="host to listen on, default : 0.0.0.0 ")
    args = parser.parse_args()

    # call main function
    main(args.listen, int(args.port[0]))
