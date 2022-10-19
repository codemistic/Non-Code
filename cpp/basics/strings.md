String is a sequence of characters terminated with a null character `\0` at the end. There are two types of strings in C++.

1. C-Strings
2. Strings that are objects of string class

# How to declare strings

Declaring strings is similar to one-dimensional character array. Below is the syntax:

```c
char var-name[size];
// or
string str;
```

# How to initialize strings

Strings can be initialized in a number of ways:
```c
char str[] = "OneCompiler";

char str[20] = "OneCompiler";

char str[] ={'O','n','e','C','o','m','p','i','l','e','r','\0'};

char str[20] ={'O','n','e','C','o','m','p','i','l','e','r','\0'};

string str = "OneCompiler";
```

# How to read strings from console

```c
#include <iostream>
using namespace std;
int main()
{
    char str[20];
    cin >> str; // to read the string values from stdin
    cout << "You have entered: " << str; // to print the sting
    return 0;
}
```
### Check Result [here](https://onecompiler.com/cpp/3vmbntfpm)

Consider if you have given `One Compiler` as input in the stdin. Surprisingly you get `One` alone as output. That is because a white space is present between `One` and `Compiler`.  So how can you read a entire line which also has white spaces in it.

Consider your input string is `Hello Everyone.. Happy Learning!!`

```c
#include <iostream>
using namespace std;

int main()
{
    string str;
    getline(cin, str);  // to read string from stdin
    cout << "String entered is : " << str ;
    return 0;
}
```

### Check Result [here](https://onecompiler.com/cpp/3vmbnzg24)

# String Functions

C++ has various in-built string functions which can manipulate null-terminated strings.

| Function name | Description|
|----|----|
|strlen(str)| to return the length of string str|
|strcat(str1, str2)| to concatenate string str2 onto the end of string str1.|
|strcpy(str1, str2)| To copy string str2 into string str1.|
|strcmp(str1, str2)| returns 0 if str1 and str2 are the same and less than 0 if str1 < str2 and a positive number if str1 > str2|
|strchr(str, c)| Returns a pointer to the first occurrence of character c in string str|
|strstr(str1, str2)| Returns a pointer to the first occurrence of string str2 in string str1|


## Examples

```c
#include <iostream>
using namespace std;
#include <cstring>

int main() 
{

   char str1[20] = "Happy";
   char str2[20] = "learning";
   char str3[20];
   char str4[20] = "learning";

   int  length, cmp , cmp1 ;

   length = strlen(str1); // to find length of a string
   cout << "length of string is :  " << length << endl;
   
   strcat( str1, str2); // concatenates str1 and str2 
   cout << "Concatenation of str1 and str2: " << str1 << endl;

   strcpy(str3, str1); // to copy a string into another
   cout << "string copy of str1 to str3 :  " << str3 << endl;

   cmp = strcmp(str2,str4); // to compare two strings
   cout << "string compare result :  "<< cmp << endl;
   
   
   cmp1 = strcmp(str1,str4); // to compare two strings
   cout << "string compare result :  " << cmp1 << endl;
   
   return 0;

}
```

### Check result [here](https://onecompiler.com/cpp/3vmbp94k9)
