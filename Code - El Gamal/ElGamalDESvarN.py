from random import randint
from time import perf_counter


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
        if u1<1:
            while u1<1:
                u1+=p
        if u1>p:
            while u1>p:
                u1-=p
        return u1


#Fonctions de ElGamal

def generation_cle(p,g):
    '''p premier,g générateur'''
    cle_priv=randint(1,p-1)
    cle_publ=puissmod(g,cle_priv,p)
    return cle_priv,cle_publ

def chiffrement(p,g,cle_dest,message_clair,sign=False):
    k1=randint(1,p-1)
    cle_sess=puissmod(cle_dest,k1,p)
    message_crypt=(message_clair*cle_sess)%p
    entete=puissmod(g,k1,p)
    if sign:
        r,s=signature(p,g,k1,message_crypt)
        return r,s,entete,message_crypt
    else:
        return k1,entete,message_crypt

def signature(p,g,k1,message_crypt):
    k2=randint(1,p-1)
    k2inv=inversmod(k2,p-1)
    while type(k2inv)==str: #tant que le k aléatoire n'est pas inversible mod p-1
        k2=randint(1,p-1)
        k2inv=inversmod(k2,p-1)
    r=puissmod(g,k2,p)
    h=message_crypt
    s=((h-k1*r)*k2inv)%(p-1)
    return r,s

def verification_signature(p,g,r,s,entete,message_crypt):
    h=message_crypt
    a=puissmod(g,h,p)
    b=(puissmod(entete,r,p)*puissmod(r,s,p))%p
    if a==b:
        return True
    else:
        return False


def dechiffrement(p,g,cle_priv,entete,message_crypt):
    cle_sess=puissmod(entete,cle_priv,p)
    message_clair=(message_crypt*inversmod(cle_sess,p))%p
    return message_clair

#Choix p à 200 chiffres

def chiffrementDES(p,g,cle_dest,m):
    k1=randint(1,p-1)
    cle_sess=puissmod(cle_dest,k1,p)
    entete=puissmod(g,k1,p)
    c=DES(m, cle_sess)
    return k1, entete, c

def dechiffrementDES(p,g,cle_priv,entete,c):
    cle_sess=puissmod(entete, cle_priv, p)
    m = DES_(c, cle_sess)
    return m

def blabla(k):
    m = ""
    L = ['a', 'b', 'c', 'd','e', 'f', 'g', 'z' ,'h', 'i', 'j','k','l','m']
    for i in range(k):
        j = randint(0,10)
        m = m+ L[j]
    return m

def listTOstrBIN(L):
    """prend une liste binaire, retourne str(binaire) de la liste"""
    b = ""
    for i in range(len(L)):
        b = b+ str(L[i])
    return b

def testElDES(i,j,pas): #taille du message en nombre de caractères
    '''taille;tchif;tdechif;tsign;tverif'''
    print("n;Tchif;Tdechif")
    global P
    global G
    for k in range(i,j,pas):
        Tchif=[]
        Tdechif=[]
        for s in range(10):
            p,g=P[s],G[s]
            cle_dest=randint(1,p-1)

            m = blabla(k)

            tchif=0
            tdechif=0

            t1=perf_counter()
            k1,entete,c =chiffrementDES(p,g,cle_dest,m)
            t2=perf_counter()
            tchif+=t2-t1

            t1=perf_counter()
            dechiffrementDES(p,g,cle_dest,entete,c)
            t2=perf_counter()
            tdechif+=t2-t1


# -------------

#            q=k//83
#            r=k-q
#            max=sum([2**pui for pui in range(8*r)])
#            B_clair=[randint(1,p-1) for i in range(q)]+[randint(1,max)]
#            tchif=0
#            tdechif=0
#            tsign=0
#            tverif=0
#            for bloc in B_clair:
#
#                t1=perf_counter()
#                k1,entete,bloc_crypt=chiffrement(p,g,cle_dest,bloc)
#                t2=perf_counter()
#                tchif+=t2-t1
#
#                t1=perf_counter()
#                r,s=signature(p,g,k1,bloc_crypt)
#                t2=perf_counter()
#                tsign+=t2-t1
#
#                t1=perf_counter()
#                dechiffrement(p,g,cle_dest,entete,bloc_crypt)
#                t2=perf_counter()
#                tdechif+=t2-t1
#
#                t1=perf_counter()
#                verification_signature(p,g,r,s,entete,bloc_crypt)
#                t2=perf_counter()
#                tverif+=t2-t1


            Tchif.append(tchif)
            Tdechif.append(tdechif)


        print(k,sum(Tchif)/10,sum(Tdechif)/10,sep=';')

