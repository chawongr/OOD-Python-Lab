print('*** multiplication or sum ***')
num1,num2 = map(int,input('Enter num1 num2 : ').split())
mul = num1 * num2
sum = num1+num2
if mul>1000:
    print('The result is',sum)
else:
        print('The result is',mul)
