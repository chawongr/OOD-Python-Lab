def palindrome(lst):
    if len(lst)==1:
        return True
    elif len(lst)==2 and lst[0]==lst[-1]:
        return True
    elif lst[0]==lst[-1]:
        return palindrome(lst[1:-1])
    else:
        return False 

com = list(input('Enter Input : '))
if palindrome(com)==True:
    print("'",*com,"'",' is palindrome',sep='')
else:
    print("'",*com,"'",' is not palindrome',sep='')
