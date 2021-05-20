class Person:
    def setPer(self,name,age):
        self.name=name
        self.age=age

    def printPer(self):
        print(self.name)
        print(self.age)



class Bank(Person):
    bank_name="sbi"#static variable
    def Account(self,acno):
        self.bname=Bank.bank_name
        self.balance=900

    def deposit(self,amount):
        self.balance+=amount
        print("your",Bank.bank_name,"is created with",amount,"aval balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
             print("insufficirent balancre")
        else:
          self.balance-=amount
          print("your",Bank.bank_name,"id debited with",amount,"aval balance",self.balance)

    def balance(self):
        print("ur acc balance=",self.balance)

obj=Bank()
obj.setPer("joe",55)
obj.printPer()
obj.Account(888)
obj.withdraw(800)
obj.deposit(600)

#differnt type of variables
#1.static variable:can be accessed using cls name(Bank.bank_name)
#2.static is keyword used for efficient memory usage
#3.instance variable always used for object
#4.ststic is used for clsass
