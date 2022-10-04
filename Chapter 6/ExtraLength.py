def length(txt):     
    if not txt:
        return 0
    else:
        y=txt.pop()
        x=1+length(txt)
        if x%2==0:
            print(y,end='~')
        else:
            print(y,end='*')
        return x
text=list(input('Enter Input : '))
print("\n",length(text), sep='')
