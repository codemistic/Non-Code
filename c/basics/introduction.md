C language is one of the most popular general-purpose programming language developed by Dennis Ritchie at Bell laboratories for UNIX operating system.

It's one of the simple and flexible programming language and infact almost all of us would have started our programming language's learning with C.

## Key Features

* Structured programming
* Popular system programming language
* UNIX, MySQL are completely written in C.
* Supports variety of platforms
* Efficient and also handle low-level activities.
* As fast as assembly language and hence used as system development language.

## Why you should learn C?

* C is considered as the best foundational language as you can understand the fundamental computer theories well.
* Easy to learn and structured programming language.
* You will get opportunities to work on open source projects.
* C is a middle level programming language means you can write system level programs as well as application level programs.
* You will also get used to programming discipline as C is a strongly typed language.

## Why C is popular?

* C is used to write compilers, interpreters, editors, operating systems and embedded programs.
* C is second popular language according to [Tiobe Index](https://www.tiobe.com/tiobe-index/)
* Most of the operating system kernels are written in C
* Many popular compilers and interpreters are written in C. For example, python interpreter is written in C.
* Not only compilers, interpreters, C is also used to write modern browsers, game engines etc.
* C is very good for embedded programming.

# C Basics

## Sample C program

```c
#include <stdio.h>    
int main(){    
printf("Hello World!!");    
return 0;   
}  
```
### Run your program [here](https://onecompiler.com/c)

Let's look into each line of the above sample program:

* `#include` is a keyword which is used to include the library file `<stdio.h>`. 
* `<stdio.h>` library file is used to read the data from terminal and to display the data on terminal. It has several in-built functions like printf(), scanf() etc.
* `main()` function is the entry point of any C program.
* `printf and scanf` are inbuilt library functions which are used for input and output in C language. They are defined in `stdio.h` header file.
* `return 0` is used to terminate the main() function and returns the value 0

## How to compile and run a C program

You can either use the shortcut `ctrl+F9` to compile and run or Go to Compile menu and then click on compile and then run.


## Comments

1. Single line comments

    `//` is used to comment a single line

2. Multi line comments

    `/**/` is used to comment multiple lines.

 
## Installation

## 1. on MacOS

* Install [Xcode](https://developer.apple.com/xcode/) from Appstore.
* Once installed, accept the terms and conditions and provide your MAC password.
* Now, components will get installed.

## 2. on Windows

* There are many C compilers available in the market which are free to use.
* Download C compiler from [VS-C-andC++](https://visualstudio.microsoft.com/vs/features/cplusplus/)
* Run the executable file.

## 3. on Linux

* Most Linux operating systems are pre-installed with GCC.

```shell
gcc -version
```
* For Ubuntu and Debian, use the below command

```shell
sudo apt-get update
sudo apt-get install build-essential manpages-dev
```
* For redhat, use the below command

```shell
yum groupinstall 'Development Tools'
```

## 4. Using Onecompiler

* You don't need to install any software or compiler.
* Just goto [OneCompiler](https://onecompiler.com/) and choose the programming language as C and enjoy programming without any installation.
