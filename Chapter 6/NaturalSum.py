def isSum(n):
    if n<=1:
        return n
    else:
        return n+isSum(n-1)
    
def isPrint(n):
    if n==0:
        print(n)
    else:
        if n==1:
            print(1,end='')
        else:
            isPrint(n-1)
            print(' +',n,end='')     
            
print(" *** Natural sum ***")
num = int(input('Enter input : '))
isPrint(num)
print(' =',isSum(num))
