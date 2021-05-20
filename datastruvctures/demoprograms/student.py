class Student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print("name=",self.name)
        print("roll",self.roll)
        print("course=",self.course)
        print("total=",self.total)

    def __str__(self):
        return self.name

f=open("student","r")

for lines in f:
    data=lines.rstrip("\n").split(",")
    print (data)
    #['1001', 'anu', 'bca', '400']
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    lst=[]
    lst.append(obj)
for i in lst:
 if(i.total>=max(total)):
     print(name)

