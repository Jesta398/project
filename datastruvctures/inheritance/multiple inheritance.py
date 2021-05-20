class Parent1:
    def m1(self):
        print("inside parent1")

class Parent2:
    def m1(self):
        print("inside parent2")

class child(Parent1,Parent2):#chils is inheriting parent1 and parent2
    def m3(self):
        print("inside child")

c=child()
c.m3()
c.m1()


#name ambiquity problem ,becaause of that java cannot used for multiple inheritance(both parent1 and 2 have m3)parent1 will only work becaue
class child(Parent1,Parent2)#parent1 is given first


















# class Student:#child cls/sub cls,derived cls
#     def det(self,rollno,school):
#         self.rollno=rollno
#         self.school=school
#     def prints(self):
#         print("rollno=",self.rollno)
#         print("school=",self.school)
# class Person:#parent cls/base cls,super cls
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printdet(self):
#         print("name=",self.name)
#
#         print("age=",self.age)
#         print("gender=",self.gender)
# class Employee(Person,Student):
#     def setVal(self,name,id,desig,salary):
#         self.name=name
#         self.id=id
#         self.desig=desig
#         self.salary=salary
#     def printVal(self):
#         print(self.name)
#         print(self.id)
#         print(self.desig)
#         print(self.salary)
# emp=Employee()
# emp.setVal("jes:",44,"developer",6000)
# emp.printVal()
# emp.det(22,"st marys")
# emp.prints()
# emp.details("rose",33,"f")
# emp.printdet()

#multilevel inheritance can inherit from various claassses
#multiplr inheritance can inherit only fron one class only.
