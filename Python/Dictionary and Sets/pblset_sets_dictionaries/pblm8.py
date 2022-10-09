#A vegetable vendor  wishes to store the vegetables 
# she sells in her shop along with the price/kg.
#  She stores at the maximum five vegetable prices.
# To this  add a new vegetable with its price
#  and also print the cost of ‘Brinjal’ 
# - print  ‘Zero’ if  not available .
#  Finally update the cost of  ‘onion’


veggies = {}

n = 0
while True & n < 5:
    print("Enter the vegetable :")
    a = input()
    print("Enter the price per kg: ")
    b = input()
    n = n + 1
    veggies[a]=b 

print("Enter the new vegetable :")
new_veg = input()
print("Enter the price per kg: ")
price = input()

veggies[new_veg]=price

if (veggies["Brinjal"] != 0):
    print("The cost of brinjal is ",veggies["Brinjal"])
else:
    print('Zero')

print("Update the cost of onion: ")
new_price = input()
veggies['onion'] = new_price