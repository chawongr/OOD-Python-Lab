class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,node,data):
        if not node:return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left,data)
            else:
                node.right = self.insert(node.right,data)
            return node

    def findHeight(self,node):
        if node:
            return max(self.findHeight(node.left),self.findHeight(node.right))+1
        return -1

def printTree(node,level=0):
    if node:
        printTree(node.right,level+1)
        print('     '*level,node)
        printTree(node.left,level+1)

T = BST()
root = None
com = [int(i) for i in input('Enter Input : ').split()]
for i in com:
    root = T.insert(root,i)
print(T.findHeight(root))
