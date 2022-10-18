class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

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

    def printPreorder(self,r):
        if r:
            print(r.data,end=' ')
            self.printPreorder(r.left)   
            self.printPreorder(r.right)

    def printInorder(self,r):
        if r:
            self.printInorder(r.left)
            print(r.data,end=' ')
            self.printInorder(r.right)
    
    def printPostorder(self,r):
        if r:
            self.printPostorder(r.left)
            self.printPostorder(r.right)
            print(r.data,end=' ')

    def printBreadth(self,r,q=[]):
        if r != None:
            print(r.data,end=' ')
            if r.left!=None:
                q.append(r.left)
            if r.right!=None:
                q.append(r.right)
            if len(q)!=0:
                self.printBreadth(q.pop(0),q)
            else:
                return

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Preorder : ',end=''),T.printPreorder(root)
print()
print('Inorder : ',end=''),T.printInorder(root)
print()
print('Postorder : ',end=''),T.printPostorder(root)
print()
print('Breadth : ',end=''),T.printBreadth(root)
