# a=int(input("enter the no"))
# b=int(input("enter the no"))
# try:
#     print(a) #it will work entire statement ,if it shown an error it move to ecxcept block
#     print(a / b)
# except:
#     print("execption occur")

#try block will work all the time but if there is an error only it will move to except block
# #index out of range
# a=[1,2,3]
# print(a[1])
# print(a[8])
a=[1,2,3]
b=int(input("enter the index"))
try:
       print(a[b])
except:
    print("execption occur")

#finally block

finally: #it will work every time
  print("inside finally")

#try anf finnal will work every time