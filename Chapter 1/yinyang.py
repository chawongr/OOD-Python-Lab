num=int(input('Enter Input : '))
#TOP
for i in range(1):
    for j in range(num+2-i,1,-1):
        print(".",end='')
    for k in range(1):
        print('#',end='')
    for l in range(num+2):
        print('+',end='') 
    print()

for i in range(num):
    for j in range(num+1-i,1,-1):
        print(".",end='')
    for k in range(i+2):
        print('#',end='')
    for l in range(1):
        print('+',end='')
    for m in range(num):
        print('#',end='') 
    for l in range(1):
        print('+',end='')
    print()

#MID
for i in range(2):
    for j in range(num+2):
        print('#',end='')
    for k in range(num+2):
        print('+',end='')
    print()
    
#BOTTOM
for i in range(num):
    for l in range(1):
        print('#',end='')
    for m in range(num):
        print('+',end='') 
    for l in range(1):
        print('#',end='')
    
    for k in range(num+2-i,1,-1):
        print('+',end='')
    for m in range(1,i+2):
        print('.',end='')
    print()

for i in range(1):
    for j in range(num+3-i,1,-1):
        print("#",end='')
    for k in range(1):
        print('+',end='')
    for l in range(num+1):
        print('.',end='') 
    print()

