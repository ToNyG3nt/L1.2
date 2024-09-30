#TP2

def estPairRec(n):
    if n==0:
        return True
    elif n==1:
        return False
    else:
        return estPairRec(n-2)

def exMult11(a,b):
    if a>=b:
        if a%11!=0:
            return False
        else:
            return True
    if a%11==0:
        return True
    else:
       return exMult11(a+1,b)

def maxMult11(a,b):
    if a==b and a%11!=0:
        return -1
    else:
        if a%11==0:
            if exMult11(a+11,b):
                return maxMult11(a+11,b)
            else:
                return a
        else:
            return maxMult11(a+1,b)
        
print(maxMult11(1,33))
