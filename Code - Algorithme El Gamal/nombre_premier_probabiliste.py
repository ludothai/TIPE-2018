from random import randint

# Génération d'un nombre premier basée su le test de primalité de Miller-Rabin

def MillerRabin_génération(n): #longueur en base 10 du nombre premier
    k=0 #candidat premier
    for i in range(n):
        k+=randint(0,9)*10**i

def puissmod(a,d,n):

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
    
    
def MillerRabin_temoin(a,n):
    #Calcul de s et d tels que n-1=2**s*d
    d=(n-1)/2
    s=1
    while d%2==0:
        d/=2
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
    

def MillerRabin_test(n,k): #primalité de n a tester et k nombre de boucles
    
    for t in range(k):
        a=randint(2,n-2)
        if MillerRabin_temoin(a,n):
            return False
        print(a,t)
    return True
    