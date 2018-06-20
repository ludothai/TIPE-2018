# Threads

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
            
class ThreadClientEmission(Thread):
    
    def __init__(self,connexion_serveur):
        Thread.__init__(self)
        self.connexion_serveur=connexion_serveur
    
    def run(self):
        
        while True:
            message=input()
            try:
                self.connexion_serveur.send(message.encode())
            except:
                break


# Client

import sys
import socket

hote = "localhost" #Remplacer par l'adresse IP
port = 12800

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))
print("Connexion etablie avec le serveur sur le port {}".format(port))

thread_reception=ThreadClientReception(connexion_serveur)
thread_emission=ThreadClientEmission(connexion_serveur)

Continue=True
thread_reception.start()
thread_emission.start()

thread_reception.join()
sys.exit()

