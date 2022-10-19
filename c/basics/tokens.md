
Token can be referred as the smallest possible unit in C. C program consists of various tokens, which can be a keyword, an identifier, a constant, a string or a symbol.

### Example

The below statement consists of 5 tokens:
```c    
printf("Happy learning");
```
1. `printf` : an inbuilt library function
2. `(` : symbol 
3. `"Happy learning"` : string
4. `)` : symbol
5. `;`  : semicolon which is a statement terminator


Token is divided into six categories as follows:

## 1. Keywords 

Keywords are the reserved words in a programming language. C supports 31 keywords as below

```c
auto         double      int        struct
break        else        long       switch
case         enum        register   typedef
char         extern      return     union
const        float       short      unsigned
continue     for         signed     void
default      goto        sizeof     volatile
do           if          static     while
```
## 2. Identifiers

Identifiers are the user defined names for variables, functions and arrays.

Rules for defining an identifier:
* They must be less than or equal to 31 characters.
* No special characters.
* Must start with a letter or under score.
* Can contain letters, digits, or underscore only.

## 3. Strings

Strings are an array of characters ended with null character. Characters are enclosed in single quotes where as strings are always enclosed in double quotes.

```c
    char str[]="onecompiler";
```

## 4. Operators

Operators are the symbols which specifies an action when applied on variables.

* Arithmetic operators
* Relational Operators
* Logical Operators
* Assignment Operators
* Conditional Operators
* Bitwise Operators

Let's learn operators in detail in coming chapters.

## 5. Constants

Constants are the fixed values. Constant values can't be changed once defined. Constants can be defined in two ways.

### 1. Using `const`:

``` c
const datatype <constant-name> = <constant-value>;
```
### 2. Using `#define`:

```c
#define <constant-name> <constant-value>
```
#### Note: 

It's a good programming practice to define constants in CAPITALS.

## 6. Special Characters

Few characters have special meaning and hence these can't be used for other purposes.

* `{}` : specifies start and end of code blocks
* `[]` : used for arrays
* `()` : used for functions
* `,` : used to seperate variables, constants etc
* `*` : used for pointers
* `#` : used as a macro processor.

