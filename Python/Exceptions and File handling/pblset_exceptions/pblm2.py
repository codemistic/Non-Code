#.Write a program that prompts the user to enter a number.
#  if the number is +ve or 0 print it., 
# otherwise raise an exception 

try:
    i = int ( input ( "Enter an integer value: " ) )
    if i < 0:
        raise ValueError 
    else :
        print(i)
except ValueError :
    print("This is a negetive number ")
