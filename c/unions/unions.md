Union is a user-defined datatype similar to structs which allows to store different data types in the same memory location. Unions can be defined with many members, but only one member can contain a value at any given time.

# How to define a Union

Union definition is similar to structure definition but you use `union` as the keyword.

```c
union union_name {
   member definition;
   member definition;
   ...
   member definition;
} [one or more union variables];  
```

## Example

```c
union mobile
{
    char model[30];
    char brand[30];
    int cost;   
};
```
# How to create Union variables

Union variables can be declared in two ways.

1. Declaring variables seperately from its definition.

```c
union union_name variable name;
```

2. Declaring variables along with definition(this method is not recommended)


```c
union union_name {
   member definition;
   member definition;
   ...
   member definition;
} one or more union variables;  
```
## Example

```c
// Declaring variables seperately from its definition
union mobile m1, m2;

//Declaring variables along with definition
union mobile {
    char model[30];
    char brand[30];
    int cost; 
}m1, m2;

```

## How to access members of a union

You can access the union member using `variable_name.membername`

# Difference between Structures and Unions

* You can access all memebers of a structure at once but you can access only one member of a union at once.
* Size of a union variable  will always be the size of its largest element where as size of a structure variable greater or equal to the sum of sizes of all its elements.
* Memory is shared by union members where as structure members are assigned with unique storage area.
* Several members can be initialized at once in structures where as first member of a union can be initialized.

