f=open("customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    if data[4] not in dic:
            dic[data[4]]=1
     else:
            dic[data[4]]+=1
print(dic)