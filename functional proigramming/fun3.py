# map(),filter(),print(),input type

lst=[2,3,4,5,6,7]


def squares(num):
    return num**2

squares=list(map(squares,lst))#function,iteratible
print(squares)


names=["ajay","aravid","jose"]


upp=list(map(lambda name:name.upper(),names))
print(upp)
