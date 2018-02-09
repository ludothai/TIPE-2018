#Codage du message 1 caractere = 8 bits

def encodage(m):
    """Message en STRING retourné en binaire 8 bits (table AISCII) """
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
        for i in range(8-n): # complète avec des zéros
            Mfin.append(0)
        for i in binaire:
            Mfin.append(int(i))
    print("m=",m)
    print("M=",M)
    print("Mord=",Mord)
    print("Mbin=",Mbin)
    return Mfin

def decodage(M):
    n=len(M)//8
    Mfin=[str(i) for i in M]
    Mbin=[]
    for i in range(n):
        binaire=Mfin[i*8]
        for j in range(1,8):
            binaire+=Mfin[i*8+j]
        Mbin.append(binaire)
    Mord=[int(binaire,2) for binaire in Mbin]
    Mchr=[chr(i) for i in Mord]
    m=Mchr[0]
    for i in range(1,len(Mchr)):
        m+=Mchr[i]
    return m
