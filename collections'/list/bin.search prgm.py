lst=[4,2,3,11,14,15,10,12,13]
lst.sort()
low=0
upper=len(lst)-1  #8(9-1)
flag=0
element=int(input("enter the element"))

while(low<=upper):#0>=8
  mid=low+upper//2#0+

  if(element>lst[mid]):
     low = mid+1
     break
  elif(element<lst[mid]):
      upper=mid-1
      break
  elif(element==lst[mid]):
      flag=1

if(flag>0):
    print("element found")
else:
    print("not found")
