#it is an assumption the bird having duck gester they may be duck
#it will have more important to function than class

class Swift:
    def start(self):#we can use any keyword instead of self
        print("swift car starts")

    def accelerate(self):
        print("swift car accelerating functionality")

    def breaks(self):
        print("swift car break method")

    def stop(self):
        print("swift car stopping")


class Seltos:

    def start(self):  # we can use any keyword instead of self
        print("seltos car starts")

    def accelerate(self):
        print("seltos car accelerating functionality")

    def breaks(self):
        print("seltos car break method")

    def stop(self):
        print("seltos car stopping")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()

p=Person()
sel=Seltos()
p.drive(sel)
swi=Swift()
p.drive(swi)


#######################



class Pycharm:
    def compile(self):
        print("compile using pycham")
    def  execute(self):
        print("execute py")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def  execute(self):
        print("execute vs")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execeute()

p=Programmer()
vc=Vscode()
p.coding(vc)