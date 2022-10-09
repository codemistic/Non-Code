#if statements 
a = 10  
b = 20  
if a<b:  
  print("a is less than b")  

#if else statements 
a = 10  
b = 20  
if a==b:  
  print("a and b are equal")  
else:  
  print("a and b are not equal")  

#elif statements 
a = 10  
b = 10  
if a < b:  
  print("a is greater than b")  
elif a == b:  
  print("a and b are equal")  
else:  
  print("b is greater than a")  

#nested if 
a= 1001  
if a> 100:  
  print("Above 100")  
  if a > 1000:  
    print("and also above 1000") 

#nested if else 
a=int(input("enter the a value"))#user give a value  
if a> 100:  
  print("Above 100")  
  if a > 1000:  
    print("and also above 1000")  
  else:  
    print("and also below 1000")  
else:  
    print("below 100")  