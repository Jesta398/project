class Employee:
    company="luminar"
    def empdet(self,name,ae,id,salary):
        self.name=name
        self.ae=ae
        self.id=id
        self.salary=salary

    def printVal(self):
        print(self.name)
        print(self.ae)
        print(self.id)
        print(self.salary)
        print("company name",Employee.company)

emp=Employee()
emp.empdet("jesta",23,2,34000)
emp.printVal()


emp1=Employee()
emp1.empdet("mariya",24,3,60000)
emp1.printVal()


#2 types varaible
#static variable(related to cls..cls name
#instance variable(related to methods....self