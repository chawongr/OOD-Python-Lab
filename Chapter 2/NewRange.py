print('*** New Range ***')

def rangeTip(start,end,step = 1.0):
    list = []
    list.append(start)
    while start+step<end:
        start+=step 
        start=round(start,3) 
        list.append(start)
    return list
start = 0.0
step = 1.0
a = list(map(float,input('Enter Input : ').split()))

if len(a)==3:
    start=a[0]
    end=a[1]
    step=a[2]

if len(a)==2:
    start = a[0]
    end=a[1]

if len(a)==1:
    end=a[0]

print(tuple(rangeTip(start,end,step))) 
