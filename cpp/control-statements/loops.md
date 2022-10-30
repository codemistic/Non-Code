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
#include <iostream>
using namespace std;

int main() 
{
   for (int i = 1; i <= 5; i++) {
    cout << i << endl;
  }
}
```

#### Check Result [here](https://onecompiler.com/cpp/3vmbgeg6b)

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
#include <iostream>
using namespace std;

int main() 
{

int i=1;

while ( i <= 5) {
  cout << i << endl;
  i++;
}
}
```
#### Check result [here](https://onecompiler.com/cpp/3vmbgh3az)

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
#include <iostream>
using namespace std;

int main() 
{
  int i=1;
  do {
  cout << i << endl;
  i++;
  } while (i<=5);
}
```

#### Check result [here](https://onecompiler.com/cpp/3vmbgkg2p)