class Stack():
    def __init__(self):
        self.lst=[]
    def push(self,x):
        self.lst.append(x)
    def pop(self):
        del self.lst[-1]
    def top(self):
        return self.lst[-1]

com = input('Enter expresion : ')
sl = Stack()
m = True
for i in com:
    if i =='(' :
        sl.push(i)
    elif i ==')' :
        if len(sl.lst)!=0:
            if sl.top()=='(':
                sl.pop()
            elif sl.top()=='[' or sl.top()=='{':
                m=False
                print(com,'Unmatch open-close')
                break
        elif len(sl.lst)==0:
            m=False
            print(com,'close paren excess')
            break
    elif i =='[':
        sl.push(i)
    elif i ==']':
        if len(sl.lst)!=0:
            if sl.top()=='[':
                sl.pop()
            elif sl.top()=='(' or sl.top()=='{':
                m=False
                print(com,'Unmatch open-close')
                break
        elif len(sl.lst)==0:
            m=False
            print(com,'close paren excess')
            break
    elif i =='{':
        sl.push(i)
    elif i =='}':
        if len(sl.lst)!=0:
            if sl.top()=='{':
                sl.pop()
            elif sl.top()=='(' or sl.top()=='[':
                m=False
                print(com,'Unmatch open-close')
                break
        elif len(sl.lst)==0:
            m=False
            print(com,'close paren excess')
            break
    
if m==True:
    if '(' in sl.lst:
        print(com,' open paren excess   ',len(sl.lst),' : ',*sl.lst,sep='')
    elif ')' in sl.lst:
        print(com,' close paren excess')
    elif len(sl.lst)==0: 
        print(com,'MATCH')
