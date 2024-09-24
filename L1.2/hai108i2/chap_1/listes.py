liste=[4,10,2,24,1,10]

def exercice1(l1):
    somme=0
    for i in l1:
        somme+=i
    produit=1
    if len(l1)==0:
        produit=0
    else :
        for k in l1:
            produit*k
    sommePairs=1
    for j in l1:
        if j%2==0:
            sommePairs+=i
    print(f"la somme des elements est: {somme}")
    print(f"le produit des elements est: {produit}")
    print(f"la somme des element pairs est: {sommePairs}")


def exercice2(l1):
    min=l1[0]
    if l1[1]<min:
        max=min
        min=l1[0]
    else:
        max=l1[1]
    for i in l1:
        if i<min:
            min=i
        if i>max:
            max=i
    print(f"le minimum de la liste est:{min}")
    print(f"le maximum de la liste est:{max}")
    

def exercice2_1(l,x):
    if x in l:
        print(f"l'element {x} est dans la liste")
        return True
    else:
        print(f"l'element {x} n'est pas dans la liste")
        return False
        
def exercice2_2(l,x):
    occ=0
    for elem in l:
        if elem==x:
            occ+=1
    print(f"il y a {occ} fois l'element {x} dans la liste")


def exercice3_1(l):
    for elem in l:
        if elem%2==0:
            print("la liste  contient des nombres pairs")
            return False
    print("la liste ne contient pas d'elements pairs")
    return False

def exercice3_2(l):
    occImpair=0
    for elem in l:
        if elem%2!=0:
            occImpair+=1
    if occImpair==1:
        print("il y a 1 nombre impair dans la liste")
        return True
    else:
        print(f"il y a {occImpair} nombre impair(s) dans la liste")
        return False


def exercice3_3(l):
    for elem in l:
        if elem%2==0:
            print("il y a au moins un element pair dans la liste")
            return False
    print("il n'y a que des nombres impairs dans la liste")
    return True

def exercice4(chaine):
    voyelle=0
    consonne=0
    autre=0
    v=['a','e','y','u','i','o']
    c=['z','r','t','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']
    for char in chaine:
        if char in v:
            voyelle+=1
        elif char in c:
            consonne+=1
        else:
            autre+=1
    print(f"il y a {voyelle} voyelles, {consonne} consonnes et {autre} characteres autres dans '{chaine}'")


#exercice 5: EZ

#exercice 6: meme que l'exercice 2

def exercice7(x):
    for i in range(2,x-1):
        if x%i==0:
            print(f"l'entier {x} n'est pas premier")
            return False
