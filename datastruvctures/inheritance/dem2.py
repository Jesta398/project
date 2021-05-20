# person child parent student
# child $parent inherit person
# student class inherit child
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printVal(self):
        print("name",self.name)
        print("age",self.age)

# class Parent(Person):
#     def m1(self):
#         print("inside parent1")


class Student(Person):
    def __init__(self,rollno,mark,name,age):#constructor
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def print(self):
        print("name=",self.name)
        print("age=",self.age)
        print("roll no=",self.rollno)

cr=Student(2,66,"jesta",77)
cr.printVal
cr.print("jes",88,"f")
# std.m2()
# std.setVal("jesta",33,"f")
# std.printVal()
# chd=Child()
# chd.m2()
# chd.persmet("jesna",23,"f")
# prt=Parent()
# prt.m1()
