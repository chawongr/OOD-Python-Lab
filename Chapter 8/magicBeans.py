class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        newNode = Node(data)
        temp = ''
        if self.root == None:
            self.root = newNode
            return '*'
        else:
            r = self.root
            while True:
                if data < r.data:
                    if r.left == None:
                        r.left = newNode
                        temp += 'L*'
                        return temp
                    else:
                        r = r.left
                        temp += 'L'
                else:
                    if r.right == None:
                        r.right = newNode
                        temp += 'R*'
                        return temp
                    else:
                        r = r.right
                        temp += 'R'

T = BST()
com = [int(i) for i in input('Enter Input : ').split()]
for i in com:
    print(T.insert(i))


