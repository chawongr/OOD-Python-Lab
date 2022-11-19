com = input('Enter Input : ').split('/')
Left, Right = sorted(list(map(int, com[0].split()))), list(map(int, com[1].split()))

for i in Right:
    greaterVal = None
    for j in Left:
        if j > i:
            greaterVal = j
            break
    if greaterVal == None:
        print("No First Greater Value")
    else:
        print(j)
