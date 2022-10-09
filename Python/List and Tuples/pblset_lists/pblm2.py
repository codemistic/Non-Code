# Given a list of positive integers, 
# find the number occuring odd number of times in a list 

from socket import TIPC_CRITICAL_IMPORTANCE


new_list =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = int(input())
    new_list.append(a)

def getOddOccurrence(new_list1,n1):
    
    for j in range(0,n1):
        c = 0
        for i in range(0,n1):
            if new_list1[i] == new_list1[j]:
                c = c + 1
        if (c % 2 != 0):
            return new_list1[j]
    return 1

print("The elements that occur odd number of times :")
print(getOddOccurrence(new_list,n))      

