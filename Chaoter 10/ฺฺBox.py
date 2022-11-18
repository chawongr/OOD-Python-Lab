def minWeight(items,box,min):
    count = 0
    weight = 0
    for i in items:
        if weight + i <= min:
            weight += i
        else:
            count += 1
            weight = i
    if count + 1 == box:
        return min
    return minWeight(items,box,min+1)

com = input('Enter Input : ').split('/')
items , num = [int(i) for i in com[0].split()] , int(com[1])
#numOfBox = int(com[1])
print(f'Minimum weigth for {num} box(es) = {minWeight(items,num,max(items))}')
