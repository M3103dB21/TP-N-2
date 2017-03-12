from socket import *

serverPort = 13000

serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket1.bind(('',serverPort))
serverSocket1.listen(1)

print "The server is ready to receive"

while 1:
	connectionSocket1, addr = serverSocket1.accept()
	sentence = connectionSocket1.recv(1024)
	print sentence
