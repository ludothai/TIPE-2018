# Attaque p-1 de Pollard

from fractions import gcd

def pollard(n, B):
    a = 2
    for i in range(2, B+1):
        a = (a**i) % n
    d = gcd(a-1, n)
    if d > 1 and d < n:
        return d
    return None