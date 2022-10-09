##LIST ->collection of data 
#versatile 

#How to create a list
list1=[]
#updatable
list1=[1,2,3,4,5,6]
print(list1)
list1=[1,2,3,4,5,6,"apple","orange",4.56]
print(type(list1[1]))#1
print(list1[-1])#4.56


print("\n\n")

#nested list 
list2=[1,2,3,["apples","oranges"]]
print(list2[3])#the whole last list 
print(list2[3][1])#access the second pos in the nested list in 3 pos


print("\n\n")


animals=["giraffe","Lion","Tiger","Panda","Polar bear"]
print(len(animals))
print(animals[0:2])#first two 
print(animals[-1:-2:-1])#last one


print("\n\n")


#changing values in a list
squares=[1,4,16,25,23,54]
print(squares[-2])
print(squares[4:])


print("\n\n")

#adding elements to list 
#append(), extend() 
squares = [1,4,9]
squares.append(17)#adds 17 to the end of the list
print(squares) 
squares.extend([54,45,76,26])#adds these to the end 
print(squares)


print("\n\n")


odd=[1,2,5,6,434,54,432,54,89,9]
#odd.insert(index,object)
odd.insert(-1,17)
print(odd)
odd.sort()
print(odd)
odd.sort(reverse=False)#default its true, sorted reverse 
print(odd)
odd.reverse()#reverse without sorting
print(odd)
#pop(index)->remove and return the element 
print(odd.pop(-2))
print(odd)
#remove(value)->doesnt not return the element but delete from the list 
odd.remove(54)
print(odd)
print(odd.count(54))#frequency
print(odd.index(434))#look for the value and returns the index 

happy = odd.copy()#storing a copy 

#list methods and functions eg: sum(),max(),min(),len(),any(),all()

