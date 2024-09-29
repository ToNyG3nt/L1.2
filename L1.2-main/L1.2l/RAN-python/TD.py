# exercice 11

def minindice(liste):
    mini = liste[0]
    indice = 0
    for i in range((len(liste))-1):
        if liste[i]<mini:
            mini = liste[i]
            indice = i 
    print(f"le minimum de cette liste est {mini} et sont indice est {indice}")
    return mini,indice 
minindice([3,2,42,0,7])

liste = [3,2,42,0,7]

def minienu(L):
    i,v = 0,L[0]
    for ind,val in enumerate(L):
        if val < v :
            i,v = ind,val
    print(f" le minimum est {v} et l'indice est {i}")
minienu(liste)


#exercice 12
def inf2(nbre):
    n=0
    a=2
    while a<=nbre:
        print(a)
        a*=2
        n+=1
        

#exercice 13
def presin(L,n):
    x= int(input("choisir un element"))
    if x in L:
        print("l'élément est présent")
        return True
    print("l'élément n'est pas présent")
    return False


    
def prewhile(L):
        x = int(input("entrer un x"))
        i = 0
        trouvé = False
        while i< len(L) and not Trouvé:
            if L[i]==x:
                trouvé = True
            else :
                i+=1
        if trouvé :
            print(f"{x} à été trouvé")
        else :
            print(f"{x} ,n'as pas été trouvé")

        

#exercice 14

def traduct(trad):
    i=0
    while i<len(trad):
        print(A[i])
        i+=1

#exercice 15

def puissenti(x,n):    
    for i in range(n-1):
        x*=x
    return x
print(puissenti(5,3))

#exercice 16
def primal(nbre):
    if nbre == 0 or x == 1 :
        return False
    elif nbre == 2 :
        return True
    elif nbre%2 == 0 :
        return False 
    else :
        for i in range(2,sqrt(nbre)):
            if nbre%i == 0 :
                print("c'est bon")
                return True
        print("c'est pas bon")
        return False

        
