def add(*x):
    return sum(x)
def sub(*x):
    result = x[0]
    for i in x[1:]:
        result = result - i
    return result 
def multiply(*x):
    result = 1
    for i in x:
        result = result*i
def divide(x,y):
    return x/y
