# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket
import time
# To find the IP use the command ifconfig
#####################################################
TCP_IP = '192.168.2.15'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#Communication astra raspberry pies


####################################################

TCP_IP2 ='192.168.2.14'
TCP_PORT2=5555









#################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('Connected to Orbbec ')

st = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
st.bind((TCP_IP2,TCP_PORT2))
st.listen(1)
print('Now waitig for s7 to connect')

conn,addr = st.accept()
print('s7 connected address: ',addr)

while True:
	data = s.recv(BUFFER_SIZE)
        print(data)
        print(type(data))
       # st.sendall(b'Hello')
	#st.sendall(bytes(data,'utf-8'))
s.close()

print ("received data:", data)
