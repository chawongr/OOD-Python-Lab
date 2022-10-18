class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BST:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def insert(self, data):
            newNode = Node(data)
            if self.root is None:
                self.root = newNode
                return self.root
            else:
                t = self.root
                while True:
                    if data < t.data:
                        if t.left == None:
                            t.left = newNode
                            return self.root
                        else:t=t.left
                    else:
                        if t.right == None:
                            t.right = newNode
                            return self.root
                        else:t=t.right
                    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        isExist = False
        r = self.root
        while True:      
            if data == r.data:
                isExist = True
                break
            if not r.right and not r.left:
                break
            if r.left and data < r.data:
                r = r.left
            elif r.right and data > r.data:
                r = r.right
                
        roots = self.root
        if data == roots.data:
            print('Root') 
        elif data == roots.left.data or data == roots.right.data:
            print('Inner')
        elif isExist:
            print('Leaf')
        else:
            print('Not exist')       

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
