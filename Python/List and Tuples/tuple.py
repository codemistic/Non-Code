#tuples
#immutable,(1,2,3)


number = 1,2,3,4
print(number)#default tuple
print(type(number))

random_tuple=(1,2,3,5.0,"Ria")
print(random_tuple)
#the comma is necessary for to be tuple
print(random_tuple[-2:-4:-1])

squares=(1,4,9,[16,25],36)
print(squares[3][1])
squares[3][1]=43
print(squares)
#here the list is mutable which is in a tuple 
