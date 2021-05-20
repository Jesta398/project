cyear=int(input("enter the current year"))
cmonth=int(input("enter the current  month"))
cdate=int(input("enter the current date"))
birthyear=int(input("enter the birth year"))
birthmonth=int(input("enter the birth month"))
birthdate=int(input("enter the birth date"))
age=cyear-birthyear
date=cdate-birthdate
if(age>=1)&(date>=0):
    print("current age is:",age)
else:
    print("age turns to 1 ")