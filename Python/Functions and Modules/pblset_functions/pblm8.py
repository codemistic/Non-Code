#. Given an array of positive and negative numbers, 
# arrange them such that all  negative integers appear
#  before all the positive integers in the array. 
# The order  of appearance should be maintained. 
#  Output arr = [-13, -5, -7,-3, -6, 12, 11, 6, 5] 

new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = int(input())
    new_list1.append(a)

arr =[]
for i in new_list1 :
    if i < 0 :
        arr.append(i)



for i in new_list1 :
    if i > 0 :
        arr.append(i)

print("Output arr =",arr)        