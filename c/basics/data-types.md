As the name suggests, data-type specifies the type of the data present in the variable. Variables must be declared with a data-type. 

There are four different types of Data types in C.

| Types | Data-type|
|----|----|
|Basic | int, char, float, double|
|Derived | array, pointer, structure, union|
|Enumeration | enum|
|Void |	void|


## 1. Basic data types

Basic data types are generally arithmetic types which are based on integer and float data types. They support both signed and unsigned values. Below are some of the oftenly used data types

| Data type | Description | Range | Memory Size| Format specifier|
|----|----|----|----|----|
| int| used to store whole numbers|-32,768 to 32,767|2 bytes| %d|
|short int| used to store whole numbers|-32,768 to 32,767| 2 bytes|%hd|
|long int| used to store whole numbers|	-2,147,483,648 to 2,147,483,647| 4 bytes|%li|
|float| used to store fractional numbers|6 to 7 decimal digits| 4 bytes|%f|
|double| used to store fractional numbers|15 decimal digits| 8 bytes|%lf|
|char|used to store a single character|one character|1 bytes|%c|

### Examples

```c
#include <stdio.h>
#include <float.h>

int main()
{
int x = 90;
int y = sizeof(x);
printf("size of x is: %d " , y);

float f = 3.14;
printf("\nsize of float is: %d " , sizeof(f));

double d = 2.25507e-308;
printf("\nsize of double is: %d " , sizeof(d));

char c = 'a';
printf("\nsize of char is: %d " , sizeof(c));
}
```
### Check result [here](https://onecompiler.com/c/3vkf2hsrg)

## 2. Derived Data types

Derived Data types are the ones which are derived from fundamental data types. Arrays, Pointers, Structures, etc. are examples of derived data types. Let's learn more about them in next chapters.

## 3. Enumeration Data types

Enumeration Data type is a user-defined data type in C. `enum` keyword is used to declare a new enumeration types in C. 

### Syntax

```c
enum name{constant1, constant2, constant3, ....... };
```
### Example

```c
#include<stdio.h> 
  
enum month{January, February, March, April, May, June, July, August, September, October, November, December};
  
int main() 
{ 
    enum month name; 
    name = June; 
    printf("%d",name); 
    return 0; 
} 
```
### Check result [here](https://onecompiler.com/c/3vkf3vuuu)

## 4. Void Data types

Void specifies that there is no return value. Generally void is used in the below situations.

* If the funtion has return type mentioned as Void, then it specifies that the function returns no value.
* A function with out any parameters can accept void. For example., char greetings(void)
* A pointer with type specified as void represents the address of an object but not it's type. Let's learn more about pointers in next chapters.

