lst=[1,2,10,3,4,6,9]

n= len(lst)
ele =  int(input("Enter the value to be searched "))

for i in range(0,n):
    if lst[i]==ele:
        print(i)
        break
else:
    print("Element not found ")


