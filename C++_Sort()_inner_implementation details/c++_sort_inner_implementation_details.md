# HOW THE C++ INBUILT SORT() FUNCTION IN STL WORKS(INNER IMPLEMENTATION)

## Introduction :

The sort function sorts the vector or array either in ascending order or in decending order.

**Syntax of sort function to sort in ascending order:**

1. in case of array --> sort(arr, arr + n).
2. in case of vector --> sort(v.begin(), v.end()).

It generally takes two parameters-->

1. The first one being the point of the array/vector from where the sorting needs to begin
2. The second parameter being the length up to which we want the array/vector to get sorted.
3. The third parameter is optional and can be used in cases such as if we want to sort the elements lexicographically.

**NOTE :** BY DEFAULT THE SORT FUNCTION SORTS IN ASCENDING ORDER.

# WHAT IF WE WANT TO SORT IN DESCENDING ORDER

Then third parameter comes into the picture which is known as comparater function.

1. The third parameter is used to specify the order in which elements are to be sorted.
2. We can pass the “greater()” function to sort in descending order.
3. This function does a comparison in a way that puts greater elements before.

**Syntax of sort function to sort in descending order:** sort(arr, arr + n, greater<int>()).

EXPLANATION -->

1. arr --> name of array.
2. arr+n --> length upto which we want the array/vector to get sorted.
3. greater<int> --> greater is the function, specifically a comparater function and having int type of values.

### NOTE : In case of priority queue, we pass greater but that was class named as greater , inside which we have our comparater but in case of sort function , greater is the name of the comparater function ,it is not class name.

Greater is the inbuilt comparater which is already defined in stl with such an implementation that it sorts the array/vector in the descending order.

Since the greater function is inbuilt comparater we are able to use it directly , but we can also define our own comparater function , and we can provide the sorting functionality according to our choice---->

**EXAMPLE**

1. arr[] = { { 6, 7 }, { 2, 9 }, { 3, 4 }, { 4, 8 } }. //here we have taken array of pairs instead of array of integers.
2. sort(arr, arr + n, comparefunc).

3. bool comparefunc(Interval i1, Interval i2)
   {
   return (i1.start < i2.start).
   }

EXPLANATION-->
“comparator” function returns a boolean value, which basically tells us whether the passed “first” argument should be placed before the passed “second” argument or not.

## TIME COMPLEXITIES-->

The time complexity of std::sort() is.

1. Best Case – O(N log N).
2. Average Case – O(N log N).
3. Worst-Case – O(N log N).
4. Space Complexity: It may use O( log N) auxiliary space.

# INNER IMPLEMENTATION OF STL SORT().

1. C++ stl sort() uses the best sorting algorithm out of all sorting algorithm.
2. It is a hybrid sorting algorithm, which means that it uses more than one sorting algorithms.
3. There are 3 sorting algorithms from which stl sort() is made i.e --> Quicksort, Heapsort and Insertion Sort .

**Why these three are used->** to reduce the running time of sort() function.

## BUT THE QUESTION IS HOW THE RUNNING TIME IS REDUCED--->

Let's first discuss some important points of quick sort , heapsort , insertion sort.

1. **QUICK SORT :** The worst case of quick sort occurs when the pivot is choosen as either the leftmost element or rightmost element in the following cases.

--> Array is already sorted in the ascending order.
--> Array is already sorted in descending order.
--> All elements are the same (a special case of cases 1 and 2).

The worst-case behavior for quicksort occurs when the partitioning routine produces one subproblem with n -1 elements and one with 0 elements.

TC - O(n^2) in worst case.
SC - O(logn) -> auxillary stack space.
Not stable.

2. **HEAP SORT :** The time complexity of heap sort in all the cases is O(nlogn).

**NOTE :** In general the quick sort is faster than heap sort but due to worst case of quick sort O(n^2) (occurs rarely), sometimes heap sort is preferred over quick sort.

Heap sort is not stable because operations in the heap can change the relative order of equivalent keys.

3. **INSERTION SORT:** The worst and average case is O(n^2) in insertion sort,and best case
   is O(n).

--> It can easily be implemented.
--> It is efficient for small data values.
--> Generally it is appropriate for data sets which are already partially sorted.

So,The sort() function uses above three algorithms which in combination , known as **INTROSORT**.

# WORKING OF INTROSORT

## OR

## HOW THE RUNNING TIME IS REDUCED USING ABOVE THREE ALGO IN COMBINATION.

1. Introsort begins with quicksort and if the recursion depth goes more than a particular limit, it switches to Heapsort to avoid Quicksort’s worse case of O(n^2) .

Also quick sort increases the recursion stack space O(log N), if tail recursion applied), so to avoid all these, quick sort have to shift to heap sort.

2.  It also uses insertion sort when the number of elements to sort is quite less. So first it creates a partition.

3.  Three cases arises from here.

--> If the partition size is such that there is a possibility to exceed the maximum depth limit then the Introsort switches to Heapsort.The maximum depth limit is defined as 2log(N).

--> Now if the partition size is too small then we know that insertion sort works well with smaller data, so Quicksort get shifted on Insertion Sort. We define this cutoff as 16 (due to research).

--> So if the partition size is less than 16 then we will do insertion sort.
If the partition size is under the limit and not too small (i.e- between 16 and 2log(N)), then it performs a simple quicksort.

## CAN WE PERFORM BUBBLE SORT OR SELECTION SORT IN PLACE OF INSERTION SORT-->.

No because insertion always gives optimal solution for smaller arrays and also have good locality of refernce.

## WHY HAVEN'T WE USE MERGE SORT IN PLACE OF HEAP SORT-->.

because merge sort requires extra space of O(n) for merging and heap sort is inplace sorting algorithm :O(1).

## WHEN PARTITION SIZE IS BETWEEN 16 TO 2logn(n) , WHY INTROSORT SWITCHES TO QUICK SORT AND NOT HEAP SORT.

We know very well that heap sort gives O(nlogn) in all the three cases and also takes constant space , so it is no less than quick sort , still introsort switches to quick sort when partition size is under limit and not heap sort.

Because as stated above too ,that quick sort is faster than heap sort as the hidden constant factor of quick sort is smaller than that of heap sort.

## What is hidden constant factor , How can we say quick sort have smaller constant factor?.

A constant factor is simply anything that doesn't depend on the input parameter.It refers to the idea that different operations with the same complexity take slightly different amounts of time to run.

Constant factor is determined not only from theoretical comparison but also implementation details. Quicksort has small constant factor because it is cache friendly or has faster locality of reference.

In quicksort, the partitioning step typically does all its reads and writes at the ends of the arrays, so the array accesses are closely packed toward one another, means the next element to be accessed is usually close in memory to the element you just looked at.

Heapsort, on the other hand, jumps around the array as it moves up and down the heap. Therefore, the array accesses in quicksort, on average, take much less time than the array accesses in heapsort.

So, since memory systems use caches and cache misses are expensive, quicksort is usually a much better option.

**That's why introsort switches to quick sort when partition size is under limit because of its faster nature.**

### WHY INTROSORT IS NOT STABLE :

because quick sort is not stable.

# TIME COMPLEXITIES OF INTROSORT

1. Worst case : O(nlogn).
2. Average case : O(nlogn).
3. Best case : O(nlogn).

# SPACE COMPLEXITY

O(logn) of Auxillary stack space as it is in quick sort.

**This article is contributed by NIKITA GUPTA**
