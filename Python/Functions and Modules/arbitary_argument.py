#arbitary_argument = uncertain about the no of values 

#acts as a tuple
def add(*x):
    print(x)
    print(type(x))
    return sum(x)

print(add(10,43,54,66,73))