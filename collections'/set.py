# set={}
# print(type(set))#set is dictionary
#
# set function  is used for empty set  because set{} denotes a dictionary

st=set()
print(type(st))

st={5,7,8,9}
print(st) #giving elements in empty{} then it is set not dictionary

st1={2,"jesta",80.0,True,False}
print(st1) #it supports heterogenous data

#above output ,insertion order not preserved

#duplicate value

# st2={5,8.9,8.9,5,"jesta","jesta"}
# print(st2)  #not support duplicate values
#
# st2={1,2,True}
# print(st2)  #doesnot print True because 1 shows of value true=1,false=0,because of
# not displaying duplicate values true willnot displayed

st3={True,False,1,0} #f,t
print(st3)  #display false then true becoz false=0,true=1

st4={3,8,4,8,5,1,9}
print(st4) #print in ascending order



#set is mutable,we can add the elements and delete