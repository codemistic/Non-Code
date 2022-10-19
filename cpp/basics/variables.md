
Variables are like containers which holds the data values. A variable specifies the name of the memory location. 

## How to declare variables

```c
data-type variable-name = value;
```
In the above syntax, assigning value is optional as you can just declare the variable and then assign value at later point in the program. Also, the value of a variable can be changed at any time.

## Naming convention of variables

* Variable names can have only letters (both uppercase and lowercase letters), digits and underscore(`_`).
* Variables naming cannot contain white spaces like `first name` which is a invalid variable name.
* First letter of a variable should be either a letter or an underscore(`_`).
* Variable type can't be changed once declared as C++ is a strongly typed language.
* In C++, Variable names are case sensitive and hence Name and name both are different.
* It is always advisable to give some meaningful names to variables.

### Example

```c
int x = 10; // declaring int variable and assigning value 10 to it
char grade = 'A'; // declaring char variable and assigning value A to it
```
The above can also be written like below

```c
int x; // declaring int variable 
char grade; // declaring char variable 

x = 10; // assigning value 10 to x variable
grade = 'A'; //and assigning value A to grade variable
```
