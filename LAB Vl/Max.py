def isMax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mx = isMax(lst[1:])
        return mx if mx > lst[0] else lst[0]
    
com = list(map(int,input('Enter Input : ').split(' ')))
print('Max :',isMax(com))
 
