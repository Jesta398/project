# lst=[20,30,40,50]
# num=int(input("enter the element"))
# if(num in lst):
#     print("element found")
# else:
#     print("element is not found")
#
# or method
lst=[20,30,40,50]
ele=int(input("enter the element"))
flag=0
for i in lst:
    if(i==ele):
        flag=1
        break
    else:
        pass
if(flag>1):
    print("element found")
else:
    print("element not found")
