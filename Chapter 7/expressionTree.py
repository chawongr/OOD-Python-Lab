class Node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.right = right
        self.left = left
    
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
        
    def infix(self,node):
        if not node:
            return ''
        elif not node.left and not node.right:
            return str(node.data)
        else:
            return '('+self.infix(node.left)+str(node.data)+self.infix(node.right)+')'
        
    def prefix(self,node):
        prefix=''
        if not node:
            return ''
        prefix += str(node.data)
        prefix += self.prefix(node.left)
        prefix += self.prefix(node.right)
        return prefix
            
    def printTree(self,node,level=0):
        if node:
            self.printTree(node.right,level+1)
            print('     '*level,node)
            self.printTree(node.left,level+1)
 
 
inp = input("Enter Postfix : ")
temp = []
t = BST()

for i in inp :
    if i in '+-*/' :
        x = temp.pop()
        y = temp.pop()
        temp.append(Node(i,y,x))
    else :
        temp.append(Node(i))

print("Tree :")
root = temp.pop()
t.printTree(root)
print("--------------------------------------------------")
print(f'Infix : {t.infix(root)}')
print(f'Prefix : {t.prefix(root)}')
