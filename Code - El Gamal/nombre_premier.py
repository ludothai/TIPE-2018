from random import random
from time import perf_counter
import matplotlib.pyplot as plt

def est_premier(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 


#Plus appliquable au dela de 20 chiffres
def premier(n):
    while n>10:
        if est_premier(n):
            return n
        n-=1
    
    
def premier_Pollard(n):
    eps=10**(-100)
    while n>10:
        if (n-1)/2-int((n-1)/2)<eps:
            if est_premier(int((n-1)/2)):
                if est_premier(n):
                    return n
        n-=1
    
def test(n):
    X=[]
    Y=[]
    for i in range(1,n+1):
        X.append(i)
        k=0
        for j in range(i):
            k+=int(random()*10)*(10**j)
        t1=perf_counter()
        premier(k)
        t2=perf_counter()
        print(i,t2-t1)
        Y.append(t2-t1)
        
    plt.plot(X,Y)
    plt.show()
            
    