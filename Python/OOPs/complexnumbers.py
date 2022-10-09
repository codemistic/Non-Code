#x+iy - > complex number 
from re import I


class Complex_No:
    def __init__(self,real,img) :
        self.r = real
        self.i = img
        
    def __str__(self): #return the string and executes when print 
        return ("The complex no is {}+{}i".format(self.r,self.i))

    def __add__(self,other):
        x = self.r+other.r
        y=self.i+other.i
        return "{}+{}i".format(x,y)
num1 = Complex_No(5,2)
num2 = Complex_No(10,3)
print(num1)
print(num1+num2)