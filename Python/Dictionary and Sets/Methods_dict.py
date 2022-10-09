#square = {expression(key:value) for loop condition}

squares = {i:i*i for i in range(1,11)}
print(squares)

##METHODS 
details = {'name':"Riya","age": 18,"grade":12}
print(details.keys())
print(details.values())
det2 = details.copy()
print(det2)
print(details.pop('name'))#remove the particular value and return the value 
#mere key doesn't exist and hence the key will also be removed 