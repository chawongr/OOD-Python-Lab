def checkSort(lst):
    if lst[0]>lst[1]:
        return 'No'
    else:
        if len(lst)==2:
            return 'Yes'
        return checkSort(lst[1:])
        
com = list(map(int,input('Enter Input : ').split()))
print(checkSort(com))
