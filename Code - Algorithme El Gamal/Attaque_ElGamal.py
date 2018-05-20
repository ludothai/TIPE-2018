from math import sqrt

#Pas de bebe,pas de geant (SHANKS)
#O(exp(p))
def shanks(p,g,x): #retourne n tel que x=g**n mod p
    K=int(sqrt(p))+1
    A=[puissmod(g,i,p) for i in range(K)]
    A.sort()
    for j in range(K):
        b=(x*puissmod(g,
