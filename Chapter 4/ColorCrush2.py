class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def top(self):
        return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.size() == 0 else False


N, M = input("Enter Input (Normal, Mirror) : ").split()
N = N[::-1]  # reversed N
Fail, Explo = 0, 0
Normal, Mirror, Bomb = Stack(), Stack(), Queue()
for i in N:  # push N in stack Normal
    Normal.push(i)
for i in M:  # push M in stack Mirror
    Mirror.push(i)
while True:  # Find a Bomb
    ts = Stack()  # tempstack
    bs = Bomb.size()
    count = 1
    c = " "
    while not Mirror.isEmpty():
        if c == Mirror.top():
            count += 1
        else:
            count = 1
            c = Mirror.top()
        ts.push(Mirror.pop())
        if count == 3:
            count = 1
            Bomb.enqueue(c)
            for i in range(3):
                if not ts.isEmpty():
                    ts.pop()
            c = " "
    while not ts.isEmpty():
        Mirror.push(ts.pop())
    if Bomb.size() == bs:
        break
while True:
    NS = Normal.size()
    ts = Stack()
    count = 1
    c = " "
    while not Normal.isEmpty():
        if c == Normal.top():
            count += 1
        else:
            count = 1
            c = Normal.top()
        ts.push(Normal.pop())
        if count == 3:
            if not Bomb.isEmpty():
                B = Bomb.dequeue()
                if c == B:
                    Fail += 1
                    for i in range(2):
                        ts.pop()
                else:
                    tc = ts.pop()
                    ts.push(B)
                    ts.push(tc)
            else:
                Explo += 1
                for i in range(3):
                    ts.pop()
                c = " "
            count = 1
    while not ts.isEmpty():
        Normal.push(ts.pop())
    if Normal.size() == NS:
        break
# print Output
print("NORMAL :")
print(Normal.size())
if Normal.isEmpty():
    print("Empty")
else:
    ts = Stack()
    while not Normal.isEmpty():
        ts.push(Normal.pop())
    while not ts.isEmpty():
        print(ts.pop(), end="")
    print()
print(Explo, "Explosive(s) ! ! ! (NORMAL)")
if Fail != 0:
    print("Failed Interrupted", Fail, "Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(Mirror.size())
if Mirror.isEmpty():
    print("ytpmE")
else:
    ts = Stack()
    while not Mirror.isEmpty():
        ts.push(Mirror.pop())
    while not ts.isEmpty():
        print(ts.pop(), end="")
    print()
print("(RORRIM) ! ! ! (s)evisolpxE", bs)
