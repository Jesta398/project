# string="HEY"  #oop HEEYYY
# cnt=1
# data=""
# for char in string:
#     data=cnt*char
#     cnt+=1
#     print(data)


# lst=[4,1,2,5,6,7]
# if x>5 x+1
# if x<5 x-1
lst=[4,1,2,5,6,7]
lst1=[]
lst2=[]
for i in lst:
    if i>5:
        print(i+1)
        lst1.append(i+1)
    elif i<5:
        print(i-1)
        lst2.append(i-1)
print(lst1)
print(lst2)
