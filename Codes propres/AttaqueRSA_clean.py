from math import exp, sqrt, log
from fractions import gcd

# Attaque p-1 de Pollard

def Pollard_p_1(n, B):
    a=2
    for i in range(2,B+1):
        a=puissmod(a,i,n)
    d=gcd(a-1, n)
    if d>1 and d<n:
        return d
    return None
    
def Pollard_rho(n, x1=1, f=lambda x: x**2+1):
    x=x1
    y=f(x)%n
    p=gcd(y-x,n)
    while p==1:
        x=f(x)%n
        y=f(f(y))%n
        p=gcd(y-x,n)
    if p==n:
        return None
    return p

#Crible algebrique : Complexe

def Modele_CribleAlgebrique(i,j,pas):
    for x in range(i,j,pas):
        print(x,exp(((64/9)*log(10**x))**(1/3)*(log(log(10**x)))**(2/3)),sep=';')
