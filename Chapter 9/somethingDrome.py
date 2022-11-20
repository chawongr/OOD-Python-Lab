def metaDrome(lst):
    if lst[0]>=lst[1]:
        return False
    elif len(lst)==2:
        return True
    return metaDrome(lst[1:])

def plainDrome(lst):
    if lst[0]>lst[1]:
        return False
    elif lst[0]==lst[1]:
        return True
    elif len(lst)==2:
            return True
    return plainDrome(lst[1:])

def kataDrome(lst):
    if lst[0]<=lst[1]:
        return False
    elif len(lst)==2:
        return True
    return kataDrome(lst[1:])

def nialpDrome(lst):
    if lst[0]<lst[1]:
        return False
    elif lst[0]==lst[1]:
        return True
    elif len(lst)==2:
            return True
    return nialpDrome(lst[1:])

def repDrome(lst):
    if lst[0]!=lst[1]:
        return False
    elif len(lst)==2:
        return True
    return repDrome(lst[1:])

com = list(map(int,input('Enter Input : ')))
if repDrome(com):print('Repdrome')
elif metaDrome(com):print('Metadrome')
elif plainDrome(com):print('Plaindrome')
elif kataDrome(com):print('Katadrome')
elif nialpDrome(com):print('Nialpdrome')
else:print('Nondrome')
