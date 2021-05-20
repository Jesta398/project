# age=(int(input("enter the age")))
# if(age>=18):
#     print("eligible")
# else:
#     raise Exception("not eligible") #here in output it gives o/p as error and expection,for that we use raise keyword.
#


#Expections

#1.divide by zero
#2.index
#3.key error
#4.type error

#expections that are not inbuild or defined ,and it is  user defined it is called customised Expection.(here its about age ,it is not inbuild expection is
# done by user so it is customised Expection


#2.

expenses=[2300,2000.3000,4000]

# month=int(input("enter the month 1)jan  2)feb 3)mar 4)april"))
#
# try:
#     print("expense",expenses[month])
#
# except Exception  as e:
#     print(e,args)


no1=int(input("enter the no1"))
no2=int(input("enter the no2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
   print(e.args)


