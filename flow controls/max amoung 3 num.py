num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
if(num1>num2)&(num1>num3):
    print(num1,"is the highest")
elif(num2>num3):
    print(num2, "is the highest")
else:
    print(num3,"is the highest")

