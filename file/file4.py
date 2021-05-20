# f=open("customer","r")
# for i in f:
#     data=i.rstrip("\n").split(",")#split use cheyyumbo it will be an list
#     print(data)
#     #fname,age,country

f=open("customer","r")
for i in f:
    data=i.rstrip("\n").split(",")#split use cheyyumbo it will be an list
    fname=data[1]
    age=data[3]
    country=data[-1]
    print(fname,",",age,",",country)


#data of people working in india

# f=open("customer","r")
# for i in f:
#     data=i.rstrip("\n").split(",")
#     if(data[5]=="india"):
#         print(data[1],",",data[3],",",data[5])

#age>50,fname,lname,age,prof,country

f=open("customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    fname=data[1]
    age=data[3]
    cou=data[-1]
    lst=([fname,age,cou])
    if(data[4]>"Doctor"):
        print(lst)


