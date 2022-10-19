# Why files are required?

* To store or retrieve large volume of data as limited data can be displayed on console.
* Usually data gets lost when program is terminated, You can access the data present in a file even when the program is terminated.
* Handling and transferring data from one system to another is quite easier using files

# File handling in C?

File operations like create, update, read, and deleting files which are stored on the local file system can be performed in C.

You need to declare a pointer of type File as below:

```c
FILE *fptr;
```
## 1. Create or Update a file

First, you need to open file in order to create or update.

### Syntax for opening a file

```c
fptr = fopen("filename","mode");
```
### Modes of opening files

|Mode | Description|
|----|----|
|r|	Opens for reading.	|
|rb| Opens for reading in binary mode.	|
|r+| Opens for both reading and writing.|	
|w|	Opens for writing. |   			
|wb| Opens for writing in binary mode.|					
|a|	Opens for append. |                      				
|ab| Opens for append in binary mode.|        			
|w+| Opens for both reading and writing.|					
|wb+| Opens for both reading and writing in binary mode.|
|rb+| Opens for both reading and writing in binary mode.|
|a+| Opens for both reading and appending.	|
|ab+| Opens for both reading and appending in binary mode.|

### Example
```c
fptr = fopen("C:\\samples\\sample.txt","w");
```
Consider `sample.txt` is not present in the above path then it creates a file named `sample.txt` and opens it for writing. 


## 2. Read and write to a file

fprintf() and fscanf() are used to read and write to a file. They are similar to  printf() and scanf() but they are file versions and expects a pointer to the structure file.

### Syntax to read a file

```c
FILE * fptr; 
fptr = fopen(“fileName.txt”, “r”);
fscanf(fptr, "format specifier", data);
```
### Syntax to write a file
```c
FILE * fptr; 
fptr = fopen(“fileName.txt”, “w”);
fprintf(fptr, "format specifier", data);
```

Any file which is opened for read or write should be closed

### Syntax to close a file
```c
fclose(fptr);
```
