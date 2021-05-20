salary=int(input("enter the salary of the person"))
service=int(input("enter the service in years"))
bonus=salary*.05
if(service>5):
  print(bonus)
else:
    print("not eligible")