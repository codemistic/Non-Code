Pointer is a variable which holds the memory information(address) of another variable of same data type.

* Pointers helps in dynamic memory management.
* Improves execution time.
* More efficient while handling arrays and structures.
* You can pass function as an argument to another function only with the help of pointers.

## Syntax

pointer data type should match with the data type of the variable which is getting pointed.

```c
datatype *pointername;
```

## Example : 1

```c
#include <stdio.h>

int main()
{
    int num = 10;     
    int *ptr;   // pointer variable

    ptr = &num;

   printf("Value of the variable: %u\n", *ptr);

   printf("Value at the address: %d\n", ptr);

   return 0;
}

```
### Check result [here](https://onecompiler.com/c/3vm525v98)


## Example : 2

```c
#include <stdio.h>
int main()
{
  int x = 10, *ptr;

/*ptr = x; // Error because ptr is adress and x is value

*ptr = &x;  // Error because x is adress and ptr is value */

ptr = &x; // valid because &x and ptr are addresses

*ptr = x; // valid because both x and *ptr values 

 printf("Value of *ptr: %u\n", *ptr);
 
 printf("Value of &x: %u\n", &x);
 
 printf("Value of ptr: %u\n", ptr);
 
 printf("Value of x: %u\n", x);

}
```
### Check result [here](https://onecompiler.com/c/3vm52fjwd)

