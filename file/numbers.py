f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num))
print(lst)
print(sum(lst))

#for removing /n in output we use "rstrip"(from last)
#for removing from last we use "lstrip"

data="hello\n"
# data1=data.lstrip("h")
data1=data.rstrip("\n")
print(data1)