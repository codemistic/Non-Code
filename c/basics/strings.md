String is a sequence of characters terminated with a null character `\0` at the end.

# How to declare strings

Declaring string is similar to one-dimensional character array. Below is the syntax:

```c
char var-name[size];
```

# How to initialize strings

Strings can be initialized in a number of ways:
```c
char str[] = "OneCompiler";

char str[20] = "OneCompiler";

char str[] ={'O','n','e','C','o','m','p','i','l','e','r','\0'};

char str[20] ={'O','n','e','C','o','m','p','i','l','e','r','\0'}
```

# How to read strings from console

```c
#include <stdio.h>
int main()
{
    char str[20];
    scanf("%s", str); // to read the string values from stdin
    printf("You have entered: %s", str); // to print the sting
    return 0;
}
```
### Check Result [here](https://onecompiler.com/c/3vm5393vz)

Consider if you have given `One Compiler` as input in the stdin. Surprisingly you get `One` alone as output. That is because a white space is present between `One` and `Compiler`.  So how can you read a entire line which also has white spaces in it.

Consider your input string is `Hello Everyone.. Happy Learning!!`

```c
#include <stdio.h>
int main()
{
    char str[50];
    fgets(str, sizeof(str), stdin);  // to read string from stdin
    printf("You entered: ");
    puts(str);    // to print entire string
    return 0;
}
```

### Check Result [here](https://onecompiler.com/c/3vm53mc6r)

# String Functions

C has various in-built string functions which can manipulate null-terminated strings.

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
#include <stdio.h>
#include <string.h>

int main () {

   char str1[20] = "Happy";
   char str2[20] = "learning";
   char str3[20];
   char str4[20] = "learning";
   char str[50] = "Hello world, learning is fun.";

   int  length, cmp , cmp1 ;
   int *ptr, * ptr1;  
   
   length = strlen(str1); // to find length of a string
   printf("length of string is :  %d\n", length );
   
   strcat( str1, str2); // concatenates str1 and str2 
   printf("Concatenation of str1 and str2:   %s\n", str1 );

   strcpy(str3, str1); // to copy a string into another
   printf("string copy of str1 to str3 :  %s\n", str3 );

   cmp = strcmp(str2,str4); // to compare two strings
   printf("string compare result :  %d\n", cmp );
   
   
   cmp1 = strcmp(str1,str4); // to compare two strings
   printf("string compare result :  %d\n", cmp1 );
   
   ptr = strchr(str1, 'p'); // usage of strchr
   printf("pointer to the first occurrence of p in string Happy :  %d\n", ptr );
   
   ptr1 = strstr(str, str2); // usage of strstr
   printf("pointer to the first occurrence of str2 in str :  %d\n", ptr1 );
   

   return 0;
}
```

### Check result [here](https://onecompiler.com/c/3vm54ajd2)
