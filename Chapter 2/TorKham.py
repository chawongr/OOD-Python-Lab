class TorKham:

    def play(self, word):
        a=[]
        for i in range(len(word)):
            if word[i][0]=='P':
                wordd=word[i].strip('P ')
                if len(a)==0:
                    a.append(wordd)  
                elif  a[-1][-2].upper()==wordd[0].upper() and a[-1][-1].upper()==wordd[1].upper():
                    a.append(wordd)   
                else:
                    print("'"+word[i].strip('P ')+"'","-> game over")
                    break
                print("'"+str(word[i].strip("P ")+"' -> "+str(a)))   
                
            elif word[i][0]=='X':
                break
            elif word[i][0]=='R':
                print('game restarted')
                a.clear()
            else:
                print("'"+word[i]+"'",'is Invalid Input !!!')
                break               

print("*** TorKham HanSaa ***")
s = input("Enter Input : ").split(',')
TorKham().play(s)

