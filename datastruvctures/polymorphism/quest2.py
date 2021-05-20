

class Parent1:
    def m1(self):
        print("inside parent1")

class Parent2:
    def m1(self):
        print("inside parent2")

class child(Parent1,Parent2):#chils is inheriting parent1 and parent2
    def m3(self):
        print("inside child")

c=child()
c.m3()
c.m1()