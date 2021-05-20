class Parent:
    def property(self):
        print("will give 2 cars")
    def marraige(self):
        print("with gopalan")
class Child:
    def marraige(self):
        print("with dq")#override the method

c=Child()
c.property()
c.marraige()

#child overrid the method of parent

# class Student:
#     company="luminar"
#     def empdet(self,rol,name,total):
#         self.rol=rol
#         self.name=name
#         self.total=total
#
#     def printVal(self):
#         print(self.rol)
#         print(self.name)
#         print(self.total)
#
#
#     def __str__(self):
#         return self.name
#
#
# obj=Student(66,"jesta",34000)
# obj1=Student(88,"jee",44444)
# print(obj)
# print(obj1)