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

On  a aussi utilisé netcat en tant que serveur (recevant du client UDP) grâce au ligne de commande suivante entrée dans le terminal
```
nc -l 127.0.0.1 12000
```
Ensuite netcat en tant que client (envoyant au serveur UDP)
```
nc 127.0.0.1 12000
```

### Filtrage 

On a crée un deuxième serveur pareil que le premier avec un différent port.
Le filtrage permet de recevoir un message d'un client (TCPClient) et de le renvoyer à 2 autres serveur (TCPServer et TCPServer2).
nous avons donc crée 3 socket et utilisé 3 port différents.

```Python 
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
```
