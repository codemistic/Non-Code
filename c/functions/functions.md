Function is a sub-routine which contains set of statements. Usually functions are written when multiple calls are required to same set of statements which increases re-usuability and modularity.

Two types of functions are present in C

1. Library Functions

  Library functions are the in-built functions which are declared in header files like printf(),scanf(),puts(),gets() etc.,

2. User defined functions

  User defined functions are the ones which are written by the programmer based on the requirement.

## How to declare a Function

```c
return_type function_name(parameters);
```

## How to call a Function

```c
function_name (parameters)
```
## How to define a Function

```c
return_type function_name(parameters){  
//code
}
```

# Different ways of calling a user-defined functions

You can call functions in different ways as given below based on your requirement.

1. Function with no arguments and no return value.
2. Function with no arguments and a return value.
3. Function with arguments and no return value.
4. Function with arguments and a return value.

Let's look into examples for the above types.

## 1. Function with no arguments and no return value.

```c
#include <stdio.h>
void greetings();  
int main()
{
    greetings();
}

void greetings()  
{  
    printf("Hello world!!");  
}  
```
### check result [here](https://onecompiler.com/c/3vm7677ax)

## 2. Function with no arguments and a return value.

```c
#include <stdio.h>
int sum();
int main()
{
  int result;
  result = sum();
  printf("Sum : %d", result);
}

int sum() {
   int x, y, sum;
   x = 10;
   y = 20;
 
   sum = x + y;
   return (sum); // returning sum value
}
```
### check result [here](https://onecompiler.com/c/3vm76us9m)

## 3. Function with arguments and no return value.

```c
#include <stdio.h>
int sum();
int main()
{
  int x= 10, y = 20;
  sum(x,y); // passing arguments to function sum
}

int sum(int x , int y) {
   int sum;
   sum = x + y;
   printf("Sum : %d", sum);
   return 0;
}
```

### Check result [here](https://onecompiler.com/c/3vm76hvmf)

## 4. Function with arguments and a return value.

```c
#include <stdio.h>
int sum();
int main()
{
  int x= 10, y = 20;
  int result;
  
  result = sum(x,y); // passing arguments to function sum
  printf("Sum : %d", result);

  
}

int sum(int x , int y) {
   int sum;
   sum = x + y;
   return sum; // returning sum value
}
```
### Check result [here](https://onecompiler.com/c/3vm774nm2)