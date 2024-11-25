#exercice 1

def aff_tas(tas):
    print("| "*tas)

def saisirDansIntervalle(debut,fin):
    valeur=int(input(f"entrez un valeur comprise entre {debut} et {fin} : "))
    while valeur<debut or valeur>fin:
        print(f"la valeur doit etre comprise entre {debut} et {fin} !")
        valeur=int(input(f"entrez un valeur comprise entre {debut} et {fin} : "))
    return valeur


def InfoJoueur(joueur):
    print(f"c'est au joueur {joueur} de jouer !")

def demanderTas():
    print("quel tas voulez vous modifier ?")
    tas =saisirDansIntervalle(1,2)
    return tas
def demanderJeton():
    print("combien de jeton voulez vous enlever ?")
    jeton=saisirDansIntervalle(1,3)
    return jeton
def changerJoueur(joueur):
    if joueur ==1:
        return 2
    if joueur==2:
        return 1
from random import *
def main():
    tas1=randint(1,20)
    tas2=randint(1,20)
    joueur=1
    game=True

    while game==True:
        print("\n")
        InfoJoueur(joueur)
        joueur=changerJoueur(joueur)
        print("")
        if tas1<1 and tas2<1:
                print(f"le joueur {changerJoueur(joueur)} a  perdu !")
                game=False
                break
        if tas2<=0:
            print("tas 1 :")
            aff_tas(tas1)
            tas1-=demanderJeton()
        elif tas1<=0:
            print("tas2 :")
            aff_tas(tas2)
            tas2-=demanderJeton()
        else:
            print("tas 1 :")
            aff_tas(tas1)
            print("tas 2 :")
            aff_tas(tas2)
            tas=demanderTas()
            if tas==1:
                tas1-=demanderJeton()
            else:
                tas2-=demanderJeton()
            
        
#exercie 2

def puissance1(x,n):
    for i in range(1,n):
        x*=n
    return x

def puissance2(x,n):
    while n>1:
        x*=x
        n-=1
    return x
def puissance3(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    else:
        return x*puissance3(x,n-1)


#exercice 3

def fact1(n):
    x=n
    if n==0:
        return 1
    for i in range(1,x):
        x*=i
    return x

def fact2(n):
    x=1
    if n==0:
        return 1
    while n>0:
        x*=n
        n-=1
    return x

def fact3(n):
    if n==0:
        return 1
    else:
        return n*fact3(n-1)


#exercice 4
"""
def palindrome(chaine):
    i,j=0,0
    n=True
    while i<=j or n:
        if chaine
            
        if chaine[i].isalpha() and chaine[len(chaine)-i-1].isalpha():
            if chaine[i]!=chaine[len(chaine)-i-1]:
                return False
"""         
                
#exercice 5

def anagrame(t,s):
    if len(s)!=len(t):
        return False
    t1=sorted(t)
    s1=sorted(s)
    return t1==s1

    
#exercice 6
liste=[0,1,3,4,5]
def manquant(liste):
    for i in range(len(liste)):
        if i!=liste[i]:
            return i
        
        
#exercice 7
s=['(','(',"[",']','[',']',")",")"]
def valide(s):
    par=0
    acc=0
    croch=0
    op=['{','(','[']
    cl=[')',']','}']
    if s[0] in cl:
        return False
    for i in range(len(s)):
        if i==0:
            if s[i]=='(':
                par+=1
            elif s[i]=='[':
                croch+=1
            elif s[i]=='{':
                acc+=1
            else:
                return False
        else:
            if s[i-1] in op:
                if s[i] in cl and s[i]!=s[i-1]:
                    return False
                else:
                    if s[i]=='(':
                        par+=1
                    if s[i]=='[':
                        croch+=1
                    if s[i]=='{':
                        acc+=1
                    if s[i]==')':
                            par-=1
                    if s[i]==']':
                        croch-=1
                    if s[i]=='}':
                        acc-=1
                


def indice()