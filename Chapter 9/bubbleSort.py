def bubbleSort(lst):
    step = 1
    for i in range(len(lst)-2): 
        c = None
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                c = lst[j]
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if c != None:
            print(f"{step} step : {lst} move[{c}]")
            step += 1
    c = None 
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            c = lst[i]
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return (f"last step : {lst} move[{c}]")

com = list(map(int, input("Enter Input : ").split()))
print(bubbleSort(com))
