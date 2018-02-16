## Serveur

# Threads

from threading import Thread

class ThreadServeurClient(Thread):
    
    def __init__(self,connexion_principale,connexion_client,infos_connexion,L_connexions):
        Thread.__init__(self)
        self.connexion_principale=connexion_principale
        self.connexion_client=connexion_client
        self.L_connexions=L_connexions
        self.infos_connexion=infos_connexion
        
    def run(self):
        Continue=True
        while Continue :
            message_recu=self.connexion_client.recv(1024).decode()
            if message_recu=='Deconnexion':
                Continue=False
                self.L_connexions.remove(self.connexion_client)
            else:
                for client in self.L_connexions:
                    if client != self.connexion_client:
                        client.send((self.infos_connexion[0]+' : '+message_recu).encode())
        
        self.connexion_client.send(b"Deconnexion")
        print("Déconnecté avec le client {}".format(self.infos_connexion))
        self.connexion_client.close()
                

# Serveur

import sys
import socket

hote=''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
connexion_principale.settimeout(10)
print("Le serveur écoute à présent sur le port {}".format(port))

L_connexions=[]
try:
    connexion_client, infos_connexion = connexion_principale.accept()
except socket.timeout:
    print("Il n'y a pas de clients : Deconnection")
    connexion_principale.close()
    sys.exit()
print("Connecté avec le client {}".format(infos_connexion))
L_connexions.append(connexion_client)
ThreadServeurClient(connexion_principale,connexion_client,infos_connexion,L_connexions).start()


while L_connexions != []:
    try:
        connexion_client, infos_connexion = connexion_principale.accept()
    except socket.timeout :
        continue
    print("Connecté avec le client {}".format(infos_connexion))
    L_connexions.append(connexion_client)
    ThreadServeurClient(connexion_principale,connexion_client,infos_connexion,L_connexions).start()

print("Il n'y a plus de clients : Deconnection")
connexion_principale.close()

sys.exit()
