class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)

class BST():
    
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.root = BST._insert(self.root,data)
        return self.root
    
    def _insert(node: 'Node' , data):
        if node == None:
            return Node(data)

        if node.left == None:
            node.left = BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)


k, inp = input("Enter Input : ").split("/")
inp = [int(i) for i in inp.split(' ')] 
van = dict()
root = None
for i in range(int(k)):
    van.update({i+1:0})
j = 1

while len(inp) > 0:
    T = BST()
    Sort = sorted(van.items(), key = lambda kv: (kv[1],kv[0]))
    for i in Sort:
        root = T.insert(list(i))
    van[root.data[0]] += inp[0]    
    print(f'Customer {j} Booking Van {root.data[0]} | {inp.pop(0)} day(s)')
    j += 1
