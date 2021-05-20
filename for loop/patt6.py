# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1


# #1
# 2  1
# 3 2 1
# 4 3 2 1
# 5 4 3 2
#
#

for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()