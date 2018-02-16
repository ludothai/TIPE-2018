espace = [0, 0, 1, 0, 0, 0, 0, 0] #(ord 32) Caractère [espace] en binaire 8 bits AISCII

def decoupe64(l):
    """ découpe une chaine binaire en bloc de 64 bits et complétant les vides par des 'espaces' """
    B = [] #Liste BLOCs, résultat
    L = l[:] #copie L
    n  = len(L)
    r = n % 64 # reste de la division euclidienne de n par 64
    nesp = (64-r)//8 #nombre de caractère 'espace' à ajouter pour compléter L

    if r != 0 : #si len(L) n'est pas un multiple de 64, on complète L avec des 'espaces'
        for i in range(nesp): #on ajoute le caractère 'espace' nesp fois
            L+=espace

    q = len(L) // 64 # quotient : [nombre éléments de L]/64 = nombre de sous liste à créer
    for i in range(q):
        SB =[] #Sous bloc (temp)
        for j in range(64):
            SB.append(L.pop(0)) #on pop et on ajoute en même temps
        B.append(SB)
    return B

def assembler(B):
    """regroupe liste contenant des sous-listes (bloc de 64) en une liste"""
    L = [] #résultat
    for i in range(len(B)):
        R+=B[i]
    return 
