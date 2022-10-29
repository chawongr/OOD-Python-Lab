def isSort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst
com = list(map(int,input('Enter Input : ').split()))
pos = []
neg = []
numSort =[]
for i in com:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
posSort = isSort(pos)
for i in com:
    if i>=0:
        numSort.append(posSort.pop(0))
    else:
        numSort.append(i)
print(*numSort,sep=' ')
