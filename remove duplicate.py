lst=[10,20,30,40,50,60,70]
duplicate=[]
for i in lst:
    if i not in lst:
        duplicate.append(i)
print(duplicate)