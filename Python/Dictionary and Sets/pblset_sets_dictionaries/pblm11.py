# Write a python program to input ‘n’ names and phone numbers to store it in 
# a dictionary and to input any name and 
# to print the phone number of that particular name

n = int(input("Enter the number of people "))
dict_ph = {}
for i in range(0,n):
    name = input("Enter the name : ")
    number = int(input("Enter phone number :"))
    dict_ph.update({name : number })

name_s = input("Enter the name to search :")
print("The number is ", dict_ph.get(name_s))
