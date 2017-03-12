# TP 2

### Creation de serveur TCP
Tout d'abord nous avons crée un serveur permettant de recevoir un message d'un client (détaillé a la suite),mettre en majuscule ce message et le renvoyer au client.
```Python
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
  ```
  
 ### Creation d'un client TCP

Le client permet d'envoyer un message au serveur, dans notre cas, ou à n'importe quel adresse IP : Port.
```Python
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
```

### Netcat
