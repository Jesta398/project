#re package

# import  re
#
# count=0
# matcher=re.finditer('ab','abaabbab')
# for match in matcher:
#     print("match availabe ",match.start())#return positions
#     print("group+",match.group())          #which object find path
#     count+=1
# print("count=",count)

# import re
#
# x="[abc]"
# # matcher =re.finditer (x ,"abt c@5kz")
# # for match in matcher:
# #     print(match.start())
# #     print(match.group( ))
#
# import re
#
# x="[A-Z]"
# matcher =re.finditer (x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))
#
# import re
#
# x="[a-zA-Z]"
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))
#

# import re
#
# x="[^a-zA-Z0-9]"
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))
#
# import re
#
# x='\s'
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))


# import re
#
# x='\d' #check digits
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))


# import re
#
# x='\D' #checking for nondigit
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))
#

# import re
#
# x='\w' #letters checking
# matcher =re.finditer (x ,"abt c@5Akz")
# for match in matcher:
#     print(match.start())
#     print(match.group( ))

import re

x='\W'
matcher =re.finditer (x ,"abt c@5Akz")
for match in matcher:
    print(match.start())
    print(match.group( ))