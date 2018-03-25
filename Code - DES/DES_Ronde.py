
def expansion(D):
    """Etend les 32 bits du bloc DO en 48 bits dans Dprime"""
    E=[32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9,10,11,12,13,
       12,13,14,15,16,17,
       16,17,18,19,20,21,
       20,21,22,23,24,25,
       24,25,26,27,28,29,
       28,29,30,31,32, 1]
    Dprime = [D[i-1] for i in E]
    return Dprime

def XOR(b1,b2):
    """OU exclusif entre 2 bits b1 et b2"""
    if b1==1:
        if b2==1:
            return 0
        else:
            return 1
    elif b2==1:
        return 1
    else:
        return 0

def XORL(Dprime,K):
    """Ou exclusif entre Dprime et clé K (48 bits)"""
    D0 = []
    for i in range(48):
        D.append(XOR(Dprime[i], K[i]))
    return D0

def scindement6(D0):
    """Scinde le bloc de 48 en 8 blocs de 6"""
    return D0[0:6], D0[6:12], D0[12:18], D0[18:24], D0[24:30], D0[30:36], D0[36:42], D0[42:48]

def selection1(D01):
    """Sélection pour D01"""
    S1=[[14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7],
        [ 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8],
        [ 4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0],
        [15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13]]
    ligne = int(str(D01[0]*10 + D01[5]), 2)
    colonne = int(str(D01[1]*1000 + D01[2]*100 + D01[3]*10 + D01[4]), 2)
    return S1[ligne][colonne]

def selection2(D02):
    """Sélection pour D02"""
    S2=[[15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10],
        [ 3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5],
        [ 0,14, 7,11,10, 4, 3, 1, 5, 8,12, 6, 9, 3, 2,15],
        [13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9]]
    ligne = int(str(D02[0]*10 + D02[5]), 2)
    colonne = int(str(D02[1]*1000 + D02[2]*100 + D02[3]*10 + D02[4]), 2)
    return S2[ligne][colonne]

def selection3(D03):
    """Sélection pour D03"""
    S3=[[10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1],
        [13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7],
        [ 1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12]]
    ligne = int(str(D03[0]*10 + D03[5]), 2)
    colonne = int(str(D03[1]*1000 + D03[2]*100 + D03[3]*10 + D03[4]), 2)
    return S3[ligne][colonne]

def selection4(D04):
    """Sélection pour D04"""
    S4=[[ 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15],
        [13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9],
        [10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4],
        [ 3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14]]
    ligne = int(str(D04[0]*10 + D04[5]), 2)
    colonne = int(str(D04[1]*1000 + D04[2]*100 + D04[3]*10 + D04[4]), 2)
    return S4[ligne][colonne]

def selection5(D05):
    """Sélection pour D05"""
    S5=[[ 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9],
        [14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6],
        [ 4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14],
        [11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3]]
    ligne = int(str(D05[0]*10 + D05[5]), 2)
    colonne = int(str(D05[1]*1000 + D05[2]*100 + D05[3]*10 + D05[4]), 2)
    return S5[ligne][colonne]

def selection6(D06):
    """Sélection pour D06"""
    S6=[[12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11],
        [10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8],
        [ 9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6],
        [ 4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13]]
    ligne = int(str(D06[0]*10 + D06[5]), 2)
    colonne = int(str(D06[1]*1000 + D06[2]*100 + D06[3]*10 + D06[4]), 2)
    return S6[ligne][colonne]

def selection7(D07):
    """Sélection pour D07"""
    S7=[[ 4, 1, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1],
        [13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6],
        [ 1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2],
        [ 6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12]]
    ligne = int(str(D07[0]*10 + D07[5]), 2)
    colonne = int(str(D07[1]*1000 + D07[2]*100 + D07[3]*10 + D07[4]), 2)
    return S7[ligne][colonne]

def selection8(D08):
    """Sélection pour D08"""
    S8=[[13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7],
        [ 1, 5,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2],
        [ 7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8],
        [ 2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11]]
    ligne = int(str(D08[0]*10 + D08[5]), 2)
    colonne = int(str(D08[1]*1000 + D08[2]*100 + D08[3]*10 + D08[4]), 2)
    return S8[ligne][colonne]

D01 = [0,0,0,0,0,0]
D02 = [0,0,0,0,0,0]
D03 = [0,0,0,0,0,0]
D04 = [0,0,0,0,0,0]
D05 = [0,0,0,0,0,0]
D06 = [0,0,0,0,0,0]
D07 = [0,0,0,0,0,0]
D08 = [0,0,0,0,0,0]

def quatre(chaine):
    """ transforme un nombre (en str) en liste contenant chaque chiffre en int ET normalise en liste de 4 éléments avec des 0 devants"""
    L = []
    for i in chaine:
        L.append(int(i))
    n = len(L)
    if n > 4:
        return 'Erreur longueur liste'
    else:
        for i in range(4-n):
            L.insert(0, int(0))
    return L

def somme(D01, D02, D03, D04, D05, D06, D07, D08):
    """Rassemble les valeurs obtenues, créé la table de 32 bits"""
    Valeurs = [selection1(D01), selection2(D02), selection3(D03), selection4(D04), selection5(D05), selection6(D06), selection7(D07), selection8(D08)]
    print("Valeurs =", Valeurs)
    ValeursBIN = [bin(Valeurs[i])[2:] for i in range(8)]
    print("ValeursBIN =", ValeursBIN) #converti les valeurs décimales en binaires
    ValeursBINlist =[]
    for i in range(8):
        ValeursBINlist.append(quatre(ValeursBIN[i]))
    print("ValeursBINlist =", ValeursBINlist)
    table32 = []
    for i in range(8):
        table32 = table32 + ValeursBINlist[i]
    print("table32 = ", table32)
    print("len(table32) = ", len(table32))
    return table32

def permutation32(L):
    P = [16, 7,	20,	21,	29,	12,	28,	17,
          1,15,	23,	26,	5,	18,	31,	10,
          2, 8,	24,	14,	32,	27,	 3,	 9,
         19,13,	30,	 6,	22,	11,	 4,	25,]
    L = [L[i-1] for i in P]
    return L


##############
S = somme(D01, D02, D03, D04, D05, D06, D07, D08)
print("S = ", S)
print("S permute =", permutation32(S) )

##############

def Ronde(G,D,K):
    ED=[D[i] for i in E]
    Dprim=[XOR(D[i],K[i]) for i in range(48)]
