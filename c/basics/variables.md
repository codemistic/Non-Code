# Variables

Variables are like containers which holds the data values. A variable specifies the name of the memory location. 

## How to declare variables

```c
data-type variable-name = value;
```
In the above syntax, assigning value is optional as you can just declare the variable and then assign value at later point in the program. Also, the value of a variable can be changed at any time.

## Naming convention of variables

* Variable names can have only letters (both uppercase and lowercase letters), digits and underscore(`_`).
* Variable names cannot contain white spaces like first name which is a invalid variable name.
* First letter of a variable should be either a letter or an underscore(`_`).
* Variable type can't be changed once declared as C is a strongly typed language.
* In C, Variable names are case sensitive and hence Name and name both are different.
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

# Literals

Literals are used to represent fixed values which can be used directly in the code.

## 1. Integer literals

Integer literals are numeric literals. They are of three types

* decimal (base 10) 
* octal (base 8)
* hexadecimal (base 16)

## 2. Float point literals

Float point literals are also numeric literals but has either a fractional form or an exponent form.

## 3. Character literals

Character literals are represented with in single quotes. For example, 'a', '1' etc.

## 4. String literals

String literals are represented with in double quotes. For example, "OneCompiler", "Foo" etc.

## 5. Escape Sequences

There are few cases where you need to represent a character(s) which has special meaning in C or which can't be typed like newline, tab etc.

|Escape sequence| Description|
|----|----|
|\n	| New line|
|\r	| Carriage Return|
|\?	| Question mark|
|\t	| Horizontal tab|
|\v	| Vertical tab|
|\f	|Form feed|
|\\	| Backslash|
|\'	| Single quotation|
|\"	| Double quotation|
|\0 | Null character|
|\b	|Back space|

# Expressions

Expression is a combination of one or more variables, operators and literals. it can be a simple sum (x+y) or a very complex mathematical formula.

You can't write the mathematical formulae in the same way in programming languages as there are certain limitations to it. For example, there is no root operator and you must use sqrt() function present in `math.h`.

`math.h` provides great support to evaluate mathematical functions.