P=[198813605729928448136287614423728297327061207877861229430286974890873557576637442197286607275014958894550700186891638160293159770508452411643121350294666316275401363114370104435755411502517549980165487429,
103597476818069762936904055157627805821271466994648940082351220992463959289504033398520796884824329947238998522733158996002797313594854346171908244046866467053786690358933853505996134065563718654527123359,
13472140925514330066456585131595637632738190306421422874304187469757372506491072663372991092271894613375291732817119956707512514556719972935996533010543789792150677145914743920275901742907886757606675787,
73882813132060031760529064324755331893148109278542764211474659802780314644894543086667374170748035765316587361298556347528801733353169082965717429069347980693730954113583675512387084148128509271657778839,
144415999329285818770580238092297107470748283986235700478451556439415722402243581041899756675555232489312091817168166400182095885302500563599229625509427424552612837019920284094655683618446379065086804321,
82813207632312480112894756905230446103686358331459842271619091895558759337283933258391183335548266737236220161818235934050314703857788353433094389034293641450464883929048398822384771698088937966079686583,
18049511082835056139925898851182647171947844531500133418310833629679834022821355551279070279497637505418146398526065765797236254021855653004220056400378772235963566754554372734551757638670428678891712877,
27565295220194786304983195993494132818186288578273287691579290272300313710302674708965253581790208401009947495332238107549586940386522526048422572955821862351989347580368656057571682157159673662924465767,
29582505600953218173873005225917292724138448474087574341814649206011588972730237766239850227900312060179299011394663689715948488718009209365660557717415152289370494491217731392454994410417278019663585697,
19565749895309177061951949398211010292900008107475428351099987520149355920153790602291736205102412965911234147581124020334696455215803578360471279266721949587153052013018516860800603252597702150957817809]


G=[73733910262437546073261585967075005486545280632052327407534396561997845123661439786270513001864908070327503261826006041366399302868613302146676703836765556035486045494327029720505227055129743739366446332,
23015292162350088395278990178924433414790422865988933280447440409035838174380095703875478864445602557000900901941395643255723215670843340114127103367150837435641982680421303931142520505330447950442170177,
1720239439958927946738921154104803601546686777362315938306562402427646085064548422241120527877299824518893246151280264467908818507656670809927587610660913177590040316656006905800535977781829081198264539,
36764460697870597314115252103461832878488184438335900951640000958553050690772514843429039096312225188847557375549300298081009619015839711103354619509626234609545615573372453253151358072912264054617782084,
86767407668537145580173120581807718534585637796405443712295176100130671133366063472444165714248276186631017884518464468018207482660394322518477695291738763492089795647195848169010910951834896778944978240,
77866519192118256099156481690399723917897193303201078628034106367823671721167154239578863766565458369024273770410117551177329145511132243318694336412600105440203112326842514613618487629773961405148229028,
13456854629267850985057000845160571393772094609203367150575461016242531115409479944233751453388375171040143718093772709817478472525046788088900162985659365591259891707404239976150865842189504473426173350,
27118237750485310359107237716555929745024869750003202766904002525720144210999928018406255888691636242782689884611828303252079636927328166564499658182990118141642446310429357228564913141945521523557906089,
24555365918634763120372030818318705273515741447745860647390524556591860623450602276587923926464525072091688285806978551833356391907858122176153150612530607918932152492043035262875025777890728916170417068,
5349568394114725607101576572671959710657324371039153118504505862768445065610704205209996477322006530899399491647720754210085134943357856079453938523760329504372458549212034606957688749244813442893714495]

