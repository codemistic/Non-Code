#Write a program to print the square root of a number. 
# Raise an  exception if the number is negative. 

import math

def sqRoot(x):
    try:
        result = math.sqrt(x)
    except ValueError:
        result = "This is a negetive number"
    return result 

n = int(input("Enter an number : "))
print(sqRoot(n))