class Stack():
    def __init__(self):
        self.lst=[]

    def push(self,x):
        self.lst.append(x)

    def pop(self):
        del self.lst[-1]

    def reset(self):
        self.lst.clear()

    def top(self):
        return (self.lst[-1])

print('******** Parking Lot ********')
mx,s,o,n = input("Enter max of car,car in soi,operation : ").split()
s = list(s.split(','))
mx,n = int(mx),int(n)
a = Stack()
b = Stack()

for i in range (len(s)):
    a.push(int(s[i]))

if len(s) < mx:
    if o =='arrive':
        if len(s)==1 and s[0]=='0':
            a.reset()
            a.push(n)
            print('car',n,'arrive! : Add Car 1')
        else:
            if str(n) not in s:
                a.push(n)
                print('car',n,'arrive! : Add Car',n)
            elif str(n) in s:
                print('car',n,'already in soi')

    elif o =='depart':
        if len(s)==1 and s[0]=='0':
            a.reset()
            print('car',n,'cannot depart : Soi Empty')
        else:
            if str(n) in s:
                for i in range(len(a.lst)):
                    if a.top()==n:
                        a.pop()
                    else:
                        b.push(a.top())
                        a.pop()
                for i in range(len(b.lst)):
                    a.push(b.top())
                    b.pop() 
                print('car',n,'depart ! : Car',n,'was remove')

            elif str(n) not in s:
                print('car',n,'cannot depart : Dont Have Car',n)            

elif len(s) == mx:
    if o =='arrive':
        print('car',n,'cannot arrive : Soi Full')
    elif o =='depart':
        if str(n) in s:
            for i in range(len(a.lst)):
                if a.top()==n:
                    a.pop()
                else:
                    b.push(a.top())
                    a.pop()
            for i in range(len(b.lst)):
                a.push(b.top())
                b.pop() 
            print('car',n,'depart ! : Car',n,'was remove')

        elif str(n) not in s:
                print('car',n,'cannot depart : Dont Have Car',n)

print(a.lst) 
