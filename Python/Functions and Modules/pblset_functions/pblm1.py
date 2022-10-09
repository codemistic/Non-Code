#. Write a program to create a list which has both positive and negative numbers.
#   Create another list using filter() that has only positive values

new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = int(input())
    new_list1.append(a)



print(list(filter(lambda x:x > 0,new_list1)))
