print('*** Converting hh.mm.ss to seconds ***')
h,m,s = map(int,input('Enter hh mm ss : ').split())
sec = h*60*60+m*60+s
if m<60 and m>=0:
    print('%02d:%02d:%02d' % (h,m,s),'=',end =" ")
    print(f"{sec:,d}",end="")
    print(" seconds")
else:
    print('mm'+'('+str(m)+')','is invalid!')
