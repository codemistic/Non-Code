def stringtoInt(num):
    ans=0
    i=0
    n=len(num)
    while i<n:
        ans=ans+((ord(num[i])-48)*(10**(n-i-1)))
        i+=1
    return ans

n1=input("Enter the value 1 ")
n2=input("Enter the value 2 ")
int1 = stringtoInt(n1)

int2 = stringtoInt(n2)

print(n1+n2)
print(int1+int2)