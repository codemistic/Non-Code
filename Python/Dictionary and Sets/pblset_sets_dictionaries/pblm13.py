#Create a dictionary to store your friend’s name 
# and their phone number.
#  a) Display the name and phone number of all your friends 
#   b) Delete a particular friend from the dictionary 
#   c) Modify the phone number of an existing friend                     
# d) Display the dictionary in sorted order of names 


n = int(input("Enter the number of people "))
dict_no = {}
for i in range(0,n):
    
    number = int(input("Enter number :"))
    name = input("Enter the name : ")
    dict_no.update({name : number })

print("The information " , dict_no)

name_n = input("Enter the name of the person whose number is to be modified ")
dict_no[name_n] = int(input("Enter the new number "))

name_n3 = input("Enter the name of the friend who is to be deleted ")
del dict_no[name_n3]
print("The phone numbers in sorted order by name ")
print(sorted(dict_no.items()))