class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        self.sizes += 1

    def addHead(self, item):
        newNode = Node(item)
        if not self.isEmpty():
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.head.next.previous = self.head
            self.sizes += 1
        else:
            self.append(item)

    def insert(self, pos, item):
        node = Node(item)
        if pos > self.size() or pos == self.size():
            if self.isEmpty():
                self.head = self.tail = node
                self.sizes += 1
                return
            else:
                cur = self.head
                self.tail.next  = node
                node.previous = self.tail
                self.tail = node
                self.sizes += 1
                return
        if pos < -(self.size()) or pos == 0:
            if self.isEmpty():
                self.head = self.tail = node
                self.sizes += 1
                return 
            else:
                node.next = self.head
                self.head.previous = node
                self.head = node
                self.sizes += 1
                return
            
        if pos > 0 and pos < self.size():
            i = 0
            cur = self.head
            while i != pos - 1:
                cur = cur.next
                i += 1
            cur.next.previous = node
            node.next = cur.next
            node.previous = cur
            cur.next = node
            self.sizes += 1
            return
        if pos < 0 and pos > -(self.size()):
            i = 0
            cur = self.tail
            while i != pos+1:
                cur = cur.previous
                i -= 1
            cur.previous.next = node
            node.previous = cur.previous
            node.next = cur
            cur.previous = node
            self.sizes += 1
            return             

    def search(self, item):
        run = self.head
        while run.value != item:
            run = run.next
            if run == None:
                return 'Not Found'
        return 'Found'
            

    def index(self, item):
        run = self.head
        for i in range(self.sizes):
            if item == run.value:
                return i
            run = run.next
        return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        
        if (pos >= self.size()) or (pos < 0):
            return 'Out of Range'
        
        if pos == 0 and self.size() == 1:
            self.head = None
            self.sizes -= 1
            return 'Success'
        elif pos == 0 and not self.isEmpty():
            self.head = self.head.next
            self.head.previous = None
            self.sizes -= 1
            return 'Success' 
        elif pos == 0 and self.isEmpty():
            return 'Out of Range'
        
        i = 0
        cur = self.head
        while i != pos - 1:
            cur = cur.next
            i += 1
        if pos+1 == self.size():
            cur.next = None
            self.tail = self.tail.previous
            return 'Success'
        cur.next = cur.next.next
        cur.next.previous = cur
        self.sizes -= 1
        return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse()) 
