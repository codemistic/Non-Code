
lst =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = input()
    lst.append(a)
print(lst)

print("\n")
j = 2
for i in range(2,len(lst)):
    if lst[i] != lst[j-2]:
        lst[j]=lst[i]
        j=j +1
for i in range(0,j):
    if (i%2 ==0):
        print(lst[i])
    