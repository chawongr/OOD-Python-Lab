def bubbleSort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

def median(lst):
    if len(lst)%2==1:
        return lst[len(lst)//2]
    else:
        return (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2


com = list(map(int,input('Enter Input : ').split()))
temp,ans = [],[]
for i in com:
    temp.append(i),ans.append(i)
    print(f'List = {ans} : median = {float(median(bubbleSort(temp)))}')
