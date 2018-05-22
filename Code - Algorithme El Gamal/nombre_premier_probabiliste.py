import random as rd
from time import perf_counter
import matplotlib.pyplot as plt
import math

# Génération d'un nombre premier basée su le test de primalité de Miller-Rabin

def MillerRabin_generation(b): #longueur en base 10 du nombre premier (proba pas premier 10**-30)
    i=0
    while True:
        i+=1
        n=rd.choice([1,3,5,7,9]) #candidat premier
        for k in range(1,b-1) :
            n+=rd.randint(0,9)*10**k
        n+=rd.randint(1,9)*10**b
        if MillerRabin_test(n,100):
            return i,n


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

def test(i,j,pas):
    X=[]
    Y=[]
    for b in range(i,j+1,pas):
        print(b)
        t1=perf_counter()
        MillerRabin_génération(b)
        t2=perf_counter()
        X.append(b)
        Y.append((t2-t1))
    plt.plot(X,Y)
    plt.show()

def conj_riemann(i,j):
    X=[]
    Y=[]
    for b in range(i,j+1):
        a=1/math.log(10**(b+1))-1/math.log(10**(b))
        X.append(b)
        Y.append(a)
        print(b,a)
    plt.plot(X,Y)
    plt.show()

def test_generateur(n):
    q=MillerRabin_generation(n)[1]
    print(q)
    for k in range(1,100):
        print(k)
        p=k*q+1
        if MillerRabin_test(p,100):
            while True:
                g=rd.randint(2,p) #Candidat générateur
                i=1
                grandordre=True
                while grandordre:
                    if puissmod2(g,i,p)==1:
                        grandordre=False
                    elif i<k:
                        i+=1
                    else:
                        return p,g
n=4
p,g=test_generateur(n)
print(p,g)

print('ssgpe engendré par le générateur')
L=[]
for i in range(1,p):
    k=puissmod2(g,i,p)
    if k not in L:
        L.append(k)
L.sort()
print('ordre : ',len(L))

