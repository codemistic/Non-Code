When ever you want to perform a set of operations based on a condition(s) If / If-Else / Nested ifs are used.

You can also use if-else , nested IFs and IF-ELSE-IF ladder when multiple conditions are to be performed on a single variable.

## 1. If

### Syntax

```c
if(conditional-expression)
{
    //code
}
```
### Example

```c
#include <stdio.h>
int main()
{
        int x = 30;
        int y = 30;

        if ( x == y) {
          printf("x and y are equal");
        }
}
```
### Check result [here](https://onecompiler.com/c/3vkukmz3s)

## 2. If-else

### Syntax

```c
if(conditional-expression)
{
    //code
} else {
    //code
}
```
### Example

```c
#include <stdio.h>
int main()
{
  int x = 30;
  int y = 20;

  if ( x == y) {
    printf("x and y are equal");
  } else {
      printf("x and y are not equal");  
    }
}
```
### Check result [here](https://onecompiler.com/c/3vkukqf28)

## 3. If-else-if ladder

### Syntax
```c
if(conditional-expression-1)
{
    //code
} else if(conditional-expression-2) {
    //code
} else if(conditional-expression-3) {
    //code
}
....
else {
    //code
}
```

### Example
```c
#include <stdio.h>
int main()
{
  int age = 15;

    if ( age <= 1 && age >= 0) {
      printf("Infant");
    } else if (age > 1 && age <= 3) {
        printf("Toddler");
    } else if (age > 3 && age <= 9) {
        printf("Child");
    } else if (age > 9 && age <= 18) {
        printf("Teen");
    } else if (age > 18) {
        printf("Adult");
    } else {
        printf("Invalid Age");
    }
}
```
### Check result [here](https://onecompiler.com/c/3vkuku699)

## 4. Nested-If

Nested-Ifs represents if block within another if block. 

### Syntax
```c
if(conditional-expression-1) {    
     //code    
          if(conditional-expression-2) {  
             //code
             if(conditional-expression-3) {
                 //code
             }  
    }    
}
```

### Example

```c
#include <stdio.h>
int main()
{
 int age = 50;
 char resident = 'Y';
 if (age > 18)
  {
    if(resident == 'Y'){
      printf("Eligible to Vote");
    }
  }
}
```
### Check result [here](https://onecompiler.com/c/3vkukyt2j)

## Switch

Switch is an alternative to IF-ELSE-IF ladder and to select one among many blocks of code.

### Syntax

```c
switch(conditional-expression){    
case value1:    
 //code    
 break;  //optional  
case value2:    
 //code    
 break;  //optional  
...    
    
default:     
 //code to be executed when all the above cases are not matched;    
} 
```
### Example
```c
#include <stdio.h>
int main()
{
 int day = 3;
      
      switch(day){
        case 1: printf("Sunday");
        break;
        case 2: printf("Monday");
        break;
        case 3: printf("Tuesday");
        break;
        case 4: printf("Wednesday");
        break;
        case 5: printf("Thursday");
        break;
        case 6: printf("Friday");
        break;
        case 7: printf("Saturday");
        break;
        default:printf("Invalid day");
        break; 
      }
}
```
###  Check Result [here](https://onecompiler.com/c/3vkumg7ys)
