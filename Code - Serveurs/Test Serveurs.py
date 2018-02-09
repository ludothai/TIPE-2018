#Lien : http://www.supinfo.com/articles/single/1232-reseau-python

## Threads

from threading import Thread

class ThreadClientReception(Thread):
    
    def __init__(self,connexion):
        Thread.__init__(self)
        self.connexion=connexion
        
    def run(self):
        Continue=True
        while Continue :
            message_recu=self.connexion.recv(1024).decode()
            print(message_recu)
            if message_recu='Deconnexion':
                Continue=False
            
class ThreadClientEmission(Thread):
    
    def __init__(self,connexion):
        Thread.__init__(self)
        self.connexion=connexion
    
    def run(self):
        Continue=True
        while Continue:
            message=input()
            if message != 'Deconnexion':
                self.connexion.send(message.encode())
            else:
                self.connexion.close()
                Continue=False

class ThreadServeurReception(Thread):
    
    def __init__(self,connexion_principale,connexion_client):
        Thread.__init__(self)
        self.connexion_principale=connexion_principale
        self.connexion_cient=connexion_client
        
    def run(self):
        Continue=True
        while Continue :
            message_recu=self.connexion_client.recv(1024).decode()
            print(message_recu)
            if message_recu='Deconnexion':
                Continue=False
                connexion_client.send(b"Deconnexion")
                connexion_client.close()
                connexion_principale.close()
                
class ThreadServeurEmission(Thread):
    
    def __init__(self,connexion):
        Thread.__init__(self)
        self.connexion=connexion
    
    def run(self):
        Continue=True
        while Continue:
            message=input()
            if message != 'Deconnexion':
                self.connexion.send(message.encode())
            else:
                self.connexion.close()
                Continue=False

## Partie Client

import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
thread_reception=ThreadClientReception(connexion_avec_serveur)
thread_emission=ThreadClientEmission(connexion_avec_serveur)

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

connexion_avec_client, infos_connexion = connexion_principale.accept()
print("Connecté avec le client {}".format(infos_connexion))

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
