#To find the largest value in the list 
# using reduce() function. 

import functools

new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = int(input())
    new_list1.append(a)

print("The largest number is :", functools.reduce(lambda a,b : a if a > b else b, new_list1))
