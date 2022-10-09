##exception handling - > 10/0; a=5; a.lower()
## try, except, else, finally

#try:
#    pass
#except:
#    pass
#else:
#    pass

#inbuilt errors 
try:
    a = 10/0
except ZeroDivisionError:
    print("division by zero impossible")
else:
    print("no errors")

#raising errors 
a = input("Enter a number ")
if a.isdigit():
    print("it is a number ")
else:
    raise ValueError