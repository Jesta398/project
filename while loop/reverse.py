num=int(input("enter the number"))
res=0
while(num!=0):#153!=0  15!=0
    digit=num%10 #153%10=3  15%10 1%10=1
    res=(res*10)+digit #(0*10)+3=3
    num=num//10 #153//10  15//10
print(res) #351
