# class Book:
#     def setVal(self,name,author,pages):
#       self.name=name
#       self.author=author
#       self.pages=pages
#       print(self.name,self.author,self.pages)
#     def __str__(self):
#         return  self.name+self.author+str(self.pages)
#
#
# bk=Book()
# bk.setVal("python","abc",999)
# print(bk)

class Employee:
    def setvalue(self,name,id,dep,salary):
        self.name=name
        self.id=id
        self.dep=dep
        self.salary=salary
        print(self.name,self.id,self.dep,self.salary)

    def __str__(self):
        return self.name+str(self.id)

emp=Employee()
emp.setvalue("jes",22,"cse",9000)
print(emp)