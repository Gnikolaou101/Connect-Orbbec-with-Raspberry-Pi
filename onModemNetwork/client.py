# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket
# To find the IP use the command ifconfig

TCP_IP = '192.168.2.15'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
while True:
	data = s.recv(BUFFER_SIZE)
	print(data)
s.close()

print ("received data:", data)