# ***************************** ENCODAGE DES CARACTERES *****************************
#Codage du message 1 caractere = 8 bits

def encodage(m):
    """Message en STRING retourné en binaire 8 bits (table AISCII)"""
    if type(m) != str :
        raise TypeError
    M = list(m) # on split tout en caracteres individuels
    Mord = [ord(M[i]) for i in range(len(M))]
    Mbin = [bin(Mord[i]) for i in range(len(M))]
    # traitement du Mbin pour enlever le '0b' du debut et taille constante
    Mfin=[]
    for binaire in Mbin:
        binaire=binaire[2:]
        n=len(binaire)
        if n>8:
            return 'Erreur len(binaire)'
        for i in range(8-n): # complète avec des zéros
            Mfin.append(0)
        for i in binaire:
            Mfin.append(int(i))
#    print("m=",m)
#    print("M=",M)
#    print("Mord=",Mord)
#    print("Mbin=",Mbin)
#    print("Mfin=",Mfin)
#    print()
    return Mfin

def decodage(M):
    n=len(M)//8
    Mfin=[str(i) for i in M]
    Mbin=[]
    for i in range(n):
        binaire=Mfin[i*8]
        for j in range(1,8):
            binaire+=Mfin[i*8+j]
        Mbin.append(binaire)
    Mord=[int(binaire,2) for binaire in Mbin]
    Mchr=[chr(i) for i in Mord]
    m=Mchr[0]
    for i in range(1,len(Mchr)):
        m+=Mchr[i]
    return m

# ***************************** GENERATION DES CLES *****************************
def permutationCP1(K):
    """Effectue la permutation initiale de la cle de 64 bits, retourne les listes G0 et D0"""
    if len(K) != 64 : return "Erreur len(K)"
    else:
        K1 = []
        CP1=[57,49,41,33,	25,17, 9, 1,58,50,42,34,26,18,
             10, 2,59,51,	43,35,27,19,11, 3,60,52,44,36,
             63,55,47,39,	31,23,15, 7,62,54,46,38,30,22,
             14, 6,61,53,	45,37,29,21,13, 5,28,20,12, 4]
        for i in CP1:
            K1.append(K[i-1])
        return K1[:28], K1[28:]

def decalageGauche(L, n):
    """ Decale les elements de la liste L de n places vers la GAUCHE"""
    Ldec = []
    for i in range(len(L)-n):
        Ldec.append(L[i+n])
    for i in range(n):
        Ldec.append(L[i])
    return Ldec

def regroupe(G,D):
    return G+D

def permutationCP2(K):
    """Effectue la permutation CP2 du bloc de 56 bits en un bloc de 48 bits qui est la clé Ki"""
    if len(K) != 56 : return "Erreur len(K)"
    else:
        Ki = []
        CP2=[14,17,11,24,	 1, 5, 3,28,15, 6,21,10,
             23,19,12, 4,	26, 8,16, 7,27,20,13, 2,
             41,52,31,37,	47,55,30,40,51,45,33,48,
             44,49,39,56,	34,53,46,42,50,36,29,32]
        for i in CP2:
            Ki.append(K[i-1])
        return Ki

def genKey(K):
    """ Retourne les 16 cles Ki a partir de la cle de 64 bits"""
    decalage = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] #Nombre de decalage a gauche pour les 16 iterations (de 0 a 15)
    cles = []
    #verification cle est de 64 bits:
    if checkBINn(K, 64) == False: return "Erreur sur la cle initilale K"
    # permutation initiale CP1:
    G, D = permutationCP1(K)
#    print("Gk=", G)
#    print("Dk=", D)
#    print("")
    if checkBINn(G, 28) == False: return "Erreur sur la cle initiale G"
    if checkBINn(D, 28) == False: return "Erreur sur la cle initiale D"
    for i in range(16):
        Gi = decalageGauche(G, decalage[i])
        Di = decalageGauche(D, decalage[i])
#        print("Gk",i,"=",Gi)
#        print("Dk",i,"=",Di)
        Ki = permutationCP2(regroupe(Gi, Di))
