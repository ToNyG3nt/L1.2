liste=[1,5,2,7]

def indice(liste):
    minimum=liste[0]
    for i in range(len(liste)):
        if minimum>liste[i]:
            minimuml[i]
    for j in range(len(liste)):
        if liste[j]==minimum:
            indice=j
    print(f"min : {minimum}  indice du min : {indice}")


def puiss2(valeur):
    n=1
    p=2
    while p<=valeur:
        print(f'2^{n}={p}')
        p*=2
        n+=1

            
def presence1(liste,elem):
    if elem in liste:
        print(f"l'element {elem} est dans la liste")
        return True
    print(f"l'element {elem} n'est pas dans la liste")
    return False

def presence2(liste, elem):
    for j in liste:
        if j==elem:
            print(f"l'element {elem} est dans la liste")
            return True
        print(f"l'element {elem} n'est pas dans la liste")
        return False
def presence3(liste,elem):
    n=0
    while n<len(liste):
        if liste[n]==elem:
            print(f"l'element {elem} est dans la liste")
            return True
        n+=1
    print(f"l'element {elem} n'est pas dans la liste")
    return False            


def traduction(A):
    i=0
    while i<len(A):
        print(A[i])
        i+=1


def puiss(x,n):
    if n==1:
        return x
    if n==0:
        return 1
    produit=1
    for i in range(n):
        produit*=x
    return produit

def estPremier(x):
    if x==1 or x==0:
        return False
    if x==2:
        True
    if x%2==0:
        return False
    for i in range(x**0.5):
        if x%i==0:
            return False
    return True
