def permutationCP1(K):
    """Effectue la permutation initiale de la cle de 64 bits, retourne les listes G0 et D0"""
    if len(K) != 64 : return "Erreur len(K)"
    else:
        K1 = []
        CP1=[57,49,41,33,	25,17, 9, 1,58,50,42,34,26,18,
             10, 2,59,51,	43,35,27,19,11, 3,60,52,44,36,
             63,55,47,39,	31,23,15, 7,62,54,46,38,30,22,
             14, 6,61,53,	45,37,29,21,13, 5,28,20,12, 4]
        for i in CP1:
            K1.append(K[i-1])
        return K1[:28], K1[28:]

def decalageGauche(L, n):
    """ Decale les elements de la liste L de n places vers la GAUCHE"""
    Ldec = []
    for i in range(len(L)-n):
        Ldec.append(L[i+n])
    for i in range(n):
        Ldec.append(L[i])
    return Ldec
        
def regroupe(G,D):
    return G+D

def permutationCP2(K):
    """Effectue la permutation CP2 du bloc de 56 bits en un bloc de 48 bits qui est la clé Ki"""
    if len(K) != 56 : return "Erreur len(K)"
    else:
        Ki = []
        CP2=[14,17,11,24,	 1, 5, 3,28,15, 6,21,10,
             23,19,12, 4,	26, 8,16, 7,27,20,13, 2,
             41,52,31,37,	47,55,30,40,51,45,33,48,
             44,49,39,56,	34,53,46,42,50,36,29,32]
        for i in CP2:
            Ki.append(K[i-1])
        return Ki

def genKey(K):
    """ Retourne les 16 cles Ki a partir de la cle de 64 bits"""
    decalage = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] #Nombre de decalage a gauche pour les 16 iterations (de 0 a 15)
    cles = []
    #verification cle est de 64 bits:
    if checkBINn(K, 64) == False: return "Erreur sur la cle initilale K"
    # permutation initiale CP1:
    G, D = permutationCP1(K)
#    print("Gk=", G)
#    print("Dk=", D)
#    print("")
    if checkBINn(G, 28) == False: return "Erreur sur la cle initiale G"
    if checkBINn(D, 28) == False: return "Erreur sur la cle initiale D"
    for i in range(16):
        Gi = decalageGauche(G, decalage[i])
        Di = decalageGauche(D, decalage[i])
#        print("Gk",i,"=",Gi)
#        print("Dk",i,"=",Di)
        Ki = permutationCP2(regroupe(Gi, Di))
#        print("K",i,"=",Ki)
#        print()
        if checkBINn(Ki, 48) == False: return "Erreur sur la cle Ki"
        cles.append(Ki)
        G = Gi
        D = Di
        
    return cles
        
def checkBINn(L, n):
    """ verifie que la liste L est une liste contenant n elements binaire (0 ou 1)"""
    binaire = [0,1]
    if len(L)==n:
        for i in range(len(L)):
            if L[i] not in binaire:
                return False
        return True
    else: 
        return False    

def gen(n):
    return ([(i+1)*10 for i in range(n)])

