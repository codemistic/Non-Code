#[1,2,3,4,5] => [1,4,9,16,25]

'''squares = []
numbers = [1,2,3,4,5]
for i in numbers:
    j = i*i
    squares.append(j)
print(squares)'''

#map(function,sequence)
print(list(map(lambda x:x*x,[1,2,3,4,5])))

list1=[1,2,3,4,5]
list2=[6,7,8,9]
print(list1+list2)

#zip : splits to half and connects 
print(list(zip(list1,list2)))

# filter -> filters every element in a sequence 
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))