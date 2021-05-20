class Book:
    def pages(self):
        print("will have 2000 pg")
    def weight(self):
        print("with 200gm")
class Child:
    def pages(self):
        print("with 1000pg")#override the method

c=Child()
c.pages()
c.weight()