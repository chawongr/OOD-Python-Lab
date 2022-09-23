class translator:
    global ber
    global sym
    ber = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    
    def deciToRoman(self,num):
        roman=[]
        for i in range(len(ber)):
            if(num//ber[i]!=0):          
                for j in range(num//ber[i]):             
                    roman.append(sym[i])                     
                num-=(num//ber[i])*(ber[i])
        return roman   
      
    def romanToDeci(self,s):
        val=0
        for i in range(len(s)):
            for j in range(len(sym)):
                if s[i]==sym[j]:
                    val+=ber[j]
        return val
                
num = int(input('Enter number to translate : '))      
print(*translator().deciToRoman(num),sep='')
print(translator().romanToDeci(translator().deciToRoman(num)))      
