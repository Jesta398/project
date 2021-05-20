def adim_Required(func):
    def wrapper(user,pin):
        if(user!="admin"):
            raise Exception("you are not allowed")
        else:
            return func(user,pin)
    return wrapper

@adim_Required
def  change_pin(user,pin):
    return pin


@adim_Required
def delete_account(user,acno):
    return str(acno)+"deleted"


print(change_pin("user1",100))
print(delete_account("user1",100))