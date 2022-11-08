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
        
    def insert(self,node,data):
        if not node :return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left,data)
            else:
                node.right = self.insert(node.right,data)
            return node

    def check(self,node,k,level=0):
        if node:
            self.check(node.right,k,level+1)
            if node.data > k:
                print('     '*level,node.data*3)
            else:
                print('     '*level,node)
            self.check(node.left,k,level+1)

def printTree(node,level=0):
    if node:
        printTree(node.right,level+1)
        print('     '*level,node)
        printTree(node.left,level+1)

T = BST()
root = None
com = input('Enter Input : ').split('/')
left = com[0].split()
for i in left:
    root = T.insert(root,int(i))
printTree(root)
print('--------------------------------------------------')
T.check(root,int(com[1]))
