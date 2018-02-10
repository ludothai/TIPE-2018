#Lien : http://www.supinfo.com/articles/single/1232-reseau-python

## Threads

from threading import Thread,Event

class ThreadClientReception(Thread):
    
    def __init__(self,connexion_serveur,event):
        Thread.__init__(self)
        self.connexion_serveur=connexion_serveur
        self.event=event
        
    def run(self):
        while not self.event.is_set() :
            message_recu=self.connexion_serveur.recv(1024).decode()
            print(message_recu)
            if message_recu=='Deconnexion':
                self.event.set()
        self.connexion_serveur.close()
            
class ThreadClientEmission(Thread):
    
    def __init__(self,connexion_serveur,event):
        Thread.__init__(self)
        self.connexion_serveur=connexion_serveur
        self.event=event
    
    def run(self):
        
        while not self.event.is_set():
            message=input()
            if message != 'Deconnexion':
                self.connexion_serveur.send(message.encode())
            else:
                self.event.set()


class ThreadServeurReception(Thread):
    
    def __init__(self,connexion_principale,connexion_client,event):
        Thread.__init__(self)
        self.connexion_principale=connexion_principale
        self.connexion_client=connexion_client
        self.event=event
        
    def run(self):
        while not self.event.is_set() :
            message_recu=self.connexion_client.recv(1024).decode()
            print(message_recu)
            if message_recu=='Deconnexion':
                self.event.set()
        self.connexion_client.send(b"Deconnexion")
        self.connexion_client.close()
        self.connexion_principale.close()
                
class ThreadServeurEmission(Thread):
    
    def __init__(self,connexion_client,event):
        Thread.__init__(self)
        self.connexion_client=connexion_client
        self.event=event
    
    def run(self):
        while not self.event.is_set():
            message=input()
            if message != 'Deconnexion':
                self.connexion_client.send(message.encode())
            else:
                self.event.set()

## Partie Client

import socket

hote = "localhost"
port = 12800

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

deconnexion=Event()
thread_reception=ThreadClientReception(connexion_serveur,deconnexion)
thread_emission=ThreadClientEmission(connexion_serveur,deconnexion)

Continue=True
thread_reception.start()
thread_emission.start()

thread_reception.join()
thread_emission.join()

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

deconnexion=Event()
thread_reception=ThreadServeurReception(connexion_principale,connexion_client,deconnexion)
thread_emission=ThreadServeurEmission(connexion_client,deconnexion)

Continue=True
thread_reception.start()
thread_emission.start()

thread_reception.join()
thread_emission.join()