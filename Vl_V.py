def staircase(n,i):
    if n>0:
        print('_'*(n-1)+'#'*(i))
        return staircase(n-1,i+1)
    elif n<0:
        if i>-n:
            pass
        else:
            print('_'*(i-1)+'#'*((0-n)-(i-1)))
            return staircase(n,i+1)
    elif n==0 and i==1:
        print("Not Draw!")

staircase(int(input("Enter Input : ")),1)