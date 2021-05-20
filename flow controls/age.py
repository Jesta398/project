age=int(input("enter the age:"))
sex=input("Male(M)/Female(F):")
marital=input("enter the marital status y/n:")
if(sex=="F"):
    print("she will work only in urban area")
elif(sex=="M" and (age>=20 and age<=40)):
    print("he may work anywhere")
elif(sex=="M"and 40<=age<=60):
    print("he will work in urban area")
else:
    print("ERROR")