#        print("K",i,"=",Ki)
#        print()
        if checkBINn(Ki, 48) == False: return "Erreur sur la cle Ki"
        cles.append(Ki)
        G = Gi
        D = Di

    return cles

def checkBINn(L, n):
    """ verifie que la liste L est une liste contenant n elements binaire (0 ou 1)"""
    binaire = [0,1]
    if len(L)==n:
        for i in range(len(L)):
            if L[i] not in binaire:
                return False
        return True
    else:
        return False

def gen(n):
    return ([(i+1)*10 for i in range(n)])



# ***************************** PERMUTATIONS *****************************
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
    Q=[L[i-1] for i in PI]
#    print("Permutation initiale:", Q)
#    print()
    return Q

def scindement2(L):
    """Retourne le scindement de L en 2 listes G0 et D0 de de 32 bits"""
    return L[0:32], L[32:64]

def permutation_inverse(L):
    """Permute les élements de L selon l'ordre de permutation défini par PII = permutation initiale inverse"""
    PII=[40,8,48,16,56,24,64,32,
         39,7,47,15,55,23,63,31,
         38,6,46,14,54,22,62,30,
         37,5,45,13,53,21,61,29,
         36,4,44,12,52,20,60,28,
         35,3,43,11,51,19,59,27,
         34,2,42,10,50,18,58,26,
         33,1,41, 9,49,17,57,25]
    Q=[L[i-1] for i in PII]
#    print("permutation initiale inverse:", Q)
#    print()
    return Q

# ***************************** RONDE *****************************

def expansion(D):
    """Etend les 32 bits du bloc DO en 48 bits dans Q"""
    E=[32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9,10,11,12,13,
       12,13,14,15,16,17,
       16,17,18,19,20,21,
       20,21,22,23,24,25,
       24,25,26,27,28,29,
       28,29,30,31,32, 1]
    Q = [D[i-1] for i in E]
#    print("expansion: ",Q)
    return Q

def XOR(b1,b2):
    """OU exclusif entre 2 bits b1 et b2"""
    if b1==1:
        if b2==1:
            return 0
        else:
            return 1
    elif b2==1:
        return 1
    else:
        return 0

def XORL(Dprime,K):
    """Ou exclusif entre Dprime et clé K (48 bits)"""
    D0 = []
    for i in range(len(Dprime)):
        D0.append(XOR(Dprime[i], K[i]))
    return D0

def scindement8(D0):
    """Scinde le bloc de 48 en 8 blocs de 6"""
    return [D0[0:6], D0[6:12], D0[12:18], D0[18:24], D0[24:30], D0[30:36], D0[36:42], D0[42:48]]

def selection1(D01):
    """Sélection pour D01"""
    S1=[[14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7],
        [ 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8],
        [ 4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0],
        [15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13]]
    ligne = int(str(D01[0]*10 + D01[5]), 2)
    colonne = int(str(D01[1]*1000 + D01[2]*100 + D01[3]*10 + D01[4]), 2)
    return S1[ligne][colonne]

def selection2(D02):
    """Sélection pour D02"""
    S2=[[15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10],
        [ 3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5],
        [ 0,14, 7,11,10, 4, 3, 1, 5, 8,12, 6, 9, 3, 2,15],
        [13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9]]
    ligne = int(str(D02[0]*10 + D02[5]), 2)
    colonne = int(str(D02[1]*1000 + D02[2]*100 + D02[3]*10 + D02[4]), 2)
    return S2[ligne][colonne]

def selection3(D03):
    """Sélection pour D03"""
    S3=[[10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1],
        [13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7],
        [ 1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12]]
    ligne = int(str(D03[0]*10 + D03[5]), 2)
    colonne = int(str(D03[1]*1000 + D03[2]*100 + D03[3]*10 + D03[4]), 2)
    return S3[ligne][colonne]

def selection4(D04):
    """Sélection pour D04"""
    S4=[[ 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15],
        [13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9],
        [10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4],
        [ 3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14]]
    ligne = int(str(D04[0]*10 + D04[5]), 2)
    colonne = int(str(D04[1]*1000 + D04[2]*100 + D04[3]*10 + D04[4]), 2)
    return S4[ligne][colonne]

