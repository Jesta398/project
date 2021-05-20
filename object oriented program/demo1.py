#we use classes(reusablity)
#classes-design pattern
#object -real world entity
#referenec-memory location of the object
#ex-planning -classes and house -objects
#referenece-for operations
#every object have differenet refereneces


#syntax:

class Person: #use capital letter for first word of name
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method",self.name,self.age,self.gender)
pe=Person()
pe.print("jesta",23,"female")

re=Person()
re.print("jesna",16,"female")