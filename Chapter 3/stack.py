class Stack():
    def __init__(self):
        self.lst=[]
    def push(self,x):
        self.lst.append(x)
    def pop(self):
        del self.lst[-1]
    def peek(self):
        return self.lst[-1]

s = Stack()
com = input('Enter Input : ').split(',')
for i in range(len(com)):
    b = com[i].split(' ')
    if b[0]=='A':
        print('Add =',b[1],end='')
        s.push(b[1])
        print(' and Size =',len(s.lst))
    elif b[0]=='P':
        if len(s.lst)>0:
            print('Pop =',s.peek(),end='')
            s.pop()
            print(' and Index =',len(s.lst))
        elif len(s.lst)==0:
            print('-1')
if len(s.lst)==0:
    print('Value in Stack = Empty')
else:
    print('Value in Stack =',*s.lst,sep=' ') 
