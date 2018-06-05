from random import randint,choice
from time import perf_counter

# Données :

# Privées : p, q, d premier avec (p-1)*(q-1)=phi(p*q)
# Publiques : n=p*q, e tel que e*d=1 mod phi(n)

def pgcd(a,b): #algorithme d'Euclide
    while a%b!=0:
        a,b=b,a%b
    return b

def inversmod(a,p):
    '''a**(-1) mod p'''
    #algorithme d'euclide étendu (solution de l'equation de Bezout)
    r1,u1,v1,r2,u2,v2=a,1,0,p,0,1

    while r2!=0:
        q=r1//r2
        r1,u1,v1,r2,u2,v2=r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2
    if r1!=1:
        return 'pas inversible'
    else:
        if u1<1:
            while u1<1:
                u1+=p
        if u1>p:
            while u1>p:
                u1-=p
        return u1

def puissmod(a,d,n):
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res

def MillerRabin_test(n,k): #primalité de n a tester et k nombre de boucles

    for t in range(k):
        a=randint(2,n-2)
        if MillerRabin_temoin(a,n):
            return False
    return True

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

def MillerRabin_generation(b): #longueur en base 10 du nombre premier (proba pas premier 10**-30)
    i=0
    while True:
        i+=1
        n=choice([1,3,5,7,9]) #candidat premier
        for k in range(1,b-1) :
            n+=randint(0,9)*10**k
        n+=randint(1,9)*10**b
        if MillerRabin_test(n,100):
            return i,n

def generateur2(n):
    while True:
        q=MillerRabin_generation(n)[1]
        for k in range(1,500):
            p=k*q+1
            if MillerRabin_test(p,100):
                return p

def RSA_generation(n):
    p=generateur2(n)
    q=generateur2(n) #pas B friable
    phi=(p-1)*(q-1)
    d=randint(1,phi)
    while pgcd(phi,d)!=1:
        d=randint(1,phi)
    e=inversmod(d,phi)
    n=p*q
    return n,e,d

def test_RSA_generation(i,j,pas):
    for n in range(i,j,pas):
        T=[]
        for s in range(10):
            t1=perf_counter()
            RSA_generation(n)
            t2=perf_counter()
            T.append(t2-t1)
        print(n,sum(T)/10,sep=';')


def RSA_chiffrement(m,e,n):
    c=puissmod(m,e,n)
    return c

def RSA_dechiffrement(c,d,n):
    m=puissmod(c,d,n)
    return m

def RSA_signature(h,d,n):
    s=puissmod(h,d,n)
    return s

def RSA_verification(s,h,e,n):
    if puissmod(s,e,n)==h:
        return True
    else:
        return False


#Choix p et q à 200 chiffres

def test_RSA(i,j,pas): #taille du message en nombre de caractères
    '''taille;tchif;tdechif;tsign;tverif'''
    global N
    global E
    global D

    for k in range(i,j,pas):
        Tchif=[]
        Tdechif=[]
        Tsign=[]
        Tverif=[]
        for s in range(10):
            n,e,d=N[s],E[s],D[s]
            q=k//83
            r=k-q
            max=sum([2**pui for pui in range(8*r)])
            B_clair=[randint(1,n-1) for i in range(q)]+[randint(1,max)]
            tchif=0
            tdechif=0
            tsign=0
            tverif=0
            for bloc in B_clair:
                t1=perf_counter()
                c=RSA_chiffrement(bloc,d,n)
                t2=perf_counter()
                tchif+=t2-t1

                t1=perf_counter()
                s=RSA_signature(c,d,n)
                t2=perf_counter()
                tsign+=t2-t1

                t1=perf_counter()
                RSA_dechiffrement(c,d,n)
                t2=perf_counter()
                tdechif+=t2-t1

                t1=perf_counter()
                RSA_verification(s,c,e,n)
                t2=perf_counter()
                tverif+=t2-t1
            Tchif.append(tchif)
            Tdechif.append(tdechif)
            Tsign.append(tsign)
            Tverif.append(tverif)


        print(k,sum(Tchif)/10,sum(Tdechif)/10,sum(Tsign)/10,sum(Tverif)/10,sep=';')

N=[]  #à générer avec le gros ordi
E=[]
D=[]


test_RSA(10,10000,10)
