def hbd(age):
    if age%2==0:
        return 'saimai is just 20, in base '+str(age//2)+'!'  
    else:
        return 'saimai is just 21, in base '+str(age//2)+'!'
      
age = int(input('Enter year : '))     
print(hbd(age)) 
