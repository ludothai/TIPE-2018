# Donnees :
# Privees : p, q, d premier avec (p-1)*(q-1)=phi(p*q)
# Publiques : n=p*q, e tel que e*d=1 mod phi(n)

def pgcd(a,b): #algorithme d'Euclide
    while a%b!=0:
        a,b=b,a%b
    return b

def generateur(n):
    while True:
        q=MillerRabin_generation(n)
        for k in range(1,500):
            p=k*q+1
            if MillerRabin_test(p,100):
                return p

def RSA_generation(n):
    p=generateur(n)
    q=generateur(n) #pas B friable
    phi=(p-1)*(q-1)
    e=3
    while pgcd(e,phi)!=1:
        e+=2
    d=inversmod(e,phi)
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

