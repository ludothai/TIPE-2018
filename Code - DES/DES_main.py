# -*- coding: utf-8 -*-

K = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,1,0, 1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0]
key = genKey(K)

m = "hello"
M = encodage(m)

M64 = decoupe64(M)
print("M64=", M64)

# on travaille avec M liste de 64 bits
#permutation initiale

