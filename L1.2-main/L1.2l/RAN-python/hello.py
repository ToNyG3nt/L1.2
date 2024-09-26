
lsite:[4,5,8,9,6,6,7,2,6,8,2,4,7,5,8,6,4,7,6,8,8,5,6,6]



#print("hello world!")
#print("bonjour le monde!")
#exercice 1
#print(f"la puissance 6 des 3 dernier chiffre de 1234567 est : {(1234567**6) % 1000}") 

#exercice 2

def divavecif(nbre):
    if nbre%5 == 0:
        a=1
    else:
        a=0
    if nbre%7 ==0:
        a+=1
    if a==0 or a== 2:
        return False
    else :
        return True

def divsansif(nbre):
    print(f"{(nbre%5==0 or nbre%7==0) and (not(nbre%5==0 and nbre%7==0)) } voila")


#exercice 3
def fauxréel():
    print(f"3 - 2.7 == 0.3 est {3-2.7 == 0.3}")


#exercice 4
def codagecesar():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    indice=int(input("choisisez un indice(entre 0 et 25) :  "))
    print(f"la lettre a coder est l'alfabet {[indice]} !")
    print(f"la lettre est {alfabet[((indice)+3)%26]}")

#exercice 5
def calculette():
    c=int(input("choisisez un nbre : "))
    d=int(input("choisisez un nbre : "))
    ope=(input("choisisez un operateur : "))
    if ope=="+":
        return c+d
    elif ope == "-":
        return c-d
    elif ope == "*" or ope == "x":
        return c*d
    elif ope == "/":
        return c/d
    else :
        return "pas bon mon reuf"

#exercice 7
def sommet(liste):
    a=0
    for e in liste:
        a+=e
    return a
def sommepair(liste):
    a=0
    for e in liste:
        if e%2 == 0:
            a+=e
    return a
def produit(liste):
    a=1
    for e in liste:
        a= a*e
    return a

#exercice 8 

def maxmin(liste):
    max = 0
    min = 0
    if len(liste) == 1 :
        max = liste[0]
        min = liste[0]
    else:
        for e in liste:
            if e > max :
                max = e
            elif e < min:
                min = e
        print(f"le max de la liste est {max} et le min de la liste est {min}")

#exercice 9
def recherche(liste,entier):
    if entier in liste:
        return True
    else :
        return False

#exercice 10

def occurence(liste,x):
    occu=0
    if x in liste:
        for elem in liste:
            if elem==x:
                occu+=1
    print(f"l'élément {x} est apparut {occu} fois dans la liste")


#exercice 11

def verifprop(liste):
    for elem in liste:
        if elem%2==1:
            print(f"il y a un entier impair donc {False}")
            break
    print(f"cette liste ne contient que des entier pair donc {True}")



def verifprop2(liste):    
    a=0
    for elm in liste :
        if elm%2==1:
            a+=1
    if a!=1:
        print(f" il y a {a} entier impair donc ")
        return False
    else:
        print(f" il n'y a quun seul et unique entier impair donc")
        return True

def verifprop3(liste):
    for elem in liste:
        if elem%2==0:
            print("cette liste ne contient pas que des impair donc")
            return False
    print("cette liste contient bien que des impair donc")
    return True

#exercice 12

def voyelle(texte):
    voyelle = ['a','e','i','o','u','y']
    consonne= ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x']
    nbrevoyelle = 0
    nbreconsonne = 0
    reste = 0
    for c in texte:
        if c in voyelle:
            nbrevoyelle += 1
        elif c in consonne:
            nbreconsonne += 1
        else:
            reste +=1
    print(f"dans ce texte il y a {nbrevoyelle} voyelles, {nbreconsonne} consonnes, et {reste} caractères autres")

#exercice 13
#celui la est vraiment EZ

#exercice 14
#le même que l'exercice 8

#exercice 15
def primal(entier):
    
    for i in range(2,(entier-1)):
        if entier%i==0:
            print(f"l'entier {entier} choisi n'est pas premier")
            return False
    print(f"l'entier {entier} choisi est un premier")
    return True




    




