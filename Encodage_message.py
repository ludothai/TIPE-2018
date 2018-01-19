#Codage du message 1 caractere = 8 bits

def encodage(m): # message en string donne une liste d'entiers 0 ou 1
    if type(m) != str :
        raise TypeError
    M = list(m) # on split tout en caracteres individuels
    Mord = [ord(M[i]) for i in range(len(M))]
    Mbin = [bin(Mord[i]) for i in range(len(M))]
    # traitement du Mbin pour enlever le '0b' du debut et taille constante
    Mfin=[]
    for binaire in Mbin:
        binaire=binaire[2:]
        n=len(binaire)
        if n>8:
            return 'Erreur len(binaire)'
        for i in range(8-n):
            Mfin.append(0)
        for i in binaire:
            Mfin.append(int(i))
    print("m=",m)
    print("M=",M)
    print("Mord=",Mord)
    print("Mbin=",Mbin)
    return Mfin
    
def decodage(M):
    n=len(M)/8
    Mbin=[]
    for i in range(n):
        binaire=sum(M[i:i+9])
        Mbin.append(binaire)
    Mord=[int(binaire,2) for binaire in Mbin]
    m=sum([chr(i) for i in Mord])
    return m

        
    
