#!/usr/bin/env python3

from threading import Thread
import socket

class Proxy2server(Thread):
	def __init__(self, host, port):
		super().__init__()
		self.client = None # socket connect to client
		self.host = host
		self.port = port
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.connect((self.host, self.port))

	def run(self):
		while True:
			data = self.server.recv(4096)
			if data :
				# forwad it
				print("[{}] <- {}".format(self.port, data.decode()))
				self.client.sendall(data)

class Client2proxy(Thread):
	def __init__(self, host, port):
		super().__init__()
		self.server = None # socket connect t to sever 
		self.host = host
		self.port = port
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((self.host, self.port))
		sock.listen(1)

		self.client, addr = sock.accept()

	def run(self):
		while True:
			data = self.client.recv(4096)

			if data :
				# forward it
				print("[{}] -> {}".format(self.port, data.decode()))
				self.server.sendall(data)

class Proxy(Thread):
	def __init__(self, from_client, to_server, port):
		super().__init__()
		self.from_client = from_client
		self.to_server = to_server
		self.port = port

	def run(self):
		while True:
			print("proxy({}) setting up".format(self.port))

			self.c2p = Client2proxy(self.from_client, self.port)
			self.p2s = Proxy2server(self.to_server, self.port)
			print('proxy ({}) connection established'.format(self.port))

			self.c2p.server = self.p2s.server
			self.p2c.client = self.cp2.client

if __name__ == '__main__':
	master_proxy = Proxy('0.0.0.0', '192.168.1.8', 80)
	master_proxy.start()