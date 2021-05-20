#remove-matching no will remove

#pop-remove the element by their index

# #empty list
# 1-100

list=[]
evenlist=[]
oddlist=[]
for i in range(1,101):
    list.append(i)
for i in list:
   if(i%2==0):
     evenlist.append(i)
   else:
    oddlist.append(i)
print(list)
print(evenlist)
print(oddlist)



