#K = [0 for i in range(64)]

K = [0,0,0,1,0,0,1,1, 0,0,1,1,0,1,0,0, 0,1,0,1,0,1,1,1, 0,1,1,1,1,0,0,1, 1,0,0,1,1,0,1,1, 1,0,1,1,1,1,0,0, 1,1,0,1,1,1,1,1, 1,1,1,1,0,0,0,1] 


M = [0,0,0,0, 0,0,0,1, 0,0,1,0, 0,0,1,1, 0,1,0,0, 0,1,0,1, 0,1,1,0, 0,1,1,1, 1,0,0,0, 1,0,0,1, 1,0,1,0, 1,0,1,1, 1,1,0,0, 1,1,0,1, 1,1,1,0, 1,1,1,1]

L= decoupe64(encodage("loooool"))[0]

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
    
def DESc(M, K):
    """ Crypte le message M (binaire de 64 bits) avec la clé K (binaire de 64 bits) par la methode du DES"""
    #Verification
    if checkBINn(M, 64) == False: return 'Erreur M'
    if checkBINn(K, 64) == False: return 'Erreur K'
    
    #Calcul des cles
    key = genKey(K)
    
    print("-----------------------------------------------")
    
    #permutation initiale
    MPI = permutation_initiale(M)
    print()

    #scindement
    G,D =  scindement2(MPI)
    print("G=", G)
    print("D=", D)
    print()
    print()

    #initialisation de la ronde
    Gi = G
    Di = D 
    print("i= *")
    print()
    print("G * =", Gi)
    print("D * =", Di)
    print()
    print()

    #ronde
    for i in range(16):
        print("i=", i)
        print()
        Dexpand= expansion(Di)
        Xi = XORL(Dexpand, key[i])
        print("XORL",i,"=", Xi)
        Si = selection(Xi)
        Ti = permutation32(Si)
        Gi, Di = Di,  XORL(Gi, Ti)
        print()
        print("G",i,"=", Gi)
        print("D",i,"=", Di)
        print()
        print()
    
    #regroupement INVERSE
    R = Di + Gi 

    #permutation inverse
    return permutation_inverse(R)


    
def DESd(M, K):
    """ Decrypte le message M (binaire de 64 bits) avec la clé K (binaire de 64 bits) par la methode du DES"""
    #Verification
    if checkBINn(M, 64) == False: return 'Erreur M'
    if checkBINn(K, 64) == False: return 'Erreur K'
    
    #Calcul des cles
    key = genKey(K)
    key.reverse()
    
    for j in range(len(key)):
        print("K.r",j,"=",key[j])
        print()
    
    print("-----------------------------------------------")
    
    #permutation initiale
    MPI = permutation_initiale(M)
    print()

    #scindement
    G,D =  scindement2(MPI)
    print("G=", G)
    print("D=", D)
    print()
    print()

    #initialisation de la ronde
    Gi = G
    Di = D 
    print("i= *")
    print()
    print("G * =", Gi)
    print("D * =", Di)
    print()
    print()

    #ronde
    for i in range(16):
        print("i=", i)
        print()
        Dexpand= expansion(Di)
        Xi = XORL(Dexpand, key[i])
        print("XORL",i,"=", Xi)
        Si = selection(Xi)
        Ti = permutation32(Si)
        Gi, Di = Di,  XORL(Gi, Ti)
        print()
        print("G",i,"=", Gi)
        print("D",i,"=", Di)
        print()
        print()
    
    #regroupement INVERSE
    R = Di + Gi 

    #permutation inverse
    return permutation_inverse(R)


C = DESc(L,K)
print()
print(C)
print(decodage(C))





