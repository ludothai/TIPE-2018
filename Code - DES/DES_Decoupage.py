espace = [0, 0, 1, 0, 0, 0, 0, 0] #(ord 32) Caractere [espace] en binaire 8 bits AISCII

def decoupe64(l):
    """ decoupe une chaine binaire en bloc de 64 bits et completant les vides par des 'espaces' """
    B = [] #Liste BLOCs, resultat
    L = l[:] #copie L
    n  = len(L)
    r = n % 64 # reste de la division euclidienne de n par 64
    nesp = (64-r)//8 #nombre de caractee 'espace' a  ajouter pour complater L

    if r != 0 : #si len(L) n'est pas un multiple de 64, on complate L avec des 'espaces'
        for i in range(nesp): #on ajoute le caractare 'espace' nesp fois
            L+=espace

    q = len(L) // 64 # quotient : [nombre elements de L]/64 = nombre de sous liste a  creer
    for i in range(q):
        SB =[] #Sous bloc (temp)
        for j in range(64):
            SB.append(L.pop(0)) #on pop et on ajoute en meme temps
        B.append(SB)
    return B

def assembler(B):
    """regroupe liste contenant des sous-listes (bloc de 64) en une liste"""
    L = [] #resultat
    for i in range(len(B)):
        L+=B[i]
    return L
