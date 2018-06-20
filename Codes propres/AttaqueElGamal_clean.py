from math import exp, sqrt, log

#Logarithme discret naif

def lognaif(p,g,x):
    for i in range(p):
        if puissmod(g,i,p)==x:
            return i
 
#Pas de bebe,pas de geant (SHANKS)

def shanks(p,g,x): #retourne n tel que x=g**n mod p
    K=int(sqrt(p))+1
    c=inversmod(puissmod(g,K,p),p)
    A=[(puissmod(g,i,p),i) for i in range(1,K)]
    A.sort(key=lambda x:x[0])
    b=x
    for j in range(K):
        if b<int(p/2): #On parcours A dans l'ordre croissant
            i=0
            while i<K-2 and b>A[i][0]:
                i+=1
            if A[i][0]==b:
                return A[i][1]+K*j
            else:
                b=(b*c)%p
        else: #On parcours A dans l'ordre decroissant
            i=K-2
            while i>0 and b<A[i][0]:
                i-=1
            if A[i][0]==b:
               return A[i][1]+K*j
            else:
                b=(b*c)%p

#Calcul de l'indice (Complexe)

def Modele_CalculIndice(i,j,pas):
    for x in range(i,j,pas):
        print(x,exp(sqrt(2*log(10**x))*sqrt(log(log(10**x)))),sep=';')

