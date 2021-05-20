# #function
# #input
# #range
# #print
# #type
#
# #function is set of code
#
# #syntax
#
# # def  fnname(arguements1,arguements2):
# #     #fn statement
# # #call() #using fn name
#
# #3 methods
#
# #1 fn without arguements and no return type
# #2 fn with arguements and no return type
# #3 fn with arguements and return type
#
# #method 1-fn without arguements and no return type
#
# def sub():
#     num1=int(input("enter number1"))
#     num2 = int(input("enter number2"))
#     sub=num1-num2
#     print(sub)
# sub()
# sub()
# sub()
# sub()
#
# #functional programming-reducing the lenght of code
#
# #lambda
# #map
# #filter
# #reduce
# #list comprehension
#
# #lambda-Anonyms(unknown function)
#
# f=lambda num1,num2:num1+num2
# print(f(10,20))
#
# #2 fn with arguements and no return type
#
# def sumn(num1,num2):
#    res=num1+num2
#    print(res)
# sumn(56.77)
# sumn(55,33)

# def div(num1,num2):
#     res=num1/num2
#     print(res)
# div(60,20)
# div(90,3)

#3 fn with arguements and return type

def sum(num1,num2):
    res=num1+num2
    return res
data=sum(50,40)
print(data)