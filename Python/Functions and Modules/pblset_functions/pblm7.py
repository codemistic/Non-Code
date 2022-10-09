# Intersection of two arrays using filter() function

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
print(list(filter(lambda x:x in new_list1,new_list2)))