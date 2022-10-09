#.Write a program that infinitely prints natural numbers.
#  Raise  the Stop lteration exception 
# after displaying first 20 numbers to  exit the pro

try:
    x = 1
    while True:
        print(x)
        x += 1
        if x > 20:
            raise StopIteration 
except StopIteration :
    print("End of the loop")






