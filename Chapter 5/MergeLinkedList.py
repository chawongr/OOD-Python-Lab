class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createList(List=[]):  # Singly Linked List
    Head = None
    List = List.split("->")
    for i in List:
        newNode = Node(i)
        if Head == None:
            Head = newNode
        else:
            run = Head
            while run.next != None:
                run = run.next
            run.next = newNode
    return Head

def reversedLL(Head):
    List = []
    run = Head
    while run.next != None:
        List.append(str(run.data))
        run = run.next
    List.append(str(run.data))
    items = ""
    for i in range(len(List)-1, -1, -1):
        items += str(List[i]) + " "
    return createList(items)

def printList(Head):
    run = Head
    while run.next != None:
        print(run.data, end=" ")
        run = run.next
    print(run.data)

def mergeList(p, q):
    List = ""
    run = p
    while run.next != None:
        List += str(run.data) + " "
        run = run.next
    List += str(run.data) + " "
    run = q
    while run.next != None:
        List += str(run.data) + " "
        run = run.next
    List += str(run.data)
    return createList(List)

L1, L2 = input("Enter Input (L1,L2) : ").split()
x = createList(L1)
y = createList(L2)
print("L1    : ", end="")
printList(x)
print("L2    : ", end="")
printList(y)
m = mergeList(x, reversedLL(y))
print("Merge : ", end="")
printList(m)
