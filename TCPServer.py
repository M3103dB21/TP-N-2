from socket import *

serverPort = 14000

serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',serverPort))
serverSocket2.listen(1)

print "The server is ready to receive"

while 1:
	connectionSocket2, addr = serverSocket2.accept()
	sentence = connectionSocket2.recv(1024)
	print sentence
