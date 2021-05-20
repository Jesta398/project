n=int(input("enter the number"))
for i in range(0,5):#1,2,3
    for j in range(i,-1,-1):#1,2
        print(n-j,end=" ")
    print()