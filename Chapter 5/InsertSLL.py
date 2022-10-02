class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            run = self.head
            s = str(self.head.data)
            while run.next!=None:   
                s += '->'       
                s += str(run.next.data)
                
                run = run.next
            return s
        
    def isEmpty(self):
        return True if self.head == None else False
     
    def Size(self):
        return self.size

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            run = self.head
            while run.next!=None:
                run = run.next
            run.next = newNode
        self.size += 1

    def insert(self, index, data):
        newNode = Node(data)   
        run = self.head
        i=0
        if int(index)==0:
            newNode.next = self.head
            self.head = newNode
        elif int(index)==self.size:       
            while run.next!=None:
                run = run.next
            run.next = newNode
        else:      
            while run.next!=None:
                if i+1 == int(index):
                    newNode.next = run.next
                    run.next = newNode
                else:
                    run = run.next    
                i += 1         
        self.size += 1  

com = input('Enter Input : ').split(',')
ll = LinkedList()

apnd = com[0].split()
for i in apnd:
    ll.append(i)

isrt = com[1:]
for i in isrt:
    isrt =  i.split(':')
    if ll.isEmpty():
        print('List is empty')
        if int(isrt[0])==0:          
            print('index =',isrt[0],'and data =',isrt[1])
            ll.insert(isrt[0],isrt[1])
        else:
            print('Data cannot be added')       
    else:
        print('link list :', ll)
        if int(isrt[0])>=0 and int(isrt[0])<=ll.Size():
            ll.insert(isrt[0],isrt[1])
            print('index =',isrt[0],'and data =',isrt[1])
        else:
            print('Data cannot be added')
            
if not ll.isEmpty():
    print('link list :', ll)
else:
    print('List is empty')
