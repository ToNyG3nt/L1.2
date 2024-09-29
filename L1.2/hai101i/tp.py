def multiple(x,y):
    return x%y==0

def triangle(a,b,c):
    if a>b and a>c:
        if (b+c)>a:
            return True
    elif b>a and b>c:
        if (a+c)>b:
            return True
    else:
        if (a+b)>c:
            return True
    return False

def triangleEqui(a,b,c):
    if(a==b and b==c):
        return True
    return False

def triangleIso(a,b,c):
    if a==b or a==c or b==c:
        return True
    return False

def triangleRect(a,b,c):
    if a>b and a>c:
        if (b**2+c**2)==a**2:
            return True
    elif b>a and b>c:
        if (a**2+c**2)==b**2:
            return True
    else:
        if (a**2+b**2)==c**2:
            return True
    return False


def memeDizaine(a,b):
    dA=a//10
    dB=b//10
    return dA%10==dB%10


def memeParité(a,b):
    return a%2==b%2

def rectangle(H,L):
    for i in range(H):
        if i==0 or i==H-1:
                print("* "*L)
        else:
            print("*"," "*(L-4),"*")

def disque(R):
    
