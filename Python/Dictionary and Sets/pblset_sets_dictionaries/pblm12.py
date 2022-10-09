# Write a program to input ‘n’ employee number and name and
#  to display all employee’s information in ascending order based upon their number.


n = int(input("Enter the number of people "))
dict_no = {}
for i in range(0,n):
    
    number = int(input("Enter employee number :"))
    name = input("Enter the name : ")
    dict_no.update({number : name})

print("The information in ascending order ")
print(sorted(dict_no.items()))
