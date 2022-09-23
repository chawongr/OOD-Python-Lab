print("*** Minesweeper ***")
IN = list(input("Enter input(5x5) : ").split(","))
M = []
print()
print()
for i in range(len(IN)):
    t = []
    print("[",end="")
    for j in range(len(IN[i])):
        if IN[i][j] == '-':
            t.append(0)
            print("'-'",end="")
        elif IN[i][j] == '#':
            t.append(-100)
            print("'#'",end="")
        if (j != len(IN[i])-1 and IN[i][j] != ' '):
            print(", ",end="")
    M.append(t)
    print("]")
print()
print()
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] < 0:
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if x >= 0 and y>=0 and x < 5 and y < 5:
                        M[x][y]+=1
for i in range(len(M)):
    print("[",end="")
    for j in range(len(M[i])):
        if(M[i][j]<0):
            print("'#'",end="")
        else :
            print("'"+str(M[i][j])+"'",end="")
        if(j != len(M[i])-1):
            print(", ",end="")    
    print("]") 
