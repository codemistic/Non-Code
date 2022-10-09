# Write a program to print the list 
# after removing the particular value from the list

new_list =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = input()
    new_list.append(a)

n = input("Enter the value to be removed ")
new_list.remove(n)
print("Updated list :", new_list)
