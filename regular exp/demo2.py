import re
# n=input("enter")
# x="(^a[a-zA-Z0-9\W]*b$)"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter")
x='a{8,15}' \

match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

