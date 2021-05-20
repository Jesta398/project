num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"is the second largest")
    else:
        print(num3,"is the second largest")
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1)
    else:
        print(num2)


#homework
#year
#month
#date
#birth date-yr,date,mon
# currentyear-year
#
# 2021,3,24-today
#
# 2020,3,22-bdate(not havre 1 yr)
