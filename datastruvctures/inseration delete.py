size=int(input("enter the size"))
stk=[]
top=0
n=0
def insert():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("enter the element to push"))
        stk.append(p)
        top+=1
        print(stk)

def delete():
    global top,size
    if top<=size:
        print("stack is empty")
    else:
        stk.pop(p)
        top+=1
        print(stk)

while n!=1:
    print(".....enter the operation want to perform.....")
    opt=int(input("press::1)insert 2)delete"))
    if opt==1:
        insert()
    elif opt==2:
        delete()
