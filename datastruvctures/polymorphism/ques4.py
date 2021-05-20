class Animal:
    def __init__(self, name, leg, price):
        self.name = name
        self.leg = leg
        self.price = price

    def printAni(self):
        print("name =", self.name)
        print("leg=", self.leg)
        print("price=", self.price)
class Dog(Animal):
    def printVal(self, name,species):
        self.name = name
        self.price=price

obj = Animal("dog",4, 90000)
obj.printAni()
obj.printVal("ggg"9000)