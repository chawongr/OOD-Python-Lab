class Node:
    def __init__(self,data,Next = None):
        self.data = data
        self.next = Next

class LinkedList():
    def __init__(self):
        self.head = 0
        self.size = 0
        self.count = 0

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        Str = self.head.data
        cur = self.head
        i = 0
        while cur.next != None:
            if i < self.Size():
                Str += '->'
            cur = cur.next
            Str += cur.data
            i += 1
        return Str
    
    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.size += 1
            return   
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self.size += 1

    def Size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def set_next(self,index1,index2):
        if self.isEmpty():
            return 'Error! {list is empty}'
        if index1 > self.Size() - 1:
            return 'Error! {index not in length}: ' + str(index1)
        if index2 > self.Size() - 1:
            self.append(str(index2))
            return 'index not in length, append : ' + str(index2)
            
        if index1 < index2:
           i = 0
           cur = self.head
           ptr = self.head
           while i < index2:
               if i < index1:
                   cur = cur.next
               ptr = ptr.next
               i += 1
           cur.next = ptr
           return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
        
        if index1 > index2:
            self.count += 1
            i = 0
            cur = self.head
            ptr = self.head
            while i < index1:
                if i < index2:
                    ptr = ptr.next
                cur = cur.next
                i += 1
            return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'

        if index1 == index2:
           self.count += 1
           i = 0
           cur = self.head
           while i < index1:
              cur = cur.next
              i += 1   
           return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{cur.data}'

LL = LinkedList()
inp = input('Enter input : ').split(',')
for i in inp:
    if i[0] == 'A':
        LL.append(i[2:])
        print(LL)
    elif i[0] == 'S':
        print(LL.set_next(int(i[2]),int(i[4])))

if LL.count > 0:
    print('Found Loop')
else:
    print('No Loop')
    print(LL) 
