st={2,4,6,5,7,8,10}
print(st)
st.add(11)
st.add("jes")
st.add(8)
st.update([80,56,78]) #use bracket while using update
print(st)

#add fn for adding elements  in set(single element)
#append fn for adding in list

#multiple value
#1.use update fn in set
#use append in list


#remove element
st.remove(5)
print(st)

#removal of muitiple ele
#1.discard

st.discard(3)
print(st) #print the set again

#differenece between remove and discard
# 1.discard -if we use discard for deleting the element which is not in the set,it will print the set again and willnot
#    show the message element is not present.
# 2.remove -if we use discard for deleting the element which is not in the set,it will print the message that
#       the element is not present in the set

#pop
st1={2,3,4,6,7}
st1.pop()
print(st1)

#oprations
#1,union
#2.intersection
#3.difference
