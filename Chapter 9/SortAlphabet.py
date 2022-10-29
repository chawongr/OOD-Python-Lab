def findAlphabet(lst):
    alphabet = []
    for i in lst:
        if i >= 'a' and i<='z':
            alphabet.append(i)
    return alphabet

def isSort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

com = input('Enter Input : ').split() 
alphabet = []
for i in com:
    for j in i:
        alphabet.append(j)

for i in isSort(findAlphabet(alphabet)):
    for j in com:
        if i in j:
            print(j,end=' ')
