f=open("sam2","r")
dic={}
for i in f:
    word=i.split(" ")
    for j in word:
        if j not in dic:
           dic[j]=1
        else:
           dic[j]+=1
for k,v in dic.items():
    print(k,",",v)
# print(dic)
#check you tube for sir progrM
