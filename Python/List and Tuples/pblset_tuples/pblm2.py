#Write a program to create a list of tuples 
# with the first element as the number and 
# the second element as the square of the number

n1 = int(input("Enter the upper range "))
n2 = int(input("Enter the lower range "))
l =[]
l2=[]
print("Enter the element ")
for i in range(n2,n1):
    l.append(i)
    l2.append(i*i)

l_tuple = list(zip(l,l2))
print("Updated list of tuple ", l_tuple)

