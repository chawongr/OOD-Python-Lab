print(' *** Summation of each digit ***')
c = input("Enter a positive number : ")
sum = 0
for i in range(len(c)):
    sum += ord(c[i])-48
print('Summation of each digit = ','%d' % sum)
