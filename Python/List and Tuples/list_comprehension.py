#generate a list of squares 

#squares=[1,4,9,16,25,36]
#squares=[#expression #for_loop #condition]
squares_1=[i*i for i in range(1,11)]
print(squares_1)

squares_even =[i*i for i in range(1,11) if i%2==0]
print(squares_even)

print("/n")


#join() method in string related to lists 
words=["I","am","a","peaceful","girl"]
#words -> a single string 
print(" ".join(words))#anything can be mentioned in the double quotes 

print("\n\n")

#Given two list and make a new list which contains the elements in both the list as in intersection
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list3=[i for i in list1 if i in list2]
print(list3)

print("\n")

#User input in list
new_list =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n):
    a = input()
    new_list.append(a)
print(new_list)

print("\n")


new_list2 =[]
n = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
new_list2 = [input() for i in range(0,n)]
print(new_list2)

print("\n")

