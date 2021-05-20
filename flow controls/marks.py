#4 subjects
#total
#180-200=aplus
# 160-179=a
# 140-169,=b plus
# 120-139=b

mark1=int(input("enter your mark1"))
mark2=int(input("enter your mark2"))
mark3=int(input("enter your mark3"))
mark4=int(input("enter your mark4"))
total=(mark1+mark2+mark3+mark4)
print(total,"total mark")
if(total>180)&(total<200):
    print("A+")
elif(total>168)&(total<179):
   print("A")
elif(total>148)&(total<159):
    print("B+")
elif(total>128)&(total<139):
    print("B")
elif(total>100)&(total<119):
    print("c+")
elif(total>80)&(total<99):
    print("c")
else:
    print("D+")


#160<=total<=179





