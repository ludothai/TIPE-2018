# 1 Permutation initiale
def permutation_initiale(L):
    """Permute les élements de L selon l'ordre de permutation défini par PI"""
    PI=[58,50,42,34,26,18,10, 2,
        60,52,44,36,28,20,12, 4,
        62,54,46,38,30,22,14, 6,
        64,56,48,40,32,24,16, 8,
        57,49,41,33,25,17, 9, 1,
        59,51,43,35,27,19,11, 3,
        61,53,45,37,29,21,13, 5,
        63,55,47,39,31,23,15, 7] #Liste de permutation initiale
    L=[L[i-1] for i in PI]
    return L

def scindement2(L):
    """Retourne le scindement de L en 2 listes G0 et D0 de de 32 bits"""
    return L[0:32], L[32:64]
