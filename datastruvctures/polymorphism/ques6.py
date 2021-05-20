class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printStudent(self):
        print("name=",self.name)
        print("age",self.age)

    def __str__(self):
        return self.name

f=open("student1","r")

for lines in f:
    data=lines.rstrip("\n").split(",")
    print (data)
    name=data[0]
    age=data[1]
    if()
    obj=Student(name,age)
    print(obj)