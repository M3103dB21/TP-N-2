from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket0 = socket(AF_INET, SOCK_STREAM)
clientSocket0.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket0.send(sentence)
modifiedSentence = clientSocket0.recv(1024)
print 'From Server:', modifiedSentence
clientSocket0.close()