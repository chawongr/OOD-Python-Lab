class Node:
     def __init__(self, data, num):
          self.data = data
          self.num = num
          self.left = None
          self.right = None
     
     def __str__(self):
          return str(self.data)

class AVL_Tree:
     def __init__(self):
          self.root = None

     def insert(self, data):
          num = 0
          if self.root == None:
               self.root = Node(data,num)
          else:
               num += 1
               node = []
               node.append(self.root)
               while node:
                    tree = node.pop(0)
                    if tree.left is None:
                         tree.left = Node(data,num)
                         break
                    else:
                         num += 1
                         node.append(tree.left)
                    if tree.right is None:
                         tree.right = Node(data,num)
                         break
                    else:
                         num += 1
                         node.append(tree.right)
          return self.root

     def search(self,ordinal):
          if self.root.num == ordinal:
               return self.isSum(self.root)
          else:
               node = []
               node.append(self.root)
               while node:
                    tree = node.pop(0)
                    if tree.num == ordinal:
                         return self.isSum(tree)
                    if tree.left:
                         node.append(tree.left)
                    if tree.right:
                         node.append(tree.right)

     def isSum(self,knight):
          sumPower = 0
          node = []
          node.append(knight)
          while node:
               tree = node.pop(0)
               sumPower += tree.data
               if tree.left:
                    node.append(tree.left)
               if tree.right:
                    node.append(tree.right)
          return sumPower

     def isCompare(self,k1,k2):
          if self.search(k1) > self.search(k2):
               print(f'{k1}>{k2}')
          elif self.search(k1) < self.search(k2):
               print(f'{k1}<{k2}')
          else:
               print(f'{k1}={k2}')

def printTree90(node, level = 0):
     if node != None:
          printTree90(node.right, level + 1)
          print('     ' * level, node.data)
          printTree90(node.left, level + 1)

T = AVL_Tree()
inp = input("Enter Input : ").split("/")
compare, power= inp[1].split(","), [int(i) for i in inp[0].split()]
for i in power:
     root = T.insert(i)
print(T.search(0))
for i in compare:
     T.isCompare(int(i[0]),int(i[2]))
