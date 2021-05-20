class Animal:
    def __init__(self,name,leg,species):
        self.name=name
        self.leg=leg
        self.species=species
    def printEmp(self):
        print("name =",self.name)
        print("leg=",self.leg)
        print("species=",self.species)

emp=Employee(1001,"dsigner",90000)
emp.printEmp()




#emp.setEmp(333,"teacher",9000)#setEmp()-for intializing#id,desig,salary
#emp.printEmp()-#for printing instance variable


#constructor

#duty?-is used for initializing instance variable
#constructor name is always __init__()-->intialization
#constructor is automatically invoked at the time of object  creation

