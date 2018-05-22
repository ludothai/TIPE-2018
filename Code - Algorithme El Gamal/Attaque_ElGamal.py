from math import sqrt

def puissmod(a,d,n):
    '''a**d mod n'''
    #itératif : beaucoup plus efficace (10^-5) 600 chiffres -> 0.024571632396359178 s
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res

def inversmod(a,p):
    '''a**(-1) mod p'''
    #algorithme d'euclide étendu (solution de l'equation de Bezout)
    r1,u1,v1,r2,u2,v2=a,1,0,p,0,1

    while r2!=0:
        q=r1//r2
        r1,u1,v1,r2,u2,v2=r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2
    if r1!=1:
        return 'pas inversible'
    else:
        return u1


#Pas de bebe,pas de geant (SHANKS)
#O(exp(p))
def shanks(p,g,x): #retourne n tel que x=g**n mod p
    K=int(sqrt(p))+1
    A=[(puissmod(g,i,p),i) for i in range(1,K)]
    A.sort(key=lambda x:x[0])
    print(A)
    for j in range(1,K):
        b=(x*inversmod(puissmod(g,K*j,p),p))%p
        print(b)
        if b<int(p/2): #On parcours A dans l'ordre croissant
            i=0
            while i<K-2 and b>A[i][0]:
                i+=1
            if A[i][0]==b:
                return A[i][1]+K*j
        else: #On parcours A dans l'ordre décroissant
            i=K-2
            while i>0 and b<A[i][0]:
                i-=1
            if A[i][0]==b:
               return A[i][1]+K*j


#p,g,x=457,13,255
#print(p,g,x,shanks(p,g,x))

#Calcule de l'indice (Complexe)



