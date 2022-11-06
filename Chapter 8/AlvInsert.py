class TreeNode(): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(): 
    def __init__(self):
        self.root = None
        
    def rotateRight(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py
    
    def rotateLeft(self,px):
        py = px.left
        px.left = py.right 
        py.right = px
        return py

    def changeHeight(self,a):
        if a != None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    def insert(self,node,data):
        data = int(data)
        if self.root == None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node!=None:
                if data < node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return TreeNode(data)

        l = node.left.height if node.left != None else -1
        r = node.right.height if node.right != None else -1

        if abs(l-r) > 1:
            t = self.root
            if l>r:
                if data<node.left.val:
                    t = self.rotateLeft(node)
                else:
                    node.left = self.rotateRight(node.left)
                    t = self.rotateLeft(node)
            else:
                if data<node.right.val:
                    node.right = self.rotateLeft(node.right)
                    t = self.rotateRight(node)
                else:
                    t = self.rotateRight(node)
            print('Not Balance, Rebalance!')
            self.changeHeight(t)
            return t
        else:
            node.height = max(l,r) + 1
            return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for i in data:
    print("insert :",i)
    root = myTree.insert(root, i)
    printTree90(root)
    print("===============")
