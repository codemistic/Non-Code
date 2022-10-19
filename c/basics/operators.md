Let us understand the below terms before we get into more details.

### 1. Operator

An operator is a symbol which has special meaning and performs an operation on single or multiple operands like addition, substraction etc. In the below example, `+` is the operator. 

```c
#include<stdio.h>
 
int main() {
   int x, y, sum;
   x = 10;
   y = 20;
 
   sum = x + y;
   printf("Sum : %d", sum);
 
   return(0);
}
```
### Check result [here](https://onecompiler.com/c/3vke66v52)

### 2. Operand

An operand is what operators are applied on. In the above example `x` and `y` are the operands.

# Types of Operators in C

## 1. Arithmetic Operators

C arithmetic operators are used to perform arithmetic operations on operands.

|Operator|	Description	| Example|
|----|----|----|
| +	| Used to perform Addition |	8+2 = 10|
| - | Used to perform Subtraction |	12-2 = 10|
| * | Used to perform Multiplication |	5*2 = 10|
| / | Used to perform Division	| 100/10 = 10|
| % | Used to return Remainder	| 40%10 = 0|
| ++ | Used to perform Increment |	int a=10; a++; // a becomes 11|
| -- | Used to perform Decrement |	int a=10; a--; // a becomes 9|


### Example

```c
#include<stdio.h>
int main() {
   int x, y, sum, diff, product, division, mod, inc, dec;
   x = 90;
   y = 10;
 
   sum = x + y;
   printf("Sum : %d", sum);
   
   diff = x - y;
   printf("\nDifference : %d", diff);
   
   product = x * y;
   printf("\nProduct : %d", product);
   
   division = x / y;
   printf("\nDivision : %d", division);
   
   mod = x % y;
   printf("\nRemainder : %d", mod);
   
   inc = x++;
   printf("\nx value after incrementing : %d", x);
   
   dec = x--;
   printf("\nx value after decrementing : %d", x);
 
   return(0);
}
```
### Check Result [here](https://onecompiler.com/c/3vke6dadr)

## 2. Comparison Operators

C comparison operators are used to compare two operands. 

| Operator | Description| Usage|
|----|----|----|
| == | Is equal to | x == y|
| != | Not equal to |	!=x |
| > | Greater than | x > y |
| >= | Greater than or equal to |	x >= y|
| < | Less than| x < y |
| <= | Less than or equal to| x <= y|

### Example

```C
#include<stdio.h>
int main() {
   int x = 90;
   int y = 10;
   
  if ( x == y) {
    printf("x and y are equal");
  }
  
  if ( x != y) {
    printf("\nx and y are not equal");
  }
  
  if ( x > y) {
    printf("\nx is greater than y");
  }
  
  if ( x < y) {
    printf("\nx is less than y");
  }
}
```
### Check Result [here](https://onecompiler.com/c/3vke6rqjc)

## 3. Bitwise Operators

C bitwise operators are used to perform bitwise operations on operands.

|Operator|	Description| Usage|
|----|----|----|
| `&` |	Bitwise AND | `(x > y) & (y > z)`|
| `|` |	Bitwise OR | `(x > y) | (y > z)`|
| `^` |	Bitwise XOR | `(x > y) ^ (y > z)`|
| `~` |	Bitwise NOT	| `(~x)`|
| `<<` | Bitwise Left Shift| `x << y`|
| `>>` | Bitwise Right Shift| `x >> y`|

## 4. Logical operators

Below are the logical operators present in C language.

|Operator|	Description| Usage|
|----|----|----|
| `&&` |	Logical AND | `(x > y) && (y > z)`|
| `||` |	Logical OR | `(x > y) || (y > z)`|
| `!` |	Logical NOT	| `(!x)`|

## 5. Assignment Operators

Below are the assignment operators present in C language.

|Operator|	Description| Usage|
|----|----|----|
| =	| Assign| int x = 10;|
| += |	Add and assign|	int x=10; x+=30; // x becomes 40|
| -= |	Subtract and assign| int x=40; x-=10; // x becomes 30|
| *= |	Multiply and assign| int x=10; x*=40; // x becomes 400|
| /= |	Divide and assign|	int x=100; x /= 10;// x becomes 10|
| %= |	Modulus and assign|	int x=100; x%=10; // x becomes 0|
| <<= | Left shift and assign|	x <<= 2 is same as x = x << 2|
| >>= | Right shift and assign|	x >>= 2 is same as x = x >> 2|
| &= | Bitwise and assign| x &= 10 is same as x = x & 10|
| ^= | Bitwise exclusive OR and assign| x ^= 10 is same as x = x ^ 10|
| `|=` |Bitwise inclusive OR and assign	| `x |= 10 is same as x = x | 10`|

### Example

```C
#include <stdio.h>
int main()
{
int x = 10; // assigning 10 to x 
printf("x value:%d " , x);
        
x+=30;
printf("\nx value after += operation:%d " , x);
        
x-=10;
printf("\nx value after -= operation: %d" , x);
        
x*=10;
printf("\nx value after *= operation:%d " , x);
        
x/=10;
printf("\nx value after /= operation:%d " , x);
        
x%=10;
printf("\nx value after %= operation:%d " , x);   
}
```

### Check Result [here](https://onecompiler.com/c/3vke7snnv)

## 6. Misc Operator

* **Ternary Operator**

If the operator is applied on three operands then it is called ternary. This is also known as conditional operator as a condition is followed by `?` and true-expression which is followed by a `:` and false expression. This is oftenly used as a shortcut to replace if-else statement

### Example

```c
#include <stdio.h>
int main()
{
    int x = 10;
    int y = 90;

    int z = x > y ? x : y;

    printf("Larger Number is: %d " , z);
}
```
### Check Result [here](https://onecompiler.com/c/3vkeha3f9)

* **sizeof()**

This operator is used to return the size of a variable.

```c
#include <stdio.h>
int main()
{
 int x = 90;
 int y = sizeof(x);

 printf("Size of x is: %d " , y);
}
```
### Check Result [here](https://onecompiler.com/c/3vkehh6my)

## Summary

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==| 
| Bitwise Operator| & , ^ , | 
| Logical Operator| && , `||`, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, `|=` |
| Ternary Operator| ? : |
| sizeof operator| sizeof() |
