#Given a list of number, 
# return the list with all even numbers doubled, 
# and all odd numbers turned  negative 

new_list =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = int(input())
    new_list.append(a)

list1 =[]

for i in range(0,n):
    if (new_list[i]%2 == 0):
        list1.append(new_list[i]*2)
    else :
        list1.append(new_list[i]*(-1))

print("Updated list ", list1)