def add(x,y):
    return x+y


result = add(5,6)
print(result)

def greet():
    print("Good morning ")
    print("Hello! ")

greet()

def update(x):
    x = 10
    print("inside functions :"+ str(x))

def randfunc():
    y = 15 
    return y

x = 5
print("outside function: "+str(x))
update(x)
print("after executing the function, the value of x: "+ str(x))

print(randfunc())
