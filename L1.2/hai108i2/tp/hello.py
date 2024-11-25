
def exercice1():
    print(((1234567)**6)%1000)

def exercice2_1(n):
    if (n%5)==0 and (n//7)==0:
        return False
    else:
        if (n%5)==0:
            return True
        else:
            if(n%7)==0:
                return True
            else:
                return False


def exercice2_2(n):
    print((n%5==0 or n%7==0) and (not(n%5==0 and n%7==0)))
 


def exercice3():
    print(3-2.7==0.3)
"""
def exercice4(indice):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    print(f"la lettre a coder est: {alphabet[indice-1]}")
    Nlettre=alphabet[((indice-1)+3%)26]
    print(f"la lettre codée par Cesar est: {Nlettre}")
"""
def exercice5(n1,n2,op):
    if op=="+":
        return n1 + n2
    elif op=="-":
        return n1 - n2
    elif op=="*" or op=="x":
        return n1*n2
    elif

exercice5(5,5,*)
