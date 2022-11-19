class Data:
     def __init__(self, key, value):
          self.key = key
          self.value = value

     def __str__(self):
          return "({0}, {1})".format(self.key, self.value)

class hash:
     def __init__(self,size,maxCol):
          self.table = [None]*size
          self.size = size
          self.maxCol = maxCol

     def insert(self,key,data):
          if self.isfull() :
               print("This table is full !!!!!!")
               exit(0)
          else:
               index = 0
               for i in key:
                    index += ord(i)
               index %= self.size

               if self.table[index] == None:
                    self.table[index] = Data(key,data)
               else:
                    col = 0
                    print(f'collision number {col+1} at {index}')
                    while True:
                         col += 1
                         newIndex = ( index + col * col ) % self.size
                         if self.table[newIndex] == None:
                              self.table[newIndex] = Data(key,data)
                              break
                         if self.maxCol == col:
                              print("Max of collisionChain")
                              break
                         print(f'collision number {col+1} at {newIndex}')
               self.printHashTable()

     def isfull(self):
          return None not in self.table

     def printHashTable(self):
          for i in range(self.size):
               print(f'#{i+1}      {self.table[i]}')
          print("---------------------------")

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
size, maxCol = inp[0].split()
H = hash(int(size),int(maxCol))
data = inp[1].split(",")

for i in data:
     H.insert(i.split()[0],i.split()[1])
