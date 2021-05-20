  # #functional programming
#
# #To reduce lenght of the pgm
#
# #lamda  function
# #map function
# #filter
# #list comprehensive
#
#
# # 1.lambda function
# # #lambda fn are anonymous function(nameless function)-no need of using  name-(def(keyword),add(fun),return)
#
# # def add(num1,num2):
# #     return num1+num2
# # print(add(6,9))
#
# f=lambda num1,num2:num1+num2
# print(f(4,9))
#
# f=lambda num1,num2:num1-num2
# print(f(9,4))
#
# f=lambda num1,num2:num1/num2
# print(f(4,2))
#
# f=lambda num1,num2:num1*num2
# print(f(9,5))
#
# # 2.Map- 
# #lst=[10,20,30,40]==>f(x)  [100,400,900,1600]
# # for every (4) object we will apply the function(f(x))= for getting 4 output
# # [ab,ae,cd,ae,fg]==>we need to convert it into uppercase==> f(x)[AB,AE,CD,AE,FG}
#
# # 3.filter
# # [1,2,3,4,5,6,7,8,9,10]
# #even,that is a filtering==>f(x)[2,4,6,8,10]
#
# # [ab,ae,cd,ae,fg]==>f(x) {ab,ae,ae] #need all the objects which starts with 'a'
#
#
# #syntax
# #................
# #1
# map(fn,iterable)
# #2
# filter(fn,iterable)

lst=[1,2,3,4,5,6,7,8,9]
# def sq(num):
#     return num*num
# s=list(map(sq,lst))
# print(s)

#using lambda(reduce the code)

s=list(map(lambda num:num*num,lst)) #using lambda
print(s)


#2filter
# lst=[1,2,3,4,5,6,7,8,9]
# def even(num):
#     return num%2==0
# ev=list(filter(even,lst))
# print(ev)
#
# #using lambda(reduce the code)
#
# ev=list(filter(lambda num:num%2==0,lst))
# print(ev)


#4,list comprehent

# #1 to 50
#
# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)
#
# lst=[i for i in range(1,51)]# syntax=print,range
# print(lst)


lst =[i for i in  range(1,51) if i%2==0]# syntax=print,range,condition
print(lst)

#even==>square,#odd==>cube
lst =[i*i  if i%2==0 else i*i*i for i in range(1,51)] #syntax=print,condition,range
print(lst)

#numis even print =even ,if odd print odd

lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,51)]
print(lst)