def selection5(D05):
    """Sélection pour D05"""
    S5=[[ 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9],
        [14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6],
        [ 4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14],
        [11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3]]
    ligne = int(str(D05[0]*10 + D05[5]), 2)
    colonne = int(str(D05[1]*1000 + D05[2]*100 + D05[3]*10 + D05[4]), 2)
    return S5[ligne][colonne]

def selection6(D06):
    """Sélection pour D06"""
    S6=[[12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11],
        [10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8],
        [ 9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6],
        [ 4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13]]
    ligne = int(str(D06[0]*10 + D06[5]), 2)
    colonne = int(str(D06[1]*1000 + D06[2]*100 + D06[3]*10 + D06[4]), 2)
    return S6[ligne][colonne]

def selection7(D07):
    """Sélection pour D07"""
    S7=[[ 4, 1, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1],
        [13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6],
        [ 1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2],
        [ 6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12]]
    ligne = int(str(D07[0]*10 + D07[5]), 2)
    colonne = int(str(D07[1]*1000 + D07[2]*100 + D07[3]*10 + D07[4]), 2)
    return S7[ligne][colonne]

def selection8(D08):
    """Sélection pour D08"""
    S8=[[13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7],
        [ 1, 5,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2],
        [ 7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8],
        [ 2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11]]
    ligne = int(str(D08[0]*10 + D08[5]), 2)
    colonne = int(str(D08[1]*1000 + D08[2]*100 + D08[3]*10 + D08[4]), 2)
    return S8[ligne][colonne]

def quatre(chaine):
    """ transforme un nombre (en str) en liste contenant chaque chiffre en int ET normalise en liste de 4 éléments avec des 0 devants"""
    L = []
    for i in chaine:
        L.append(int(i))
    n = len(L)
    if n > 4:
        return 'Erreur longueur liste'
    else:
        for i in range(4-n):
            L.insert(0, int(0))
    return L

def somme(D01, D02, D03, D04, D05, D06, D07, D08):
    """Rassemble les valeurs obtenues, créé la table de 32 bits"""
#    print("Bloc de 6: ",D01, D02, D03, D04, D05, D06, D07, D08)
    Valeurs = [selection1(D01), selection2(D02), selection3(D03), selection4(D04), selection5(D05), selection6(D06), selection7(D07), selection8(D08)]
#    print()
#    print("Valeurs =", Valeurs)
    ValeursBIN = [bin(Valeurs[i])[2:] for i in range(8)]
#    print("ValeursBIN =", ValeursBIN) #converti les valeurs décimales en binaires
    ValeursBINlist =[]
    for i in range(8):
        ValeursBINlist.append(quatre(ValeursBIN[i]))
#    print("ValeursBINlist =", ValeursBINlist)
    table32 = []
    for i in range(8):
        table32 = table32 + ValeursBINlist[i]
#    print()
#    print("table32 = ", table32)
#    print("len(table32) = ", len(table32))
    return table32

def selection(D0):
    """Etape de selection d'une liste D0 de 48 bits en une liste de 32 bits"""
    #vérification
    if checkBINn(D0, 48) == False : return "Erreur LO"
    #scindement :
    D0i = scindement8(D0)
    return somme(D0i[0], D0i[1], D0i[2], D0i[3], D0i[4], D0i[5], D0i[6], D0i[7])

def permutation32(L):
    P = [16, 7,20,21,29,12,28,17,
          1,15,23,26, 5,18,31,10,
          2, 8,24,14,32,27, 3, 9,
         19,13,30, 6,22,11, 4,25,]
    Q = [L[i-1] for i in P]
#    print("permutation 32 :", Q)
    return Q

# ***************************** ENCODAGE CLE *****************************

def intbin(K):
    """ Retourne l'entier positif K en binaire dans une liste L"""
    if type(K) != int: return "Erreur type K"
    if K < 0: return "Erreur 'K est negatif'"
    kbinstr = list(bin(K))
    kbinstr = kbinstr[2:]
    # kbin = [int(kbinstr[i]) for i in range(len(kbinstr))]
    kbin = [int(i) for i in kbinstr]
    return kbin

