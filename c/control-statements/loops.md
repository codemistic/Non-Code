## 1. For

For loop is used to iterate a set of statements based on a condition. Usually for loop is preferred when number of iterations are known in advance.

### Syntax

```c
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```
### Example

```c
#include <stdio.h>
int main()
{
  for (int i = 1; i <= 5; i++) {
    printf("%d\n",i);
  }
}
```

### Check Result [here](https://onecompiler.com/c/3vkumntmg)

## 2. While

While is also used to iterate a set of statements based on a condition. Usually while is preferred when number of iterations is not known in advance.

### Syntax

```c
while(condition){  
//code 
}  
```
### Example

```c
#include <stdio.h>
int main()
{
int i=1;
while ( i <= 5) {
  printf("%d\n",i);
  i++;
  }
}
```
### Check result [here](https://onecompiler.com/c/3vkumvqrm)

## 3. Do-while

Do-while is also used to iterate a set of statements based on a condition. It is mostly used when you need to execute the statements atleast once.

### Syntax

```c
do{  
//code 
} while(condition); 
```
### Example

```c
#include <stdio.h>
int main()
{
  int i=1;
  do {
  printf("%d\n",i);
  i++;
  } while (i<=5);
}
```

### Check result [here](https://onecompiler.com/c/3vkumzhwu)