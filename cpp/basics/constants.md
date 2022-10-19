
Literals/constants are used to represent fixed values which can't be altered later in the code.

## 1. Integer literals

Interger literals are numeric literals. Below are the examples of various types of literals

```c
79         // decimal (base 10) 
0253       // octal (base 8)
0x4F       // hexadecimal (base 16)
22         // int
53u        // unsigned int
79l        // long
7953ul       // unsigned long
```

## 2. Float point literals

Float point literals are also numeric literals but has either a fractional form or an exponent form.

```c
79.22         // valid
79E-5L        // valid
53E          // not valid as it is incomplete exponent
.e22          // not valid as missing integer or fraction
```

## 3. Boolean literals

There are two Boolean literals which are part of standard C++ keywords −

* true value representing true.

* false value representing false

## 4. Character literals

Character literals are represented with in single quotes. For example, `a`, `1` etc. A character literal can be a simple character (e.g., 'a'), an escape sequence (e.g., '\n'), or a universal character (e.g., '\u02C0').

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
|\? | ? Question mark|
|\b	|Back space|
|\a | alert or bell|

## 5. String literals

String literals are represented with in double quotes. String literals contains series of characters which can be plain characters, escape sequence or a universal character.

```c
"Hello World"
```

##  How to define constants

You can use either `#define` or `const` to define constants as shown below.

* Using #define

```c
#define identifier-name value
```
* Using Const

```c
const datatype variable-name = value;
```
