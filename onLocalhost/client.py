# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket
#print needs parenthesis

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)