class Vehicle:
    def printVal(self,engine,colour,brand):
        self.engine=engine
        self.colour=colour
        self.brand=brand
        print("type is ",self.engine,self.colour,self.brand)

class Bus(Vehicle):
    def printSet(self,wheeler,seat):
        self.wheeler=wheeler
        self.seat=seat
        print("type is ",self.wheeler,"and",self.seat)

b=Bus()
b.printSet(4,54)
b.printVal(3414,"red","maruthi")