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
        if not node:return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left,data)
            else:
                node.right = self.insert(node.right,data)
            return node
    
    def Preorder(self,node,):
        if node:
            print(node.data,end=' ')
            self.Preorder(node.left)
            self.Preorder(node.right)
        
    def Inorder(self,node):
        if node:
            self.Inorder(node.left)
            print(node.data,end=' ')
            self.Inorder(node.right)
    
    def Postorder(self,node):
        if node:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data,end=' ')

    def Breadth(self,node,q=[]):
        if node:
            print(node.data,end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if len(q)!=0:
                self.Breadth(q.pop(0),q)


def printTree(node,level=0):
    if node:
        printTree(node.right,level+1)
        print('     '*level,node)
        printTree(node.left,level+1)

T = BST()
root = None
com = input('Enter Input : ').split()
for i in com:
    root = T.insert(root,int(i))
printTree(root)
print('Preorder : ',end='')
T.Preorder(root)
print()
print('Inorder : ',end='')
T.Inorder(root)
print()
print('Postorder : ',end='')
T.Postorder(root)
print()
print('Breadth : ',end='')
T.Breadth(root)
