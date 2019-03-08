# -*- coding: utf-8 -*-
#!/usr/bin/env python
import thread
import socket
import time
# To find the IP use the command ifconfig
#####################################################
TCP_IP = '192.168.2.15'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#Communication astra raspberry pies


####################################################

TCP_IP2 ='192.168.2.10'
TCP_PORT2=5555






#################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('Connected to Orbbec ')

s2 =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s2.connect((TCP_IP2,TCP_PORT2))


print('Connected to s7')
while True:
	data = s.recv(BUFFER_SIZE)
       # print(data)
       # print(type(data))
       # s2.sendall(b'Hello')
	s2.sendall(bytes((data,'utf-8')))
s.close()

print ("received data:", data)
