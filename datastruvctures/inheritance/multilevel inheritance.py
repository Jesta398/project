#multilevel  inheritance

class Parent:
    def m1(self):
        print("inside parent1")

class  Child(Parent):
    def m2(self):
        print("inside Child")

class SubChild(Child,Parent):#multiple inheritance
    def m3(self):
        print("inside subChild")


sb=SubChild()

sb.m3()
sb.m2()
sb.m1()


sb2=Child()
sb2.m2()
sb2.m1()
sb2.m3()#error

p=Parent()
p.m1()
p.m2()#error
p.m3()#error
