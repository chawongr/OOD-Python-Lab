def findMax(lst):
    if len(lst)==1:
        return lst[0]
    else:
        mx=findMax(lst[1:])
        return mx if mx>lst[0] else lst[0]

def isSort(ll,temp=[]):
    if len(ll) == 0:
        return temp
    else:
        mx = findMax(ll)
        temp.append(int(mx))
        ll.remove(mx)
        return isSort(ll,temp)

com = list(map(int,input('Enter Input : ').split(',')))
print(isSort(com))
