def isMax (ll, mx = 0,i = 0) :
    if i== len(ll):
        return mx
    if int(ll[i]) > int(ll[mx]):
        return isMax(ll,i,i+1)
    else:
        return isMax(ll,mx,i+1)

def isSort(ll, temp = []):
    if len(ll) == 0:
        return temp
    else:
        temp.append(int(ll.pop(isMax(ll))))
        return isSort(ll,temp)

com = list(map(int,input('Enter your List : ').split(',')))
print('List after Sorted :',isSort(com))
