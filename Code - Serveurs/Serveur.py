#Lien : http://www.supinfo.com/articles/single/1232-reseau-python

## Threads

from threading import Thread

class ThreadClientReception(Thread):
    
    def __init__(self,connexion_serveur):
        Thread.__init__(self)
        self.connexion_serveur=connexion_serveur
        
    def run(self):
        Continue=True
        while Continue:
            message_recu=self.connexion_serveur.recv(1024).decode()
            print(message_recu)
            if message_recu=='Deconnexion':
                Continue=False
        self.connexion_serveur.send(b'Deconnexion')
        self.connexion_serveur.close()
            
class ThreadClientEmission(Thread):
    
    def __init__(self,connexion_serveur):
        Thread.__init__(self)
        self.connexion_serveur=connexion_serveur
    
    def run(self):
        
        while True:
            message=input()
            self.connexion_serveur.send(message.encode())


class ThreadServeurReception(Thread):
    
    def __init__(self,connexion_principale,connexion_client):
        Thread.__init__(self)
        self.connexion_principale=connexion_principale
        self.connexion_client=connexion_client
        
    def run(self):
        Continue=True
        while Continue :
            message_recu=self.connexion_client.recv(1024).decode()
            print(message_recu)
            if message_recu=='Deconnexion':
                Continue=False
        self.connexion_client.send(b"Deconnexion")
        self.connexion_client.close()
        self.connexion_principale.close()
                
class ThreadServeurEmission(Thread):
    
    def __init__(self,connexion_client):
        Thread.__init__(self)
        self.connexion_client=connexion_client
    
    def run(self):
        while True:
            message=input()
            self.connexion_client.send(message.encode())

## Partie Client

import socket

hote = "localhost"
port = 12800

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

thread_reception=ThreadClientReception(connexion_serveur)
thread_emission=ThreadClientEmission(connexion_serveur)

Continue=True
thread_reception.start()
thread_emission.start()

thread_reception.join()


## Partie Serveur

import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_client, infos_connexion = connexion_principale.accept()
print("Connecté avec le client {}".format(infos_connexion))

thread_reception=ThreadServeurReception(connexion_principale,connexion_client)
thread_emission=ThreadServeurEmission(connexion_client)

Continue=True
thread_reception.start()
thread_emission.start()

thread_reception.join()
