# To convert strings of all uppercase to lowercase 
# using map() function

value = input("Enter the string ")
new_list = list(value)

def case_value(n):
    return n.upper()

a = (map(case_value,new_list))
print("".join(a))