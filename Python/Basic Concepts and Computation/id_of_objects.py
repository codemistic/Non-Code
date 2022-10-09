num1 = 5

print(id(num1))
print(id(5))
#these id will be same 

num2 = num1
print(num2)
print(id(num2))
#num2 is being reffered to the same value and hence the id will be same 

num3 = 5
print(id(num3))
#this too will be same 
#address is all about the value and not the variable name

num1=10
id(num1)
#here the is will be different as the value is different 

