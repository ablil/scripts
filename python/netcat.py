#!/usr/bin/env python3

# import most used modules
import sys
import argparse
import subprocess
import socket
import os

TARGET = None
PORT = None
LISTEN = False
COMMAND = False
UPLOAD = None
EXECUTE = list()

file_exists = lambda filename : True if os.path.isfile(filename) else False

def run_command(cmd):
	'''
	Run command on host machine and return output
	Input value is of type string.
	Output value is of type byte.
	'''
	try:
		output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
	except :
		output = b'Failed to Execute command '
	return output

def execute_from_file(filename):
	'''
	run command from file and retunr ouput.
	Commands are line seperated
	Input value is of type string
	Output value is of type byte.
	'''
	output = b''
	with open(filename, 'r') as file:
		commands = file.read()
		commands = commands.split('\n')
		for cmd in commands :
			output += run_command(cmd)
			output += b'\n'
	return output

def upload_data(client_socket, dst):
	'''
	Read received data and store.
	Input value : client_socket is of type socket.
				dst : upload destiincation is of type str (filename)
	Output value : True if successfull, False if note.
	'''
	with open(dst, 'ba+') as file:
		file_buffer = b''
		while True:
			buffer = client_socket.recv(4096)

			# if not data is received
			if not buffer :
				break
			else :
				file_buffer += buffer

		file.write(file_buffer)

	

def host_handler(target, port):
	'''
	Create socket and connect to host.
	This fucntion is used with target mode
	'''
	host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try :
		host_socket.connect((target, port))
		print("<ctrl + c> to exit")
		while True :
			buffer = str(input())

			# send buffer
			host_socket.send(buffer.encode())

			# recv bufffer
			buffer = host_socket.recv(4096)
			if not len(buffer):
				# close socket if not data is received
				host_socket.close()
				return 0 # exit code
			
			# print buffer
			for line in buffer.decode().split('\n'):
				print(line)

	except ConnectionRefusedError:
		print('Connection Refused')
		return 1 # exit code
	except KeyboardInterrupt:
		host_socket.send('cl0s3'.encode())
		host_socket.close()
		exit()
	except BrokenPipeError:
		pass
	except Exception as e:
		raise e	

def client_handler(port, command=False, upload=False, execute=False):
	'''
	Create socket and listen for incoming connnection from client.
	this function is used with listen mode.
	'''
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.bind(('0.0.0.0', port))
	mysocket.listen(1)

	client_socket, port = mysocket.accept()
	print('Established connection with {}'.format(port))


	if command :
		while True:
			# recv command and run
			buffer = client_socket.recv(4096)

			# close connection wheen recv cl0s3
			if buffer.decode() == 'cl0s3':
				client_socket.close()
				exit()

			print(buffer.decode())

			output = run_command(buffer.decode())

			# send ouput
			client_socket.send(output)

	if upload :
		upload_data(client_socket, upload)
		exit()

	if execute:
		output = execute_from_file(execute)
		client_socket.send(output)
		client_socket.close()
		exit()

def main(target=None, port=None, listen=False, command=False, upload=None, execute=list()):
	''' main function'''
	if target :
		host_handler(target, port)

	if listen :
		client_handler(port, command, upload, execute)
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='netcat in python')

	parser.add_argument('-p', '--port', nargs=1, type=int, metavar='port', help='port number', required=True)

	# listen mode , connect mode
	subgroup1 = parser.add_mutually_exclusive_group(required=True)
	subgroup1.add_argument('-t', '--target', nargs=1, type=str, metavar='ip', help='target ip')
	subgroup1.add_argument('-l', '--listen', action='store_true')

	# options for listen mode
	listen_mode = parser.add_mutually_exclusive_group()
	listen_mode.add_argument('-c', '--command', action='store_true', help='command mode')
	listen_mode.add_argument('-e', '--execute', nargs=1, metavar='file', help='execute cmd from files and send output')
	listen_mode.add_argument('-u', '--upload', nargs=1, metavar='dst', help='receivce data and store it in dst')

	args = parser.parse_args()
	# solve conflict between listen mode and target mode
	if any([args.command, args.execute, args.upload]) and args.target:
		parser.print_help()
		print('Cant have ( -l | -e | -u ) options  with target options')
		exit()

	# set varaible and call main function
	PORT = args.port[0]
	LISTEN = args.listen
	COMMAND = args.command
	if args.target :
		TARGET = args.target[0]
	if args.execute :
		EXECUTE = args.execute[0]
		assert file_exists(EXECUTE)
	if args.upload :
		UPLOAD = args.upload[0]

	main(target=TARGET, port=PORT, listen=LISTEN, command=COMMAND, upload=UPLOAD, execute=EXECUTE)