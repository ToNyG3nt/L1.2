#exercice 1
def multiple(x,y):
    if x == 0  :
        print(" 0 est multiple de tout hehe")
        return True
    elif y == 0 :
         print("on ne peux multiplier 0")
         return False
    elif x % y == 0:
        print(f"{x} et {y} sont multiple ")
        return True
    print(f"{x} et {y} ne sont pas multiple")
    return False


#exercice 2.1
def max (a,b):
    if a == b :
        return a
    if a>b :
        return a
    return b


def esttriangle(x,y,z):
    PGC = max(x,max(y,z))
    if PGC == x :
        if y+z > x:
            print("ce triangle est bien un triangle")
            return True
        else:
            print("ce triangle n'est pas un triangle")
    elif PGC == y:
        if x+z > y:
            print("ce triangle est bien un triangle")
            return True
        else:
            print("ce triangle n'est pas un triangle")
    else :
        if x+y > z:
            print("ce triangle est bien un triangle")
            return True
        else:
            print("ce triangle n'est pas un triangle")
    return False

#exercice 2.2
def triestequi(x,y,z):
    if x==y and y==z :
        print("ce triangle est equilatéral")
        return True
    print("ce triangle n'est pas un trianle équilatéral")
    return False

#exercice 2.3
def triestiso(x,y,z):
    if (x==y or (x==z or y==z)):
        print("ce triangle est isocelle")
        return True
    print("ce triangle n'est pas isocelle")
    return False

#exercice 2.4
def triestrect(x,y,z):
    PGC = max(x,max(y,z))
    hypo = 0
    if PGC == x:
        hypo = (y**2) + (z**2)
        if (hypo == x**2) :
            print("ce triangle est rectangle")
            return True
        print("ce triangle n'est pas rectangle")
        return False
    elif PGC == y :
        hypo = (x**2) + (z**2)
        if (hypo == y**2) :
            print("ce triangle est rectangle")
            return True
        print("ce triangle n'est pas rectangle")
        return False
    else :
        hypo = (y**2) + (x**2)
        if (hypo == z**2) :
            print("ce triangle est rectangle")
            return True
        print("ce triangle n'est pas rectangle")
        return False

#exercice 3
def memedizaine(a,b):
    passeunit1 = a//10
    passeunit2 = b//10
    reste1 = passeunit1 % 10
    reste2 = passeunit2 % 10
    if reste1 == reste2 :
        print(f"{a} et {b} Sont dans la même dizaine")
        return True
    print(f"{a} et {b} Ne sont pas dans la même dizaine")
    return False

def memeparité(a,b):
    if (a%2 == b%2):
        print(f"{a} et {b} sont de même parité")
        return True
    print(f"{a} et {b} Ne sont pas de même parité")
    return False

#exercice 4
def rectangle(H,L):
    l1 = "*" * L
    print(l1)
    for ligne in range (1,H-2):
        print("*"+(" "*(L-2))+"*")
    print(l1)

def disque(R):
    if R%2 == 0:
        for i in range(1,R):
            print(" "*(R-i)+"*"*(i*2))
        for i in range(1,R):
            print(" "*(R-(R-i))+"*"*((R-i)*2))


#exercice 5
def estpair(nbre):
    if nbre == 0 :
        print("ce nombre est pair")
        return True
    if nbre == -1 or nbre == 1 :
        print("ce nombre n'est pas pair")
        return False
    elif nbre < 0 :
        return estpair(nbre+2)
    elif nbre > 0 :
        return estpair(nbre-2)

    
#exercice 6
def estmulti(it1,it2):
    if (it1 - it2 == 0):
        #print ("est ce que c bon")
        return ((it1 % 11) == 0)
    elif it1 < it2 :
        if ((it1%11)==0):
            #print(f"{it1} est bien un multiple de 11")
            return True
        
        else:
            return estmulti((it1+1),it2)
    else:
        #print(f"aucun des élément de l'interval [{it1},{it2}].")
        return False

    
def maxmulti(it1,it2):
    if it1>it2 :
        return -1
    elif it2%11 == 0 :
        return it2
    else :
        return maxmult(it1,it2-1)

def nbremulti(it1,it2):
    if estmulti(it1,it2):
        if it2-it1 == 0 :
            return 0 
        elif ((it1%11)==0):
            return 1+nbremulti((it1+1),it2)
        else :
            return nbremulti(it1+1,it2)
    return 0


def sommmulti(it1,it2):
    if it1 > it2 :
        return 0
    elif it1%11 == 0:
        return it1+sommmulti(it1+1,it2)
    else :
        return sommmulti(it1+1,it2)
    
