def permutationCP1(K):
    """Effectue la permutation initiale de la clé de 64 bits, retourne les listes G0 et D0"""
    if len(K) != 64 : return "Erreur len(K)"
    else:
        K1 = []
        CP1=[57,49,	41,	33,	25,	17,	9,	1,	58,	50,	42,	34,	26,	18,
            10,	2,	59,	51,	43,	35,	27,	19,	11,	3,	60,	52,	44,	36,
            63,	55,	47,	39,	31,	23,	15,	7,	62,	54,	46,	38,	30,	22,
            14,	6,	61,	53,	45,	37,	29,	21,	13,	5,	28,	20,	12,	4]
        for i in CP1:
            K1.append(K[i-1])
        return K1[:28], K1[28:]

def rotationGauche(L):
    """ Rotation à gauche de L:  les bits en seconde position prennent la première position, ceux en troisième position la seconde, ...
Les bits en première position passent en dernière position."""
    n = len(L)
    L.append(L[0])
    L.pop(0)
    return L

def regroup(G,D):
    return G+D

def permutationCP2(K):
    """Effectue la permutation CP2 du bloc de 56 bits en un bloc de 48 bits qui est la clé Ki"""
    if len(K) != 56 : return "Erreur len(K)"
    else:
        Ki = []
        CP2=[14,17, 11,	24,	 1,	5,	3,	28,	15,	6,	21,	10,
            23,	19,	12,	 4,	26,	8,	16,	7,	27,	20,	13,	 2,
            41,	52,	31,	37,	47,	55,	30,	40,	51,	45,	33,	48,
            44,	49,	39,	56,	34,	53,	46,	42,	50,	36,	29,	32]
        for i in CP2:
            Ki.append(K[i-1])
        return Ki

def genKey(L):


def gen(n):
    return ([(i+1)*10 for i in range(n)])

K = gen(64)

print(K)
print(permutationCP1(K))
print(rotationGauche(K))
