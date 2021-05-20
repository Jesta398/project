# class Vehicle:
#     def print(self,engine,colour,brand):
#         self.engine=engine
#         self.colour=colour
#         self.brand=brand
#         print("type is ",self.engine,self.colour,self.brand)
# ve=Vehicle()
# ve.print(444,"blue","maruthi")
#
# ve=Vehicle()
# ve.print(999,"red","honda")


class  Person:
    def setval(self,name,age):
        self.name=name
        self.age=age

    def printval(self,gender):
        self.gender=gender
        print(self.age)
        print(self.name)
        print(self.gender)

per=Person()
per.setval("jesta",22)
per.printval("female")