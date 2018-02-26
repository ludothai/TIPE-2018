def premier(n):
    """ Renvoie le premier nombre premier inférieur à n."""
    n += 1
    tableau = [0,0] + [i for i in range(2, n)]
    for i in range(2, n):
        if tableau[i] != 0:
            # c'est un nombre 1er: on garde, mais on neutralise ses multiples
            for j in range(i*2, n, i):
                tableau[j] = 0
    L= [p for p in tableau if p!=0]
    return L[len(L)-1]
