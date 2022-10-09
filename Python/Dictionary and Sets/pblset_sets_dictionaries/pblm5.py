#Create the following three sets 
#A = {squares less than 20} 
#B = {even numbers less than 20} 
#C = {odd squares less than 20 } 
#i. Find the numbers which are both even number and squares less than 20 
#ii. Find the resultant set of adding all the three set elements 
#iii.  find the union of set A and B 
#iv. Find the total count of elements in all the three sets. 
#v. Check if number 14 occurs in set B. if so, print “yes” else “no” 
#vi. How an element 16 is removed from set A?

A= set()
B=set()
C=set()

for i in range(1,20):
    for j in range(1,5):
        if i == j*j :
            A.update(i)
            if (i%2 != 0):
                C.update(i)
    if i%2 == 0 :
        B.update(i)

#i. 
print("Both even and square :",A&B)
#ii.
print("Resultant of all the sets ", A&B)
#iii
print("Union of set A and B:",A|B)
#iv
D=A|B
print("Total count of elements in all three sets :",len(D))
#v
for i in B:
    if i == 14 :
        print("yes")
    else :
        print("no")

#vi
A.discard(16)
print(A)