# -*- coding: utf-8 -*-

K = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,1,0, 1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0]
#K = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
key = genKey(K)

m = "hello"
M = encodage(m)

M64 = decoupe64(M) 
print("M64=", M64)

M0 = M64[0]

print("M0=", M0)
print()
# on travaille avec M0 liste de 64 bits

#permutation initiale
Mpermini = permutation_initiale(M0)
print("Mpermini=", Mpermini)
print()

#scindement
G,D =  scindement2(Mpermini)
print("G=", G)
print("D=", D)
print()

GD = []

Gi = G
Di = D 
GD.append([Gi, Di])

print("i= -1")
print()
print("G -1 =", Gi)
print("D -1 =", Di)
print()
print()

#ronde
for i in range(16):
    print("i=", i)
    Dexpand= expansion(Di)
    X = XORL(Dexpand, key[i])
    Si = selection(X)
    Ti = permutation32(Si)
    Di = XORL(Gi, Ti)
    Gi = Di
    print()
    print("G",i,"=", Gi)
    print("D",i,"=", Di)
    GD.append([Gi,Di])
    print()
    print()
    
#regroupement 
R = Gi + Di 

#permutation inverse
M0c = permutation_inverse(R)
print(decodage(M0c))

