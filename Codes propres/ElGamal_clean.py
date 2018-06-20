from random import randint
from math import log

def puissmod(a,d,n):
    """a**d mod n"""
    #iteratif : beaucoup plus efficace (10^-5) 600 chiffres -> 0.024571632396359178 s
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res

def inversmod(a,p):
    """a**(-1) mod p"""
    #algorithme d'euclide etendu (solution de l'equation de Bezout)
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

#Fonctions de ElGamal
def chiffrement(p,g,cle_dest,message_clair,sign):
    k1=randint(1,p-1)
    cle_sess=puissmod(cle_dest,k1,p)
    message_crypt=(message_clair*cle_sess)%p
    entete=puissmod(g,k1,p)
    if sign:
        r,s=signature(p,g,k1,message_crypt)
        return r,s,entete,message_crypt
    else:
        return entete,message_crypt

def dechiffrement(p,g,cle_priv,entete,message_crypt):
    cle_sess=puissmod(entete,cle_priv,p)
    message_clair=(message_crypt*inversmod(cle_sess,p))%p
    return message_clair

def signature(p,g,k1,message_crypt):
    k2=randint(1,p-1)
    k2inv=inversmod(k2,p-1)
    while type(k2inv)==str: #tant que le k aleatoire n'est pas inversible mod p-1
        k2=randint(1,p-1)
        k2inv=inversmod(k2,p-1)
    r=puissmod(g,k2,p)
    h=message_crypt
    s=((h-k1*r)*k2inv)%(p-1)
    return r,s

def verification_signature(p,g,r,s,entete,message_crypt):
    h=message_crypt
    a=puissmod(g,h,p)
    b=(puissmod(entete,r,p)*puissmod(r,s,p))%p
    if a==b:
        return True
    else:
        return False

def generation_cle(p,g):
    """p premier,g generateur"""
    cle_priv=randint(1,p-1)
    cle_publ=puissmod(g,cle_priv,p)
    return cle_priv,cle_publ
