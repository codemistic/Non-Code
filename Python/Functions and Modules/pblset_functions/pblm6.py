#Given a list of strings,
#  find all palindromes using filter() function. 


new_list1 =[]
n1 = int(input("Enter the size of the list :"))
print("Enter the elements one by one :")
for i in range(0,n1):
    a = input()
    new_list1.append(a)


def check_palindrome(wrd):
    wrd2 = wrd[::-1]
    if (wrd == wrd2):
        return True 

print("The palindromes are ", list(filter(check_palindrome,new_list1)))