def binint(L):
    """ Retourne la liste binaire L en entier positif """
    if checkBINn(L, len(L)) == False : return "Erreur liste L"
    N =''
    for i in range(len(L)):
        N+=str(L[i])
    return int(N,2)

def min64(L):
    """ Verifie et normalise avec des 0 devants la liste L tel que contienne au moins 64 bits """
    if len(L)>63 :
        return L
    else:
        n = len(L)
        Q = L[:]
        Q.reverse()
        for i in range(64-n):
            Q.append(int(0))
        Q.reverse()
        return Q

# ***************************** FONCTIONS DE DECOUPAGE *****************************
espace = [0, 0, 1, 0, 0, 0, 0, 0] #(ord 32) Caractere [espace] en binaire 8 bits AISCII

def decoupe64(l):
    """ decoupe une chaine binaire en bloc de 64 bits et completant les vides par des 'espaces' """
    B = [] #Liste BLOCs, resultat
    L = l[:] #copie L
    n  = len(L)
    r = n % 64 # reste de la division euclidienne de n par 64
    nesp = (64-r)//8 #nombre de caractee 'espace' a  ajouter pour complater L

    if r != 0 : #si len(L) n'est pas un multiple de 64, on complate L avec des 'espaces'
        for i in range(nesp): #on ajoute le caractare 'espace' nesp fois
            L+=espace

    q = len(L) // 64 # quotient : [nombre elements de L]/64 = nombre de sous liste a  creer
    for i in range(q):
        SB =[] #Sous bloc (temp)
        for j in range(64):
            SB.append(L.pop(0)) #on pop et on ajoute en meme temps
        B.append(SB)
    return B

def assembler(B):
    """regroupe liste contenant des sous-listes (bloc de 64) en une liste"""
    L = [] #resultat
    for i in range(len(B)):
        L+=B[i]
    return L


# ***************************** FONCTION DE VERIFICATION *****************************

def checkBINn(L, n):
    """ verifie que la liste L est une liste contenant n elements binaire (0 ou 1)"""
    binaire = [0,1]
    if len(L)==n:
        for i in range(len(L)):
            if L[i] not in binaire:
                return False
        return True
    else:
        return False

# ***************************** MAIN *****************************

def DESc(M, K):
    """ Crypte le message M (binaire de 64 bits) avec la clé K (binaire de 64 bits) par la methode du DES"""
    #Verification
    if checkBINn(M, 64) == False: return 'Erreur M'
    if checkBINn(K, 64) == False: return 'Erreur K'

    #Calcul des cles
    key = genKey(K)

#    print("-----------------------------------------------")

    #permutation initiale
    MPI = permutation_initiale(M)
#    print()

    #scindement
    G,D =  scindement2(MPI)
#    print("G=", G)
#    print("D=", D)
#    print()
#    print()

    #initialisation de la ronde
    Gi = G
    Di = D
#    print("i= *")
#    print()
#    print("G * =", Gi)
#    print("D * =", Di)
#    print()
#    print()

    #ronde
    for i in range(16):
#        print("i=", i)
#        print()
        Dexpand= expansion(Di)
        Xi = XORL(Dexpand, key[i])
#        print("XORL",i,"=", Xi)
        Si = selection(Xi)
        Ti = permutation32(Si)
        Gi, Di = Di,  XORL(Gi, Ti)
#        print()
#        print("G",i,"=", Gi)
#        print("D",i,"=", Di)
#        print()
#        print()

    #regroupement INVERSE
    R = Di + Gi

    #permutation inverse
    return permutation_inverse(R)



def DESd(M, K):
    """ Decrypte le message M (binaire de 64 bits) avec la clé K (binaire de 64 bits) par la methode du DES"""
    #Verification
    if checkBINn(M, 64) == False: return 'Erreur M'
    if checkBINn(K, 64) == False: return 'Erreur K'

    #Calcul des cles
    key = genKey(K)
    key.reverse()

