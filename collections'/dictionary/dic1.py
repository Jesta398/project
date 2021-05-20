#dictionary
#1.define
dic={} #if we eneter the values it will be an set

#key:value pairs(syntax)

#name:jesta,loc:kakkanad,course:python django

# key=name,loc,course
# values=jesta,kakkanad,python django

dic={"name":"jesta","loc":"kakkanad","course":"python"}
# print(dic)

# #2.heterogeneous
# dic={"name":"jesta","loc":"kakkanad","course":"python","data":25,"marks":44}
# print(dic)

# #3.insertion order preserved

#4.dulicate key
# dic={"name":"jesta","loc":"kakkanad","course":"python","data":25,"marks":44,"marks":77}#duplicate keys are not supported
# print(dic)

#5.duplicate value
# dic={"name":"jesta","loc":"kakkanad","course":"python","data":25,"marks":25}#duplicate values are  supported
# print(dic)

#6.value can be collected by using their particular key
# dic={"name":"jesta","loc":"kakkanad","course":"python","data":25,"marks":25}
# print(dic)

# dic={"name":"jesta","loc":"kakkanad","course":"python","data":25,"marks":25}
# for i in dic:
#     print(i,":",dic[i])#print i then o/p=name,course,loc,data,marks
#     #dic 1 their information
#
# #mutable
# dic["marks"]=40
# print(dic)
# dic["marks"]+=25
# print(dic)
#
# #delete
# del dic["name"]
# print(dic)
#
# #pop checkout
# pop dic["name"]
# print(dic)


dic={"name":"jesta","loc":"kakkanad","course":"python"}

print("total" in dic)
dic["total"]=66
print(dic)


