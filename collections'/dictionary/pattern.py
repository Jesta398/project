#pattern :"abcdbca

pattern="ABCDBCA"
dic={}
for char in pattern:#a
    if(char not in dic):#a not in dic,b not in dic
        dic[char] = 1
    else:
       print(char)
       break

