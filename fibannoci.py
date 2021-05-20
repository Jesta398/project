num=int(input("enter the number"))
first=0
sec=1
for i in range(num):
    print(first)
    temp=first
    first=sec
    sec=temp+sec