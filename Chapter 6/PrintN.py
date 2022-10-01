def print1ToN(n):
    if n<=0:
        print(1,end=' ')
    else:
        if n==1:
            print(n,end=' ')
        else:
            print1ToN(n-1)
            print(n,end=' ')

def printNto1(n):
    if n<=0:
        print(1)
    else:
        if n==1:
            print(n)
        else:
            print(n,end=' ')
            return printNto1(n-1) 

n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)
