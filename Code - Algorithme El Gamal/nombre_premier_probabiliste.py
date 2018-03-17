import random as rd
import time

# Génération d'un nombre premier basée su le test de primalité de Miller-Rabin

def MillerRabin_génération(b): #longueur en base 10 du nombre premier (proba pas premier 10**-30)
    while True:
        n=rd.choice([1,3,5,7,9]) #candidat premier
        for k in range(1,b-1) :
            n+=rd.randint(0,9)*10**k
        n+=rd.randint(1,9)*10**b
        if MillerRabin_test(n,100):
            return n


def puissmod(a,d,n): # récursif

    if d==0:
        return 1
    elif d==1:
        return a
    elif d%2==0:
        b=(a**2)
        return puissmod(b,d//2,n)%n
    else:
        b=(a**2)
        return a*puissmod(b,d//2,n)%n
    
def puissmod2(a,d,n): #itératif : beaucoup plus efficace (10^-5) 600 chiffres -> 0.024571632396359178 s
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res



def MillerRabin_temoin(a,n):
    #Calcul de s et d tels que n-1=2**s*d
    d=(n-1)//2
    s=1
    while d%2==0:
        d=d//2
        s+=1
    
    #Premier test
    x=puissmod2(a,d,n)
    if x==1 or x==n-1 :
        return False
    
    #Boucle principale
    
    while s>1:
        x=x**2%n
        if x==n-1:
            return False
        s-=1
    
    return True
    

def MillerRabin_test(n,k): #primalité de n a tester et k nombre de boucles
    
    for t in range(k):
        a=rd.randint(2,n-2)
        if MillerRabin_temoin(a,n):
            return False
    return True

def test(i,j):
    for b in range(i,j+1):
        n=rd.choice([1,3,5,7,9])
        for k in range(1,b) :
            n+=rd.randint(0,9)*10**k
        n+=rd.randint(1,9)*10**b
        a=rd.randint(0,n)
        d=rd.randint(0,n)
        t1=time.clock()
        puissmod2(a,d,n)
        t2=time.clock()
        
        print(b,t2-t1)
