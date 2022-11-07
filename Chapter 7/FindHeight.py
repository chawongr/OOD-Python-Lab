class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            r = self.root
            while True:
                if data < r.data:
                    if r.left == None:
                        r.left = Node(data)
                        return self.root
                    r = r.left
                else:
                    if r.right == None:
                        r.right = Node(data)
                        return self.root
                    r = r.right

    def height(self,node):
        if node != None:
            return max(self.height(node.left),self.height(node.right))+1
        return -1

T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:T.insert(i)
print("Height of this tree is :",T.height(T.root))                 
