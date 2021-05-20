lst=[[1000,"jesta",25,1001],
     [3000,"mery",38,2000],
     [5000,"bruno",67,8000]]


#nested list
#1001,"jesta,25,1001
# 3000,mery,38,2000
# 5000,bruno,67,8000
#
# for emp in lst:
#    print(emp)
# #emp name
# for emp in lst:
#   print(emp[3])

#names aboove 2000

for emp in lst:
 if(emp[3]>2000):
  print(emp[1])

