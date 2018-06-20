import random as rd
from time import perf_counter
import math

## Generation d'un nombre premier de maniere deterministe

def est_premier(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

def premier(n): # Plus appliquable au dela de 20 chiffres
    while n>10:
        if est_premier(n):
            return n
        n-=1
    
def premier_Pollard(n):
    eps=10**(-100)
    while n>10:
        if (n-1)/2-int((n-1)/2)<eps:
            if est_premier(int((n-1)/2)):
                if est_premier(n):
                    return n
        n-=1

## Generation d'un nombre premier basee sur le test de primalite de Miller-Rabin

def MillerRabin_generation(b): #longueur en base 10 du nombre premier (proba pas premier 10**-300)
    i=0
    while True:
        i+=1
        n=rd.choice([1,3,5,7,9]) #candidat premier
        for k in range(1,b-1) :
            n+=rd.randint(0,9)*10**k
        n+=rd.randint(1,9)*10**b
        if MillerRabin_test(n,500):
            return i,n

def MillerRabin_temoin(a,n):
    #Calcul de s et d tels que n-1=2**s*d
    d=(n-1)//2
    s=1
    while d%2==0:
        d=d//2
        s+=1
    #Premier test
    x=puissmod(a,d,n)
    if x==1 or x==n-1 :
        return False
    #Boucle principale
    while s>1:
        x=x**2%n
        if x==n-1:
            return False
        s-=1
    return True

def MillerRabin_test(n,k): #primalite de n a tester et k nombre de boucles
    for t in range(k):
        a=rd.randint(2,n-2)
        if MillerRabin_temoin(a,n):
            return False
    return True

def generateur_ElGamal(n):
    while True:
        q=MillerRabin_generation(n)[1]
        for k in range(1,500):
            p=k*q+1
            if MillerRabin_test(p,100):
                while True:
                    g=rd.randint(2,p) #Candidat generateur
                    i=1
                    grandordre=True
                    while grandordre:
                        if puissmod2(g,i,p)==1:
                            grandordre=False
                        elif i<k:
                            i+=1
                        else:
                            return p,g

def generateur_RSA(n):
    while True:
        q=MillerRabin_generation(n)[1]
        for k in range(1,500):
            p=k*q+1
            if MillerRabin_test(p,100):
                return p
