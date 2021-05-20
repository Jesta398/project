dic={"employee":"jesta","id":66,"desigination":"professor","salary":20000}
print(dic)

print(dic["employee"])

dic["salary"]+=5000
print(dic)

for i in dic:
     print(i,":",dic[i])

print("company" in dic)
dic["company"]=66
print(dic)