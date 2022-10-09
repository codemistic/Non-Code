#SETS 
#immutable 
set1={1,3,35}
#doesn't have any order or index 


#create empty set 
y = set() 
print(type(y))
x={}#this will be dict 

set1.add(17)#this will be added in random position
set1.remove(3)
print(set1)

#set1.remove(50)#shows error as it isn not present in the set 
set1.discard(50)#doesn't show error 
set1.pop()#deletes and returns the first value 


#Set operations -> union, intersections, difference 
A={1,2,3,4,5,6,7}
B={6,7,8,9,10}
#A U B
print(A|B)
print(A.union(B))
print(B.union(A))
 #A n B 
print(A&B)

print(B-A)
print(A.difference(B))

A={1,2,3}
B={1,2,3,4,5}
#subsets 
print(A.issubset(B))
print(A.issuperset(B))
A.clear()
#clear set 