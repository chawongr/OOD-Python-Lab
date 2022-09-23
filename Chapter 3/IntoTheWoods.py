class Stack():
    def __init__(self):
        self.lst=[]

    def push(self,x):
        self.lst.append(x)

    def pop(self):
        if not self.isEmpty():
            x = self.top()
            del self.lst[-1]
            return x

    def top(self):
        if not self.isEmpty():
            return self.lst[-1]

    def isEmpty(self):
        if len(self.lst) == 0:
            return True
        else :
            return False

sl = Stack()
com = input('Enter Input : ').split(',')
for i in com:
    if i[0]=='A':
        a=int(i.strip('A '))
        sl.push(a)
    elif i[0]=='B':
        if sl.isEmpty():
            print('0')
        else:
            count = 1
            sll = Stack()
            mx = sl.top()               
            while not sl.isEmpty():
                sll.push(sl.top())
                if mx < sl.top():
                    mx = sl.top()
                    count += 1
                sl.pop()
            print(count)
            while not sll.isEmpty():
                 sl.push(sll.pop()) 
