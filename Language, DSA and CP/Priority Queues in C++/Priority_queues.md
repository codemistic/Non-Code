# WHAT IS A PRIORITY QUEUE ?

A priority queue is a special type of queue where each and every element is assigned a priority value.

Elements are arranged on the basis of priority of the elements.

### priority can be decided in two ways -->

1. either the elements having lower value have higher priority
2. or the elements having higher value will have higher priority

**NOTE** ->

1. BY DEAFULT THE PRIORITY IS LIKE THE ELEMENTS WHICH ARE LARGER HAVE HIGHER PRIORITIES THAN SAMLLER ONES.
2. IF ELEMENTS HAVE EQUAL VALUE THEN THEY FOLLOW THE FIFO CONCEPT(first in first out)

# WAYS TO IMPLEMENT PRIORITY QUEUE

1. using arrays.
2. using linked_lists.
3. using heap.
4. using binary search tress.

## Comparison table for different ways to implement PQ in terms of Time complexity

**OPERATIONS Arrays Linkedlist Heap BST**

1. insert O(1) O(n) O(logn) O(logn)
2. delete O(n) O(1) O(logn) O(logn)
3. peek O(n) O(1) O(1) O(1)

**NOTE** --> If we see then bst and binary heap both are having same time complexities, still Binary Heap is preferred over BST.

# WHY BINARY HEAP IS PREFERRED OVER BST FOR PRIORITY QUEUE IMPLEMENTATION

1. Because of the reason that binary heap is implemented using arrays and there is always better locality of reference in arrays and also operations are more cache friendly.

2. Construction of Binary heap requires O(n) and BST requires O(nlogn) to construct.

3. Also Binary heaps are easier to implementand doesn't require extra space for pointers.

**Now since we know that binary heap is the way to implement priority queue so there are two types of heaps --> max heap and min heap**

**so same goes for priority queue -->**
there are two types of priority queue -->

1. Min Priority Queue
2. Max Priority Queue

-->Min priority queue have smaller elements on top and max priority queue have larger elements on top.

#### Syntax for max priority queue

priority_queue<int>q; // by default it's always max pq.

#### Syntax for min priority queue

priority_queue<int,vector<int>,greater<int>>q;

# Explanation of syntax of min priority queue

1. **int -->** this signifies the type of values that is going to be inserted in priority queue. This datatype can vary according to our needs like we can take string , pairs , vectors etc.

2. **vector<int>** this is the container which contains this datatype(in this case it is int). It has to be passed when we are making min pq.

3. **greater<int>** greater is a class template in which comparater is defined.
   In greater class a comparater is defined which makes sure that elements are sorted in decreasing order, and int is again a datatype.

**Now the question arises ,if 'greater class' ensures the order of elements in descending order then the first element should be the largest element , but this is min priority queue and the element that comes first will be smaller or minimum**.

-->so ans is ,in priority queues the element comes out from the opposite side.

### Example -->

1. push(5) --> 5.
2. push(4) --> 5,4.
3. push(3) --> 5,4,3.

now see elements are arranged in decreasing order only.(which is a functionality of greater class).
but when a element get's popped out from queue it will be 3 ,then 4 then 5, because 3 has the highest priority here ,since this min heap.

**so always remember in case of max priority queue the order of elements that will come out will be descending order and in case of min pq the order of elements that comes out will be in increasing order.**

Now as we have learnt that greater is a class inside which a comparater is defined,so instead of using greater class and its comparater we can make our own class and our own comparater inside it.

### NOTE --> REMEMBER THAT IN GENERAL WE PASS COMPARATER AS A FUNCTION BUT IN PRIORITY QUEUE WE PASS CLASS IN WHICH () THIS OPERATOR IS OVERLOADED WHICH LOOKS LIKE A FUNCTION.

syntax --> Defining our own comparater class

priority_queue<int,vector<int>,compare<int>>q;

class compare
{
public:
bool operator()(int a ,int b)
{
return(a>b);
}
};

**Comparater is a binary predicate -> input ---->logic---->boolean value(output)**

# APPLICATIONS OF PRIORITY QUEUE

1. CPU Scheduling
2. Graph algorithms like Dijkstra’s ,Prim’s,etc.
3. In Stack Implementation
4. Data compression in Huffman code
5. Event-driven simulation such as customers waiting in a queue.(ex--ticket counter)
6. In Finding Kth largest/smallest element.

**This article is contributed by NIKITA GUPTA**
   
 Characteristics of Priority Queue
 1. An item with the highest priority is moved at the front and deleted first.
 2. If two elements share the same priority value, then the priority queue follows the first-in-first-out principle for de queue operation.
 3. Each item has some priority associated with it.
 4. Max Heap.
 5. Inserting an Element in a Max Heap Binary Tree.  
