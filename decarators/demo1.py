

#already defined function if we try to add any feature ,without changing the fn def ,for that we use decarotors.
#code reusability
#decarator fn accept an fn(revert_value)


def avoid_zero(func):
    def wrapper(no1,no2):
        if(no1==0) or (no2==0):
            raise Expection("zero division not allowed")
        else:
            return func(no1,no2)
    return wrapper

def revert_values(func):#revert(sub) #revert_value is an decarator fn
    def  wrapper(no1,no2): #(5,10)#it have an inner fn,arguements count will be equal to the fn which we want to decarate,for ex sub is decarating it have 2 arguements
       if(no1<no2):#5<10
           (no1,no2)=(no2,no1)#(10,5)
       return func(no1,no2) #sub(10,5)
    return wrapper



@avoid_zero
@revert_values
def sub(no1,no2):
    # if(no1<no2):
    #     (no1,no2)=(no2,no1)#for adding an condition we have to add this coding (here for removing negative numbers we use thses codes.

    return no1-no2

@avoid_zero
@revert_values
def div(no1,no2):
    # if (no1 < no2):
    #     (no1, no2) = (no2, no1)#here too we have to repeat this code so for avoiding this we use decarators.
    return no1/no2

print(sub(10,2))
print(div(2,8))