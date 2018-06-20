from math import exp, sqrt, log

# Attaque p-1 de Pollard

from fractions import gcd

def puissmod(a,d,n):
    dbin=bin(d)
    L=[int(dbin[-i-1]) for i in range(len(dbin)-2)]
    res=1
    while L!=[]:
        k=L.pop(0)
        if k>0:
            res=res*a%n
        a=a**2%n
    return res

def Pollard_p_1(n, B):
    a = 2
    for i in range(2, B+1):
        a =puissmod(a,i,n)
    d = gcd(a-1, n)
    if d > 1 and d < n:
        return d
    return None
    
def Pollard_rho(n, x1=1, f=lambda x: x**2+1):
    x=x1
    y=f(x)%n
    p=pgcd(y-x,n)
    while p==1:
        x=f(x)%n
        y=f(f(y))%n
        p=pgcd(y-x,n)
    if p==n:
        return None
    return p
    
def test_pollard_rho(i,j,pas): #ordre de grandeur de p et q en base 10
    for k in range(i,j,pas):
        n,e,d=RSA_generation(k)
        t1=perf_counter()
        Pollard_rho(n)
        t2=perf_counter()
        print(k,t2-t1,sep=';')
        
#Crible algebrique : Complexe

def Modele_CribleAlgebrique(i,j,pas):
    for x in range(i,j,pas):
        print(x,exp(((64/9)*log(10**x))**(1/3)*(log(log(10**x)))**(2/3)),sep=';')
