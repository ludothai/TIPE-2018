# Données :

# Privées : p, q, d premier avec (p-1)*(q-1)=phi(p*q)
# Publiques : n=p*q, e tel que e*d=1 mod phi(n)

def RSA_chiffrement(m,e,n):
    c=(m**e)%n
    return c
    
def RSA_dechiffrement(c,d,n):
    m=(c**d)%n
    return m
    
def RSA_signature(h,d,n):
    s=(h**d)%n
    return s
    
def RSA_verification(s,h,e,n):
    if (s**e)%n==h:
        return True
    else:
        return False
