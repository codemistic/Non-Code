#Given an array of positive and negative numbers, 
# arrange them such that all negative  integers appear before 
# all the positive integers in the array. 
# The order of appearance  should be maintained 

new_list =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = int(input())
    new_list.append(a)


list1 =[]
for i in range(0,n):
    if new_list[i] < 0:
       a =new_list[i]
       list1.append(a)
    
for i in range(0,n):
    if new_list[i] > 0:
        list1.append(new_list[i])

print(list1)