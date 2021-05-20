# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1



for i in range(0,5):#1 2 3
  for j in range(5-i,0,-1):#1 2 3
    print(j,end=" ") #1,1,1 #2,2,2 #3,3,3
  print()