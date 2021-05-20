num=int(input("enter the number"))
res=0
while(num!=0):#123 ,12
   digit=num%10 #3 ,2
   res=(res*10)+(digit**3) #0*10+3=3 ,30+2=32
   num=num//10 #12 ,1
print(res)