# add
#
# def add(num1,num2):#parameters
#     return num1+num2
#
# res=add(10,20)#arguements
# print(res)
#
#add three
# addThree-camalion notation
# add_three-in python we use this snake notatation for functions


#
# def add_three(num1,numw,num3):#for 3 arguements
#     return num1+num2+num3
#
# def add_four(num1,num2,num3,num4):#for 4 argue

#for many arguements we use *args

# def add(*args):#accept any number of arguements
#     print(args))
# add(10)
# add(9,7)
# add(9,6,7) #the output will be in the form  of tuple

#
# def add(*args):#args=(10,20)
#     res=0
#     for num in args:#10
#         res+=num#res=0+10=10+20=30
#     return res#30
# print(add(10,20))
# print(add(10,50,70,77))#we can also use this many arguements too



def print_employee(**kwargs):
    for k,v in kwargs.items():
        print(k,"=>",v)


print_employee(id=100,nat_place="thrissur",job="kakkanad",sal=35000)

#o/p will be dictionary

# *args ==> tuples
#**kwargs==>dictionary




#
# def  print_employe(**kwargs):
#     print(kwargs)
# print_employe(1=2000,name="jesta",salary=2000)

#
#
employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"desigination ":"developer"},
    1001:{"eid":1001,"name":"vijay","salary":22000,"desigination ":"developer"},
    1002:{"eid":1002,"name":"arun","salary":26000,"desigination ":"qa"},
    1003:{"eid":1003,"name":"varun","salary":27000,"desigination ":"ba"},
    1004:{"eid":1004,"name":"ram","salary":20000,"desigination ":"market"},




def print_employee(**kwargs): #kwargs={id:1003,,prop:"salary"}
    id=kwargs["id"]
    if id in employees:
        print(employees[id]["name"])
    else:
        print("invalid id")


print_employee(id=1003)