Structure is a user-defined data type where it allows you to combine data of different data types. In a way, Structures are similar to arrays but the difference is in type of the data. Arrays is a collection of similar data but structures combine different types of data.

# How to define a structure

`struct` keyword is used to define a structure. 

```c
struct structure_name {

   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables]; 
```

# How to declare structure variables

Structure variables can be declared in two ways.

1. Declaring variables seperately from its definition.

```c
[struct] structure_name variable name;
```

2. Declaring variables along with definition(this method is not recommended)


```c
struct structure_name {

   member definition;
   member definition;
   ...
   member definition;
} one or more structure variables; 
```

## Example 

```c
// structure definition
struct mobile {
    char model[30];
    char brand[30];
    int cost; 
}

// Declaring variables seperately from its definition

mobile m1, m2;

//Declaring variables along with definition

struct mobile {
    char model[30];
    char brand[30];
    int cost; 
}m1, m2;

```

## How to access structure members

You can access the structure member using `variable_name.membername`


### Example 
```c
#include <iostream>
using namespace std;

struct mobile {
    string model;
    string brand;
    int cost; 
};


int main()
{
  mobile m1;
  m1.brand = "Apple";

  // display the value of structure variable and accessing structure variable - brand
  cout << "Brand of the mobile: " << m1.brand;
    
  return 0;
}

```

### Check result [here](https://onecompiler.com/cpp/3vmdham3n)

## Difference between C structures and C++ structures

| C Structures | C++ Structures |
|----|----|
| Member functions are not allowed inside structures| Member functions are allowed inside structures|
| Direct initialization of members are not possible| Direct initialization of memebers can be done |
| struct keyword is compulsory to declare structure variables | struct keyword is not required to declare structure variables |
| Constructor can't be present in structures | Can have constructor in structure|
| Can not have static members | Can have static members |

