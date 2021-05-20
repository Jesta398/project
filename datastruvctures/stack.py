#stack
#data store
#stack particular size
#FIFA
#push ,pop
# size=int(input("enter the size"))
# stk=[]
# top=0
# n=0
# def insert():
#     global top,size
#     if top>=size:
#         print("stack is full")
#     else:
#         p=int(input("enter the element to push"))
#         stk.append(p)
#         top+=1
#         print(stk)
#
# def delete():
#     global top,size
#     if top<=size:
#         print("stack is empty")
#     else:
#         stk.pop(p)
#         top+=1
#         print(stk)
#
# while n!=1:
#     print(".....enter the operation want to perform.....")
#     opt=int(input("press::1)insert 2)delete"))
#     if opt==1:
#         insert()
#     elif opt==2:
#         delete()

stk=[]
size=int(input("enter the size"))
n=0
top=0
def push():
    global top,size
    if(top>=size):
        print("the stack is full")
    else:
        element = int(input("enter the element"))
        stk.append(element)
        top+=1
        print(stk)
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
        print(stk)
while(n!=1):
    print(".....enter the operation want to perform.....")
    opt=int(input("press::1)push 2)pop"))
    if(opt==1):
        push()
    else:
        pop()







