lines="hi hello hi hello"
# o/p
#hai,2
#hello,2

#split function
words=lines.split(" ")
print(words)

dic={}
for word in words:#hai hello
    if(word not in dic):#hai not in dic,hello not in dic
        dic[word]=1
    else:
        dic[word]+=1
print(dic)