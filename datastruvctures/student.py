# class Student:
#     def print(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# st=Student()
# st.print("jesta  ",22,"female")




# class Add:
#     def add(selfself,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
# a=Add()
# b=int(input("enter"))
# c=int(input("enter"))
# a=add(b,c)

class Student:
    def setValues(self,id,name):
        self.id=id
        self.name=name

    def printValues(self):
        print("id=",self.id)
        print("name=",self.name)


 #reference name=classname()
obj=Student()
obj.setValues(77,"arun")
obj.printValues()
obj2=Student()
obj2.setValues(22,"jesna")
obj2.printValues()
#self is a keyword which points current object instance


obj=Student()
obj.setValues(77,"arun")
obj2=Student()
obj2.setValues(22,"jesna")
print(obj)
print(obj2)#here we are printing object __str__(self)  tostring method(hexaddecimal_)