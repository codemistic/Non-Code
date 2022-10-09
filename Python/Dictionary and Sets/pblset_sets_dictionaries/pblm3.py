#Let X={‘p’,’r’,’o’,’g’,’r’,’a’,’m’,’m’,’i’,’n’,’g’, ‘i’,’n’,’ p’,’y’,’t’,’h’,’o’,’n’} 
#  Y={a,e,i,o,u} 
#write scripts to find elements 
# a) that occur only in X but not in Y 
# b) that occur in X or Y. 
# c) that occur in X and Y
# . d) Check whether X contains all elements of Y, i
# f so print “All vowels are in X”.
#  e) Create a new set by deleting all vowels from X

X={'p','r','o','g','r','a','m','m','i','n','g', 'i','n','p','y','t','h','o','n'} 
Y={'a','e','i','o','u'} 
print("Only in X but not in Y :",X.difference(Y))
print("That occur in X or Y :", X|Y)
print("That occurs in X and Y :", X&Y)
print("If X contains all elements of Y: ",Y.issubset(X))
if Y.issubset(X) == True:
    print("All vowels are in X")

L = set()
for i in X:
    if i not in Y:
        L.update(i)

print("The new set X after deleting vowels is :", L)

