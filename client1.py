import socket
s=socket.socket()
port=4443
s.connect(('127.0.0.1',port))
while(True):
	print s.recv(1024)
	a=raw_input("enter the msg:")
	s.send(a)
s.close()
