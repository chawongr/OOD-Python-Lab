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

people, time = input("Enter people and time : ").split()
q, cashA, cashB = Queue(), Queue(), Queue()
countA, countB = 0, 0
for i in people:
    q.enqueue(i)
for i in range(int(time)):
    if not q.isEmpty():
        if cashA.size() < 5:
            cashA.enqueue(q.dequeue())
        else:
            cashB.enqueue(q.dequeue())
    print(i+1, q.items, cashA.items, cashB.items)
    if not cashA.isEmpty():
        countA += 1
    if countA == 3:
        countA = 0
        cashA.dequeue()
    if not cashB.isEmpty():
        countB += 1
    if countB == 2:
        countB = 0
        cashB.dequeue()
