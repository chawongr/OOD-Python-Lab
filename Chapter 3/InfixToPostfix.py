class Stack():
    def __init__(self):
        self.lst=[]
    def push(self,x):
        self.lst.append(x)
    def pop(self):
        a=self.lst[-1]
        del self.lst[-1]
        return a      
    def peek(self):
        return self.lst[-1]
      
com = input('Enter Infix : ')
s = Stack()
Operators = set(['+', '-', '*', '/', '(', ')', '^'])
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':4}
print('Postfix :',end=' ')
for i in range(len(com)):
    if com[i] not in Operators :
        print(com[i],end='')
    else:
        if len(s.lst)==0:
            s.push(com[i])
        else:
            if com[i]=='(':
                s.push(com[i])
            elif com[i]==')':
                while s.peek()!='(':
                    print(s.pop(),end='')
                s.pop()
            elif Priority[com[i]] > Priority[s.peek()]:
                s.push(com[i])
            else : # Priority com <= peek
                while len(s.lst)>0:
                    if s.peek() != '(' and Priority[com[i]] <= Priority[s.peek()]:
                        print(s.pop(),end='')
                    else:
                        break
                s.push(com[i])
while len(s.lst)>0:
    print(s.pop(),end='')

