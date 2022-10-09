#intersection of two lists 

new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = input()
    new_list1.append(a)

new_list2 =[]
n2 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n2):
    a = input()
    new_list2.append(a)

list3 = [i for i in new_list1 if i in new_list2]
print("The list which is an intersection of the inputted list is :")
print(list3)