#FIND WHETHER A STRING IS PALINDROME OR NOT 
# malayalam -> palindrome

string_a = input("Enter the word :")
string_b = string_a[::-1]
if string_a == string_b:
    print("Palindrome")
else:
    print("OOPS!")