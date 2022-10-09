##Solve a quadratic equation ax2+bx+c=0
import math
def quadratic(b,c, a = 1): #default argument
   
    #x1=(-b+sqrt(b*b-4ac))/2*a
    #x2=(-b-sqrt(b*b-4ac))/2*a
    determinant = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + determinant)/(2*a)
    x2 = (-b - determinant)/(2*a)
    return x1,x2

print("One ")
root1, root2 = quadratic(b = 5, c = 6)
print("x1 = "+str(root1))
print("x2 = "+str(root2))

print("\n")

print("Two ")
root1, root2 = quadratic(-1,-1,2)
print("x1 = "+str(root1))
print("x2 = "+str(root2))