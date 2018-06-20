from random import randint


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
    while type(k2inv)==str: #tant que le k aléatoire n'est pas inversible mod p-1
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
    '''p premier,g générateur'''
    cle_priv=randint(1,p-1)
    cle_publ=puissmod(g,cle_priv,p)
    return cle_priv,cle_publ
