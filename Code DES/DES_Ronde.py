#Ronde du DES

def XOR(b1,b2):
    if b1==1:
        if b2==1:
            return 0
        else:
            return 1
    elif b2==1:
        return 1
    else:
        return 0

def Ronde(G,D,K):
    ED=[D[i] for i in E]
    Dprim=[XOR(D[i],K[i]) for i in range(48)]
    