#Lien : http://www.supinfo.com/articles/single/1232-reseau-python

# Threads

from threading import Thread

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


# Serveur

import socket

hote = '192.168.1.16'
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
