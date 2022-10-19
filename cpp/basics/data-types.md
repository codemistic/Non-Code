As the name suggests, data-type specifies the type of the data present in the variable. Variables must be declared with a data-type. 

There are three different types of Data types in C++.

| Types | Data-type|
|----|----|
|Basic | int, char, float, double, short, short int, long int etc |
|Derived | array, pointer etc |
|User Defined Data Type | structure, enum, Class, Union, Typedef |


## 1. Basic data types

Basic data types are generally arithmetic types which are based on integer and float data types. They support both signed and unsigned values. Below are some of the oftenly used data types

| Data type | Description | Range | Memory Size|
|----|----|----|----|----|
| int| used to store whole numbers|-32,768 to 32,767|2 bytes| 
|short int| used to store whole numbers|-32,768 to 32,767| 2 bytes|
|long int| used to store whole numbers|	-2,147,483,648 to 2,147,483,647| 4 bytes|
|float| used to store fractional numbers|6 to 7 decimal digits| 4 bytes|
|double| used to store fractional numbers|15 decimal digits| 8 bytes|
|char|used to store a single character|one character|1 bytes|
|bool| Boolean data type| 1 byte|

### Examples

```c
#include <iostream>
using namespace std;

int main() 
{

int x = 90;
int y = sizeof(x);
cout << "size of x is: " << y << endl;

float f = 3.14;
cout << "size of float is: " << sizeof(f) << endl;

double d = 2.25507e-308;
cout << "size of double is: " << sizeof(d) << endl;

char c = 'a';
cout << "size of char is: " << sizeof(c) << endl;

return 0;
}

```
#### Run [here](https://onecompiler.com/cpp/3vm83rs6y)

## 2. Derived or User defined Data types 

Derived Data types and user defined dta types are the ones which are derived from fundamental data types and are defined by user. Arrays, Pointers, functions etc. are examples of derived data types. Enum, Structures, Class, union, enum, typedef etc are User defined data types. Let's learn more about them in next chapters.
