C doesn't support error or exception handling directly but there are some ways to implement error handling in C. 

A developer is expected to prevent the errors from occuring by checking if the program works fine for all possible scenarios and doesn't end in infinite loops. 

You can handle errors based on return values of the function. In most of the cases functions return -1 or NULL in case of any errors. 

## 1. By using errno

`errno` is set by system calls and some library functions in the event of an error to tell if something goes wrong. You need to include <errno.h> header to use the external variable "errno". 

Below are the different return codes of errno for different types of errors.

|errno value | Error Description|
|----|----|
|1 | Operation not permitted |
|2 | No such file or directory |
|3 | No such process |
|4 | Interrupted system call |
|5 | I/O error |
|6 | No such device or address |
|7 | Argument list too long |
|8 | Exec format error |
|9 | Bad file number |
|10 | No child processes |
|11 | Try again |
|12 | Out of memory |
|13 | Permission denied |


## Example

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

extern int errno ;

int main () {
   FILE *f;

   f = fopen("example.txt", "r"); // consider this file doesn't exist.

   if( f == NULL ) {
      fprintf(stderr, "errno value: %d\n", errno);
      fprintf(stderr, "Error info: %s\n", strerror(errno));
      perror("perror info: "); 
   } else {
      //code goes here
   }
   
   return(0);
}
```
### Check result [here](https://onecompiler.com/c/3vkzzpdsk)

## Note

You can either use `strerror` or `perror` to display the error information.

## 2. By using EXIT CONSTANTS

EXIT_SUCCESS and EXIT_FAILURE are two macros defined in <stdlib.h> which can be passed to exit() function to indicate successful or unsuccessful termination.

If you write anything after exit() function, it will not get executed.

```c
#include <stdio.h> // to use fprintf and stderr
#include <errno.h> // to use errno
#include <string.h> // to use perror and strerror
#include <stdlib.h> // to use EXIT_SUCCESS and EXIT_FAILURE

extern int errno ;

int main () {
   FILE *f;

   f = fopen("example.txt", "r"); // consider this file doesn't exist.

   if( f == NULL ) {
      fprintf(stderr, "errno value: %d\n", errno);
      fprintf(stderr, "Error info: %s\n", strerror(errno));
      perror("perror info: "); 
      exit(EXIT_FAILURE); 
   } else {
      //code goes here
      exit(EXIT_SUCCESS); 
   }
   
   return(0);
}
```

### Check result [here](https://onecompiler.com/c/3vm22tq2a)

## 3. Division by zero 

There might be certain situations where a divisor can become zero which will produce runtime error. It is always advisable to check if the divisor is zero in your program.

```c
#include <stdio.h> // to use fprintf and stderr 
#include <stdlib.h> // to use exit 
int main()
{
    int dividend = 100;
    int divisor = 0;
    int result;

    if (divisor == 0) {
        fprintf(stderr, "Abort!! Division by zero\n");
        exit(EXIT_FAILURE); 
    } else {
    result = dividend / divisor;
    exit(EXIT_SUCCESS);
    }
}
```
### Check result [here](https://onecompiler.com/c/3vm244258)
