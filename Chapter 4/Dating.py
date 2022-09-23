class Queue():
    def __init__(self):
        self.lst=[]
    def dequeue(self):
        x=self.lst[0]
        del self.lst[0]
        return x
    def enqueue(self,x):
        self.lst.append(x)
    def peek(self):
        return self.lst[-1]
        
day = input('Enter Input : ').split(',')
act = Queue()
place = Queue()
count = 0
g = []
h = []
gStr = []
hStr = []

for i in range(len(day)):   
    a = day[i].split(' ')
    act.enqueue(a[0])
    place.enqueue(a[1])
    
    tempStr = ""
    tempG = a[0].split(':')
    if tempG[0] == '0' : tempStr = tempStr + "Eat:"
    elif tempG[0] == '1' : tempStr = tempStr + "Game:"
    elif tempG[0] == '2' : tempStr = tempStr + "Learn:"
    elif tempG[0] == '3' : tempStr = tempStr + "Movie:"
    if tempG[1] == '0' : tempStr = tempStr + "Res."
    elif tempG[1] == '1' : tempStr = tempStr + "ClassR."
    elif tempG[1] == '2' : tempStr = tempStr + "SuperM."
    elif tempG[1] == '3' : tempStr = tempStr + "Home"
    gStr.append(tempStr)
    tempStr = ""
    tempH = a[1].split(':')
    if tempH[0] == '0' : tempStr = tempStr + "Eat:"
    elif tempH[0] == '1' : tempStr = tempStr + "Game:"
    elif tempH[0] == '2' : tempStr = tempStr + "Learn:"
    elif tempH[0] == '3' : tempStr = tempStr + "Movie:"
    if tempH[1] == '0' : tempStr = tempStr + "Res."
    elif tempH[1] == '1' : tempStr = tempStr + "ClassR."
    elif tempH[1] == '2' : tempStr = tempStr + "SuperM."
    elif tempH[1] == '3' : tempStr = tempStr + "Home"
    hStr.append(tempStr)

    g.append(a[0])
    h.append(a[1])
    
    x,y=act.dequeue().split(':')
    j,k=place.dequeue().split(':')
    
    if x==j and y!=k:
        count+=1
    elif x!=j and y==k:
        count+=2
    elif x==j and y==k:
        count+=4
    elif x!=j and y!=k:
        count-=5 
        
print('My   Queue = ',end='')
print(*g,sep=', ')
print('Your Queue = ',end='')
print(*h,sep=', ')
print('My   Activity:Location = ', end = '')
print(*gStr,sep=', ')
print('Your Activity:Location = ', end = '')
print(*hStr,sep = ", ")
if count>=7:
    print("Yes! You're my love! : Score is",count,end='.')
elif count<7 and count>0:
    print("Umm.. It's complicated relationship! : Score is",count,end='.')
else:
    print("No! We're just friends. : Score is",count,end='.') 
