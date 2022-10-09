#anonymous functions : lambda 
#only one return statement , take any number of arguments 
#no name, use keyword lambda 

#structure 
#variable = lambda arguments:return expression 

add = lambda x,y:x+y 
print(add(4,6))

squares = lambda x:x**2
print(squares(3))

#tuples and lists can also be passed 

#APPLICATIONS 

#sorting 

list1=[(1,10),(122,4),(23,67),(34,56)]
print("sorted on the basis of the first element ")
print(sorted(list1))
print("Sorted on the order of the second element ")
print(sorted(list1,key = lambda x:x[1]))