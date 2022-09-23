class Queue():
    def __init__(self):
        self.lst=[]
    def dequeue(self):
        x= self.lst[0]
        del self.lst[0]
        return x
    def enqueue(self,x):
        self.lst.append(x)

com = input('Enter String and Code : ').split(',')
coms = com[0].split(' ')
decode = Queue()
decode_ll = Queue()
encode = Queue()
num = Queue()

for i in range(len(coms)):
     for j in range(len(coms[i])):
        decode.enqueue(coms[i][j])
        decode_ll.enqueue(coms[i][j])

for i in range(len(com[1])):
    num.enqueue(com[1][i])

for i in range(len(decode.lst)):
    x = decode.dequeue() 
    y = num.dequeue()
    
    if (ord(x)+int(y)>=65 and ord(x)+int(y)<=90) or (ord(x)+int(y)>=97 and ord(x)+int(y)<=122):
        encode.enqueue(chr(ord(x)+int(y)))
    else:
        encode.enqueue(chr(ord(x)+(int(y)-26)))
    num.enqueue(y)
    
print('Encode message is : ',encode.lst)
print('Decode message is : ',decode_ll.lst)
