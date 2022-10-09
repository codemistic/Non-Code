#If X = {2,4, 6, 8, 10,12,14,16,18,20} and 
# Y = {1,3,6,9,12,15,18}. 
# Using python sets X, Y write a script to find all elements
#  i) that occur only in X but not in Y 
# ii) that may occur X or Y 
# iii). Print all elements that are common to X and Y 
# iv) does Y contain all elements of X .
# v)  X. pop() will return which element? 
# vi) Add 21 to set Y
#  vii) Delete 20 from X .
#  viii) does 24’ occur in Y?.
# ix) print all elements in X, one per new line.
#  x) find the total elements in X and Y together

X = {2,4, 6, 8, 10,12,14,16,18,20}
Y = {1,3,6,9,12,15,18}
print("Only occur in X and not in Y :", X.difference(Y))
print("Occur in X or Y :", X.union(Y))
print("Common to X and Y :",X&Y)
print("Does Y contain all elements of X: ", X.issubset(Y))
print("X.pop() will return: ",X.pop())
Y.add(21)#adding 21 to set Y
X.discard(20)#removing 20 from X

#to find if 24 is present in Y
if 24 in Y:
    print("Yes 24 is present in Y")

print("The elements in X line by line ")
for i in X:
    print(i)

c = 0
S = X|Y
for j in S:
    c = c + 1
print("The total no of elements in X and Y together : ",c)