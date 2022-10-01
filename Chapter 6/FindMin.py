def findMin(lst):
    if len(lst)==1:
        return lst[0]
    else:
        mn = findMin(lst[1:])
        return mn if mn < lst[0] else lst[0]

com = list(map(int,input('Enter Input : ').split(' ')))
print('Min :',findMin(com))