#    for j in range(len(key)):
#        print("K.r",j,"=",key[j])
#        print()

#    print("-----------------------------------------------")

    #permutation initiale
    MPI = permutation_initiale(M)
#    print()

    #scindement
    G,D =  scindement2(MPI)
#    print("G=", G)
#    print("D=", D)
#    print()
#    print()

    #initialisation de la ronde
    Gi = G
    Di = D
#    print("i= *")
#    print()
#    print("G * =", Gi)
#    print("D * =", Di)
#    print()
#    print()

    #ronde
    for i in range(16):
#        print("i=", i)
#        print()
        Dexpand= expansion(Di)
        Xi = XORL(Dexpand, key[i])
#        print("XORL",i,"=", Xi)
        Si = selection(Xi)
        Ti = permutation32(Si)
        Gi, Di = Di,  XORL(Gi, Ti)
#        print()
#        print("G",i,"=", Gi)
#        print("D",i,"=", Di)
#        print()
#        print()

    #regroupement INVERSE
    R = Di + Gi

    #permutation inverse
    return permutation_inverse(R)

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

def aide():
    print("-----------------------------------------")
    print("************* FONCTIONEMENT *************")
    print("-----------------------------------------")
    print()
    print("FONCTION CRYPTAGE DES(m, K)")
    print("_____________________")
    print("--> permet de crypter un message m avec K")
    print("1. m est un message en clair - str")
    print("2. K est la cle de cryptage - entier naturel")
    print()
    print()
    print("FONCTION DECRYPTAGE DES_(M, K)")
    print("______________________")
    print("--> permet de decrypter un message M cryte avec K")
    print("1. M est un message crypte avec K - liste de contenant des 0 et 1")
    print("2. K est la cle de decryptage - entier naturel")
    print()
    print("-----------------------------------------")
    print("****************** FIN ******************")
    print("-----------------------------------------")

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def DES(m, K):
    """ Crypte le message m (str) avec la cle K (entier), retourne liste binaire correpondant a m crypter en AISCII """
    #Verification:
    if type(m) != str: return "Erreur type m"
    if type(K) != int: return "Erreur type K"

    Kentiere = intbin(K)
#    print("Kentiere =", Kentiere)
#    print()
    Kentiere = min64(Kentiere) #pour avoir une clé binaire de taille 64 bits minimum
    Kentiere.reverse()
#    print("Kentiere normaliser inverse=", Kentiere)
#    print()

    key = Kentiere[:64]
#    print("Cle =", K,"-->", "key =",key )
#    print()
#    cles = genKey(key)
#    print()
#    for i in range(16):
#        print("Sous-cle",i,"=",cles[i])
#        print()

    M = decoupe64(encodage(m))
    n = len(M) # nombre de blocs de 64 bits
    Mc = [] # M crypte
    for i in range(n):
        Mc.append(DESc(M[i], key))

    return assembler(Mc)

def DES_(M, K):
    """ Decrypte le message M (liste binaire) avec la cle K (entier), message m en claire  """
    #Verification:
    if checkBINn(M, len(M)) == False : return "Erreur M"
    if type(K) != int: return "Erreur type K"

    Kentiere = intbin(K)
#    print("Kentiere =", Kentiere)
#    print()
    Kentiere = min64(Kentiere) #pour avoir une clé binaire de taille 64 bits minimum
    Kentiere.reverse()
#    print("Kentiere normaliser inverse=", Kentiere)
#    print()

    key = Kentiere[:64]
#    print("Cle =", K,"-->", "key =",key )
#    print()
#    cles = genKey(key)
#    print()
#    for i in range(16):
#        print("Sous-cle",i,"=",cles[i])
#        print()

    Mc = decoupe64(M)
#    print("Mc =",Mc)
    n = len(Mc) # nombre de blocs de 64 bits
    Mclair = [] # M decrypte
    for i in range(n):
        Mclair.append(DESd(Mc[i], key))

#    return decodage(assembler(Mclair))


print("Entrer 'aide()' pour le fonctionnement")


testElDES(1,10000,10)
