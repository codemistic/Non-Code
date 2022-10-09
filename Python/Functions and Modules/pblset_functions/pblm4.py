# Write a program to combine values in two lists using list comprehension.  
# Combine only those values of a list that are the multiples of values in the first  list.  

new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = int(input())
    new_list1.append(a)

new_list2 =[]
n2 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n2):
    a = int(input())
    new_list2.append(a)


def multiples(n):
    for i in new_list1:
        if(n & (i-1) == 0):
            return True 


list3=[i for i in new_list2 if multiples(i) == True]
print(list3)

# x must be a power of 2 for below
# logic to work
#if (n & (x -1) == 0)
#   n is a multiple of x
#Else
#   n is NOT a multiple of x