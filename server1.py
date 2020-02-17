import socket
s=socket.socket()
print "socket succesfully created"
port=4443
s.bind(('',port))
print "socket binded to %s" %(port) 
s.listen(sz)
print "socket is listening"


while True:
	c,addr=s.accept()
	print"got connection from ",addr
	c.send("thank you for connecting")
	while True:
		print c.recv(1024)
		a=raw_input("enter the messege:")

		c.send(a)

c.close()
