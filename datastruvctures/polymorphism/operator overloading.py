class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages + other.pages# adding obj pages ang obj1 pages

    def __sub__(self,other):
        return self.pages-other.pages

    def __mul__(self, other):
        return Book(self.pages*other.pages)

    def __truediv__(self, other):
        return self.pages/other.pages

    def __str__(self):
        return str(self.pages)



obj=Book(150)
print(obj)
obj1=Book(200)
print(obj1)
obj2=Book(400)
print(obj+obj1)#error,obj is book type
print(obj1-obj)
print(obj/obj1)
print(obj*obj1*obj2)#obj&obj1 is book type, 350 *obj3(integer +book type ) so convert it into book by giving book infront of every operation

# + is used for string for integer for addition and concatenation

# obj1 and obj is book type so we cannot use + operator ,they can only done if both is string or integer.