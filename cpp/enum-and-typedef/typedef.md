Typedef is used to explicitly define new data type names by using the keyword `typedef`. It defines a name for an existing data type but doesn't create a new data type. 

Typedefs helps in portability as you can just change the typedefs alone when you move from one system to another. 

## Syntax

```c
typedef data-type name;
```

## Example

```c
#include <iostream> 
using namespace std; 


int main() 
{ 
    typedef unsigned int distance;  // typedef of int 
	distance d1; 
	d1 = 150;
	cout << "Distance is: " << d1; 
	return 0; 
} 
```
### Check result [here](https://onecompiler.com/cpp/3vm85rv7t)
