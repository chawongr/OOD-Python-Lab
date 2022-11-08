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
    
    def check(self,node,k,q=[]):
        if node:
            self.check(node.left,k)
            if node.data < k:
                q.append(node.data)
            self.check(node.right,k)
            return q

def printTree(node,level=0):
    if node:
        printTree(node.right,level+1)
        print('     '*level,node)
        printTree(node.left,level+1)

T = BST()
root = None
com = input('Enter Input : ').split('|')
left = com[0].split()
for i in left:
    root = T.insert(root,int(i))
printTree(root)
temp=T.check(root,int(com[1]))
if len(temp)!=0:
    print(*temp,sep=' ')
else:
    print('Not have')
