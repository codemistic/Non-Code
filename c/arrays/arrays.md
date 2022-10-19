Array is a collection of similar data which is stored in continuous memory addresses. Array values can be fetched using index. 

Index starts from 0 to size-1.

Arrays can be one-dimensional or multi-dimensional in C language. The more popular and frequently used arrays are one-dimensional and two-dimensional arrays.

Arrays store the collection of data sequentially in memory and they must share same data type.

# How to declare an array?

### One dimentional Array:

```c
data-type array-name[size];
```

### Two dimensional array:

```c
data-type array-name[size][size];
```

## Examples

### One dimentional Array:

```c
int a[5];
```

### Two dimentional Array:

```c
int a[2][3];
int b[][3]; // is also valid
```

# How to initialize arrays

### One dimentional Array:

```c
int a[5] = {1,2,3,4,5};
```

### Two dimentional Array:

```c
int a[2][3] = {
                {1,2,3},
                {4,5,6}
              };
```

# How to access array elements

Array elements can be accessed by using indices. Array indices starts from `0` and  `Array[n-1]` can be used to access nth element of an array.

## Examples

### One dimentional array:

```c
#include <stdio.h>
int main()
{
    int arr[5] = {1,2,3,4,5};
    int n = sizeof(arr)/sizeof(arr[0]); // gives length of an array
    printf("Length of the array:%d", n);
    printf("\nfirst element: %d", arr[0]); // prints first element of the array
    printf("\nlast element: %d", arr[n-1]); // prints last element of the array
}
```
### Check result [here](https://onecompiler.com/c/3vku4yuj5)

### Two dimentional array:

```c
#include <stdio.h>
int main()
{
  int a[2][3] = {
                {1,2,3},
                {4,5,6}
              };
  for(int i=0; i<2; i++) // iterates for each row
  {
    for(int j=0; j<3; j++) // iterates for each column
    {
        printf("%d ", a[i][j]);
    }
        printf("\n");
}   
}
```
### Check result [here](https://onecompiler.com/c/3vkud9xj4)

## Summary

* Array is a collection of homogeneous data.
* Arrays stores data sequentially in memory.
* Arrays are finite.

