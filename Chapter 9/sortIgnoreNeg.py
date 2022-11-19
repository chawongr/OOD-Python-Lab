def bubbleSort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

com = list(map(int,input('Enter Input : ').split()))
tmp = []
for i in com :
    if i>=0:
        tmp.append(i)
        
tmp = bubbleSort(tmp)

for i in com:
    if i<0:
        print(i,end=' ')
    else : 
        print(tmp.pop(0),end=' ')
