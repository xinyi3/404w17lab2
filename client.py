#!/user/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF>INET indicates that we want an IPV4 socket
#scoket,SOCK_STREAM indicates that we want a TCP scoket

clientSocket.connect(("www.google.com",80))
#note there are no http://
#port 80 is the standard http port

request = "GET / HTTP/1.0\r\n\r\n"

clientSocket.sendall(request)

response = bytearray()
while True:
	part = clientSocket.recv(1024)
	if(part):
		response.extend(part)
	else:
		break
print response
