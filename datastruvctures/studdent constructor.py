class Student:
    college_name="sahrdaya college"#static variable intial
    def __init__(self,name,age,gender):#constructor
        self.name=name
        self.age=age
        self.gender=gender
    def printStd(self):
        print("name=",self.name)
        print("age=",self.age)
        print("gender=",self.gender)
        print("college name=",Student.college_name)#tatic variable


std=Student("jesta",22,"female")#calling constructor
std.printStd()