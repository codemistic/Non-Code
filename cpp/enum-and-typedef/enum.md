Enumeration data type is a user-defined data type in C++. `enum` keyword is used to declare a new enumeration types in C++. 

### Syntax

```c
enum name{constant1, constant2, constant3, ....... } var-list;
```
### Example

```c
#include <iostream>
using namespace std;


enum month{January, February, March, April, May, June, July, August, September, October, November, December} name;

int main() 
{
  name = June; 
  cout << name; 
  return 0; 
}
```
### Run [here](https://onecompiler.com/cpp/3vm845a9w)
