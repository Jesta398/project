quantity=int(input("enter the quantity"))
total=quantity*100
discount=total*.10
if(total>1000):
    print(total,discount)
else:
    print("no discount")