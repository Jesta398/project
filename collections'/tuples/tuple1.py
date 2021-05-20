#tuple
#
# tp=()-parathesis
tp=()
print(type(tp))

tp=tuple() #using function

tp1=(1,10,5,"jesta",True,False)
print(tp1) #it supports heterogenous data

tp2=(1,2,3,4,5,10,3.5,4.6,9)
print(tp2) #same order (insertation order reserved)

tp3=(2.2,3,4.4,5,6,7,7.7,"true","true")
print(tp3) #duplicate value supports

#tuple immutable

tp3=(2.2,3,4.4,5,6,7,7.7,"true","true")
print(tp3)
tp3(3)=8
print(tp3) #it doesnot support muttable prop


