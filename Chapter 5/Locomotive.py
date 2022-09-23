class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = node
        else:
            run = self.head
            while run.next !=None:
                run = run.next
            run.next = node

    def pop(self):
        run = self.head
        if run.next.next != None:
            run = run.next
        run.next = None

    def printList(self):
        run = self.head
        while run.next != None:
            print(run.data,end=" <- ")
            run = run.next
        print(run.data)

    def isEmpty(self):
        return True if self.head == None else False
        
print(' *** Locomotive ***')
com = input('Enter Input : ').split(' ')
ll = linkedList()
bf = linkedList()
lls = linkedList()

for i in range(len(com)):
    node = Node(com[i])
    bf.append(node)

for i in range(len(com)):
    if com[i] != '0':
        node = Node(com[i])
        ll.append(node)
    else:
        break
for j in range(i,len(com)):
    node = Node(com[j])
    lls.append(node)

if ll.isEmpty():
    pass
else:
    node = Node(ll.head.data,ll.head.next)
    lls.append(node)

print('Before : ',end='')
bf.printList()
print('After : ',end='')
lls.printList() 
