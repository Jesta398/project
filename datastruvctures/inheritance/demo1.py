#inheritance
#single inheritance
class Parent:
    def phone(self):
        print("i have nokia 3310")

class Child(Parent):#inherit the method of parent
    pass

c=Child()
c.phone()

#2 example

# class Person:#parent cls/base cls,super cls
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printdet(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("gender=",self.gender)
# class Student(Person):#child cls/sub cls,derived cls
#     def det(self,rollno,school):
#         self.rollno=rollno
#         self.school=school
#     def prints(self):
#         print("rollno=",self.rollno)
#         print("school=",self.school)
#
# per=Person()
# per.details("jesta",22,"f")
# per.printdet()
# # per.det(33,"st marys")#it shows error because person is not inherit student
# # per.prints()#error
# st=Student()
# st.det(22,"st joseph")
# st.prints()
# st.details("jesto",22,"m")
# st.printdet()

#person,employe

class Person:#parent cls/base cls,super cls
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print("name=",self.name)
        print("age=",self.age)
        print("gender=",self.gender)
class Employee(Person):
    def setVal(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
    def printVal(self):
        print(self.name)
        print(self.id)
        print(self.desig)
        print(self.salary)
emp=Employee()
emp.setVal("jesta",66,"developer",90000)
emp.printVal()
emp.details("jose",44,"f")
emp.printdet()
pr=Person()
# pr.setVal("jesta",66,"developer",90000)
# pr.printVal() /error person cant be called by employee