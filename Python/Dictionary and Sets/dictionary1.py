#create dictionary 
details = {"name": "Riya" , "age": 25 , "contact": 756973705 }
print(details)

#get me the age 
a =details["age"]
print(a)


#KeyError is due to the group not being present in the dictionary as key 

#adding new keys and assigning values 
details["blood group"] = "O+"
print(details)

#changing the value 
details["age"]= 18 
print(details)
print(details.get("name"))

#creating dictionary using another method 
squares=dict([(1,1),(2,4),(3,9)])
#dict[list(tuplepairs)]
print(squares)