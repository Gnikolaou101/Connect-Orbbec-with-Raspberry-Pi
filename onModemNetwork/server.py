
# -*- coding: utf-8 -*- !/usr/bin/env python

import socket
#The first line it is needed for the orbbec to understand the coding
# To find the IP use the command ifconfig

<<<<<<< HEAD
TCP_IP = '192.168.2.14' 
=======
TCP_IP = '192.168.2.15' 
>>>>>>> refs/remotes/origin/master
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
<<<<<<< HEAD
print ('wait for connection')
=======
print ('now accepting')
>>>>>>> refs/remotes/origin/master
conn, addr = s.accept()
print ('Connection address:', addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break			#What does 'if not data: break' mean? https://stackoverflow.com/questions/17898779/what-does-if-not-data-break-mean
    print ("received data:", data)
<<<<<<< HEAD
    conn.send(data)  # echo
conn.close()
=======
    #conn.send(data)  # echo
conn.close()
>>>>>>> refs/remotes/origin/master
