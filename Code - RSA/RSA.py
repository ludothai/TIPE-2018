from random import randint

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
