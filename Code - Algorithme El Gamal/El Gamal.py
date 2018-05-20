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
    cle_priv=randint(0,p-1)
    cle_publ=puissmod(g,cle_priv,p)
    return cle_priv,cle_publ

def chiffrement(p,g,cle_
