from socket import *

serverName = "localhost"
serverPort = 12000
serverPort2 = 13000
serverPort3 = 14000
serverSocket0 = socket(AF_INET,SOCK_STREAM)
serverSocket0.bind(('',serverPort))
serverSocket0.listen(1)

serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket1.connect((serverName,serverPort2))
serverSocket1.bind(('',serverPort))
serverSocket1.listen(1)

serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.connect((serverName,serverPort3))
serverSocket2.bind(('',serverPort))
serverSocket2.listen(1)


print "The server is ready to receive"

while 1:
	connectionSocket0, addr = serverSocket0.accept()
	sentence = connectionSocket0.recv(1024)
	print sentence
	capitalizedSentence = sentence.upper()
	connectionSocket0.close()
	connectionSocket1, addr = serverSocket1.accept()
	connectionSocket1.send(capitalizedSentence)
	connectionSocket1.close()
	connectionSocket2, addr = serverSocket2.accept()
	connectionSocket2.send(capitalizedSentence)
	connectionSocket2.close()
	connectionSocket0.close()