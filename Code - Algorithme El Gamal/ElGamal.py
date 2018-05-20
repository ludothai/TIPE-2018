from random import randint

def puissmod(a,d,n): '''a**d mod n'''
    #itératif : beaucoup plus efficace (10^-5) 600 chiffres -> 0.024571632396359178 s
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res

def generation_cle(p,g): '''p premier,g générateur'''
    cle_priv=randint(1,p-1)
    cle_publ=puissmod(g,cle_priv,p)
    return cle_priv,cle_publ

def chiffrement(p,g,cle_dest,message_clair,signature=True):
    k=randint(1,p-1)
    cle_sess=puissmod(cle_dest,k,p)
    message_crypt=DES(message_clair,cle_sess)
    entete=puissmod(g,k,p)
    return entete,message_crypt

def dechiffrement(p,g,cle_priv,entete,message_crypt)
    cle_sess=puissmod(entete,cle_priv,p)
    message_clair=DES(message_crypt,cle_sess)
    return message_clair




