def sortlist(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

def combination(lst, n):
    if n == 0:
        return [[]]
    templst = []
    for i in range(len(lst)):
        c = lst[i]  
        remLst = lst[i+1:]
        remainlst_combo = combination(remLst, n-1)
        for j in remainlst_combo:
            templst.append([c, *j])
    return templst

left, right = input("Enter Input : ").split("/")
left, right = int(left), sortlist([int(i) for i in right.split()])
found = False
for i in range(1, len(right)+1):
    subset = combination(right, i)
    for j in subset:
        result = 0
        for x in j:
            result += x
        if result == left:
            found = True
            print(j)
if not found:
    print("No Subset")
